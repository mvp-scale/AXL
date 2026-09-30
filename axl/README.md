# AXL

A machine-readable way to say what design words mean, check them with tools, and show who says so.

- `site/` the static site (open with `python3 -m http.server`).
- `SPEC.md`, `spec/` the language: describe, evaluate, correct.
- `data/` claims, sources, lineage, verbs and definitions (generated; see `scripts/build_all.sh`).
- `receipts/runs/` every tool run: command, version, input hash, result.
- `skills/` four agent skills that run the checks.
- `SUMMARY.md` what passed, what is open, what to run next.
