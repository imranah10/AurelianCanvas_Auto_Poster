#!/usr/bin/env python3
"""Builds data/schedule.json - the full 90-day posting plan with captions inline.
Run once locally (or re-run any time): python3 scripts/gen_schedule.py
Day 1 = settings.start_date. Rotation is deterministic so posts are varied and repeat
visits to the same asset always get a fresh caption/variant."""
import json
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ap_common import ROOT, SETTINGS, PRODUCTS, log
from captions_bank import (ART_CONTENT, BUNDLE_PINS, BUNDLE_IG_CAPS, REPEAT_PS,
                           SHARED_DESC_INFO)

ARTS = list(PRODUCTS["products"].keys())  # 7 arts, stable order
BUNDLES = list(PRODUCTS["bundles"].keys())  # 4 bundles, stable order
BUNDLE_BOARDS = {
    "gold-series-duo": "Gold Leaf Wall Art",
    "luxe-abstract-duo": "Modern Luxury Decor",
    "storybook-diptych": "Cottagecore Aesthetic",
    "full-collection": "Printable Wall Art",
}
# Per-art round sequence (13 rounds ~ 90 days / 7 arts)
ROUNDS_SEQ = [("video", 1), ("video", 2), ("video", 3),
              ("image", 1), ("image", 2), ("image", 3), ("image", 4), ("image", 5), ("image", 6),
              ("video", 1), ("video", 2), ("video", 3), ("image", 1)]


def build_ig_items():
    items = []
    total_days = SETTINGS["plan_days"]
    for d in range(1, total_days + 1):
        art = ARTS[(d - 1) % len(ARTS)]
        rnd = (d - 1) // len(ARTS)  # 0-based round
        asset_type, slot = ROUNDS_SEQ[rnd]
        ac = ART_CONTENT[art]
        if asset_type == "image":
            cap = ac["ig_image_caps"][(slot - 1) % len(ac["ig_image_caps"])]
        else:
            cap = ac["ig_reel_caps"][(slot - 1) % len(ac["ig_reel_caps"])]
            if rnd >= 9:  # second pass on reels: add rotating PS
                cap = cap + "\n\n" + REPEAT_PS[(d - 1) % len(REPEAT_PS)]
        date = (date0 + timedelta(days=d - 1)).isoformat()
        items.append({
            "id": f"IG-D{d:03d}", "seq": 1, "day": d, "date": date, "platform": "ig",
            "art": art, "asset_type": asset_type, "asset_slot": slot,
            "ig_caption": f"{cap}\n\n{ac['hashtags']}",
        })
    return items


def build_pinterest_items():
    items = []
    total_days = SETTINGS["plan_days"]
    pins_per_day = SETTINGS["pinterest_pins_per_day"]
    # interleaved asset list: rotate across arts so consecutive pins differ
    assets = []
    for slot in range(1, 10):
        a_type = "video" if slot <= 3 else "image"
        s = slot if slot <= 3 else slot - 3
        for art in ARTS:
            assets.append((art, a_type, s))
    # 63 entries; boards rotate every 3 pins, caption variant every full cycle
    pin_i = 0
    for d in range(1, total_days + 1):
        date = (date0 + timedelta(days=d - 1)).isoformat()
        slots_today = list(range(1, pins_per_day + 1))
        if d % 7 == 0:  # weekly collage pin for bundles
            b = BUNDLES[(d // 7 - 1) % len(BUNDLES)]
            bp = BUNDLE_PINS[b]
            items.append({
                "id": f"PIN-D{d:03d}-0", "seq": 0, "day": d, "date": date,
                "platform": "pinterest", "art": "bundles", "asset_type": "image",
                "asset_slot": (d // 7 - 1) % 4 + 1, "board": BUNDLE_BOARDS[b],
                "link": f"{PRODUCTS['base_url']}{b}",
                "pin_title": bp["title"], "pin_description": bp["desc"],
            })
            slots_today = slots_today[1:]  # 3 art pins on bundle days
        for s in slots_today:
            art, a_type, a_slot = assets[pin_i % len(assets)]
            variant = (pin_i // len(assets)) % 6
            ac = ART_CONTENT[art]
            title = ac["pin_titles"][variant]
            desc = ac["desc_seed"] + " " + ac["alt_hooks"][variant] + " " + \
                SHARED_DESC_INFO[(pin_i + variant) % len(SHARED_DESC_INFO)]
            board = PRODUCTS["products"][art]["boards"][variant % 4]
            items.append({
                "id": f"PIN-D{d:03d}-{s}", "seq": s, "day": d, "date": date,
                "platform": "pinterest", "art": art, "asset_type": a_type,
                "asset_slot": a_slot, "board": board,
                "link": f"{PRODUCTS['base_url']}{art}",
                "pin_title": title, "pin_description": desc,
            })
            pin_i += 1
    return items


if __name__ == "__main__":
    date0 = None
    from datetime import date as _date
    y, m, dd = (int(x) for x in SETTINGS["start_date"].split("-"))
    date0 = _date(y, m, dd)

    ig = build_ig_items()
    pins = build_pinterest_items()
    schedule = sorted(ig + pins, key=lambda x: (x["date"], x["platform"], x["seq"]))

    # validation
    problems = []
    for it in schedule:
        if it["platform"] == "pinterest":
            if len(it["pin_title"]) > 100:
                problems.append(f"{it['id']} title {len(it['pin_title'])}ch")
            if len(it["pin_description"]) > 800:
                problems.append(f"{it['id']} desc {len(it['pin_description'])}ch")
        else:
            if len(it["ig_caption"]) > 2200:
                problems.append(f"{it['id']} caption {len(it['ig_caption'])}ch")
    if problems:
        for p in problems[:20]:
            log("LIMIT ISSUE: " + p)
        sys.exit(1)

    out = ROOT / "data" / "schedule.json"
    out.write_text(json.dumps(schedule, indent=1, ensure_ascii=False), encoding="utf-8")
    log(f"Schedule written: {out} ({out.stat().st_size // 1024} KB)")
    log(f"IG items: {len(ig)} | Pinterest items: {len(pins)} | total {len(schedule)}")
    vids = sum(1 for it in schedule if it["asset_type"] == "video")
    log(f"Video-based items: {vids} | Image-based: {len(schedule) - vids}")
    for art in ARTS + ["bundles"]:
        n = sum(1 for it in schedule if it["art"] == art)
        log(f"  {art}: {n} posts")
