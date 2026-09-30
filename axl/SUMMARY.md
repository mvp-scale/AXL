# AXL — summary

Open `axl/site/index.html` (one file).

## What the page does (plan v2: `PLAN_V2.md`, standard: `RULE_STANDARD.md`)
- **Commands × Sources** pickers as before; ▶ walks either one; the Northstar demo is clickable (nine views) and Shift shows the original.
- **The list is Class › Element › Rules.** 13 classes anchored to standards (CSS modules, WCAG, Lighthouse, ARIA Practices); element rows use ARIA / Open UI / type-scale names; each rule is `element property test` in standard vocabulary, shown as a plain sentence.
- **Picking a command lights its rows** with "n of 13" = how many of the selected definitions ask for something there; a rule shows every value sources state (disagreements visible) and source chips that open the exact quote IDs.
- **Get my word → one kit** (Markdown): rules in words + code + quote IDs, how to use them, and the `axl` definition block; an optional console check.
- Numbers and method: `reports/phase3-rules.md`.

## Not done yet
- **Phase 4:** the 127 proposed `axl:` measures (and the CLI reading the kit) are not implemented; "measurable" means a check can be written, not that it exists. Existing checks (12 console checks, axe, Lighthouse) still run.
- **Phase 7:** the command matrix view is deferred until its place is decided.
- 25 rules without evidence are withheld; a LICENSE and deployment are still open.

## Checked by the gates (all pass)
- Site: `scripts/gates/site_check.py` checks that the page changes on its own within 2 s, one tap builds your word, save gives a valid file with a command, there are no network requests and no overflow, and axe finds nothing serious at 390 and 1440 px in light and dark.
- Tool: `scripts/gates/phase8.py` checks that `axl.py check` fails the original demo, passes the fixed one, `fix` writes a page, and `tweaks` lists tweaks.
- Data: `scripts/validate_atlas.py` checks 71 tweaks, all 42 demo effects used, and all 363 statements mapped (308 to at least one tweak, 55 to none). Phases 0–6 are unchanged.

## Review first
1. **The mapping from statement to tweak (`data/tweak_map.json`) was made by a model.** It is the heart of the overlap picture, so spot-check it.
2. The Taste-Skill and Anthropic versions of "polish" are my mapping of one verbatim quote each to tweaks. Impeccable and OneRedOak come from their own statements.
3. 12 sources is a start, not "the industry". Adding sources is how the overlap picture gets honest.

## Open
- A LICENSE is still needed.
- Nothing is deployed (`DEPLOY.md`).
- The 13 older "AXL definitions" (`data/definitions.json`) still back the checks. They are proposals.

## How changes are shown
- The page compares the changed demo with the original element by element (computed styles) and outlines every element that differs, in the source's colour ("37 changed"). Toggle with "Outline changes".
- 51 of 71 tweaks have a visible stand-in on the demo. The other 20 (performance, alt text, localisation, real-device testing, stress tests…) are labelled "not visual". A definition made only of those shows "Nothing to see" with what it asks for instead.
- A source that doesn't use the chosen command says so and offers to show its own commands.

## Audit (7 parallel agents, results checked by script before use)
- **Links:** all 363 statement-to-tweak links re-read. Batches 1–2: 239 of 242 correct. Batch 3 (paraphrased older groups): 98 of 121 correct. 24 edits applied; 6 concrete changes no tweak covers are listed in `reports/link_audit_gaps.json`.
- **35 newer definitions:** all quotes verbatim, links valid.
- **Coverage:** 71 tweaks was never the size of the field. The gap agent estimates a full catalogue at 200–400+. **20 tweaks added** (18 from WCAG 2.2, 2 from Smashing's form-validation guide), bringing the total to **91**. The agent's own quotes for 17 of its 21 suggestions were not in the pages it saved, so they were rejected and every quote was re-sourced from the fetched WCAG text.
- **Blend:** of 17 proposed non-Impeccable definitions, 5 were kept (GOV.UK *adapt*, web.dev *optimize*, W3C WAI *audit*, NN/g *critique*, Style Dictionary *extract*). The rest quoted text that doesn't define the command, or text that wasn't on the page. W3C WCAG 2.2 and Smashing Magazine were added as sources.
- **Now:** 32 sources, 25 commands, 91 tweaks. 16 of the 25 commands have two or more independent authors. Impeccable and its copies are 26 of 68 definitions (38%). Still Impeccable-only: animate, colorize, harden, layout, onboard, shape, typeset.

## The full catalogue (harvest, this pass)
- **Every rule from 21 sources + 3 standards**, not just their command pages: Impeccable (all 47 files incl. 61 detector anti-patterns), Taste-Skill (15 skills), UI Craft, Hallmark, samber deslop, Unslop UI, Feel Better, Anthropic, OpenAI, shadcn/ui, Google DESIGN.md, OneRedOak, Claw Design, Vercel Web Interface Guidelines, Apple HIG, NN/g, GOV.UK, web.dev; axe-core (105 rules), Lighthouse (139 audits), WCAG 2.2 (85 success criteria) harvested by script from the installed tools and the fetched standard.
- **5,800 unique rules** (after filtering file chatter and near-duplicates), each verbatim and substring-checked against its saved page. 4,219 are sorted into **1,325 tweaks**; 1,581 were judged not to be UI rules (tooling, file descriptions, example rows).
- Sorting: a Sonnet agent built a 414-tweak taxonomy; four Sonnet agents read and sorted every rule (a Haiku attempt was discarded: it keyword-matched and wrote row numbers). 911 tweaks were proposed from rules nothing else covered; 629 of those come from a single rule and are kept, marked by count.
- Material 3 could not be harvested (JavaScript-only site).
- Licence note: `data/catalog.json` commits ~5,800 short attributed quotes (<= 45 words each). Most sources are MIT/Apache; Apple HIG, NN/g and GOV.UK are not open-licensed; review before publishing.
