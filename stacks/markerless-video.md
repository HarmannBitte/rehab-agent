# Stack: Markerless video rehab (recommended first build)

```
phones/webcams ──► freemocap or opencap-core ──► pose2sim ──► opensim-core
                                                              │ joint angles (.mot)
                                          aitviewer-skel ◄────┘ + opencap-processing
```
| Step | Repo | Command/entry point (see upstream README) |
|---|---|---|
| Capture + 3D pose | `freemocap/freemocap` (or `opencap-org/opencap-core` for the phone/OpenSim-native path) | record a scripted exercise |
| 2D→3D→OpenSim | `perfanalytics/pose2sim` | produces OpenSim kinematics from cameras |
| Biomechanics | `opensim-org/opensim-core`, `opencap-org/opencap-processing` | inverse kinematics/dynamics |
| Review | `MarilynKeller/aitviewer-skel`, `opencap-org/opencap-viewer` | clinician opens the session |

Clone it: `python scripts/clone.py --only freemocap/freemocap,perfanalytics/pose2sim,opensim-org/opensim-core,opencap-org/opencap-processing,MarilynKeller/aitviewer-skel`
