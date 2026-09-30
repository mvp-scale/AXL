# 08 — How Claude Works (skills, rules, order)

## Bottom line

Keep the instruction surface **light**: one pointer in `CLAUDE.md`, one design skill, one
review agent. Everything checkable lives in lint and tests, not prose. Claude always
works **direction → tokens → build → verify → review**, and never goes straight to code.

## The instruction layers

| Layer | File | Holds | Size |
|---|---|---|---|
| Always loaded | `CLAUDE.md` / `AGENTS.md` | Pointers only: "UI work → read `DESIGN.md` + the app's `brand.md`, use the `gauntlet-design` skill, never ship UI without `/design-review`" | ~10 lines |
| Brand contract | `DESIGN.md` + `brand.md` | Tokens + rationale ([01](01-design-md.md), [02](02-brand-md.md)) | Structured |
| Taste + process | `gauntlet-design` skill (`SKILL.md`) | The anti-slop standard, the moment catalog, the brand-brief interview, the build order below. It points to these docs rather than copying them | ~400–800 tokens + references |
| Library know-how | `shadcn/skills`, Anthropic `frontend-design`, Context7 docs | Current API usage | External |
| Judgment gate | `design-review` subagent + `/design-review` command | Phased review with screenshots ([07](07-guardrails-and-verification.md)) | Agent |
| Hard gate | ESLint / Stylelint / Playwright in CI | Everything deterministic | Config |

Principle (Evil Martians and Anthropic): a skill sets **taste and order**, and lint enforces
**rules**. If a skill line could be a regex, move it into lint.

## Build order for Rev1 of any gauntlet

1. **Brand brief interview**: the five questions in [02](02-brand-md.md). No code.
2. **Write `brand.md`.** The user approves it.
3. **Generate tokens**: OKLCH scales, `@theme` CSS, TS skin types. Run the contrast lint.
4. **Specimen page first**: type, color steps, verdict bands, every component variant,
   and each moment in its final state, on one page. The user approves the *look* here,
   before any real screens exist. This is the cheapest place to fix taste.
5. **Build screens** from registry components only. Missing component → add it to the
   registry with variants, never a one-off.
6. **Self-verify**: lint green, Playwright screenshots at 375/1440 × light/dark, and
   computed styles match the tokens.
7. **`/design-review`**, including the anti-slop and celebration audits.
8. **Commit baselines**, and the result is Rev1.

## Working rules for Claude

- **Name the direction out loud** before writing UI (aesthetic family + adjectives).
  If it can't be named, stop and ask.
- **Iterate on the output; don't re-prompt from scratch.** Adjust tokens and components
  from the screenshot, as the Claude Design "Tweaks" pattern does.
- **Use Context7 for library APIs.** Tailwind v4, shadcn CLI v4, Base UI, Motion and
  View Transitions have all changed in 2025–26, so training memory is out of date.
- **No speculative components.** Build only what a screen needs, but always as a
  registry item with typed variants.
- **Claude's own design tools** (`/design` artboards, Claude Design) are good for
  exploring a brand in steps 1–4, and their output goes back into `brand.md` tokens.
