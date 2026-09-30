# AXL Rule Standard (draft 0.2)

A rule is **element + property + test**, written in the web's existing standard vocabularies. AXL adds as little vocabulary of its own as it can.
A command like "polish" is a list of rules. Any two commands can be compared rule by rule because rules with the same element and property are the same rule.

## 1. The rule

```
<element>  <property>  <test>  [<context>]
text:body  font-size   >= 16px
aria:textbox font-size >= 16px  @media:narrow
text:*     wcag:1.4.3  pass
state:invalid  ask  "Does the message say how to fix it?"
```

- **Rule ID** = `<element>/<property>` (e.g. `text:body/font-size`). Two sources asking about the same element and property are asking about the same rule; if their values differ, that is a visible disagreement, not two rules.
- **Test**: `>= <= == between A B contains !contains pass` with a value and unit, or `ask "<yes/no question>"` when no script can decide.
- **Context** (optional) narrows where the rule applies: a `state:` or `media:` term.

## 2. Element: standard vocabularies, namespaced

| Namespace | Standard | Found on a page by | Examples |
|---|---|---|---|
| `aria:` | WAI-ARIA 1.2 roles (W3C Recommendation, 2023); 1.3 roles when published | the accessibility tree (native HTML and explicit `role`) | `aria:button` `aria:link` `aria:textbox` `aria:heading` `aria:dialog` `aria:navigation` `aria:img` `aria:table` `aria:alert` `aria:status` `aria:tab` |
| `text:` | Type-scale roles (Material 3: display, headline, title, body, label) + `caption`, `code` | size/weight bands of the page's own type scale, plus element hints (`h1`…, `p`, `label`, `figcaption`, `code`) | `text:display` `text:headline` `text:title` `text:body` `text:label` `text:caption` `text:code` `text:*` |
| `ui:` | Open UI component names (W3C Community Group research) | class, `data-` and structural heuristics; weakest namespace, so each heuristic is documented | `ui:card` `ui:badge` `ui:avatar` `ui:toast` `ui:skeleton` `ui:icon` `ui:carousel` |
| `state:` | ARIA states + CSS pseudo-classes | `:hover` `:focus-visible` `:disabled`, `aria-invalid` `aria-busy` `aria-expanded`… | `state:hover` `state:focus-visible` `state:disabled` `state:invalid` `state:busy` `state:empty` |
| `media:` | CSS media features | emulated in the browser | `media:dark` `media:reduced-motion` `media:narrow` (≤ 390px) `media:print` |
| `page` | the whole document | | `page` |
| `x-<name>:` | anyone's own extension | defined by its author | `x-acme:pricing-table` |

## 3. Property: standard vocabularies, namespaced

| Namespace | Standard | Examples |
|---|---|---|
| (none) | CSS properties, as computed by the browser | `font-size` `line-height` `font-weight` `letter-spacing` `text-transform` `text-align` `border-radius` `box-shadow` `transition-duration` `background-image` `max-width` |
| `wcag:` | WCAG 2.2 success criteria, run by axe where axe covers them | `wcag:1.4.3` contrast · `wcag:1.4.10` reflow · `wcag:2.4.7` focus visible · `wcag:2.5.8` target size · `wcag:3.1.1` page language |
| `lighthouse:` | Lighthouse audit IDs | `lighthouse:cls` `lighthouse:lcp` `lighthouse:unsized-images` `lighthouse:font-display` |
| `axl:` | **only** measures no standard defines, each defined once in `axl/measures.md` | `axl:distinct-font-sizes` `axl:distinct-font-families` `axl:distinct-hues` `axl:icon-sets` `axl:emoji-as-icons` `axl:spacing-off-scale` `axl:chars-per-line` |
| `ask` | a yes/no question when nothing can be measured | `ask "Is there exactly one action that stands out most?"` |

An `axl:` measure is added only when no CSS property, WCAG criterion or Lighthouse audit expresses it. Each one is implemented once and proven on Northstar: it fails on the original and passes with the demo fix.

## 4. Grouping (display only)

Rules are grouped for people, never renamed:
- **By class**, derived from the property: font and text properties → Type; colour, `wcag:1.4.3`, `axl:distinct-hues` → Color; spacing and size → Space & layout; radius, shadow, borders, `background-image` → Surface; `transition-*`, `animation-*`, `media:reduced-motion` → Motion; `state:*` → Interaction & states; `ui:*` and composite `aria:*` → Components; `wcag:*` → Access; `lighthouse:*` → Performance; `ask` with element `page` or `process` → Content & process / Agent workflow.
- **By element**, e.g. "text:body · 4 rules".
- **A plain label** may be shown ("Minimum body text size"); it is not an identifier.

## 5. Evidence

Every rule lists the source statements behind each stated value, as permanent quote IDs (`<source-id>:<hash of exact text>`, see `data/catalog.json`):

```
text:body/font-size   >= 16px   ← impeccable:b3b1d9, ui-craft:f24d64, deslop:b4223e
                      >= 14px   ← hallmark:f0d4a2, taste-skill:f282ba
default: 16px (most statements)
```

## 6. When a rule is accepted

1. Element and property come from the vocabularies above; anything `x-` or `axl:` is defined in its list.
2. It has at least one evidence quote ID, or cites the standard it comes from (e.g. a WCAG criterion).
3. An automatic rule passes the Northstar round-trip; an `ask` rule is a yes/no question about something observable.
4. No other rule has the same `element/property` (otherwise it is the same rule with another value).

## 7. Files

- `data/rules.json`: every rule (element, property, default test, evidence, label)
- `axl/measures.md`: the `axl:` measures, each with its exact definition
- `data/catalog.json`: statements with permanent quote IDs; `data/sources_index.json`: source IDs
- `data/previews.json`: the Northstar demonstration per rule
