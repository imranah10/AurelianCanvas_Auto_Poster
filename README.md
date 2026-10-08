# Aurelian Auto-Poster 🤖🎨

A fully automated, 90-day content publishing pipeline for the **Aurelian Canvas**
digital art store — built on GitHub Actions. It posts to **Pinterest and
Instagram every day, hands-free**, with zero paid infrastructure.

| What | Count |
|------|-------|
| Plan length | 90 days (Day 1 = 2026-10-09 → Day 90 = 2027-01-06) |
| Pinterest | 4 pins/day = **360 pins** (7 art products × caption variants + bundle collages) |
| Instagram | 1 reel/post/day = **90 posts** (42 reels + 48 image posts) |
| Media managed | 67 files (46 images + 21 reels), 4:5 auto-crop for IG |
| Boards | Auto-created by the bot (22 boards pre-configured) |
| Captions | Per-post hooks + hashtags, stored inline in the schedule |
| Links | Every pin deep-links to the matching Gumroad product or bundle |
| Cost | ₹0 — free forever, no SaaS subscription needed |

---

## How It Works

```
┌────────────────────┐    ┌──────────────────────┐    ┌─────────────────────┐
│  GitHub Actions     │    │  poster.py            │    │  Platform APIs      │
│  cron: 2x daily     │ →  │  reads schedule.json  │ →  │  Pinterest API v5   │
│  04:00 & 14:30 UTC  │    │  picks due posts      │    │  Instagram Graph API│
└────────────────────┘    │  resolves media files │    └─────────────────────┘
                          │  posts + logs state   │
                          └──────────────────────┘
```

1. **GitHub Actions** wakes a runner twice a day (9:30 AM IST and 8:00 PM IST).
2. **`poster.py`** loads `data/schedule.json` — a pre-generated plan of 450 posts,
   each with platform, art slug, media slot, caption, hashtags and Gumroad link.
3. **`resolve_asset()`** maps each post to a real media file with slot-cycling
   (fewer files than slots? it wraps around — nothing ever skips).
4. Instagram images are **auto-cropped to 4:5** (`ig_api.crop_to_45`) and cached
   in `media-ig/`; reels are published straight from raw GitHub URLs.
5. Every outcome is written to `state/posted.json` — the pipeline is
   **idempotent and catch-up safe**: missed days are posted on the next run,
   duplicates are never sent twice.

---

## Repository Structure

```
├── SETUP-GUIDE.md                  ← full step-by-step setup (English)
├── .github/workflows/auto-post.yml ← the robot's schedule + manual trigger
├── scripts/
│   ├── poster.py                   ← main entry point (CLI: --dry-run --platform --date)
│   ├── ap_common.py                ← schedule/state/media helpers
│   ├── ig_api.py                   ← Instagram Graph API (container → publish flow)
│   ├── pinterest_api.py            ← Pinterest API v5 (incl. video pin upload)
│   ├── pinterest_setup.py          ← OAuth helper to mint the refresh token
│   ├── captions_bank.py            ← all captions/hashtags source
│   └── gen_schedule.py             ← regenerates the 450-post plan
├── config/
│   ├── products.json               ← 7 art products + 4 bundles + Gumroad links
│   └── settings.json               ← timings, per-run caps, board map
├── data/schedule.json              ← the 450-post plan (auto-generated)
├── media/                          ← 67 media files (8 art-slug folders)
├── state/posted.json               ← run diary (idempotency guard)
└── n8n/aurelian-autopost.json      ← optional self-hosted n8n alternative
```

---

## Two Automations, One Pipeline

### 1. GitHub Actions (production)
The primary system. A single `auto-post.yml` workflow drives everything:
scheduled cron runs + `workflow_dispatch` manual runs with `dry_run` and
`platform` inputs. All credentials live in **encrypted GitHub repository
secrets** — nothing sensitive is ever committed.

### 2. n8n (self-hosted alternative)
`n8n/aurelian-autopost.json` is an 8-node workflow implementing the same
pipeline visually: **Schedule trigger → Fetch schedule (HTTP) → Pick today's
posts (Code) → IF Pinterest → Create Pin / IG Create Container → Wait 20s →
IG Publish**. Point it at the same `schedule.json` raw URL and it runs the
identical plan from any self-hosted n8n instance.

---

## Reliability Features

- **Dry-run mode** — full simulation (media resolution, captions, scheduling)
  without posting; used to validate everything before going live.
- **Graceful degradation** — missing platform secrets or media files are
  skipped with a logged reason; one broken post never blocks the batch.
- **Idempotent state** — `state/posted.json` records every OK/FAIL with the
  error message; re-runs never double-post.
- **Catch-up scheduling** — turn your laptop off for a week; the next run
  publishes everything that came due.
- **Token rotation** — Pinterest refresh tokens are rotated automatically and
  persisted back to GitHub Secrets (via `GH_PAT`) when the platform issues
  a new one.
- **Never-expiring page token** — Instagram publishing uses a long-lived
  Facebook Page access token (`expires_at = 0`), so the pipeline does not
  depend on any 60-day user token.

---

## Quick Start

1. Follow **SETUP-GUIDE.md** (Steps 1–7, one-time ~60–90 min).
2. Test: repo **Actions → Run workflow → dry_run = true** → check logs.
3. Go live: run again with **dry_run = false** (or just wait for cron).

## Customization

- **Timing** → cron lines in `.github/workflows/auto-post.yml` (UTC).
- **Posts per day** → `config/settings.json`.
- **Captions** → edit `scripts/captions_bank.py`, re-run
  `python3 scripts/gen_schedule.py` (media and state are untouched).
- **New art product** → add to `config/products.json`, drop a folder in
  `media/`, extend the captions bank, regenerate the schedule.

## Ground Rules

- Keep the repo **public** — platforms fetch media from raw URLs.
- Never rename folders inside `media/` — the schedule resolves by slug.
- Never hand-edit `state/posted.json` — it is the duplicate-post guard.
- Store credentials only in GitHub **Secrets**, never in files.
