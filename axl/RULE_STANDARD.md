# AXL Rule Standard (draft 0.1)

The canonical model every AXL rule follows. Commands like "polish" are not defined here. A command is just a list of rules with chosen settings, so any two commands (anyone's "polish", your "super polish") can be compared rule by rule.

## 1. The model

```
Class    (fixed, 11)     Type · Color · Space & layout · Surface · Motion · Interaction & states ·
                          Components · Access · Content & process · Performance · Agent workflow
Rule     (open)          one general idea, true for any site           e.g. type.min-size  "Minimum text size"
Setting  (open)          one checkable part of a rule                  e.g. type.min-size/body   body text ≥ 16px
Evidence (append-only)   the source statements behind a setting        e.g. impeccable:ab12cd says "16px"
```

- **Class** is the readable bucket, and the list is fixed. A new class needs an explicit decision recorded in DECISIONS.md.
- **Rules and settings are open.** Add them only when source statements call for them. Nothing is pre-generated.
- **Evidence** links a setting to permanent quote IDs (`<source-id>:<hash of the exact text>`). It is never copied into rules.

## 2. What a rule must have

| Field | Must | Example |
|---|---|---|
| `id` | `<class-prefix>.<kebab-name>`. No values, numbers or element names. Never renamed or reused; retired rules are marked `deprecated`, not deleted. | `type.min-size` |
| `name` | 2–4 plain words | Minimum text size |
| `rule` | one sentence that is true or false for **any** website | Text is at least a minimum size for its role. |
| `class` | one of the 11 | Type |
| `settings` | one or more | see §3 |
| `see` | optional: another rule this one overlaps with (shown, not merged) | `access.text-scaling` |

A rule is **one idea**. If its settings don't share the rule sentence, split the rule. If two rules have the same sentence, merge them.

## 3. What a setting must have

| Field | Must | Example |
|---|---|---|
| `id` | `<rule-id>/<aspect>`, where aspect is kebab-case and describes *what* is checked | `type.min-size/body` |
| `applies_to` | element roles from §4 (one or more) | `[body]` |
| `check` | `auto` (a script decides) or `ask` (a person or agent decides) | `auto` |
| `measure` + `test` | **auto only**: a measure from §5 and a comparison with a default value | `font-size >= 16px` |
| `question` | **ask only**: yes/no, answerable by looking at the page; YES = met | Does every error say how to fix it? |
| `evidence` | each value sources state → quote IDs; empty only if the default comes from a named standard | `16px ← impeccable:ab12cd, wcag22:…` |

- **The default value** is the value most sources state. Other stated values stay listed, and that's how disagreements show.
- **A command overrides values, never meanings.** "super polish" may set `type.min-size/body >= 18px`, but it can't make that setting measure something else.

## 4. Element roles (fixed list; extend by decision)

page · body · small · caption · label · heading (h1–h6) · display · link · button · input · form · error · icon · image · media · card · surface · nav · dialog · toast · table · chart · list · code · focus · hover · active · disabled · loading · empty · motion · dark-mode · mobile · print · process (not on the page: team or agent workflow)

## 5. Measures (fixed registry)

An `auto` setting may only use a registered measure. Each measure is defined once, implemented once in `axl.py`, and verified on Northstar: it fails before the demo fix and passes after it.

A measure entry has: `id`, what is computed, on which roles, unit, and how an element is found on any page.
First set (from the Type pilot and the existing checks): font-size, line-height, letter-spacing, font-weight, font-family-count, font-weight-count, measure-ch, contrast, non-text-contrast, target-size, spacing-scale, radius, radius-count, shadow-count, duration, reduced-motion, distinct-hues, accent-count, gradient, emoji-icons, icon-set-count, alt-text, label, focus-visible, heading-order, lang, overflow-320, text-wrap, tabular-nums, quotes-typographic, all-caps, justify, italic, lcp, cls, font-display.
A setting that doesn't fit a registered measure is `ask` until a measure is added. Never stretch a measure to fit.

## 6. When a rule is accepted

1. It has at least one evidence quote ID, or it cites a named standard.
2. Every `auto` setting uses a registered measure, and its test passes the Northstar round-trip (fails on the original, passes with the demo fix).
3. Every `ask` question is yes/no and about what is visible or observable.
4. It shows on Northstar (the demo fix), or carries a reason it can't (behaviour, performance, process…).
5. No other rule in any class has the same sentence (the overlap check).

## 7. Files

- `data/rules.json`: classes, rules and settings (this standard's instances); the site, kit and CLI all read it.
- `data/catalog.json`: every harvested statement with its permanent quote ID.
- `data/sources_index.json`: source IDs.
- `data/previews.json`: the Northstar demonstration per setting.
