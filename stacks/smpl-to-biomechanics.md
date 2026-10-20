# Stack: SMPL → biomechanics (the glue path)

```
image/video ──► smplify-x / HSMR ──► smplx params ──► SKEL / OSSO (skeleton)
   ──► SMPL2AddBiomechanics ──► AddBiomechanics ──► opensim-core
   ──► myoconverter (optional) ──► myo_sim / myosuite (MuJoCo)
```
Clone it: `python scripts/clone.py --only vchoutas/smplify-x,IsshikiHugh/HSMR,MarilynKeller/SKEL,MarilynKeller/OSSO,MarilynKeller/SMPL2AddBiomechanics,keenon/AddBiomechanics,MyoHub/myoconverter`
⚠️ SMPL-family model weights are license-gated — register upstream before running.
