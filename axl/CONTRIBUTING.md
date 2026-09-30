# Add or challenge a word

AXL only works if the vocabulary can be extended and argued with in the open. A term is worth adding when a person can say what it changes and a tool can say pass or fail.

## Add a definition (about 15 minutes)
1. Pick a word that is `undefined` in `terms.json`, or a new one.
2. In `scripts/definitions_spec.py` add a pattern: a plain sentence, a threshold, one or more **verbatim** quotes from public sources (the build fails if a quote is not found in the fetched page), and the receipts that prove a tool can fail the "before" and pass the "after".
3. If no tool exists yet, add a runner in `tools/runners/` that prints `{findings:[{rule_id,result,evidence,location}]}` and a before/after fixture in `demo/`. Add both to `tools/receipts.json`.
4. Run `bash scripts/build_all.sh` and the gates in `scripts/gates/`. A pattern with no receipt cannot be `enforced`.
5. Say in your change which parts are your choice ("AXL default") and which a source states.

## Challenge a definition
Open the pattern's claim (`data/claims.json`) and show a source that contradicts the threshold, or a page where the check gives a wrong answer. A challenged claim is kept with the reason; nothing is silently deleted.

## Rules that do not bend
- Quotes are copied from a page that was fetched, never reconstructed. Unfetched means `unverified`.
- Two sources that trace back to one origin count once.
- No brand names as authority. Sources are cited as sources.
- A word with no measurable definition stays in the catalog, labelled that way.
