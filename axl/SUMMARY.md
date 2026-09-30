# AXL — pass 1 summary (Phases 0–4)

Branch: `claude/plan-phases-0-4-e54290` (the session forced this name instead of `axl-build`; logged in `DECISIONS.md`). One commit per phase, all pushed. `legacy/` and `best-practices/` are untouched (`git diff origin/main` on both is empty).

## Gates
| Phase | Result | Evidence |
|---|---|---|
| 0 Setup | PASS | tree exists; legacy/best-practices unchanged |
| 1 Extract | PASS | 41 groups, 470 prescriptions, 3 truncated, 3 caveats (g4 items 8–10), 331 map to no legacy effect; re-run is byte-identical |
| 2 Recon | PASS | 90 URLs registered, 52 fetched (all HTTP 200), 16 new primaries beyond legacy, 0 dead among fetched |
| 3 Claims | PASS | 475 claims; 243 quotes verified verbatim against saved text; validator has 0 errors |
| 4 Verbs | PASS | 34 verbs; every delta cites a measurable claim id; every definition quote is verbatim |

Nothing is BLOCKED (no `BLOCKED.md`). Phases 5–9 were not run, by instruction.

## Headline numbers (public claims only, 368)
- Status: **0 verified**, 243 single-source, 125 unverified, 0 rejected.
- Tier: 325 subjective, 32 process, 11 measurable, 0 enforced (no tool has been run yet).
- 107 private-kit claims (g0–g11) are excluded (`reports/excluded.md`).
- Verbs: 32 of 34 resolve to `undefined`; 2 (`typeset`, `audit`) resolve to `measurable` on one to three concrete claims each.
- Rebrand clusters (roots with ≥ 2 sources): 5. The largest is 23 sources: Impeccable's own README says it "started from" Anthropic's frontend-design, and Anthropic's blog, cookbook and skill are treated as one root.

## What to review first
1. **`verified` = 0 is a real result, not a bug.** Only Impeccable's per-command pages matched (243 claims), and they all share one root. Every other group is a paraphrase in the legacy page and its text was not found in the source. Two independent roots for one claim never occurred.
2. Lineage calls in `data/sources.json` (`derives_from`, `lineage_note`): the Impeccable→Anthropic and blog/cookbook/skill decisions are conservative judgment calls (D5).
3. Tier and `delta` extraction is regex over claim text (D8). It is deliberately conservative, so 11 measurable is a floor; a manual pass would raise it.
4. Verb "disagreement" is an auto-flag (no shared 4-word phrase), not an analysis of the actual disagreements.

## Known gaps / caveats
- Recon fetched 52 sources, above the "about 40" cap: 18 Impeccable pages and 16 new primaries were required by the plan. The other ~38 URLs from `SOURCES.md` are registered but not fetched (`reports/recon.md`).
- The samber skill, OneRedOak, and Taste-Skill v1 `SKILL.md` were not fetched at the deep path (README only), so those groups are `unverified`; the samber and vibecoded-design-tells roots are placeholders.
- Licences are detected from LICENSE files; non-GitHub pages and `anthropics/skills` are `unknown`. **The repo still needs a `LICENSE`; the owner must choose it.**
- `receipts/sources/` is gitignored, so a fresh checkout must run `python3 axl/scripts/refetch_sources.py --init` before Phase 3/4 gates.
- `pip install jsonschema` is required for `validate_claims.py`.
- The Section 4 language spec (`spec/*.schema.json` beyond `claim.schema.json`, `SPEC.md`) is not part of Phases 0–4 and was not written.

## Run next
1. `pip install jsonschema && python3 axl/scripts/refetch_sources.py --init` (restores saved texts).
2. Phase 5: install and pin axe-core, Lighthouse, Playwright, Stylelint, better-tailwindcss; run them on the Northstar demo (`data/legacy_effects.json` → `appTemplate`) and write `receipts/runs/`. `tool_candidate` on 11 measurable claims says which tool to try.
3. Phase 6 (metrics) can run right after; Phases 7–9 follow. Write `spec/` schemas and `SPEC.md` before Phase 8.
