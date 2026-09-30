# AXL Command Standard (draft 0.3)

**What AXL is:** design commands like *polish*, *bolder* or *quieter* have no shared definition. AXL records what each source means by a command, expresses it in the web's existing standard structure, and shows where definitions agree, differ or conflict. Anyone can then define their own version and check a site against it.

**What AXL is not:** a UI ontology. The structure of UI (what can be styled, what elements exist, how accessibility and performance are checked) is already defined by W3C and industry standards. AXL references it and defines only the command layer on top.

## 1. What AXL defines

```
Command      a word people give designers or agents: polish, bolder, quieter, distill …
 └ Definition   one source's (or one person's) meaning of that command
     ├ origin     who defined it and where (e.g. Impeccable, first published <date>)
     ├ linkage    the rules it points to, each with the value that source asks for
     └ evidence   the statements behind each link, as permanent quote IDs
```

| Object | Fields | Example |
|---|---|---|
| Command | `id`, aliases | `polish` (aliases: refine, finalize) |
| Definition | `command`, `source` (source ID or `you`), `origin` (URL, date), `based_on` (another definition it copies or extends), `rules` | `polish@impeccable` |
| Link | `rule`, `test` (that source's value), `evidence` (quote IDs) | `text:body font-size >= 16px ← impeccable:b3b1d9` |

**Credit.** The definition that originated a command is marked `origin` (earliest public definition, or the one others demonstrably copy, per `data/lineage.json`). Where a source is the reference definition, as Impeccable is for *polish*, it's credited as such. Copies and rebrands are linked with `based_on` and counted as one independent voice.

## 2. What AXL references (not ours)

A **rule** is `<element> <property> <test>`, written in standard vocabularies. Its ID is `<element>/<property>`.

| Part | Vocabulary | Source of truth |
|---|---|---|
| Element | `aria:` roles | WAI-ARIA 1.2 (W3C Rec., 2023); 1.3 roles when published |
| | `text:` roles | type-scale roles (display, headline, title, body, label) + caption, code |
| | `ui:` components | Open UI component research (W3C Community Group) |
| | `state:` | ARIA states + CSS pseudo-classes |
| | `media:` | CSS media features |
| | `page`, `process` | the whole document; work that isn't on the page |
| Property | CSS properties | CSS specifications (computed values) |
| | `wcag:` | WCAG 2.2 success criteria |
| | `lighthouse:` | Lighthouse audit IDs |
| Test | `>= <= == between contains !contains pass` + value | |

**Grouping for display** is read from the standards too, never invented:
- **Aspect**, by the property's family: Type (CSS Fonts, Text) · Color & theming (CSS Color) · Space & layout (Box Model, Sizing, Flexbox, Grid) · Surface (Backgrounds & Borders) · Imagery (CSS Images, Filter Effects) · Motion (Transitions, Animations) · Access (WCAG) · Performance (Lighthouse, Core Web Vitals) · Search & metadata (Lighthouse SEO) · Locale (Writing Modes, Logical Properties) · Content and Process (no standard; see §3). Staged: Sound & haptics.
- **Element family**, by ARIA's own role categories: Landmarks & navigation · Document structure · Widgets & forms · Live regions & feedback · Windows · plus Components (`ui:`), States (`state:`) and Contexts (`media:`). Staged: conversational/AI interfaces, voice, spatial.

## 3. AXL's gap-fillers (kept minimal, each listed)

Only where no standard expresses what a source asks for:
- **`axl:` measures:** computed page properties no standard names, e.g. `axl:distinct-font-sizes`, `axl:icon-sets`, `axl:emoji-as-icons`, `axl:spacing-off-scale`. Each is defined once in `axl/measures.md`, implemented once in `axl.py`, and proven on the Northstar demo (fails on the original, passes with the fix).
- **`ask` tests:** a yes/no question when nothing can be measured, e.g. `state:invalid ask "Does every error say how to fix it?"`. Content and Process rules are mostly these.
- **`x-<name>:` elements:** anyone's own extension, defined by its author.

## 4. Views this makes possible

- **Main screen:** a command and its rules, what each rule changes on Northstar, sources as compact IDs, and building your own definition.
- **Command matrix** (secondary screen, "see the problem"): for one command, the rules down the side (grouped by aspect) and the definitions across the top (Impeccable, Taste-Skill, UI Craft … you). Each cell holds that source's value, blank where it doesn't ask for that rule. A final column shows how many independent sources ask for the rule. What it shows at a glance: the origin definition, which rules everyone shares (few), which one source adds, and where values conflict (16px vs 14px).
- **The whole space:** the union of every definition of a command. This is the most complete answer to "what could *polish* mean?", with the origin and each source credited.
- **Across commands:** the same rule linked from *polish*, *harden* and *audit* shows where commands overlap.

## 5. When a link is accepted

1. The rule uses the vocabularies above (or a listed gap-filler).
2. It cites at least one quote ID from that source's own statements, and the quote says what the link claims.
3. An automatic rule passes the Northstar round-trip; an `ask` rule is a yes/no question about something observable.
4. The same `element/property` is never two rules; different values are a disagreement, shown in the matrix.

## 6. Files

- `data/commands.json`: commands, definitions, links (the AXL-owned layer)
- `data/rules.json`: rules referenced by links (element, property, default test, label)
- `axl/measures.md`: `axl:` measures
- `data/catalog.json`: statements with permanent quote IDs; `data/sources_index.json`: source IDs; `data/lineage.json`: who copies whom
- `data/previews.json`: the Northstar demonstration per rule
