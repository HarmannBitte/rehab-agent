# Validation protocol — executable checklist

Run order matters: a later step may not start until the earlier gate passes.
Output of a full run is one `validation-report` (schema:
`schemas/validation-report.schema.json`) stored with the twin manifest.
Targets are from `docs/accuracy.md` (project targets, clinician to confirm).

## 0. Setup identity
- [ ] Hardware list matches `docs/hardware.md` (device IDs, firmware logged)
- [ ] Calibration files from *this* setup (not last week's) in the session folder
- [ ] Twin manifest exists; every accuracy layer marked personalised/generic/unvalidated

## 1. Calibration gate
- [ ] ChArUco intrinsics check per RGB camera; D455 intrinsics verified in librealsense; iPhone intrinsics taken from the stream
- [ ] Shared extrinsic capture (all devices see the board) → room frame; reprojection error logged (target < 0.5 px)
- [ ] `kalibr` camera–IMU calibration if any IMU stream is used for kinematics
- **Gate:** reprojection or calibration failure = stop. No "fix it in post."

## 2. Synchronisation gate
- [ ] All streams flowing through Lab Streaming Layer; hardware timestamps preserved (D455, Record3D metadata)
- [ ] LED-flash/hand-clap proof event recorded at session start
- [ ] Measured inter-stream offset after correction **< 5 ms** (else kinematics use is prohibited)

## 3. Surface-scan gate (Tier B and Tier-A registration)
- [ ] iPhone LiDAR A-pose rotational scan; hole check (armpits, hair, feet, dark clothing) done while the person is still present
- [ ] Optional photogrammetry pass (`Meshroom`) for higher-resolution static surface
- [ ] Segment lengths vs tape measurements: disagreement > 2 cm on a long segment → investigate and log, never silently accept

## 4. Anatomy gate (Tier A only)
- [ ] Segmentation (TotalSegmentator ± nnU-Net) **reviewed and corrected by a clinician in 3D Slicer**
- [ ] Joint centres vs MRI landmarks: ≤ 5 mm target, per-joint values recorded
- [ ] Personalised OpenSim model built (msk-PIPE / TPS workflow / STAPLE); muscle attachments present

## 5. Kinematics validation (per setup, per movement — not once forever)
Scripted movements, performed slowly then at exercise speed:
hip flexion/extension, knee flexion (squat), sit-to-stand, trunk flexion,
trunk rotation, shoulder flexion/abduction.
- [ ] Reference comparison recorded (marker-mocap lab session, or the best
      available reference; name it in the report — "no reference" = screening only)
- [ ] RMSE computed **per joint and per plane** (sagittal / frontal / transverse separately)
- [ ] Gates: sagittal ≤ 3°, frontal ≤ 5°; transverse reported — feedback use
      prohibited until ≤ 5° is demonstrated (see accuracy.md for why)
- **Gate failure on a joint/plane = that joint/plane is excluded from feedback
  rules.** The system degrades its claims, not its standards.

## 6. Muscle-layer validation (before any "underdeveloped muscle" language)
- [ ] Muscle volumes vs MRI segmentation ≤ 10 % per major group (Tier A)
- [ ] CEINMS calibration performed if EMG is used; MVC protocol recorded
- [ ] Strength reference (dynamometer or clinician test) filed for claimed muscles

## 7. Sign-off
- [ ] Report lists `approved_for`: screening / posture-feedback / muscle-claims / exo-assistance
- [ ] `exo-assistance` requires **all** gates above passed + the safety review in `stacks/haptic-exo-suit.md`
- [ ] Report path linked from the twin manifest; clinician sign-off recorded

## Re-validation triggers
New camera position, new room/lighting, device firmware update, new exercise,
new patient population, or 3 months elapsed — whichever comes first.
