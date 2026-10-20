#!/usr/bin/env python3
"""Show which upstream repos are cloned locally, and their git HEAD. Stdlib only."""
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"catalog"/"repos.json").read_text())
cloned=0
for r in DATA["repos"]:
    d=ROOT/r["upstream_path"]
    if d.exists():
        cloned+=1
        head=subprocess.run(["git","-C",str(d),"rev-parse","--short","HEAD"],capture_output=True,text=True).stdout.strip()
        print(f"CLONED  {r['slug']:<52} {head}  {r['upstream_path']}")
    else:
        print(f"missing {r['slug']:<52} {r['upstream_path']}")
print(f"\n{cloned}/{len(DATA['repos'])} cloned into upstream/ (git-ignored)")
