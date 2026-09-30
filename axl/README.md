# AXL

Open **`site/index.html`** in a browser. That is the whole product page: one file, no server, no network.

Everything else is what produced it, and can be ignored unless you want to rebuild or check it:

| Path | What it is |
|---|---|
| `site/index.html` | The story page (built; do not edit by hand) |
| `scripts/story_template.html`, `scripts/build_story.py` | Source of the page and its builder |
| `data/`, `receipts/runs/` | Claims, sources, verbs, and the saved tool runs the page reads |
| `tools/`, `demo/` | The pinned checkers and the demo app they run on |
| `skills/` | Four agent skills that run the same checks on your own page |
| `terms.json`, `CONTRIBUTING.md` | The stable term registry other tools can read, and how to add or challenge a word |
| `SPEC.md`, `spec/` | The AXL language |
| `SUMMARY.md` | What passed, what is open, what to run next |

Rebuild: `pip install jsonschema pyyaml && (cd tools && npm ci) && bash scripts/build_all.sh`
