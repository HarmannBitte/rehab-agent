# Roadmap

## Phase 0 — Meta-repo (this repo) ✅
Catalog all 70 repos, tier them, provide clone/list/validate tooling.

## Phase 1 — One honest end-to-end slice (weeks, not months)
Pick ONE stack (`stacks/markerless-video.md`): record a healthy volunteer doing
one exercise (e.g. sit-to-stand or knee flexion), run it to OpenSim joint angles,
view it in aitviewer-skel. Success = a clinician can open the outputs and agree
or disagree with the measured angles. No patient data, no feedback generation yet.

## Phase 2 — Measurement validation
Compare joint angles/ROM against a reference (goniometer, lab mocap, or OpenCap)
on scripted movements. Publish error per joint/movement inside this repo.
A repo graduates from `experimental`/`extended` to `core` only with a note here.

## Phase 3 — Clinician-authored feedback rules
Rule checks on measured outputs only (e.g. "knee flexion < target on 3/5 reps"),
clinician reviews/edits every patient-facing message. Log rule firings.

## Phase 4 — Simulation & assistance (optional track)
MyoSuite/SCONE path: simulate muscle effort and assistive strategies in silico.
Nothing from this track reaches a patient without Phase 2-grade validation.

## Explicit non-goals (for now)
Diagnosis, automated treatment decisions, patient-facing unsupervised feedback,
and any use of gated model weights outside their license terms.
