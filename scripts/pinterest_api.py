#!/usr/bin/env python3
"""Pinterest posting via Pinterest API v5 (image pins + video pins + board management).
Env: PINTEREST_ACCESS_TOKEN (and PINTEREST_CLIENT_ID / PINTEREST_CLIENT_SECRET for refresh)."""
import base64
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

from ap_common import log

API = "https://api.pinterest.com/v5"


def _req(method: str, path: str, token: str, body: dict = None, form=None,
         headers: dict = None, timeout: int = 90, raw=False):
    url = f"{API}{path}"
    data = None
    hdrs = {"Authorization": f"Bearer {token}"}
    if form is not None:  # multipart bytes already built
        data, extra_hdr = form
        hdrs.update(extra_hdr)
    elif body is not None:
        data = json.dumps(body).encode()
        hdrs["Content-Type"] = "application/json"
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            payload = r.read().decode()
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Pinterest HTTP {e.code}: {e.read().decode()[:500]}") from None


def refresh_access_token() -> dict:
    """Rotate tokens. Returns {'access_token':..., 'refresh_token':...}.
    Caller must persist new refresh_token (GitHub secret update)."""
    cid = os.environ.get("PINTEREST_CLIENT_ID", "")
    csec = os.environ.get("PINTEREST_CLIENT_SECRET", "")
    rtok = os.environ.get("PINTEREST_REFRESH_TOKEN", "")
    if not (cid and csec and rtok):
        raise RuntimeError("Pinterest OAuth secrets missing (CLIENT_ID/CLIENT_SECRET/REFRESH_TOKEN)")
    basic = base64.b64encode(f"{cid}:{csec}".encode()).decode()
    data = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": rtok,
                                   "scopes": "boards:read,boards:write,pins:read,pins:write,user_accounts:read"}).encode()
    req = urllib.request.Request(f"{API}/oauth/token", data=data, method="POST",
                                 headers={"Authorization": f"Basic {basic}",
                                          "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Pinterest refresh HTTP {e.code}: {e.read().decode()[:400]}") from None


def list_boards(token: str) -> dict:
    names = {}
    bookmark = None
    while True:
        path = "/boards?page_size=100" + (f"&bookmark={bookmark}" if bookmark else "")
        r = _req("GET", path, token)
        for b in r.get("items", []):
            names[b["name"]] = b["id"]
        bookmark = r.get("bookmark")
        if not bookmark:
            break
    return names


def ensure_board(token: str, name: str, description: str) -> str:
    boards = list_boards(token)
    if name in boards:
        return boards[name]
    log(f"  Creating Pinterest board: {name}")
    r = _req("POST", "/boards", token, {"name": name, "description": description[:500]})
    return r["id"]


def create_image_pin(token: str, board_id: str, title: str, description: str,
                     link: str, image_url: str) -> str:
    body = {"board_id": board_id, "title": title[:100], "description": description[:800],
            "link": link,
            "media_source": {"media_type": "static", "items": [{"url": image_url}]}}
    r = _req("POST", "/pins", token, body)
    return r["id"]


def _upload_video(token: str, file_path: Path) -> str:
    """3-step Pinterest video upload: register -> S3 PUT -> poll -> media_id."""
    r = _req("POST", "/media", token, {"media_type": "video"})
    media_id = r["media_id"]
    up_url = r["upload_url"]
    up_params = r.get("upload_parameters", {})
    # Build multipart/form-data manually (S3 POST policy form)
    boundary = "----AurelianBoundary7d1a2c"
    parts = []
    for k, v in up_params.items():
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    file_bytes = file_path.read_bytes()
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{file_path.name}"\r\nContent-Type: video/mp4\r\n\r\n'.encode())
    parts.append(file_bytes)
    parts.append(f"\r\n--{boundary}--\r\n".encode())
    body = b"".join(parts)
    req = urllib.request.Request(up_url, data=body, method="POST",
                                 headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        resp.read()
    deadline = time.time() + 900
    while time.time() < deadline:
        s = _req("GET", f"/media/{media_id}", token)
        st = s.get("status")
        if st == "processed":
            return media_id
        if st == "failed":
            raise RuntimeError(f"Pinterest video processing failed ({s.get('message')})")
        time.sleep(20)
    raise RuntimeError("Pinterest video processing timeout")


def create_video_pin(token: str, board_id: str, title: str, description: str,
                     link: str, video_file: Path, cover_url: str = None) -> str:
    media_id = _upload_video(token, video_file)
    ms = {"media_type": "video", "items": [{"media_id": media_id}]}
    if cover_url:
        ms["cover_image_url"] = cover_url
    body = {"board_id": board_id, "title": title[:100], "description": description[:800],
            "link": link, "media_source": ms}
    r = _req("POST", "/pins", token, body)
    return r["id"]


def post_item(item: dict, token: str, board_map: dict, board_desc: dict,
              image_url: str, video_file: Path = None) -> str:
    board_name = item["board"]
    if board_name not in board_map:
        board_map[board_name] = ensure_board(token, board_name, board_desc.get(board_name, ""))
    board_id = board_map[board_name]
    if item["asset_type"] == "video":
        return create_video_pin(token, board_id, item["pin_title"], item["pin_description"],
                                item["link"], video_file, cover_url=image_url)
    return create_image_pin(token, board_id, item["pin_title"], item["pin_description"],
                            item["link"], image_url)
