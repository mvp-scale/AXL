# AXL

Open **`site/index.html`**: one file, no server, no network. It shows that design words like "polish" mean different things to different sources, lays out every concrete tweak behind them, and lets you build your own version of a word as a file a tool can check.

Check a page against your word: `python3 axl.py check my-polish.axl.json yourpage.html`

| Path | What it is |
|---|---|
| `site/index.html` | The page (built; do not edit by hand) |
| `axl.py` | The tool: `check`, `fix`, `tweaks`. Deterministic; no agent interprets anything |
| `data/tweaks.json`, `data/tweak_map.json` | The 71 tweaks, and which source statement asks for which (model-assisted, reviewable) |
| `data/claims.json`, `data/sources.json`, `receipts/` | The statements, their verbatim quotes, the fetched sources and the saved tool runs |
| `scripts/atlas_template.html`, `scripts/build_atlas.py` | Source and builder of the page |
| `tools/`, `demo/` | The pinned checkers and the demo app they run on |
| `SPEC.md`, `spec/` | The AXL document format |
| `CONTRIBUTING.md` | How to add or challenge a tweak or a mapping |

Rebuild: `pip install jsonschema pyyaml && (cd tools && npm ci) && bash scripts/build_all.sh`
