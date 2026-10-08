# 🚀 AURELIAN AUTO-POSTER — COMPLETE SETUP GUIDE

This system publishes your 90-day content plan (450 posts: 90 Instagram +
360 Pinterest) **automatically every day through GitHub** — no n8n needed,
no trial expirations, free forever.

```
Your job:                     The robot's job (daily, automatic):
─────────────                 ──────────────────────────────
One-time setup (60-90 min)    4 Pinterest pins / day (auto)
Upload media to the repo      1 Instagram reel/post / day (auto)
Add tokens once               Captions + hashtags + links all included
                              Boards are auto-created
                              Every post is logged in the state file
```

**How it runs:** GitHub wakes twice a day (9:30 AM and 8:00 PM Indian time),
runs a small script that reads `data/schedule.json`, picks today's posts, and
publishes them to Instagram + Pinterest using your stored tokens.

---

## STEP 1 — Convert Instagram to a BUSINESS account (2 min)

API posting requires a **Business** account (Creator is not enough):

1. Instagram app → Profile → menu (☰) → **Settings and privacy**
2. Scroll down → **Account type and tools** → **Switch to professional account**
3. Choose **Business** (not Creator) → Category: **Digital creator** works fine
4. If asked to **connect a Facebook Page**:
   - If you have a Page, choose it. If not, **"Create new Page"** with the
     name `AurelianCanvas`. (The Page is only a technical bridge — you never
     have to manage it.)

⚠️ Do this step first — without it Step 4 will not work.

---

## STEP 2 — Create a Pinterest Developer App (5 min)

1. Open **https://developers.pinterest.com** in a browser
2. Log in with the Pinterest **Business** account (AurelianCanvas)
3. **App management** / **"Connect app"** → create a new app:
   - App name: `Aurelian Canvas Poster`
   - Description: `Auto posting for Aurelian Canvas`
4. When the app opens, COPY two values:
   - **App ID** → this becomes `PINTEREST_CLIENT_ID`
   - **App secret** → this becomes `PINTEREST_CLIENT_SECRET`
5. In the app's **Settings/Dashboard**, set the **Redirect URI** to:
   ```
   https://localhost/callback
   ```

---

## STEP 3 — Mint the Pinterest token (10 min)

A helper script ships in the repo: `scripts/pinterest_setup.py`

**Method A (Python installed):**
```
python3 scripts/pinterest_setup.py
```
It asks for your App ID, Secret, and a CODE. To get the code:

1. Open this URL in a browser (replace `APP_ID_HERE` with your App ID):
```
https://www.pinterest.com/oauth/?response_type=code&redirect_uri=https://localhost/callback&consumer_id=APP_ID_HERE&scope=boards:read,boards:write,pins:read,pins:write,user_accounts:read&refreshable=true
```
2. Pinterest shows a permissions screen → click **Allow/Grant**
3. The browser shows an error page (`localhost` can't be reached) — **this is
   NORMAL!** Look at the **address bar**:
   ```
   https://localhost/callback?code=pina_xxxxxxxxxx&...
   ```
   COPY everything after `code=` (up to the next `&`).
4. Paste the code into the script → it prints your **REFRESH TOKEN**.

**Method B (no Python):** after extracting the code, run in Command Prompt
(fill in all three placeholders):
```
curl -X POST https://api.pinterest.com/v5/oauth/token -H "Authorization: Basic BASE64_HERE" -d "grant_type=authorization_code&code=CODE_HERE&redirect_uri=https://localhost/callback"
```
(`BASE64_HERE` = base64 of `APP_ID:APP_SECRET` — if unsure, use Method A.)

✅ You now have: **PINTEREST_REFRESH_TOKEN** (the long-lived token)

---

## STEP 4 — Instagram tokens via Meta (15 min)

Four short browser steps:

**4a. Create the Meta app:**
1. Open **https://developers.facebook.com** → log in
2. **My Apps → Create App** → type: **Business** → name: `Aurelian Poster`
3. In the use-case wizard select **"Manage messaging & content on
   Instagram"**, and also add **"Manage everything on your Page"**
   (Page permissions like `pages_show_list` live in that second use case)
4. Copy **App ID** and **App Secret** (App settings → Basic) — save them

**4b. Generate a short token (Graph API Explorer):**
1. Open **https://developers.facebook.com/tools/explorer/**
2. Top right: select your app `Aurelian Poster`
3. Add these permissions (old-style names — the `instagram_business_*`
   variants belong to a different login flow and may be rejected):
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_show_list`
   - `pages_read_engagement`
4. Click **Generate Access Token** → approve every popup (allow all)
5. COPY the token it produces (a short-lived token)

**4c. Exchange for a 60-day token (open in browser):**
```
https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=SHORT_TOKEN
```
→ JSON appears: `{"access_token":"EAA...",...}` — copy this new token
(valid 60 days).

**4d. Get the Page token + IG user ID (two browser URLs):**

URL 1 (paste the 4c token):
```
https://graph.facebook.com/v21.0/me/accounts?access_token=LONG_TOKEN
```
→ Find your Facebook Page in the JSON and COPY: `"access_token"`
(the Page token — **this one never expires**; this is your
`PAGE_ACCESS_TOKEN`) and `"id"` (the PAGE_ID).

URL 2 (insert PAGE_ID):
```
https://graph.facebook.com/v21.0/PAGE_ID?fields=instagram_business_account&access_token=PAGE_TOKEN
```
→ `instagram_business_account: { "id": "1784..." }` — that ID is your
**IG_USER_ID**.

✅ You now have: **PAGE_ACCESS_TOKEN** + **IG_USER_ID**

⚠️ If URL 2 shows no `instagram_business_account` — Step 1 (business switch
+ Page↔Instagram link) is incomplete. Re-do Step 1: connect the Instagram
profile to the Facebook Page (Meta will offer "Add to business portfolio"
— accept it).

---

## STEP 5 — Repo + media upload (15 min)

✅ **GOOD NEWS — THIS STEP IS ALREADY DONE:** the repo
**https://github.com/imranah10/AurelianCanvas_Auto_Poster** exists and all
scripts/config/data/workflow files are pushed. Steps below remain only as
reference for future re-uploads.

1. Repo: **https://github.com/imranah10/AurelianCanvas_Auto_Poster**
   (visibility must stay **PUBLIC** — platforms download media from raw
   URLs; a private repo breaks posting)
2. To upload files: **Add file → Upload files** → drag-and-drop
3. Your 67 generated files go under `media/` following
   `media/README-MEDIA.txt`: one folder per art slug (exact names), images
   + final joined reels in the same folder, the 4 bundle collages in
   `media/bundles/`
4. Click **Commit changes**

📁 **Easiest media upload method (GitHub Desktop):**
1. Install from **https://desktop.github.com**
2. **File → Clone repository** → choose `imranah10/AurelianCanvas_Auto_Poster`
3. Copy your 67 files into the repo's `media/` folders per the naming rules
4. GitHub Desktop shows the changes → summary: `media add` →
   **Commit to main** → **Push origin** — DONE (no 25 MB web limit)

---

## STEP 6 — Add GitHub Secrets (10 min)

Repo page: **Settings → Secrets and variables → Actions →
New repository secret** — create these:

| Name | Value |
|------|-------|
| `PINTEREST_CLIENT_ID` | App ID from Step 2 |
| `PINTEREST_CLIENT_SECRET` | App Secret from Step 2 |
| `PINTEREST_REFRESH_TOKEN` | Refresh token from Step 3 |
| `IG_USER_ID` | `1784...` ID from Step 4d |
| `PAGE_ACCESS_TOKEN` | Page token from Step 4d (never expires) |
| `GH_PAT` | From Step 6b below (optional — token auto-rotation) |
| `AURELIAN_BRANCH` | `main` |

**6b. Create GH_PAT (for Pinterest token auto-rotation):**
1. **https://github.com/settings/personal-access-tokens/new**
2. Token name: `autoposter` → Expiration: 90 days
3. **Only select repositories** → pick `AurelianCanvas_Auto_Poster`
4. **Permissions**: `Secrets: Read and write`, `Contents: Read and write`
5. Generate → copy → paste into the `GH_PAT` secret

---

## STEP 7 — TEST (5 min)

1. Open the repo's **Actions** tab → enable workflows if asked
2. Left sidebar: **Aurelian Auto-Poster** → **Run workflow**
3. Set `dry_run` = **true**, platform = `all` → **Run workflow**
4. Open the run and read the logs:
   - You should see `DRY POST PIN-D001-1 | Renaissance Decor | ...`
   - `media missing` means a folder/file name mismatch — fix names exactly

Dry-run behaves like the real thing except it doesn't publish. When it's
green: run again with `dry_run` = **false** and watch posts go live! 🎉

---

## STEP 8 — DAILY OPERATION (0 min)

Do nothing. GitHub runs automatically:
- **9:30 AM IST** — 2 Pinterest pins
- **8:00 PM IST** — 2 Pinterest pins + 1 Instagram post

Once a week, open both apps to check notifications and likes.

---

## 🩹 TROUBLESHOOTING

| Problem | Meaning | Fix |
|---------|---------|-----|
| IG: "must be a business account" | Business switch not done | Redo Step 1 |
| IG: no instagram_business_account in 4d | Page↔IG link missing | Step 1 Page connect ("Add to portfolio") |
| Pinterest: 401 unauthorized | Refresh token expired/bad | Redo Step 3 |
| Pin images blank | Repo private OR wrong media path | Make repo public / check folder names |
| "media missing" in logs | Folder/file naming mismatch | Follow `media/README-MEDIA.txt` exactly |
| Workflow missing in Actions | Not enabled | Enable via Step 7 |
| Some days skipped | PC off or an error — fine | Next run catch-up publishes due posts |

## ⛔ NEVER DO THIS

- Don't make the repo **private** (media URLs must be publicly fetchable)
- Don't paste secrets into any file — **GitHub Secrets only**
- Don't hand-edit `state/posted.json` (duplicate-post guard)
- Don't rename folders in `media/` (schedule resolves by exact slug)
- Don't reduce app permissions in Meta/Pinterest dashboards

## 🔐 SECURITY NOTE

All tokens live in GitHub **Secrets** — encrypted at rest; even you cannot
view them again (only replace). The Pinterest token is refreshed
automatically by the robot (that's what `GH_PAT` enables). The public repo
contains only media and captions — no secrets.

## 📞 If you get stuck

Steps 1, 2 and 5 are the easy ones. Steps 3–4 (tokens) are the technical
ones — go slowly, open one URL at a time, copy outputs as you go. If a step
fails, screenshot it and work through the fix line by line.
