---
name: axl-correct
description: Apply measurable fixes to an HTML file (snap spacing to a 4px scale, raise tap targets to 44px, darken low-contrast text) or apply the correct.ops of an AXL document. Use after axl-evaluate reports failures a tool can fix mechanically.
---

# axl-correct

Two modes, both mechanical. If a fix needs judgment, do not use this skill; write a note instead.

```
python3 axl/skills/axl-correct/scripts/correct.py auto  <file.html> --out fixed.html [--ops-out ops.json]
python3 axl/skills/axl-correct/scripts/correct.py apply <file.html> <axl.json> --out fixed.html
```

- `auto` finds the problems, generates the patch, applies it, re-checks, and prints `findings before: N, after: M`. Exit 1 means M is not 0: report the remainder.
- `apply` writes each `correct.ops` entry (`set`, `add`, `remove`) as CSS. Every op must cite a claim id or the script refuses.
- The patch is one `<style id="axl-patch">` block, easy to review and to remove.

Claim ids covered: clm_0476, clm_0477, clm_0471.
Limits: `auto` patches the visible screen state at one width; run axl-evaluate on the output and at other widths.
Setup: `cd axl/tools && npm ci`.
