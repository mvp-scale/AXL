# AXL v0.1 — the language in one page

AXL is a small JSON document with three operations. Schema: `spec/axl.schema.json`. Validate with `python3 axl/scripts/validate_axl.py <file>`.

| Operation | Question it answers | Content |
|---|---|---|
| `describe` | What is this experience? | surface, tokens (colour, type, space, motion), components, states, viewports |
| `evaluate` | Does it meet the definition? | rules `{id, tier, check, pass_criteria, tool?, command?, claim_ids[]}` and findings `{rule_id, pass/fail/na, evidence, location}` |
| `correct` | What exactly changes? | ops `{op: set/add/remove, target, property, value, reason, claim_id}` a tool can apply; anything needing judgment goes in `notes`, never in `ops` |

Every rule and op cites a claim id. A claim says who states it, the verbatim quote, the tier (`enforced`, `measurable`, `subjective`, `process`) and whether two independent sources back it. A rule with tier `enforced` must carry the command that was run.

## Example 1 — web (`spec/examples/web.axl.json`)

```json
{
  "axl": "0.1",
  "describe": { "surface": "web", "states": ["ready","loading","empty","error","success"], "viewports": ["1440x900","375x812"] },
  "evaluate": { "rules": [{
      "id": "contrast-4.5", "tier": "enforced", "check": "Text contrast is at least 4.5:1",
      "pass_criteria": "axe color-contrast reports 0 violations", "tool": "axe-core",
      "command": "node axl/tools/runners/axe.js axl/demo/after.html 1440", "claim_ids": ["clm_0471"] }],
    "findings": [{ "rule_id": "contrast-4.5", "result": "fail", "evidence": "#8a97a8 on #f5f6f8 = 2.74:1", "location": "footer > span" }] },
  "correct": { "ops": [{ "op": "set", "target": "footer span", "property": "color", "value": "#566579",
      "reason": "raise contrast from 2.74:1 to 5.5:1", "claim_id": "clm_0471" }] }
}
```

## Example 2 — mobile (`spec/examples/mobile.axl.json`, illustrative, no receipts)

```json
{
  "axl": "0.1",
  "describe": { "surface": "mobile", "states": ["ready","loading","empty","error"], "viewports": ["390x844","320x568"] },
  "evaluate": { "rules": [{ "id": "target-44", "tier": "measurable", "check": "Tap targets are at least 44x44 points",
      "pass_criteria": "every interactive element is >= 44x44pt", "claim_ids": ["clm_0477"] }],
    "findings": [{ "rule_id": "target-44", "result": "fail", "evidence": "tab-bar icon is 32x32pt", "location": "tab-bar/item[2]" }] },
  "correct": { "ops": [{ "op": "set", "target": "tab-bar/item", "property": "min-size", "value": "44pt",
      "reason": "raise to the 44x44 minimum", "claim_id": "clm_0477" }] }
}
```

The mobile example is a shape demonstration: the claim (44x44 targets) is real and double-sourced, but no mobile tool run backs it in v0.1.

## What v0.1 leaves out
Live tool execution in a browser, a mobile runner, and any rule with no measurable definition. Those stay `subjective` in the catalog and cannot be exported as `correct` ops.
