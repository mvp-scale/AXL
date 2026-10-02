# Harvest spec (every agent follows this exactly)

Goal: capture EVERY rule, guideline, check, anti-pattern or best practice a source states about UI/UX, visual design, interaction, accessibility, content, performance or agent design workflow. Not a summary: every item.

For each source:
1. Fetch the page(s) ONCE with `curl -sSL -m 45 -A "axl-harvest/0.2" <url>`. Prefer raw.githubusercontent.com for repo files (skill files, rule lists, reference folders: fetch every reference file the skill links to). Convert HTML to text with a small python script (strip script/style, collapse whitespace). Save to /home/user/AXL/axl/receipts/sources/h_<source-slug>__<n>.txt.
2. Split into items by script where the source is a list (bullets, table rows, numbered rules), then read and keep each item that states something to do or avoid. One item = one atomic rule. Keep the source's own wording.
3. Write /home/user/AXL/axl/data/harvest/<source-slug>.json:
   {"source":"Short Name","publisher":"...","kind":"skill|design-system|standard|tool|guide","urls":[...],"retrieved_at":"ISO","items":[
     {"text":"VERBATIM from the saved file, <= 45 words","file":"h_...txt","section":"heading it sits under or null",
      "category":"Type|Color|Space & layout|Surface|Motion|Interaction & states|Access|Content & process|Performance|Components|Agent workflow",
      "command":"the command/skill name it belongs to if the source groups rules under commands (e.g. polish), else null",
      "measurable":true|false}]}
4. BEFORE writing, run a python check that every item's text (whitespace-collapsed) is a substring of its saved file (whitespace-collapsed). DROP any item that fails. Never write text that is not in the file. Never paraphrase in `text`.
5. Final reply: <= 5 lines: items per source, pages fetched, pages that failed.
Rules: never paste page contents into your reply; process with scripts; do not edit files other than your own harvest JSONs and saved texts; do not commit.
