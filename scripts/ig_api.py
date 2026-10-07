#!/usr/bin/env python3
"""Instagram posting via Graph API (Content Publishing).
Requires: IG account switched to BUSINESS type + linked to a Facebook Page.
Secrets/env: IG_USER_ID, PAGE_ACCESS_TOKEN. Optional: DRY_RUN."""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

from ap_common import MEDIA_IG_DIR, log

GRAPH = "https://graph.facebook.com/v21.0"
MAX_CAPTION = 2200


def _req(method: str, url: str, params: dict = None, timeout: int = 60):
    data = None
    if params is not None:
        qs = urllib.parse.urlencode(params)
        if method == "GET":
            url = f"{url}?{qs}"
        else:
            data = qs.encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:500]
        raise RuntimeError(f"IG HTTP {e.code}: {body}") from None


def _token() -> str:
    import os
    tok = os.environ.get("PAGE_ACCESS_TOKEN", "")
    if not tok:
        raise RuntimeError("PAGE_ACCESS_TOKEN secret not set")
    return tok


def crop_to_45(src: Path, dest_dir: Path) -> Path:
    """Center-crop images taller than 4:5 down to exactly 4:5 (IG minimum ratio).
    Landscape/square images are left untouched (IG accepts up to 1.91:1 wide).
    Returns cached file path."""
    from PIL import Image
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{src.stem}_45{src.suffix.lower()}"
    if dest.exists():
        return dest
    img = Image.open(src)
    if img.mode in ("P", "RGBA"):
        img = img.convert("RGB")
    w, h = img.size
    if w / h >= 0.74:  # within IG limits (4:5 = 0.8, with tolerance)
        img.save(dest, quality=92)
        return dest
    new_h = int(w * 1.25)  # exact 4:5
    top = max(0, (h - new_h) // 3)  # slightly above center keeps art subject visible
    img = img.crop((0, top, w, top + new_h))
    img.save(dest, quality=92)
    return dest


def publish_image(ig_user_id: str, image_url: str, caption: str) -> str:
    tok = _token()
    r = _req("POST", f"{GRAPH}/{ig_user_id}/media",
             {"image_url": image_url, "caption": caption[:MAX_CAPTION], "access_token": tok})
    container = r["id"]
    log(f"  IG image container {container} created, publishing...")
    r2 = _req("POST", f"{GRAPH}/{ig_user_id}/media_publish",
              {"creation_id": container, "access_token": tok})
    return r2["id"]


def publish_reel(ig_user_id: str, video_url: str, caption: str, poll_seconds: int = 300) -> str:
    tok = _token()
    r = _req("POST", f"{GRAPH}/{ig_user_id}/media",
             {"media_type": "REELS", "video_url": video_url,
              "caption": caption[:MAX_CAPTION], "share_to_feed": "true",
              "access_token": tok})
    container = r["id"]
    log(f"  IG reel container {container} created, waiting for processing...")
    deadline = time.time() + poll_seconds
    status = None
    while time.time() < deadline:
        s = _req("GET", f"{GRAPH}/{container}", {"fields": "status_code", "access_token": tok})
        status = s.get("status_code")
        if status == "FINISHED":
            break
        if status == "ERROR":
            raise RuntimeError(f"IG reel processing failed for container {container}")
        time.sleep(15)
    if status != "FINISHED":
        raise RuntimeError(f"IG reel not ready after {poll_seconds}s (status={status})")
    r2 = _req("POST", f"{GRAPH}/{ig_user_id}/media_publish",
              {"creation_id": container, "access_token": tok})
    return r2["id"]


def post_item(item: dict, image_url: str = None, video_url: str = None) -> str:
    ig_user = __import__("os").environ.get("IG_USER_ID", "")
    if not ig_user:
        raise RuntimeError("IG_USER_ID secret not set")
    caption = item["ig_caption"]
    if item.get("asset_type") == "video":
        return publish_reel(ig_user, video_url, caption)
    return publish_image(ig_user, image_url, caption)
