# Changelog

## Unreleased
- Master anatomy-issues checklist (`docs/anatomy-issues-checklist.md`): 202 posture/movement-relevant anatomical issues in 13 groups (incl. niche/rare layer) with per-issue model-audit status
- Research note on breathing tracking: diaphragm→rib-cage/abdominal mechanics, OEP/RIP/depth-camera tracking, diaphragm ultrasound (`docs/research-breathing-tracking.md`)
- Research note on detailed anatomy models: foot arch/flat feet, articulated spine bending, ribcage/diaphragm breathing (`docs/research-detailed-anatomy-models.md`)
- Fat-measurement reference notes (`fat-distribution/measurement-notes.md`): method hierarchy, twin metrics, LiDAR conclusiveness
- Research note on dance→3D mapping and motion data beyond squats (`docs/research-dance-3d-motion.md`)
- New separate `fat-distribution/` folder: 12 fat/adipose-distribution models (8 code repos, 2 paper-only, 2 closed references) with Tier A/B usage rules
- Gap pass: resolved all `needs-review` entries; added kalibr, apriltag, Meshroom (108 repos)
- CI, unit tests, schemas + synthetic example, validation protocol, environment isolation
- Metadata enrichment (`scripts/enrich_metadata.py`) and clone pinning (`scripts/record_pins.py`, `catalog/pins.json`)

## 2026-10-21 — Hardware lock
- Selected hardware fixed: RGB cameras + iPhone LiDAR + optional RealSense D455 (`docs/hardware.md`)
- Added `realsenseai/librealsense` (105 repos)

## 2026-10-21 — Accuracy first
- Anatomical accuracy made design priority #1 (`docs/accuracy.md`, Tier A/B/C claim rules)
- Added medical-imaging personalisation repos (104 repos)

## 2026-10-21 — Digital-twin expansion
- Added 28 repos: personalisation, live tracking, correction, CEINMS/SOFA, haptic/exo hardware (98 repos)

## 2026-10-21 — Initial meta-repo
- Catalog of the original 70 repos with tiers, categories, clone/list/validate tooling
