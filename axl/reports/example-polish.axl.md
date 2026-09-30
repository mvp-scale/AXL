# polish

> Example kit (draft format). The rules are the ones Impeccable's `polish` asks for, rewritten as AXL rules.
> Rule IDs, settings and roles follow `RULE_STANDARD.md` (draft). Quote IDs are real and look up on the AXL site.

**What it means:** a final pass that makes the page consistent, complete and ready to ship.
**8 rules · 13 settings · 7 checked automatically · 6 reviewed by a person or agent**

## Rules

### 1. Size scale · `type.size-scale` · Type
Text sizes come from one small, consistent scale.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `type.size-scale/steps` | `text:*` | auto · distinct font sizes | ≤ 6 |
| `type.size-scale/roles` | `text:display` `text:headline` `text:title` `text:body` `text:label` | ask | Does every piece of text map to one of the scale's roles? |

Sources say: ≤ 5 sizes (hallmark:40775f) · 4–6 steps (ui-craft:4522a2) · 6–8 sizes (deslop:3d2e5c) · roles display/headline/title/body/label (impeccable:e6cc70)

### 2. Minimum text size · `type.min-size` · Type
Text is at least a minimum size for its role.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `type.min-size/body` | `text:body` | auto · font-size | ≥ 16px |
| `type.min-size/input` | `aria:textbox` `aria:searchbox` + `media:narrow` | auto · font-size | ≥ 16px |

Sources disagree: 16px (impeccable:b3b1d9, impeccable:e6d3a0, ui-craft:f24d64, deslop:b4223e) · 14px (hallmark:f0d4a2, impeccable:a2b590, deslop:f6b6cc, taste-skill:f282ba). Inputs 16px on phones (ui-craft:4562d9, vercel:6dd3d5).

### 3. Line height · `type.line-height` · Type
Line height is set by role: open for body copy, tight for large headings.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `type.line-height/body` | `text:body` | auto · line-height | ≥ 1.5 |
| `type.line-height/display` | `text:display` `text:headline` | auto · line-height | ≤ 1.2 |

Sources: 1.5 (impeccable:701826, oneredoak:88d955, deslop:f6b6cc) · 1.6 (taste-skill:6cf995) · headings 1.05–1.2 (ui-craft:2b39b8) · 0.95–1.05 (hallmark:867659)

### 4. Spacing rhythm · `layout.spacing-scale` · Space & layout
Spacing comes from a small set of repeated steps.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `layout.spacing-scale/steps` | `page` | auto · margins, paddings and gaps are multiples of the base unit | base 4px |

Sources: impeccable:6b3702, impeccable:4b2dac, claw-design:bce1dd, claw-design:59f92d (+ hallmark, openai, taste-skill, ui-craft)

### 5. One icon style · `surface.icon-style` · Surface
All icons come from one set, with one stroke weight.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `surface.icon-style/sets` | `ui:icon` | auto · distinct icon sets | ≤ 1 |
| `surface.icon-style/no-emoji` | `ui:icon` | auto · emoji used as icons | 0 |

Sources: impeccable:9864e3, feel-better:2ba963, feel-better:f32af7 (+ 6 more sources)

### 6. One primary action · `interaction.primary-action` · Interaction & states
Each view has one clearly strongest action.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `interaction.primary-action/count` | `aria:button` `aria:link` in a view | ask | Is there exactly one action that stands out most in each view? |

Sources: impeccable:cf7c3f, impeccable:52b4ae, claw-design:51e026, claw-design:49fb14 (+ 5 more sources)

### 7. Designed states · `interaction.states` · Interaction & states
Every view has a designed empty, loading and error state.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `interaction.states/empty` | `state:empty` | ask | Does the empty state say why it's empty and offer an action? |
| `interaction.states/loading` | `state:busy` | ask | Does loading name the operation and show progress when the wait is long? |
| `interaction.states/error` | `state:invalid` `aria:alert` | ask | Does every error say what went wrong and how to fix it? |

Sources: impeccable:9a6ecc, impeccable:331c13, hallmark:381ce7, hallmark:4e26fd (+ 3 more sources)

### 8. Media keeps its space · `perf.media-dimensions` · Performance
Images reserve their space before they load.

| Setting | Applies to | Check | Default |
|---|---|---|---|
| `perf.media-dimensions/size` | `aria:img` | auto · has width + height or aspect-ratio | all |

Sources: impeccable:ed3181, lighthouse:62c011, openai:2ebba0

## Run it

```
axl check polish.axl.md https://yoursite.com
```

What the report looks like:

```
polish — 5 of 7 automatic checks pass, 6 questions to review

FAIL  type.min-size/body          14px < 16px     p.card-copy (12 elements)
FAIL  surface.icon-style/no-emoji  3 emoji icons   .feature .emoji
PASS  type.size-scale/steps        5 sizes
PASS  type.line-height/body        1.55
…
ASK   interaction.primary-action/count   Is there exactly one action that stands out most in each view?
…
JSON for your agent: polish.report.json
```

## Definition (what the CLI reads)

```axl
word: polish
based_on: impeccable:polish
rules:
  type.size-scale:        { steps: "<= 6" }
  type.min-size:          { body: ">= 16px", input: ">= 16px" }
  type.line-height:       { body: ">= 1.5", display: "<= 1.2" }
  layout.spacing-scale:   { steps: "base 4px" }
  surface.icon-style:     { sets: "<= 1", no-emoji: "0" }
  interaction.primary-action: { count: ask }
  interaction.states:     { empty: ask, loading: ask, error: ask }
  perf.media-dimensions:  { size: all }
```

**Making it yours ("super polish"):** copy the block, change a value (`body: ">= 18px"`), add a rule (`color.contrast: { text: ">= 7" }`), or remove one. The rules keep their meaning; only your settings change.
