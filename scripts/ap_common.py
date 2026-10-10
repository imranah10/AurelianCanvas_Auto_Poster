#!/usr/bin/env python3
"""Aurelian Canvas Auto-Poster - common utilities."""
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
SETTINGS = json.loads((ROOT / "config" / "settings.json").read_text(encoding="utf-8"))
PRODUCTS = json.loads((ROOT / "config" / "products.json").read_text(encoding="utf-8"))
STATE_FILE = ROOT / "state" / "posted.json"
SCHEDULE_FILE = ROOT / "data" / "schedule.json"
MEDIA_DIR = ROOT / "media"
MEDIA_IG_DIR = ROOT / "media-ig"

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
VID_EXTS = {".mp4", ".mov", ".webm"}

BASE_URL = PRODUCTS["base_url"]


def log(msg: str) -> None:
    print(f"[{datetime.now(ZoneInfo('UTC')).strftime('%Y-%m-%d %H:%M:%S')}Z] {msg}", flush=True)


def today_str() -> str:
    tz = ZoneInfo(SETTINGS["timezone"])
    return datetime.now(tz).strftime("%Y-%m-%d")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"posted": [], "failed": []}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")


def load_schedule() -> list:
    if not SCHEDULE_FILE.exists():
        log(f"FATAL: {SCHEDULE_FILE} not found. Run scripts/gen_schedule.py first.")
        sys.exit(1)
    return json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))


def scan_art_media(art: str) -> dict:
    """Return {'images': [Path...], 'videos': [Path...]} sorted alphabetically for an art slug.
    Part files (part1/part2) are ignored - upload only the JOINED final reels."""
    folder = MEDIA_DIR / art
    out = {"images": [], "videos": []}
    if not folder.is_dir():
        return out
    for f in sorted(folder.rglob("*")):
        if not f.is_file():
            continue
        name = f.name.lower()
        if "part1" in name or "part2" in name or name.startswith("."):
            continue
        ext = f.suffix.lower()
        if ext in IMG_EXTS:
            out["images"].append(f)
        elif ext in VID_EXTS:
            out["videos"].append(f)
    return out


def resolve_asset(art: str, asset_type: str, slot: int):
    """Resolve (art, asset_type, slot) to a real file Path or None."""
    media = scan_art_media(art)
    files = media["videos"] if asset_type == "video" else media["images"]
    if not files:
        return None
    slot = ((slot - 1) % len(files)) + 1  # wrap around if fewer files uploaded
    return files[slot - 1]


def raw_url(path: Path, repo: str, branch: str) -> str:
    rel = path.relative_to(ROOT).as_posix()
    quoted = "/".join(__import__("urllib.parse", fromlist=["quote"]).quote(p) for p in rel.split("/"))
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{quoted}"


def pick_due_items(schedule: list, date: str, state: dict, platform: str, max_items: int) -> list:
    """Due = date <= today, not already posted (item_id), platform match, oldest first."""
    # state entries can be dicts ({"id":..,"at":..,"note":..}) or plain id strings
    posted = {e["id"] if isinstance(e, dict) else e for e in state.get("posted", [])}
    due = [it for it in schedule if it["date"] <= date and it["platform"] == platform]
    due.sort(key=lambda x: (x["date"], x["day"], x["seq"]))
    out = []
    for it in due:
        if it["id"] in posted:
            continue
        out.append(it)
        if len(out) >= max_items:
            break
    return out


def mark(state: dict, item_id: str, ok: bool, note: str = "") -> None:
    entry = {"id": item_id, "at": datetime.now(ZoneInfo("UTC")).isoformat(), "note": note}
    state.setdefault("posted" if ok else "failed", []).append(entry)
    if ok and entry["id"] in [f["id"] for f in state.get("failed", [])]:
        state["failed"] = [f for f in state["failed"] if f["id"] != item_id]


def art_link(art: str) -> str:
    return f"{BASE_URL}{art}"


def bundle_link(slug: str) -> str:
    return f"{BASE_URL}{slug}"
