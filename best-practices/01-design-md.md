# 01 — The Base `DESIGN.md`

## Bottom line

Adopt Google Labs' open **DESIGN.md** format (Apache 2.0, April 2026). It has two parts:
YAML front matter holding the exact tokens, and prose explaining *why*. Claude Code,
Cursor, Copilot and Codex read it at session start. `npx @google/design.md lint`
validates tokens and WCAG contrast, and it exports to Tailwind or W3C DTCG.

## Where it lives

- `packages/gauntlet-ui/DESIGN.md` is the **base system** every gauntlet inherits:
  layout, spacing rhythm, type scale *structure*, motion vocabulary, the celebration
  moments, and the component inventory.
- `apps/<gauntlet>/brand.md` overrides **only the brand layer** (see [02](02-brand-md.md)).
- Reference both from `CLAUDE.md` / `AGENTS.md` under a "UI & Design System" heading so
  discovery doesn't depend on each agent's own conventions.

## What goes in the base file

| Section | Content | Why it's base, not brand |
|---|---|---|
| Principles | Voice as the interface, verdicts you can trust, productive pressure, celebrating progress (carried over from `gauntlet-ux`) | Every gauntlet is the same game |
| Layout & spacing | 4px base grid, the spacing scale, the content widths, how each screen type is laid out (Run, Report, Climb, Worst Day) | Structural consistency |
| Type scale | Sizes, line heights, weights **as roles** (`display`, `title`, `body`, `mono-data`), with no font families | Families are brand |
| Color roles | Semantic role names and which 12-step scale step each maps to (see [03](03-tokens-and-typescript.md)) | Roles are shared; hues are brand |
| Verdict colors | `absent / gestured / landed / nailed` as fixed semantic roles | Scores must mean the same thing across brands |
| Motion | Duration + spring tokens, the moment catalog (see [05](05-motion-and-celebration.md)) | The feel of the game is shared |
| Components | The list of allowed components and their variants (see [04](04-component-systems.md)) | Cuts down improvisation |
| Do / Don't | Links to [06-anti-slop](06-anti-slop.md) | Taste rules |

## Rules for keeping it useful

- **The prose explains decisions; it does not restate the tokens.** "Body text is 17px
  because answers are read right after speaking, on a phone, often while stressed"
  helps an agent. "Body is 17px" alone does not.
- **One source of truth.** Tokens in the YAML are generated into CSS and TS
  ([03](03-tokens-and-typescript.md)). Never hand-edit the generated files.
- **A stale file is worse than none.** CI checks that the YAML tokens match the
  generated `@theme` output ([07](07-guardrails-and-verification.md)).
- **Never copy another company's DESIGN.md.** The 67k-star `awesome-design-md`
  collection is fine for studying structure. Copying its tokens gives you a knockoff
  (Adam Wathan's criticism).
- **DESIGN.md covers tokens, not behavior.** Component behavior (states, focus,
  loading) comes from the component registry and its types, not from this file.
