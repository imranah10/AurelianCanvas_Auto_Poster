#!/usr/bin/env python3
"""Aurelian Canvas Auto-Poster - main entry.
Usage: python3 poster.py [--dry-run] [--platform all|pinterest|ig] [--date YYYY-MM-DD]
Reads data/schedule.json, posts due items, updates state/posted.json."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ap_common as C
from ap_common import (log, today_str, load_state, save_state, load_schedule,
                       pick_due_items, mark, resolve_asset, raw_url, SETTINGS)

REPO = None  # set from env GITHUB_REPOSITORY (owner/repo) in Actions
BRANCH = None


def git_commit(message: str) -> None:
    global REPO, BRANCH
    if not REPO:
        REPO = __import__("os").environ.get("GITHUB_REPOSITORY", "")
    if not REPO:
        log("Not in GitHub Actions; skipping git commit.")
        return
    cmds = [
        ["git", "config", "user.name", "aurelian-bot"],
        ["git", "config", "user.email", "bot@aureliancanvas.local"],
        ["git", "add", "state/posted.json", "media-ig"],
        ["git", "commit", "-m", message] if _has_staged() else ["git", "status"],
        ["git", "pull", "--rebase", "--autostash", "origin", BRANCH or "main"],
        ["git", "push", "origin", f"HEAD:{BRANCH or 'main'}"],
    ]
    for cmd in cmds:
        if cmd[0] == "git" and cmd[1] == "commit" and not _has_staged():
            log("Nothing to commit.")
            continue
        r = subprocess.run(cmd, cwd=C.ROOT, capture_output=True, text=True)
        if r.returncode != 0 and "nothing to commit" not in r.stdout.lower():
            log(f"git {' '.join(cmd[1:])} rc={r.returncode}: {r.stderr.strip()[:300]}")


def _has_staged() -> bool:
    r = subprocess.run(["git", "status", "--porcelain", "state/posted.json", "media-ig"],
                       cwd=C.ROOT, capture_output=True, text=True)
    return bool(r.stdout.strip())


def post_pinterest_items(items: list, dry: bool, state: dict, today: str) -> None:
    if not items:
        return
    import pinterest_api as P
    token = None
    refreshed = False
    if not dry:
        if __import__("os").environ.get("PINTEREST_REFRESH_TOKEN"):
            try:
                tok = P.refresh_access_token()
                token = tok["access_token"]
                refreshed = True
                __import__("os").environ["PINTEREST_ACCESS_TOKEN"] = token
                _persist_refresh_token(tok.get("refresh_token", ""))
            except Exception as e:
                log(f"Token refresh failed, falling back to static token: {e}")
                token = __import__("os").environ.get("PINTEREST_ACCESS_TOKEN")
        else:
            token = __import__("os").environ.get("PINTEREST_ACCESS_TOKEN")
        if not token:
            log("PINTEREST secrets not set - skipping Pinterest this run.")
            return
        board_map = P.list_boards(token)
    else:
        board_map = {}
    ok_n = fail_n = 0
    for it in items:
        art = it["art"]
        f = resolve_asset(art, it["asset_type"], it["asset_slot"])
        if f is None:
            log(f"SKIP {it['id']}: media file missing for {art}/{it['asset_type']} slot {it['asset_slot']}")
            continue
        img_url = raw_url(f, _repo(), _branch())
        vid_file = f if it["asset_type"] == "video" else None
        if dry:
            log(f"DRY POST {it['id']} | {it['board']} | {it['asset_type']} {f.name} | {it['pin_title'][:60]}")
            ok_n += 1
            continue
        try:
            pin_id = P.post_item(it, token, board_map, SETTINGS["board_descriptions"], img_url, vid_file)
            log(f"OK {it['id']} -> pin {pin_id}")
            mark(state, it["id"], True)
            ok_n += 1
        except Exception as e:
            log(f"FAIL {it['id']}: {e}")
            mark(state, it["id"], False, str(e)[:200])
            fail_n += 1
    save_state(state)
    git_commit(f"state: pinterest {today} ok={ok_n} fail={fail_n}" + (" +token-rotated" if refreshed else ""))
    if refreshed:
        log("Pinterest token rotated; new refresh token saved to GitHub secret if GH_PAT present.")


def _persist_refresh_token(new_rt: str) -> None:
    if not new_rt:
        return
    tok_name = "PINTEREST_REFRESH_TOKEN"
    pat = __import__("os").environ.get("GH_PAT", "")
    if not pat or not REPO:
        log("WARN: cannot update secret (GH_PAT/GITHUB_REPOSITORY missing). "
            "If pins start failing auth errors, refresh token manually per guide.")
        return
    import base64
    from urllib.request import Request, urlopen
    # fetch repo public key
    r = json.loads(_gh_api(f"https://api.github.com/repos/{REPO}/actions/secrets/public-key", pat))
    enc = _encrypt_secret(r["key"], new_rt)
    body = json.dumps({"encrypted_value": enc, "key_id": r["key_id"]}).encode()
    req = Request(f"https://api.github.com/repos/{REPO}/actions/secrets/{tok_name}",
                  data=body, method="PUT",
                  headers={"Authorization": f"token {pat}", "Accept": "application/vnd.github+json"})
    with urlopen(req, timeout=30) as resp:
        resp.read()
    log(f"GitHub secret {tok_name} updated.")


def _gh_api(url: str, pat: str):
    from urllib.request import Request, urlopen
    req = Request(url, headers={"Authorization": f"token {pat}", "Accept": "application/vnd.github+json"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode()


def _encrypt_secret(pubkey_b64: str, secret: str) -> str:
    import base64
    import nacl.public  # pynacl
    pk = nacl.public.PublicKey(base64.b64decode(pubkey_b64))
    sealed = nacl.public.SealedBox(pk).encrypt(secret.encode())
    return base64.b64encode(sealed).decode()


def post_ig_items(items: list, dry: bool, state: dict, today: str) -> None:
    if not items:
        return
    import os
    if not dry and not (os.environ.get("IG_USER_ID") and os.environ.get("PAGE_ACCESS_TOKEN")):
        log("IG secrets not set - skipping Instagram this run.")
        return
    import ig_api as IG
    ok_n = fail_n = 0
    new_crops = False
    for it in items:
        f = resolve_asset(it["art"], it["asset_type"], it["asset_slot"])
        if f is None:
            log(f"SKIP {it['id']}: media file missing for {it['art']}/{it['asset_type']} slot {it['asset_slot']}")
            continue
        if dry:
            log(f"DRY POST {it['id']} | {it['asset_type']} {f.name} | cap={len(it['ig_caption'])}ch")
            ok_n += 1
            continue
        try:
            if it["asset_type"] == "video":
                url = raw_url(f, _repo(), _branch())
                post_id = IG.publish_reel(os.environ["IG_USER_ID"], url, it["ig_caption"])
            else:
                dest = IG.crop_to_45(f, C.MEDIA_IG_DIR / it["art"])
                new_crops = new_crops or not _was_committed(dest)
                url = raw_url(dest, _repo(), _branch())
                post_id = IG.publish_image(os.environ["IG_USER_ID"], url, it["ig_caption"])
            log(f"OK {it['id']} -> IG {post_id}")
            mark(state, it["id"], True)
            ok_n += 1
        except Exception as e:
            log(f"FAIL {it['id']}: {e}")
            mark(state, it["id"], False, str(e)[:200])
            fail_n += 1
    save_state(state)
    if new_crops and not dry:
        git_commit(f"media: new 4:5 IG crops {today}")
    git_commit(f"state: ig {today} ok={ok_n} fail={fail_n}")


def _was_committed(path: Path) -> bool:
    r = subprocess.run(["git", "ls-files", "--error-unmatch", str(path.relative_to(C.ROOT))],
                       cwd=C.ROOT, capture_output=True, text=True)
    return r.returncode == 0


def _repo() -> str:
    global REPO
    if not REPO:
        REPO = __import__("os").environ.get("GITHUB_REPOSITORY", "OWNER/REPO")
    return REPO


def _branch() -> str:
    global BRANCH
    if not BRANCH:
        import os
        BRANCH = os.environ.get("AURELIAN_BRANCH") or os.environ.get("GITHUB_REF_NAME", "main")
        if not BRANCH or BRANCH == "null":
            BRANCH = "main"
    return BRANCH


def main():
    global REPO, BRANCH
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--platform", choices=["all", "pinterest", "ig"], default="all")
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    REPO = __import__("os").environ.get("GITHUB_REPOSITORY")
    BRANCH = __import__("os").environ.get("AURELIAN_BRANCH") or __import__("os").environ.get("GITHUB_REF_NAME", "main")

    today = args.date or today_str()
    schedule = load_schedule()
    state = load_state()
    log(f"Aurelian Auto-Poster | today={today} | dry={args.dry_run} | platform={args.platform}")
    log(f"Schedule: {len(schedule)} items | posted={len(state.get('posted', []))}")

    posted_before = len(state.get("posted", []))
    due_total = 0

    if args.platform in ("all", "pinterest"):
        pins = pick_due_items(schedule, today, state, "pinterest", SETTINGS["max_pinterest_per_run"])
        log(f"Pinterest due: {len(pins)}")
        due_total += len(pins)
        post_pinterest_items(pins, args.dry_run, state, today)

    if args.platform in ("all", "ig"):
        igs = pick_due_items(schedule, today, state, "ig", SETTINGS["max_ig_per_run"])
        log(f"Instagram due: {len(igs)}")
        due_total += len(igs)
        post_ig_items(igs, args.dry_run, state, today)

    state2 = load_state()
    posted_this_run = len(state2.get("posted", [])) - posted_before
    log(f"DONE. total posted={len(state2.get('posted', []))} failed={len(state2.get('failed', []))} | this run: due={due_total} posted={posted_this_run}")

    # LOUD FAILURE (v1.1): due items existed but ZERO posts went live -> this run is a
    # FAILURE, not a success. Exit 1 makes the run RED so GitHub emails the owner.
    if not args.dry_run and due_total > 0 and posted_this_run == 0:
        log("=" * 60)
        log("ZERO POSTS WENT LIVE despite due items - marking this run FAILED (exit 1).")
        log("Check the lines above: missing secrets, bad token permissions or media errors.")
        log("=" * 60)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
