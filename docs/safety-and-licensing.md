# Safety, privacy & licensing

## Safety
- Research prototype only; **not a medical device**. No diagnosis or treatment claims.
- Validate every measurement against a clinical reference before any exercise
  feedback is shown to a patient (see `docs/roadmap.md`, Phase 2).
- Fail loudly on occlusions, missing joints, and calibration errors.

## Privacy
- Rehab video/IMU data is health data. Keep it out of git (see `.gitignore`),
  process locally where possible, and get consent + ethics approval before
  recording anyone. Cloud pipelines (e.g. hosted mocap processing) need a
  data-processing review per deployment.

## Licensing — read this before using the "core" stack
- This meta-repo is MIT for its own text/code only.
- **SMPL / SMPL-X / STAR / SUPR and similar body-model weights are usually
  distributed under separate, gated, often non-commercial licenses** via the
  Max Planck / model-owner websites. Cloning the GitHub code does *not* grant
  weight rights. Register and comply per model.
- OpenSim, MuJoCo-ecosystem, Blender add-ons and datasets (e.g. BEHAVE) each
  carry their own terms. Record the license of every upstream repo you actually
  ship in your deployment's own NOTICE file.
- The `private` repo in the catalog (DAAPT) is listed for completeness only.
