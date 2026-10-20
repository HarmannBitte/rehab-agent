#!/usr/bin/env python3
"""List/filter the catalog. Stdlib only.  e.g. python scripts/list.py --tier core"""
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"catalog"/"repos.json").read_text())
p=argparse.ArgumentParser()
p.add_argument("--tier", action="append", choices=list(DATA["tiers"]))
p.add_argument("--category", action="append", choices=list(DATA["categories"]))
p.add_argument("--stage", action="append")
p.add_argument("--search")
a=p.parse_args()
rows=DATA["repos"]
if a.tier: rows=[r for r in rows if r["tier"] in a.tier]
if a.category: rows=[r for r in rows if r["category"] in a.category]
if a.stage: rows=[r for r in rows if set(a.stage)&set(r["pipeline_stages"])]
if a.search:
    import re
    q=a.search.lower()
    rows=[r for r in rows if any(tok.startswith(q) for tok in re.findall(r"[a-z0-9]+",(r["slug"]+" "+r["description"]+" "+" ".join(r["tags"])).lower()))]
for r in rows:
    print(f"{r['id']:>2}. [{r['tier']:<12}] [{r['category']:<19}] {r['slug']:<52} {r['description'][:90]}")
print(f"\n{len(rows)} repo(s)")
