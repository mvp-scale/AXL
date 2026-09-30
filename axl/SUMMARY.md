# AXL — summary

Open `axl/site/index.html`. It is one file that tells the story in five touches; everything else in `axl/` produced it.

## The page (what a stranger does)
1. **The word.** "polish" breaks into three real meanings (final pass, add motion, look expensive) taken from three sources. Touch one to see the quote.
2. **Measured.** The same page, before and after. A fix wipes across it, the problem counter falls from 59 to 0, and numbered dots land on each change. Touch a dot: before and after close-ups, the measured numbers, the command that checks it, and who says so.
3. **The wall.** All 34 design words. 7 light up with their numbers; 27 stay dark with no number anywhere.
4. **Who says so.** 3 of 378 claims have two independent sources. The map shows how many sources trace back to one origin.
5. **Your page next.** One command.

Checked by `axl/scripts/gates/site_check.py`: 9 words and one control on the first screen, movement inside 1.2 s, no scrolling to find the button, the stage ends at 0 with 5 pins, each dot opens close-up, command and source, all 34 tiles answer, no network requests, no serious accessibility issues at 375 and 1440 px in light and dark, reduced-motion end states present.

## Gates (all pass)
0 setup, 1 legacy extract (41 groups, 470 prescriptions), 2 recon (90 sources, 52 fetched), 3 claims (485; 253 verbatim quotes), 4 verbs (7 tool-backed, 27 undefined), 5 tools (27/27 receipts reproduce; 21 claims enforced), 6 metrics, 7 site, 8 skills, 9 GCP files (not deployed).

## Headline (computed)
97.9% of 332 audited guidance statements have no measurable definition; 2.1% do; 1.8% are enforced by a tool with a receipt.

## Review first
1. The 13 AXL definitions in `data/definitions.json` are proposals: thresholds marked "AXL default" (4px, 44px, 500ms, 14px) are our choice.
2. The three meanings of "polish" are real quotes but a selection; other sources say other things.
3. Lineage judgment calls (`data/sources.json`): Impeccable derives from Anthropic's frontend-design; blog, cookbook and skill count as one root.

## Open
- The demo table overflows a 320px screen by 12px (receipt `craft-reflow-320-polished`).
- Legacy paraphrased groups are unverified; deeper source fetches were not done.
- A `LICENSE` is still needed; the owner chooses it.
- Nothing is deployed (`axl/DEPLOY.md`).
