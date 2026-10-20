#!/usr/bin/env python3
"""Validate catalog/repos.json. Stdlib only. Exits non-zero on any problem."""
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/"catalog"/"repos.json").read_text())
errs=[]
slugs=[r["slug"].lower() for r in D["repos"]]
if len(slugs)!=len(set(slugs)): errs.append("duplicate slugs")
if D["count"]!=len(D["repos"]): errs.append(f"count field {D['count']} != {len(D['repos'])} repos")
for r in D["repos"]:
    if r["url"]!=f"https://github.com/{r['slug']}": errs.append(f"url mismatch: {r['slug']}")
    if r["category"] not in D["categories"]: errs.append(f"bad category: {r['slug']}")
    if r["tier"] not in D["tiers"]: errs.append(f"bad tier: {r['slug']}")
    for s in r["pipeline_stages"]:
        if s not in D["pipeline_stages"]: errs.append(f"bad stage {s}: {r['slug']}")
    if not r["description"]: errs.append(f"empty description: {r['slug']}")
print("\n".join(errs) if errs else f"OK: {len(D['repos'])} repos, catalog is valid.")
sys.exit(1 if errs else 0)
