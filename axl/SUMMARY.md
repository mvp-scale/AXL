# AXL — summary

Open `axl/site/index.html` (one file).

## What the page does, in the order a person meets it
1. **0–2 s, no clicks.** The word "polish" and the demo page. The page changes every 1.8 s as it cycles through four sources' versions of "polish", each with its verbatim quote. The only claim: "Same word. 4 sources, 4 different pages."
2. **The subway map (right).** Each source is a coloured line leaving the station "polish" and stopping at the tweaks it asks for, grouped by category. A stop that several lines share is joined across them, so you can see which sources agree. Headline numbers: 4 sources, 20 different tweaks, 6 shared by two or more, **0 shared by all**.
3. **Compare instantly.** Hold **Shift**, or press and hold the page on a phone, to flash the original; release to go back. Keys **1–4** switch source and **Y** shows yours.
4. **1 tap on a stop** adds it to *your* line (pink) and the page shows your version. The bar shows how many of your tweaks a tool can check and the nearest named words ("polish (Taste-Skill) 33%, bolder (Impeccable) 20%").
5. **Save:** your word as a small JSON file, plus `python3 axl/axl.py check my-polish.axl.json yourpage.html`.
6. **The word menu** lists all 29 words with how many sources define each. **All 71 tweaks** sit in a collapsed list under the map. Below the fold is one line ("12 sources. 29 words. 71 tweaks. No standard.") and the statements no tool can check.

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
