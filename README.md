# Aurelian Auto-Poster 🤖🎨

**Aurelian Canvas ka 90-din posting robot** — GitHub Actions se roz apne aap
Pinterest + Instagram par content post karta hai. Free forever, n8n nahi chahiye.

| Kya | Kitna |
|-----|-------|
| Plan days | 90 (Day 1 = 2026-10-09, khatam 2027-01-06) |
| Pinterest | 4 pins/din = **360 pins** (7 arts × 6 caption variants + bundle collages) |
| Instagram | 1 reel/post/din = **90 posts** (reels pehle, phir mockups) |
| Media chahiye | 67 files (42 images + 21 reels + 4 bundle collages) |
| Boards | Robot khud banata hai (22 boards ready) |
| Captions | Inline schedule me — har post ka apna hook + hashtags |
| Links | Har pin direct Gumroad product/bundle par jata hai |

## Files

```
├── SETUP-GUIDE.md          ← PEHLE YE KHOLO (poora setup yahi se)
├── .github/workflows/auto-post.yml   (GitHub robot ka schedule)
├── scripts/
│   ├── poster.py           (main robot)
│   ├── gen_schedule.py     (90-din plan banane wala)
│   ├── captions_bank.py    (sab captions/captions ka bank)
│   ├── ig_api.py           (Instagram Graph API)
│   ├── pinterest_api.py    (Pinterest API v5, video upload bhi)
│   ├── ap_common.py        (helpers)
│   └── pinterest_setup.py  (token nikalne ka helper)
├── config/
│   ├── products.json       (7 arts + 4 bundles + links)
│   └── settings.json       (timing/counts — chaho to badlo)
├── data/schedule.json      (450 posts ka pura plan — auto-generated)
├── media/                  ← TUMHARI 67 FILES YAHAN JAAYENGI
├── state/posted.json       (robot ka diary — mat chhedo)
└── n8n/                    (optional n8n workflow — agar kabhi self-host karo)
```

## Quick Start (2 line)

1. `SETUP-GUIDE.md` kholo — Step 1 se Step 7 order me karo
2. Test: Actions → Run workflow → dry_run=true → logs dekho → phir false

## Customize karna

- **Timing badalni hai?** `.github/workflows/auto-post.yml` me cron lines
  (UTC me hain: `0 4` = 9:30 AM IST, `30 14` = 8:00 PM IST)
- **Posts per din?** `config/settings.json` me `pinterest_pins_per_day`
- **Captions badalni hain?** `scripts/captions_bank.py` edit karke
  `python3 scripts/gen_schedule.py` dobara chalao (media/state untouched
  rehte hain)
- **Naya art add karna?** `config/products.json` me entry + `media/` me
  folder + captions bank me content, phir schedule regenerate

## Backup plan

Agar GitHub Actions kabhi band karna ho: Actions → Aurelian Auto-Poster →
"..." → Disable workflow. Sab kuch waise ka waisa rehta hai.
