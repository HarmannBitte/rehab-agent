# Changelog

## Unreleased
- Joint load & stress scenario model designed: `docs/design-joint-load-stress-model.md` (OpenSim Joint-Reaction pipeline, Messier-anchored fat scenarios, honest muscle-effort/stability outputs) + illustrative demo `examples/joint-load-demo/index.html`
- **Anatomy-audit integration pass**: audit mechanisms folded into `schemas/twin-manifest.schema.json` (spinopelvic parameters, limb alignment/torsion, muscle parameters with separate weakness/contracture/reflex-gain groups, bone quality + exo derating, devices/prostheses, clinician-only safety flags, body state), `breathing` block added to `schemas/session.schema.json` and the synthetic example, integration table + red lines in `docs/accuracy.md`, manifest contract in `docs/architecture.md`; new schema test (12 tests)
- **Anatomy audit COMPLETE (202/202)**: Batch 8 (niche spine + cross-cutting, 13 issues), `docs/anatomy-audit-batch8-niche-spine-crosscutting.md`, with five-mechanism closing synthesis
- Anatomy audit Batch 7 (neuromotor NM-01…NM-15) completed: `docs/anatomy-audit-batch7-neuromotor.md` (189/202 researched)
- Anatomy audit Batch 6 (arm/hand + bone/joint, 22 issues) completed: `docs/anatomy-audit-batch6-armhand-bonejoint.md` (174/202 researched; MS-03 formally closed)
- Anatomy audit Batch 5 (head/neck + chest remainder, 20 issues) completed: `docs/anatomy-audit-batch5-headneck-chest.md` (151/202 researched)
- Added 7 previously research-note-only repos to the catalog (IDs 109–115: Motion-X, LODGE, ChoreoMaster, MotoricaDanceDataset, 3dpredictsim, Synergy-Based-Foot-Model, Foot3D) with full documentation-standard metadata; catalog now 115 repos
- Full repo-documentation pass: licenses + license provenance for all 108 catalog repos (and fat-distribution models), live metadata refresh for repos 1–52 + gap entries, expanded generated catalog with per-repo detail sections, documentation standard now enforced by validator and tests
- Anatomy audit Batch 4 (whole-body/muscle, 32 issues) completed: `docs/anatomy-audit-batch4-wholebody-muscle.md` (131/202 researched; muscle-parameter pipeline finding)
- Anatomy audit Batch 3 (shoulder SH-01…SH-15) completed: `docs/anatomy-audit-batch3-shoulder.md` (99/202 researched; scapula = model-inferred rule)
- Anatomy audit Batch 2 (hip/knee/foot, 57 issues) completed: `docs/anatomy-audit-batch2-hip-knee-foot.md` (84/202 researched; Torsion Tool adoption identified)
- Anatomy audit Batch 1 (spine SP-02…SP-19) completed: `docs/anatomy-audit-batch1-spine.md`, checklist statuses updated (27/202 researched)
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
