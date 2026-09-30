# AXL — summary

Open `axl/site/index.html` (one file).

## What the page does
- **Two matching pickers:** **Words** (24: polish, bolder, quieter…) × **Sources** (25: Impeccable, UI Craft, Anthropic…). Both are multi-select, and each item has its own colour.
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
