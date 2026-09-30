# Decisions

- D1: Session forced branch `claude/plan-phases-0-4-e54290` instead of `axl-build`; using it.
- D2: Gates are Python scripts in `axl/scripts/gates/`, run via `python3 axl/scripts/gates/phaseN.py`.
- D3: `git diff origin/main` gate for legacy/best-practices is used as written.
- D4: Recon fetched 52 sources (cap "about 40" exceeded: 18 Impeccable command pages are required, plus 16 new primaries required by the plan). Remaining URLs from SOURCES.md are registered but skipped.
- D5: Lineage is conservative: Impeccable (README says it "started from" Anthropic frontend-design) shares a root with it; Anthropic blog/cookbook/skill are one root. Composite-parent derivatives count as their parents' roots.
- D6: Licences are detected from raw LICENSE files (GitHub API not accessible); unknown otherwise.
