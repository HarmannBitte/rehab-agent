# Evaluation rubric — how tiers were assigned, and how to re-score

Score each upstream repo 0–2 per axis before promoting it a tier:

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| License clarity | unclear / gated weights | code OK, weights gated | permissive code + weights |
| Maintenance | untouched >1y | sporadic | active in last ~3 months |
| Docs & install | README only | install docs | tested install + examples |
| I/O honesty | opaque tensors | some file outputs | standard files (SMPL/OpenSim/MuJoCo) |
| Rehab relevance | general 3D/CV | human motion | joint angles / torques / gait / clinical task |
| Hardware burden | lab mocap / cluster | workstation GPU | phone / webcam / laptop |

Rules used for the initial tiering in `catalog/repos.json`:
- **core**: rehab-relevant, standard I/O, and either active or a de-facto standard (OpenSim, SMPL-X).
- **experimental**: 2025–26 paper code or very recent releases — promising, unproven reproducibility.
- **needs-review**: the source list gave no description. All four original cases
  (MyoBack, MASS, mass-dart-exo, RC-SMPL) were resolved from upstream READMEs on
  2026-10-21; the tier remains available for future incompletely-described additions.
- **private**: DAAPT — catalogued for completeness; do not attempt to clone.

Stars/forks in the catalog are a pasted snapshot for orientation only.
Re-check upstream before quoting them anywhere.
