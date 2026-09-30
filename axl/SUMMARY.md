# AXL — summary

Open `axl/site/index.html` (one file).

## What the page does
- **Two matching pickers:** **Commands** (25: polish, bolder, quieter… plus "checklist" for sources that publish a general checklist instead of commands) × **Sources** (25: Impeccable, UI Craft, Anthropic…). Both are multi-select, and each item has its own colour.
- **▶ on either picker walks through it:** one word or one source at a time. The demo changes, the progress ticks advance, a label names what's on screen, and the board of all 71 tweaks lights up in that colour.
- **First screen:** "polish" × all 25 sources, walking the sources. The counters read 13 definitions, 11 independent, 28 tweaks, **0 shared by all**.
- **Controls:** hold **Shift**, or the button on the page, for the original. Tap any tweak on the board to build your own word, then save it as a file that `axl.py check` runs.

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
