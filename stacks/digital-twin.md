# Stack: Personalised digital twin (1:1 tracking + correction view)

```
ONBOARDING (once per person)
  photo(s)/scan ──► shapy (metric measurements) / ECON / PIXIE ──► smplx shape (betas)
                 ──► SKEL / OSSO (skeleton) ──► OpenSim scaled model (+ CEINMS calibration if EMG available)

LIVE TWIN (every session)
  clinic:  cameras ──► mediapipe / mmpose ──► GVHMR (world frame) / EasyMocap (multi-view)
  home:    SlimeVR trackers ──► SlimeVR-Server ─┐
  always:  labstreaminglayer (LSL) syncs video + IMU + EMG (+ haptics) into one XDF recording
                 ──► twin in aitviewer-skel / Unity (Realtime_SMPLX_Unity pattern)

CORRECTION VIEW
  measured motion ──► STGCN-rehab / UI-PRMD models (quality score, what is wrong)
                  ──► motion-diffusion-model (propose corrected motion)
                      ⚠️ constrained by SKEL/OpenSim joint limits — never show raw diffusion output
                  ──► OpenSim Moco (muscle activity the corrected motion requires)
                  ──► side-by-side: patient twin vs corrected twin
```

Clone the twin additions:
`python scripts/clone.py --only muelea/shapy,google-ai-edge/mediapipe,open-mmlab/mmpose,zju3dv/GVHMR,SlimeVR/SlimeVR-Server,SlimeVR/SlimeVR-Tracker-ESP,sccn/labstreaminglayer,fokhruli/STGCN-rehab,CEINMS/CEINMS`

Reality checks:
- "1:1" is a target, not a monocular-video property. Accuracy tier must be stated per setup (single phone < multi-cam < multi-cam+IMU).
- Muscle size/underdevelopment cannot be read from surface shape alone — onboarding needs strength/MVC (and ideally EMG via CEINMS) calibration.
- Every corrected-motion visualisation must cite the measurement file it was derived from (see docs/architecture.md).
