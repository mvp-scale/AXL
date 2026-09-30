# Decisions

- D1: Session forced branch `claude/plan-phases-0-4-e54290` instead of `axl-build`; using it.
- D2: Gates are Python scripts in `axl/scripts/gates/`, run via `python3 axl/scripts/gates/phaseN.py`.
- D3: `git diff origin/main` gate for legacy/best-practices is used as written.
