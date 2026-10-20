# Stack: Haptic feedback suit + exoskeleton support (two different tracks)

## Track 1 — Haptic posture cueing (buildable now, low risk)
```
SlimeVR trackers (posture sensing) ──► twin (stacks/digital-twin.md)
   ──► rule: joint/posture deviation > clinician-set threshold
   ──► senseshift-firmware vest/sleeves (vibrotactile cue at the deviating segment)
       [LucidVR/lucidgloves only if hand rehab is in scope]
```
Clone: `python scripts/clone.py --only SlimeVR/SlimeVR-Server,SlimeVR/SlimeVR-Tracker-ESP,senseshift/senseshift-firmware`

## Track 2 — Powered joint support (research build, safety-gated)
```
naubiomech/OpenExo (modular exo base: hip/ankle/elbow, mechanics+electronics+control)
   + neurobionics/opensourceleg (lower-limb actuator/sensor SDK patterns)
   + mjbots/moteus or simplefoc/Arduino-FOC (actuator controllers)
   + CEINMS / OpenSimRT (person-specific, EMG-informed assistance targets)
```
Clone: `python scripts/clone.py --only naubiomech/OpenExo,neurobionics/opensourceleg,mjbots/moteus,simplefoc/Arduino-FOC,CEINMS/CEINMS,mitkof6/OpenSimRT`

⚠️ No turnkey open repo provides powered *spinal* posture support. Track 2 is joint
assistance adapted from OpenExo. Before anything load-bearing touches a person:
hardware e-stop, firmware torque limits, clinician-set range limits, and a written
risk assessment are mandatory — none of that ships in these repos.
