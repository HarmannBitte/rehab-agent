# Examples

`synthetic-session/session.json` is a **fully synthetic** example session
record conforming to `schemas/session.schema.json`. It contains no patient
data (`"synthetic": true`, pseudonymous ref) and exists so developers can
build parsers, UIs and tests before any real recording happens.

Note how the synthetic example is honestly labelled Tier B: its surface is
personalised (LiDAR scan) while bone/joint layers are still `generic` —
the twin must display exactly that, per `docs/accuracy.md`.

Real session folders follow `docs/hardware.md` step 7 and are **never**
committed to this repository (see `.gitignore`).
