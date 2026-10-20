#!/usr/bin/env python3
"""Refresh live GitHub metadata for every catalog repo. Stdlib only.

Reads catalog/repos.json, calls the GitHub API, and (with --apply) writes back
stars/forks/language/updated plus `license_api` and `archived_api` fields.
Default is a dry run that only prints what would change.

Auth: set GITHUB_TOKEN to raise the rate limit (60/h anonymous -> 5000/h).
Usage:  GITHUB_TOKEN=... python3 scripts/enrich_metadata.py [--apply] [--only owner/repo]
"""
import argparse, json, os, sys, urllib.request, urllib.error
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "catalog" / "repos.json"

def fetch(slug, token):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{slug}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "rehab-agent-catalog",
                 **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("warning: no GITHUB_TOKEN — anonymous limit is 60 requests/hour", file=sys.stderr)
    D = json.loads(PATH.read_text())
    today = date.today().isoformat()
    changed = failed = 0
    for r in D["repos"]:
        if a.only and r["slug"] != a.only:
            continue
        if r["private"]:
            continue
        try:
            api = fetch(r["slug"], token)
        except Exception as e:
            print(f"FAIL {r['slug']}: {e}"); failed += 1; continue
        new = {
            "stars_snapshot": api.get("stargazers_count"),
            "forks_snapshot": api.get("forks_count"),
            "language": api.get("language"),
            "updated_snapshot": f"{(api.get('updated_at') or '')[:10]} (live API {today})",
            "license_api": (api.get("license") or {}).get("spdx_id"),
            "archived_api": bool(api.get("archived")),
        }
        diff = {k: (r.get(k), v) for k, v in new.items() if r.get(k) != v}
        if diff:
            changed += 1
            print(f"{r['slug']}: " + "; ".join(f"{k} {o!r} -> {n!r}" for k, (o, n) in diff.items()))
            if a.apply:
                r.update(new)
    if a.apply and changed:
        D["count"] = len(D["repos"])
        PATH.write_text(json.dumps(D, indent=2, ensure_ascii=False) + "\n")
        print(f"\nApplied. Run: python3 scripts/generate_catalog.py && python3 scripts/validate_catalog.py")
    print(f"\n{changed} repo(s) would change / changed, {failed} failed. Mode: {'APPLY' if a.apply else 'dry-run'}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
