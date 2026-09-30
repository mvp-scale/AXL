# AXL — summary

Open `axl/site/index.html` (one file).

## What the page does, in the order a person meets it
1. **0–2 s, no clicks.** The word "polish" and the demo page. The page changes every 1.8 s as it cycles through four sources' versions of "polish" (Impeccable, Taste-Skill, Anthropic, OneRedOak), each with its verbatim quote. The only claim: "Same word. 4 sources, 4 different pages."
2. **Beside it:** all 71 tweaks behind the words, in 8 categories. Shading shows how many of the 12 sources ask for each one, a tick means a tool can check it, and an outline marks the tweaks in the version on screen.
3. **1 tap:** a tweak joins *your* word and the page switches to your version. The bar shows how many of your tweaks a tool can check and which existing words yours is closest to ("closest to quieter (Impeccable) 57%"). This is the "polish-adjacent" grouping, computed live.
4. **Save:** your word as a small JSON file, plus the command `python3 axl/axl.py check my-polish.axl.json yourpage.html`. No agent interprets it.
5. **Scroll, if curious:** a table of which source asks for which tweak (only 21 of 71 are asked for by 3 or more sources), and the statements no tool can check (55 of 363).

Any of the 29 words can be picked from the word menu.

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
