# Contributing

## Add or re-tier a repository
1. Edit `catalog/repos.json` (one entry; keep `url` = `https://github.com/<slug>`).
2. `python3 scripts/generate_catalog.py` — regenerates CSV/YAML/`docs/catalog.md`.
3. `python3 scripts/validate_catalog.py` — must pass.
4. If re-tiering, add the evidence (install test, validation result) to `docs/evaluation.md` or `docs/roadmap.md`.

## Rules
- No upstream code, model weights, datasets, or patient data in this repo.
- Descriptions must be factual and sourced from the upstream README.
- Note license/weight gating in the entry's `notes` field whenever it exists.
