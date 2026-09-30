# Check any website against a word (e.g. your "super polish")

You need a **kit**: one Markdown file with the rules. Make one on the AXL site (pick rules → **Get my word** → download `your-word.axl.md`), or use `demo/kit/polish.axl.md`.

## A. Nothing to install: one file in the browser
1. On the AXL site, **Get my word → Check any page (one file) → Download**. You get `your-word.check.js` (about 600 KB: your rules, the AXL engine and axe-core). No network needed.
   From the repo you can make the same file: `python3 axl/axl.py bundle your-word.axl.md --out your-word.check.js`.
2. Open any website, press **F12** → **Console**, paste the whole file, press Enter.
3. You get PASS / FAIL / ASK per rule, each FAIL with the fix and the elements, and a JSON report copied to your clipboard to hand to your agent.

What a page can't do by itself (phone width, dark mode, hover, Lighthouse) is marked "not checkable here". Use B for those.

## B. Command line: the full check
Once, in the repo:
```
cd axl/tools && npm ci && npx playwright install chromium && cd ../..
```
Then:
```
python3 axl/axl.py check your-word.axl.md https://any-site.com          # or a local file: page.html
python3 axl/axl.py check your-word.axl.md https://any-site.com --json   # JSON for an agent
python3 axl/axl.py check your-word.axl.md https://any-site.com --quick  # skip Lighthouse (faster)
```
Exit code 0 = everything checkable passed, 1 = something failed. Behind a proxy with its own certificate add `--insecure`.

## What each result means
- **PASS / FAIL**: measured on the page. CSS rules read the browser's computed values; `wcag:` rules use axe-core; `lighthouse:` rules run Lighthouse; `axl:` rules use a measure defined in `axl/measures.md`.
- **ASK**: a question for a person or an agent. No script can decide it.
- **not checkable yet**: the rule uses an `axl:` measure that is proposed but not built yet, or axe has no automated rule for that WCAG criterion.
- **INVALID**: the rule has a typo (an unknown element or property). Nothing is guessed.

Tested: `scripts/gates/kit_check.py`. The original Northstar page fails 5 polish rules with the fixes named; all 5 pass once those fixes are applied; the offline one-file checker gives the same verdicts as the command line.
