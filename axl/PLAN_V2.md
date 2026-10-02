# AXL plan v2: commands aligned to the standard structure

Approved by the owner, 2026-09-30. Standard: `RULE_STANDARD.md` (AXL Command Standard).

## Definition of done
1. The list reads **Class › Element › Rules** in plain English, grouped by the standards (CSS modules → class; ARIA / type-scale roles → element). No subjective verbs in the list.
2. Picking a command lights up its rows, with how many sources ask for each and the value each asks for; disagreements show inside the rows.
3. Every rule is **element + property + test** in standard vocabulary. The only AXL additions are a short listed set of `axl:` measures and `ask` questions.
4. Behind every rule: command → source definition → rule → value → quote IDs. Every quote ID is verified by script; the origin definition is credited.
5. Every rule shows on Northstar or says why it can't; every automatic check fails on the original demo and passes with the fix.
6. One downloadable kit: readable rules, the code form for the CLI, sources as IDs. `axl check kit.md <site>` runs it on any site.
7. The command matrix is placed last, once the data shows where it belongs.

## Phases
| # | Work | Owner checks |
|---|---|---|
| 1 | Vocabulary: element list (ARIA, text roles, Open UI, states, media), class ↔ standard map, word lists that render code as sentences (`data/vocab.json`) | element names read naturally |
| 2 | Type pilot: Type's 123 tweaks → element rows + rules; commands/sources linked with quote IDs | Type reads right; polish's Type rows make sense |
| 3 | All classes, parallel agents; scripts check quote IDs, duplicates and vocabulary | totals per class + sample |
| 4 | `axl:` measures and automatic checks built; Northstar round-trip; previews moved onto rules | which checks are automatic vs questions |
| 5 | Left-hand list → Class › Element › Rules, lit per command; detail with check, Northstar change, source chips → quote IDs | the site |
| 6 | Kit + CLI (`axl check kit.md <site>`), PASS / FAIL / ASK + JSON | polish on Northstar and one real site |
| 7 | Command matrix: placement decided from real data | owner's call |

## Guardrails
- Never invent quotes. A link without a verbatim quote is marked unverified.
- `legacy/` and `best-practices/` untouched. Commit and push after every phase.
- Agents draft, scripts verify. Phases 1–3 change data only; the site changes from phase 5.
