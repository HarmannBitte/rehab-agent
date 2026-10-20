#!/usr/bin/env python3
"""Record the exact upstream commits currently cloned in upstream/ into
catalog/pins.json, so an experiment can be reproduced. Stdlib only.

Workflow: clone (scripts/clone.py) -> test -> python3 scripts/record_pins.py
Commit catalog/pins.json. Fresh checkouts can verify with --check.
"""
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "catalog" / "repos.json").read_text())
PINS = ROOT / "catalog" / "pins.json"

def head(path):
    out = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                         capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify clones match pins.json")
    a = ap.parse_args()
    if a.check:
        pins = json.loads(PINS.read_text()) if PINS.exists() else {}
        bad = 0
        for slug, pin in pins.items():
            d = ROOT / "upstream" / slug
            cur = head(d) if d.exists() else None
            if cur != pin["commit"]:
                print(f"MISMATCH {slug}: pinned {pin['commit'][:10]} vs local {cur[:10] if cur else 'not cloned'}")
                bad += 1
        print(f"{len(pins)} pinned, {bad} mismatch(es)")
        return 1 if bad else 0
    pins = {}
    for r in DATA["repos"]:
        d = ROOT / r["upstream_path"]
        if d.exists():
            c = head(d)
            if c:
                pins[r["slug"]] = {"commit": c, "path": r["upstream_path"]}
    PINS.write_text(json.dumps(pins, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {len(pins)} pin(s) to catalog/pins.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
