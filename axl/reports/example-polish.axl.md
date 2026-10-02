# polish

> Example kit, draft format 0.2: each rule is **element + property + test** in standard vocabularies (see `RULE_STANDARD.md`).
> The rules are the ones Impeccable's `polish` asks for, with evidence from every source that states them (rows 8 and 12 come from other sources). Quote IDs are real and look up on the AXL site.

**12 rules · 8 automatic · 4 questions**

## Rules

| # | Rule | Test | Class | Sources |
|---|---|---|---|---|
| 1 | `text:* axl:distinct-font-sizes` | `<= 6` | Type | hallmark:40775f (≤5) · ui-craft:4522a2 (4–6) · deslop:3d2e5c (6–8) |
| 2 | `text:body font-size` | `>= 16px` | Type | 16px: impeccable:b3b1d9, ui-craft:f24d64, deslop:b4223e · **14px**: hallmark:f0d4a2, taste-skill:f282ba |
| 3 | `aria:textbox font-size` `@media:narrow` | `>= 16px` | Type | ui-craft:4562d9, vercel:6dd3d5 |
| 4 | `text:body line-height` | `>= 1.5` | Type | impeccable:701826, oneredoak:88d955 · 1.6: taste-skill:6cf995 |
| 5 | `text:display line-height` | `<= 1.2` | Type | ui-craft:2b39b8 (1.05–1.2) · hallmark:867659 (0.95–1.05) |
| 6 | `page axl:spacing-off-scale` | `== 0` (base 4px) | Space & layout | impeccable:6b3702, impeccable:4b2dac, claw-design:59f92d |
| 7 | `ui:icon axl:icon-sets` | `<= 1` | Surface | impeccable:9864e3, feel-better:2ba963 |
| 8 | `ui:icon axl:emoji-as-icons` | `== 0` | Surface | hallmark:0560d5, ui-craft:0be8cf, unslop:67cbfb, claw-design:4f1bfd |
| 9 | `aria:img lighthouse:unsized-images` | `pass` | Performance | impeccable:ed3181, lighthouse:62c011, openai:2ebba0 |
| 10 | `page ask` | "Is there exactly one action that stands out most in each view?" | Interaction & states | impeccable:cf7c3f, claw-design:49fb14 |
| 11 | `state:empty ask` | "Does the empty state say why it's empty and offer an action?" | Interaction & states | impeccable:331c13, hallmark:4e26fd |
| 12 | `state:invalid ask` | "Does every error say what went wrong and how to fix it?" | Interaction & states | nngroup:12c78e, deslop:c17b4d, deslop:4dbf4d |

(Rows 1–5 as the front end would group them: **text:body · 2 rules**, **text:display · 1 rule**…)

## Run it

```
axl check polish.axl.md https://yoursite.com
```

```
polish — 6 of 8 automatic rules pass · 4 questions to review
FAIL  text:body font-size >= 16px        14px on 12 elements (p.card-copy …)
FAIL  ui:icon axl:emoji-as-icons == 0    3 found (.feature .emoji)
PASS  text:* axl:distinct-font-sizes <= 6   5
PASS  text:body line-height >= 1.5       1.55
…
ASK   page — Is there exactly one action that stands out most in each view?
```

## Definition (what the CLI reads)

```axl
word: polish
based_on: impeccable
rules:
  - text:* axl:distinct-font-sizes <= 6
  - text:body font-size >= 16px
  - aria:textbox font-size >= 16px @media:narrow
  - text:body line-height >= 1.5
  - text:display line-height <= 1.2
  - page axl:spacing-off-scale == 0 base=4px
  - ui:icon axl:icon-sets <= 1
  - ui:icon axl:emoji-as-icons == 0
  - aria:img lighthouse:unsized-images pass
  - page ask "Is there exactly one action that stands out most in each view?"
  - state:empty ask "Does the empty state say why it's empty and offer an action?"
  - state:invalid ask "Does every error say what went wrong and how to fix it?"
```

**super polish** = the same list, changing values in place (`text:body font-size >= 18px`) and adding lines (`text:* wcag:1.4.6 pass` for 7:1 contrast).
