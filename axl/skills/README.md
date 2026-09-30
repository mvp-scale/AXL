# AXL skills hub

Four skills in the standard Agent Skills layout (`SKILL.md` with `name` and `description`, plus `scripts/`). A skill's script does the deciding; its `SKILL.md` only says when to call it and how to read the result.

| Skill | Does | Claims |
|---|---|---|
| `axl-evaluate` | runs the enforced checks on an HTML file and prints findings | see its SKILL.md |
| `axl-correct` | applies measurable patches (auto, or from an AXL document) | see its SKILL.md |
| `axl-verbs` | maps a vague request to checks, or says the word is undefined | all patterns |
| `axl-tokens` | finds raw colours and off-scale spacing, aligns to a token file | see its SKILL.md |

## Admission rule
A skill may cite only claims whose tier is `enforced` or `measurable`. `python3 axl/scripts/lint_skills.py` fails the build if any claim id in a skill is `subjective` or `process`, or is missing from the claim set.

## Maintenance rules
1. **Claims.** Every skill lists the claim ids it relies on (in its `SKILL.md`). Change a claim and re-run the linter.
2. **Nightly source check.** Run `python3 axl/scripts/refetch_sources.py` nightly (scheduling is described in `DEPLOY.md`). It flags any page whose content hash changed and any page that is dead.
3. **Status drops.** If a claim's status falls below `single-source` (a quote no longer matches after a re-fetch), the linter flags every skill that cites it for review. Do not ship those skills until a person has looked.
4. **Pinned tools.** Every wrapped tool is pinned in `axl/tools/package-lock.json` (`npm ci`). Bump a version only together with `python3 axl/scripts/run_receipts.py` and `rerun_receipts.py`; receipts must still reproduce (90% or more).
5. **Receipts.** The command a skill runs must exist as a receipt in `axl/receipts/runs/`. `rerun_receipts.py` re-runs them all.
6. **Refresh.** `python3 axl/scripts/build_skills.py` regenerates `axl-verbs/references/verbs.json` from the data files.
