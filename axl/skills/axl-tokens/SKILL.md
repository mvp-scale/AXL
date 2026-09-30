---
name: axl-tokens
description: Find raw hex colours and off-scale spacing in a stylesheet and align it to a design token file. Use when asked to extract, consolidate or standardise colours and spacing, or to check a stylesheet against tokens.
---

# axl-tokens

```
python3 axl/skills/axl-tokens/scripts/tokens.py init  <style.css> tokens.json --n 12
python3 axl/skills/axl-tokens/scripts/tokens.py check <style.css> tokens.json [--strict]
python3 axl/skills/axl-tokens/scripts/tokens.py fix   <style.css> tokens.json <out.css>
```

- `init` derives a token set from the most-used colours. Prefer the project's own token file when one exists.
- `check` prints findings as JSON: `raw-colour` (a hex value that is not a token) and `off-scale-spacing` (not a multiple of the spacing unit).
- `fix` snaps colours to the nearest token (distance 60 or less in RGB) and spacing to the unit. Values it cannot place safely are left alone and remain findings.

Claim ids covered: clm_0485, clm_0476.
Limits: hex colours and padding/margin/gap only. Snapping a colour can change contrast: run axl-evaluate on the result. Choosing which values deserve a name is a judgment call and stays with the user.
