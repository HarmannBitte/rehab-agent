#!/usr/bin/env python3
"""Clone selected upstream repos into upstream/<owner>/<repo>. Stdlib only.

Examples:
  python scripts/clone.py --tier core
  python scripts/clone.py --category pose-mocap --dry-run
  python scripts/clone.py --only vchoutas/smplx,freemocap/freemocap
  python scripts/clone.py --search imu
Safety: never clones private repos; shallow by default; skips existing dirs.
"""
import argparse, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/"catalog"/"repos.json").read_text())

def match(r, a):
    if r["private"]: return False
    if a.tier and r["tier"] not in a.tier: return False
    if a.category and r["category"] not in a.category: return False
    if a.stage and not set(a.stage) & set(r["pipeline_stages"]): return False
    if a.only and r["slug"] not in a.only: return False
    if a.search:
        import re
        q=a.search.lower()
        tokens=re.findall(r"[a-z0-9]+", (r["slug"]+" "+r["description"]+" "+" ".join(r["tags"])).lower())
        if not any(tok.startswith(q) for tok in tokens): return False
    return True

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--tier", action="append", choices=list(DATA["tiers"]))
    p.add_argument("--category", action="append", choices=list(DATA["categories"]))
    p.add_argument("--stage", action="append", choices=list(DATA["pipeline_stages"]))
    p.add_argument("--only", help="comma-separated owner/repo list")
    p.add_argument("--search")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--full", action="store_true", help="full clone instead of --depth 1")
    p.add_argument("--all", action="store_true", help="clone every public repo (large!)")
    a=p.parse_args()
    if a.only: a.only={s.strip() for s in a.only.split(",") if s.strip()}
    selected=[r for r in DATA["repos"] if match(r,a)] if (a.tier or a.category or a.stage or a.only or a.search or a.all) else []
    if not selected:
        print("Nothing selected. Pass --tier/--category/--stage/--only/--search or --all.\nRun: python scripts/list.py --tier core", file=sys.stderr); return 2
    print(f"Selected {len(selected)} repo(s):")
    for r in selected:
        dest=ROOT/r["upstream_path"]
        print(f" - {r['slug']:55} -> {r['upstream_path']}  {'[exists, skip]' if dest.exists() else ''}")
        if a.dry_run or dest.exists(): continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        cmd=["git","clone"] + ([] if a.full else ["--depth","1"]) + [r["url"], str(dest)]
        subprocess.run(cmd, check=False)
    return 0
if __name__=="__main__": raise SystemExit(main())
