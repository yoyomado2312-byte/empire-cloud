#!/usr/bin/env python3
"""
================================================================================
Empire Cloud - Zero-Dependency YouTube OAuth Token Refresher
================================================================================
Generates new permanent YouTube OAuth refresh tokens without requiring pip packages.
Uses Python standard library (http.server, urllib, webbrowser).

Usage:
    python refresh_yt_token.py
================================================================================
"""

import http.server
import json
import os
import sys
import urllib.parse
import urllib.request
import webbrowser

PORT = 8080
REDIRECT_URI = f"http://localhost:{PORT}/"
AUTH_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
SCOPES = "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.readonly"

auth_code = None

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = """
            <html>
            <body style="font-family:sans-serif; text-align:center; padding:50px; background:#0f172a; color:#f8fafc;">
                <h1 style="color:#22c55e;">&#10004; Authentication Successful!</h1>
                <p style="font-size:18px;">You can now close this tab and return to your terminal.</p>
                <p style="color:#94a3b8;">Empire Cloud Automation</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
        else:
            err = params.get("error", ["Unknown error"])[0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"<h1>Authentication Failed: {err}</h1>".encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Suppress default HTTP logging


def get_credentials():
    # 1. Try client_secrets.json
    for fname in ["client_secrets.json", "client_secret.json"]:
        if os.path.exists(fname):
            try:
                with open(fname, "r", encoding="utf-8") as f:
                    data = json.load(f)
                inst = data.get("installed") or data.get("web")
                if inst:
                    print(f"[*] Loaded credentials from {fname}")
                    return inst.get("client_id"), inst.get("client_secret")
            except Exception:
                pass

    # 2. Try environment variables
    cid = os.environ.get("YT_CLIENT_ID", "").strip()
    csec = os.environ.get("YT_CLIENT_SECRET", "").strip()
    if cid and csec:
        print("[*] Loaded credentials from environment variables (YT_CLIENT_ID, YT_CLIENT_SECRET)")
        return cid, csec

    # 3. Interactive prompt
    print("\n" + "=" * 70)
    print("  GOOGLE OAUTH CREDENTIALS REQUIRED")
    print("=" * 70)
    print("You can find these in Google Cloud Console -> APIs & Services -> Credentials.")
    print("Or place your downloaded 'client_secrets.json' in this directory.\n")
    cid = input("Enter your Client ID: ").strip()
    if not cid:
        sys.exit(0)
    csec = input("Enter your Client Secret: ").strip()
    if not csec:
        sys.exit(0)
    return cid, csec


def main():
    print("=" * 70)
    print("  EMPIRE CLOUD: YOUTUBE REFRESH TOKEN GENERATOR")
    print("=" * 70)

    client_id, client_secret = get_credentials()

    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = f"{AUTH_ENDPOINT}?{urllib.parse.urlencode(params)}"

    print(f"\n[*] Starting local listener on {REDIRECT_URI}...")
    try:
        server = http.server.HTTPServer(("localhost", PORT), OAuthCallbackHandler)
    except OSError as e:
        print(f"[!] Error binding to port {PORT}: {e}")
        print("Please ensure no other service is using port 8080 and retry.")
        return

    print("[*] Opening your browser to authenticate...")
    print(f"URL: {auth_url}\n")
    webbrowser.open(auth_url)

    print("[*] Waiting for authorization in browser...")
    while not auth_code:
        server.handle_request()

    server.server_close()
    print("[*] Authorization code received! Exchanging for tokens...")

    # Exchange code for tokens
    token_params = {
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    req_data = urllib.parse.urlencode(token_params).encode("utf-8")
    req = urllib.request.Request(TOKEN_ENDPOINT, data=req_data, headers={"Content-Type": "application/x-www-form-urlencoded"})

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            tok_data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"[!] Failed to exchange code for tokens: {e}")
        return

    refresh_token = tok_data.get("refresh_token")
    if not refresh_token:
        print("\n[!] WARNING: Google did not return a refresh token.")
        print("Google only sends a refresh_token when access is first granted.")
        print("Go to https://myaccount.google.com/permissions, remove access for this app, and run this script again.")
        return

    print("\n" + "=" * 70)
    print("  SUCCESS! YOUR NEW YOUTUBE REFRESH TOKEN:")
    print("=" * 70)
    print(f"\n{refresh_token}\n")
    print("=" * 70)
    print("INSTRUCTIONS TO UPDATE GITHUB SECRETS:")
    print("1. Go to your repo on GitHub: Settings -> Secrets and variables -> Actions")
    print("2. For Arabic channel (AI & Tech): Update 'YT_TOKEN_CH02_AR'")
    print("3. For English channel (Wealth): Update 'YT_TOKEN_CH03_EN'")
    print("\nCRITICAL - PREVENT 7-DAY EXPIRATION:")
    print("- In Google Cloud Console -> APIs & Services -> OAuth consent screen")
    print("- Under 'Publishing status', click 'PUBLISH APP' and change to Production.")
    print("- In Production mode, your refresh token will NEVER expire!")
    print("=" * 70)


if __name__ == "__main__":
    main()
