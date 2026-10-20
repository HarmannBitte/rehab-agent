#!/usr/bin/env python3
"""Regenerate repos.csv, repos.yaml and docs/catalog.md from catalog/repos.json (source of truth). Stdlib only."""
import csv, io, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/"catalog"/"repos.json").read_text())
repos=D["repos"]
# CSV
buf=io.StringIO(); wr=csv.writer(buf)
wr.writerow(["id","slug","url","category","tier","pipeline_stages","language","stars_snapshot","forks_snapshot","updated_snapshot","private","tags","description","notes","upstream_path"])
for r in repos:
    wr.writerow([r["id"],r["slug"],r["url"],r["category"],r["tier"],"|".join(r["pipeline_stages"]),r["language"] or "",r["stars_snapshot"] if r["stars_snapshot"] is not None else "",r["forks_snapshot"] if r["forks_snapshot"] is not None else "",r["updated_snapshot"],r["private"],"|".join(r["tags"]),r["description"],r["notes"],r["upstream_path"]])
(ROOT/"catalog"/"repos.csv").write_text(buf.getvalue(),encoding="utf-8")
# YAML (simple, quoted scalars — generated, do not hand-edit)
def q(v):
    if v is None: return "null"
    if isinstance(v,bool): return "true" if v else "false"
    return '"' + str(v).replace("\\","\\\\").replace('"','\\"') + '"'
lines=["# GENERATED from catalog/repos.json by scripts/generate_catalog.py — do not hand-edit.","repos:"]
for r in repos:
    lines.append(f"  - slug: {q(r['slug'])}")
    for k in ["url","category","tier","language","updated_snapshot","description","notes","upstream_path"]:
        lines.append(f"    {k}: {q(r[k])}")
    lines.append(f"    stars_snapshot: {r['stars_snapshot'] if r['stars_snapshot'] is not None else 'null'}")
    lines.append(f"    forks_snapshot: {r['forks_snapshot'] if r['forks_snapshot'] is not None else 'null'}")
    lines.append(f"    private: {q(r['private'])}")
    lines.append("    pipeline_stages: [" + ", ".join(q(s) for s in r["pipeline_stages"]) + "]")
    lines.append("    tags: [" + ", ".join(q(s) for s in r["tags"]) + "]")
(ROOT/"catalog"/"repos.yaml").write_text("\n".join(lines)+"\n",encoding="utf-8")
# Markdown catalog grouped by category
out=["# Full catalog — all 70 repositories","","Generated from `catalog/repos.json` by `scripts/generate_catalog.py`. Do not hand-edit this file; edit the JSON and regenerate.","","Stars/forks/updated are the maintainer's pasted snapshot, **not live data**.",""]
for cat,label in D["categories"].items():
    rows=[r for r in repos if r["category"]==cat]
    if not rows: continue
    out.append(f"## {cat} — {label} ({len(rows)})\n")
    out.append("| # | Repository | Tier | Stages | Lang | ★ snapshot | Description |")
    out.append("|---:|---|---|---|---|---:|---|")
    for r in rows:
        stages=", ".join(r["pipeline_stages"])
        out.append(f"| {r['id']} | [{r['slug']}]({r['url']}){' 🔒' if r['private'] else ''} | {r['tier']} | {stages} | {r['language'] or '—'} | {r['stars_snapshot'] if r['stars_snapshot'] is not None else '—'} | {r['description']} |")
    out.append("")
(ROOT/"docs").mkdir(exist_ok=True)
(ROOT/"docs"/"catalog.md").write_text("\n".join(out),encoding="utf-8")
print(f"Generated catalog/repos.csv, catalog/repos.yaml, docs/catalog.md from {len(repos)} repos.")
