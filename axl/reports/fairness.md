# Fairness audit

2430 renders (definitions x 9 demo pages x desktop/tablet/mobile). **6 made the page worse** (4 definitions).

A preview is AXL's rendering of a rule, not the source's own code: any harm listed here is AXL's to fix, not the source's.

| Definition | Page | Size | Worse on | Before → after |
|---|---|---|---|---|
| checklist · UI Craft | editor | desktop | overlap | overlap 0→1 |
| checklist · UI Craft | site | desktop | squeezed | squeezed 0→2 |
| checklist · UI Craft | editor | tablet | overlap | overlap 0→1 |
| checklist · Hallmark | site | mobile | hscroll, offscreen | hscroll 0→1, offscreen 0→2 |
| checklist · Taste-Skill | site | mobile | hscroll, offscreen | hscroll 0→1, offscreen 0→7 |
| checklist · samber deslop | overview | mobile | overlap | overlap 0→2 |
