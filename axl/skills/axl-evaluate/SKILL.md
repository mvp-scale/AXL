---
name: axl-evaluate
description: Run measurable UI checks (text contrast, spacing scale, tap targets, line length, text size, reflow, reduced motion, accessibility rules) on a local HTML file and get pass/fail findings. Use when asked to check, audit or verify a page, or before and after a design change.
---

# axl-evaluate

Call the script; do not judge the page yourself.

```
python3 axl/skills/axl-evaluate/scripts/evaluate.py <file.html> [--width 1440] [--json] [--axl out.json] [--strict]
```

Read the result:
- `PASS` / `FAIL` / `NA` per rule, with the claim ids that define the rule. `NA` means the tool errored; say so, do not treat it as a pass.
- Each `FAIL` lists a location and the measured evidence. Report those, not your opinion.
- `--axl out.json` writes an AXL document (`evaluate` section) you can hand to axl-correct or keep as a receipt.
- Exit code is 0 when the checks ran; add `--strict` to fail the command when anything fails.

Claim ids covered: clm_0471, clm_0476, clm_0477, clm_0478, clm_0481, clm_0480, clm_0479, clm_0483, clm_0484.
Every claim is enforced or measurable; anything subjective is out of scope for this skill.

Limits: only the visible screen state is checked; the accessibility rules find about 57% of WCAG issues automatically (per axe-core), so a clean run is not a full audit.
Setup: `cd axl/tools && npm ci`; set `CHROME_PATH` if Chromium is not at the default path.
