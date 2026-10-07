# 🚀 AURELIAN AUTO-POSTER — COMPLETE SETUP GUIDE (Hinglish)

Ye system tumhare 90-din ke content (450 posts: 90 Instagram + 360 Pinterest)
ko **GitHub ke through ROZ APNE AAP post karega** — n8n ki zaroorat nahi,
trial ka jhanjhat nahi, FREE FOREVER.

```
Tumhara kaam:                Robot ka kaam (roz, apne aap):
─────────────                ──────────────────────────────
Ek baar setup (60-90 min)    4 Pinterest pins / din (auto)
Media files repo me upload   1 Instagram reel/post / din (auto)
Ek baar tokens daal do       Captions + hashtags + links sab apne aap
                             Boards khud banata hai
                             Har post ka record state file me rakhta hai
```

**Kaise chalega:** GitHub roz 2 baar (subah 9:30 AM + shaam 8:00 PM Indian
time) ek chhota computer on karega jo `data/schedule.json` padhega, aaj ke
posts uthayega, tumhare tokens se Instagram + Pinterest par daal dega.

---

## STEP 1 — Instagram ko BUSINESS banao (2 min)

Tumhara account abhi **Creator** hai. API posting ke liye **Business**
chahiye:

1. Instagram app → Profile → menu (☰) → **Settings and privacy**
2. Neeche scroll → **Account type and tools** → **Switch to professional account**
   (ya "Switch account type" dikhe to wo)
3. **Business** chuno (Creator nahi) → Category: **Digital creator** theek hai
4. Agar **Facebook Page connect** karne ka puche:
   - Page hai to wo chuno. Page NAHI hai to **"Create new Page"** — naam
     `AurelianCanvas` rakho. (Page sirf technical link ke liye hai, usko
     manage nahi karna padega.)

⚠️ Ye step sabse pehle karo — bina iske Step 3 kaam nahi karega.

---

## STEP 2 — Pinterest Developer App banao (5 min)

1. Browser me kholo: **https://developers.pinterest.com**
2. Pinterest Business account (AurelianCanvas) se **log in** karo
3. **App management** ya **"Connect app"** → New app banao:
   - App name: `Aurelian Canvas Poster`
   - Description: `Auto posting for Aurelian Canvas`
4. App khulne par 2 cheezein COPY karo:
   - **App ID** → ye hai `PINTEREST_CLIENT_ID`
   - **App secret** → ye hai `PINTEREST_CLIENT_SECRET`
   (Notepad me save kar lo)
5. App ke **Settings/Dashboard** me **Redirect URI** wali jagah ye daalo:
   ```
   https://localhost/callback
   ```

---

## STEP 3 — Pinterest Token nikalo (10 min)

Repo me ek helper script di hai: `scripts/pinterest_setup.py`

**Tareeka A (Python hai computer me):**
```
python3 scripts/pinterest_setup.py
```
Ye tumse App ID, Secret, aur ek CODE mangega. Code aise nikalta hai:

1. Neeche wali URL browser me kholo — `APP_ID_YAHAN` ki jagah apna App ID:
```
https://www.pinterest.com/oauth/?response_type=code&redirect_uri=https://localhost/callback&consumer_id=APP_ID_YAHAN&scope=boards:read,boards:write,pins:read,pins:write,user_accounts:read&refreshable=true
```
2. Pinterest tumhe permissions dikhayega → **Allow/Grant** dabao
3. Browser ek error page dikhayega (`localhost` khul nahi sakta) — **ye
   NORMAL hai!** Sirf browser ke **address bar** me upar dekho:
   ```
   https://localhost/callback?code=pina_xxxxxxxxxx&...
   ```
   `code=` ke baad wala pura hissa (tak ki `&` se pehle) COPY karo.
4. Ye code script me paste karo → script tumhe **REFRESH TOKEN** dega.

**Tareeka B (agar Python nahi hai):** Step 3 ka code nikalne ke baad
Command Prompt (Windows) me ye chalao (teen jagah apni values daalo):
```
curl -X POST https://api.pinterest.com/v5/oauth/token -H "Authorization: Basic BASE64HERE" -d "grant_type=authorization_code&code=CODE_YAHAN&redirect_uri=https://localhost/callback"
```
(`BASE64HERE` = base64 of `APP_ID:APP_SECRET` — nahi pata to Tareeka A
use karo, wo khud handle karta hai)

✅ End me tumhare paas hoga: **PINTEREST_REFRESH_TOKEN** (lamba wala token)

---

## STEP 4 — Instagram Tokens nikalo (15 min)

Ye Meta ka process hai — 4 chhote browser steps. Ek-ek karke:

**4a. Meta App banao:**
1. Kholo: **https://developers.facebook.com** → Facebook account se login
2. **My Apps** → **Create App** → App type: **Business** → App name:
   `Aurelian Poster` → Create
3. App ke dashboard par **App ID** aur **App Secret** copy karo
   (Settings → Basic me App Secret dikhega) — Notepad me rakho

**4b. Short token lo:**
1. Kholo: **https://developers.facebook.com/tools/explorer/**
2. Right-top me apna app `Aurelian Poster` select karo
3. **Permissions** dropdown se YE CHAR permissions add karo:
   - `instagram_business_basic`
   - `instagram_business_content_publishing`
   - `pages_show_list`
   - `pages_read_engagement`
4. **Generate Access Token** dabao → popup allow karo (sab yes)
5. Jo token bana, usko COPY karo (ye SHORT token hai, agli step me use hoga)

**4c. Long token banao (browser me URL kholo):**
Neeche wali URL me 3 jagah apni values daal ke browser me kholo:
```
https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=SHORT_TOKEN
```
→ JSON dikhega: `{"access_token":"EAA...","token_type":...}` — ye naya
token **60 din** chalta hai. Copy karo.

**4d. Page token + IG ID nikalo (browser me 2 URL):**

URL 1 (LONG_TOKEN ki jagah 4c ka token):
```
https://graph.facebook.com/v21.0/me/accounts?access_token=LONG_TOKEN
```
→ JSON me tumhare Facebook Page ki list dikhegi. Us page ke entry se 2
cheezein COPY karo: `"access_token"` (page ka token — **ye kabhi expire
nahi hota**, yahi PAGE_ACCESS_TOKEN hai) aur `"id"` (ye hai PAGE_ID).

URL 2 (PAGE_ID daal ke):
```
https://graph.facebook.com/v21.0/PAGE_ID?fields=instagram_business_account&access_token=PAGE_TOKEN
```
→ `instagram_business_account: { id: "1784..." }` — ye ID hai
**IG_USER_ID**.

✅ End me tumhare paas: **PAGE_ACCESS_TOKEN** + **IG_USER_ID**

⚠️ Agar URL 2 me `instagram_business_account` NAHI dikhe — matlab Step 1
(business switch + page connect) complete nahi hua. Wapas Step 1 check karo.

---

## STEP 5 — GitHub Repo banao + files upload (15 min)

✅ **GOOD NEWS — YE STEP ADHURA HO CHUKA HAI:** Repo
**https://github.com/imranah10/AurelianCanvas_Auto_Poster** ban chuka hai
aur isme scripts/config/data/workflow SAB PUSH ho chuke hain. Neeche ke
steps sirf isliye diye hain ki agar kabhi dobara khud upload karna ho.

1. Repo: **https://github.com/imranah10/AurelianCanvas_Auto_Poster**
   (Visibility PUBLIC hai — zaroori hai! Instagram/Pinterest ko media
   files khulkar download karni hain — private repo me ye kaam nahi karega)
2. Files upload karni ho to repo page par **Add file → Upload files**
   par click karke DRAG-DROP karo:
   - `scripts/`, `config/`, `data/`, `state/`, `.github/` folders
   - `README.md`, `SETUP-GUIDE.md`
3. **Ab tumhari 67 generated files** `media/` me daalo:
   - Pehle `media/` folder me ghuse (GitHub web par folder banao: Add
     file → upload → file path me `media/fresco-of-the-gods/1.jpg` type
     karke folder auto-ban jata hai)
   - Rules ZIP ke `media/README-MEDIA.txt` me likhe hain — short me:
     har art ka folder uske slug naam se, images + final joined reels
     same folder me, bundles ke 4 collages `media/bundles/` me
     `1-gold-series-duo.jpg` ... `4-full-collection.jpg` naam se
4. Neeche **Commit changes** dabao

⚠️ Ek file ka size 25MB se kam hona chahiye web upload ke liye. Reels
720p ki ~10-15MB hoti hain — theek chalengi. Badi ho to zip se pehle
compress kar lo, ya GitHub Desktop use karo (25MB limit nahi, 100MB tak
chalega).

📁 **MEDIA UPLOAD KA SABSE AASAN TARIKA (GitHub Desktop):**
1. https://desktop.github.com se GitHub Desktop install karo
2. File → Clone repository → `imranah10/AurelianCanvas_Auto_Poster` chuno
   → Local path: `C:\Users\Imran ahamad\Documents\AutoPoster` rakho
3. Windows Explorer me local `aurelian-canvas` folder se apni 67 files
   media/README-MEDIA.txt ke rules ke hisab se repo ke `media/` folders
   me copy-paste karo
4. GitHub Desktop khud changes dikhega → neeche summary likho `media add`
   → **Commit to main** → upar **Push origin** — DONE! (25MB limit nahi)

---

## STEP 6 — GitHub Secrets daalo (10 min)

Repo page par: **Settings → Secrets and variables → Actions** →
**New repository secret** — YE 7 secrets ek-ek karke banao:

| Name | Value kya hai |
|------|---------------|
| `PINTEREST_CLIENT_ID` | Step 2 ka App ID |
| `PINTEREST_CLIENT_SECRET` | Step 2 ka App Secret |
| `PINTEREST_REFRESH_TOKEN` | Step 3 ka refresh token |
| `IG_USER_ID` | Step 4d ki `1784...` ID |
| `PAGE_ACCESS_TOKEN` | Step 4d ka page token (jo kabhi expire nahi hota) |
| `GH_PAT` | Neeche Step 6b se banega |
| `AURELIAN_BRANCH` | `main` (bas itna hi likhna hai) |

**6b. GH_PAT banana (token auto-rotate ke liye):**
1. **https://github.com/settings/personal-access-tokens/new**
2. Token name: `autoposter` → Expiration: 90 din (baad me bana dena)
3. **Only select repositories** → apna `AurelianCanvas_Auto_Poster` chuno
4. **Permissions** me:
   - `Secrets`: **Read and write**
   - `Contents`: **Read and write**
5. Generate → token copy → wahan `GH_PAT` secret me paste karo

---

## STEP 7 — TEST KARO (5 min)

1. Repo me **Actions** tab kholo → agar puche to **"I understand my
   workflows, go ahead and enable them"**
2. Left me **Aurelian Auto-Poster** → right me **Run workflow** button
3. Dropdown: `dry_run` = **true**, platform = `all` → **Run workflow**
4. Run par click karke logs padho:
   - `DRY POST PIN-D001-1 | Renaissance Decor | ...` dikhna chahiye
   - `media missing` dikhe to koi folder/file naam galat hai — media
     folders dobara check karo (names EXACT hone chahiye)

Dry-run bilkul real jaisa hai — bas posting nahi karta. Logs me dikh
jayega kya-kya post hota.

**Ab REAL run:** dubara Run workflow → `dry_run` = **false** → aur dekho
jaise apne aap Pinterest + Instagram par posts live hoti hain! 🎉

---

## STEP 8 — ROZ KA SYSTEM (0 min)

Bas kuch bhi mat karo. GitHub roz khud:
- **9:30 AM IST** — 2 Pinterest pins
- **8:00 PM IST** — 2 Pinterest pins + 1 Instagram post

Har hafte ek baar dono apps khol ke notifications/likes dekh lo.
Pinterest analytics me monthly views 30 din me grow honge.

---

## 🩹 TROUBLESHOOTING

| Problem | Matlab | Fix |
|---------|--------|-----|
| IG: "must be a business account" | Business switch nahi hua | Step 1 dubara |
| IG: 4d me instagram_business_account nahi | Page link nahi hua | Step 1 ka Page connect |
| Pinterest: 401 unauthorized | Refresh token expire/bad | Step 3 dubara (naya token) |
| Pins me image nahi dikhti | Repo private hai YA media path galat | Repo public karo / folder names check |
| "media missing" logs me | Folder/file naming mismatch | `media/README-MEDIA.txt` follow karo |
| Actions tab me workflow nahi | Enable nahi kiya | Step 7 ka enable line |
| Kuch din skip ho gaye | PC band tha ya error — koi baat nahi | Agla run purane due posts khud catch-up karega |

## ⛔ YE MAT KARNA

- Repo **private mat karo** (media URLs public hone chahiye)
- Secrets ko kisi file me **paste mat karo** — sirf GitHub Secrets me
- `state/posted.json` **haath se mat chhedo** (robot isse duplicate
  posts rokta hai)
- `media/` ke folder **naam mat badlo** (schedule unhi naam se dhoondta hai)
- Meta/Pinterest app me **permissions kam mat karo**

## 🔐 SECURITY NOTE

Tokens GitHub ke **Secrets** me hote hain — encrypted, koi nahi dekh
sakta (tum bhi dubara nahi dekh paoge, bas replace kar sakte ho).
Pinterest token robot khud roz refresh karta hai (isliye `GH_PAT` chahiye).
Repo public hai par sirf media + captions hain — koi secret nahi.

## 📞 Agar phas jao

Step 1-2-5 sabse aasan hain. Step 3-4 tokens wale thode technical hain —
dheere dheere, ek-ek URL kholo, output copy karte jao. Koi step atke to
mujhe wahan ka screenshot bhejo, main exact next line bata dunga.
