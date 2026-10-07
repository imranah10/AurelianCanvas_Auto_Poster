#!/usr/bin/env python3
"""Pinterest Token Setup Helper - ye script tumhe refresh token dega.
Chalane ka tareeka:  python3 scripts/pinterest_setup.py
(Normal Python jisme internet chalta ho, bas.)"""
import base64
import json
import sys
import urllib.parse
import urllib.request

AUTH_URL = ("https://www.pinterest.com/oauth/?response_type=code"
            "&redirect_uri=https://localhost/callback"
            "&consumer_id={app_id}"
            "&scope=boards%3Aread%2Cboards%3Awrite%2Cpins%3Aread%2Cpins%3Awrite%2Cuser_accounts%3Aread"
            "&refreshable=true")


def main():
    print("=" * 64)
    print("PINTEREST TOKEN SETUP - Aurelian Canvas Auto-Poster")
    print("=" * 64)
    app_id = input("\n1) Pinterest App ID paste karo: ").strip()
    app_secret = input("2) Pinterest App Secret paste karo: ").strip()

    print("\n3) Ye URL browser me kholo (ek line me):")
    print("\n" + AUTH_URL.format(app_id=app_id) + "\n")
    print("   -> 'Allow' dabao. Browser error page dikhaye to DARO MAT -")
    print("   upar address bar me ?code=AAAA... wala code copy karo.")
    code = input("\n4) Wo code yahan paste karo: ").strip()

    basic = base64.b64encode(f"{app_id}:{app_secret}".encode()).decode()
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://localhost/callback",
        "scope": "boards:read,boards:write,pins:read,pins:write,user_accounts:read",
    }).encode()
    req = urllib.request.Request(
        "https://api.pinterest.com/v5/oauth/token", data=data, method="POST",
        headers={"Authorization": f"Basic {basic}",
                 "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            tok = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print(f"\nERROR: token exchange failed ({e.code})")
        print(e.read().decode()[:400])
        sys.exit(1)

    print("\n" + "=" * 64)
    print("SUCCESS! Ab ye GitHub Secrets me daalo (Step 6 of SETUP-GUIDE):")
    print("=" * 64)
    print(f"\nPINTEREST_CLIENT_ID      = {app_id}")
    print(f"PINTEREST_CLIENT_SECRET  = {app_secret[:4]}{'*' * (len(app_secret) - 4)}")
    print(f"PINTEREST_REFRESH_TOKEN  = {tok.get('refresh_token', 'MISSING!')}")
    print(f"\n(Access token abhi ke liye: {tok.get('access_token', '')[:20]}...)")
    print("\nIn 3 values ko GitHub repo ke Settings > Secrets and variables >")
    print("Actions me 'New repository secret' se daal do. BAS HO GAYA!")


if __name__ == "__main__":
    main()
