# Stack: IMU real-time home rehab

```
6×IMU ──► TransPose (pose) ──► PIP/PNP (pose + joint torques + GRF)
   └────► OpenSimLive (live OpenSim IK) ──► opensim-core models
```
Clone it: `python scripts/clone.py --category pose-mocap --search imu`
Then add: `python scripts/clone.py --only jerela/OpenSimLive,opensim-org/opensim-core`
Note: OpenSimLive targets OpenSim 4.1 — budget time for version pinning.
