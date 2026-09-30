# AXL — build summary (Phases 0–9)

Branch `claude/plan-phases-0-4-e54290` (forced by the session; `axl-build` was not used, see `DECISIONS.md` D1). Every phase was committed and pushed. `legacy/` and `best-practices/` are unchanged. **Nothing is deployed.**

## Gates
| Phase | Result | Evidence |
|---|---|---|
| 0 Setup | PASS | tree exists; legacy/ and best-practices/ untouched |
| 1 Extract | PASS | 41 groups, 470 prescriptions, deterministic |
| 2 Recon | PASS | 90 sources registered, 52 fetched OK, 16 new primaries, lineage complete |
| 3 Claims | PASS | 485 claims, 253 quotes verbatim-verified against saved text |
| 4 Verbs | PASS | 34 verbs: 7 tool-backed, 27 undefined |
| 5 Tools | PASS | 27/27 receipts reproduce (100%); 21 claims enforced, 16 fail before and pass after |
| 6 Metrics | PASS | computed from `claims.json` (`reports/metrics.md`) |
| 7 Site | PASS | 375 and 1440 px, light and dark: 0 console errors, 0 serious/critical axe, no external requests; 378/378 claims open the Sources drawer; export validates against the AXL schema |
| 8 Skills | PASS | 4 skills, lint clean (no subjective claims), scripts exit 0 on the demo; auto-correct cut failing findings 42 to 11 |
| 9 GCP | PASS (files only) | `cloudbuild.yaml`, `cloudbuild.nightly.yaml`, `firebase.json`, `DEPLOY.md` parse; not deployed |

Nothing is blocked (no `BLOCKED.md`).

## Headline (computed)
- Of **332** audited public UI-guidance statements, **97.9%** have no measurable definition ("luck"), **2.1%** do, **1.8%** are enforced by a tool with a receipt.
- **3** claims are double-sourced (two independent roots). 5 rebrand clusters; the largest has 23 sources.
- **7 words are defined and automated:** polish, layout, typeset, adapt, animate, audit, extract. **27 words are honestly undefined** (bolder, quieter, delight, clarify, ...).
- 107 private-kit claims excluded (`reports/excluded.md`).

## What was built beyond Phases 0–4
- **Real tool runs on the Northstar demo** (axe-core 4.13, Lighthouse 13.5, Playwright 1.63, Stylelint 17, `@google/design.md` lint 0.4): the original page really fails (11 low-contrast nodes, no title, `outline:none`, a gradient, 61 spacing/target findings); axe and Lighthouse agree. Each run is a receipt with the exact command. better-tailwindcss and APCA were dropped (`reports/tools.md`).
- **A closed loop:** `fix.js` checks, generates a CSS patch, re-checks. 61 findings to 0 in one round (56 rules).
- **AXL definitions** (`data/definitions.json`, 7 verbs, 13 patterns): plain-language meaning, threshold, verbatim source quotes, command, receipts, and where sources disagree.
- **Site** (`axl/site/`): launch view (pick a word, see original vs applied with tool findings), dictionary, evidence rail, lineage map, Sources drawer, AXL export. Open with `cd axl/site && python3 -m http.server`.
- **Language** (`SPEC.md`, `spec/axl.schema.json`, two examples) and **skills** (`axl/skills/`).

## Review first
1. **The 13 AXL definitions are proposals.** Claim text and thresholds are written by AXL; each cites verbatim quotes, but the choice of 4px, 44px, 500ms and 14px as thresholds is ours where marked "AXL default". Two are double-sourced (44px targets, reduced motion) plus colour tokens.
2. **Lineage judgment calls** (`sources.json`): Impeccable derives from Anthropic's frontend-design; Anthropic blog/cookbook/skill are one root; WCAG Understanding pages share the WCAG root. All conservative.
3. **Regex tiering** (D8): 11 measurable + 21 enforced is a floor.
4. **Copy on the site** is plain-language first; check it reads the way you want.

## Known gaps
- Open finding: the demo table overflows a 320px screen by 12px (receipt `craft-reflow-320-polished`, marked `discriminates: false`).
- Checks cover the visible screen state at one width. `target-size` (24px) passes on the original too, so it does not discriminate.
- The site's demo "original" pane is intentionally faulty, so it is excluded from the axe gate.
- The site preview applies CSS only for patterns a receipt validated; others show the command instead.
- Zero verified claims came from the legacy paraphrased groups (g30–extra40): their text is not in the fetched sources. Deeper fetches (Taste-Skill v1 `SKILL.md`, samber, OneRedOak files) were not done.
- Recon fetched 52 sources (cap "about 40" exceeded to satisfy the plan's minimums).
- **The repo still needs a `LICENSE`; the owner must choose it.** Source licences are auto-detected or `unknown`.
- Not run: any deploy, a mobile tool runner, live in-browser tool execution (designed in `DEPLOY.md`).

## Run next
1. Read the site: `cd axl/site && python3 -m http.server`, then review `reports/metrics.md` and `data/definitions.json`.
2. Fresh checkout: `pip install jsonschema pyyaml && (cd axl/tools && npm ci) && bash axl/scripts/build_all.sh`.
3. Deploy when ready: follow `axl/DEPLOY.md` (`GCP_PROJECT`, then `gcloud builds submit --config axl/cloudbuild.yaml --substitutions=_DEPLOY=1 .`).
4. Next research pass: fetch the deeper legacy sources and re-run Phase 3; add definitions for `bolder`, `quieter`, `colorize`, `harden` only if a measurable source appears.
