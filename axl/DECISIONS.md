# Decisions

- D1: Session forced branch `claude/plan-phases-0-4-e54290` instead of `axl-build`; using it.
- D2: Gates are Python scripts in `axl/scripts/gates/`, run via `python3 axl/scripts/gates/phaseN.py`.
- D3: `git diff origin/main` gate for legacy/best-practices is used as written.
- D4: Recon fetched 52 sources (cap "about 40" exceeded: 18 Impeccable command pages are required, plus 16 new primaries required by the plan). Remaining URLs from SOURCES.md are registered but skipped.
- D5: Lineage is conservative: Impeccable (README says it "started from" Anthropic frontend-design) shares a root with it; Anthropic blog/cookbook/skill are one root. Composite-parent derivatives count as their parents' roots.
- D6: Licences are detected from raw LICENSE files (GitHub API not accessible); unknown otherwise.
- D7: Private-kit claims (g0–g11, 107) stay in claims.json tagged `private-kit`, status `unverified`, no quote; consumers filter on origin. Their text is already public in legacy/.
- D8: `measurable` requires a `delta` (`before` may be null when the source states only a target value) — numeric rules are expressed as deltas. Tier is decided by regex over claim text only; the legacy effect mapping is ignored.
- D9: A quote counts as verified when >=60% of the legacy words (min 4-word run) match as one contiguous run in the saved source; the quote is the raw slice (<=40 words). Partial matches are noted. Everything else is `unverified` (paraphrase or source not fetched).
- D10: Independence: atomic lineage roots of the primary plus supports (a support needs >=60% coverage of the claim by a different fetched source); multi-parent aggregator sources never add a root.
- D11: No claim is `enforced` yet: no tool has been run (Phase 5).
- D12: Phase 5 tools: axe-core, Lighthouse, Playwright (toHaveScreenshot, reducedMotion), Stylelint, @google/design.md lint, WCAG contrast script. better-tailwindcss and APCA dropped (see reports/tools.md). Chromium is run by explicit executablePath.
- D13: `enforced` is set by `scripts/apply_receipts.py` only for public claims with a receipt; `discriminates` records whether the tool failed before and passed after. Pipeline order is in `scripts/build_all.sh`.
- D14 (owner-approved scope change): Phases 5–9 plus (a) a curated `data/definitions.json` layer of measurable craft patterns per verb, labelled "AXL definitions" and cited to standards, (b) the site leads with a launch view (term -> definition -> check -> live pass/fail), (c) plain-language explanations first, syntax only as example.
