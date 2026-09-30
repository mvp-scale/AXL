# 03 — Tokens, Tailwind v4 and TypeScript

## Bottom line

Tokens flow one way: `brand.md` + base `DESIGN.md` → generator → **Tailwind v4 `@theme`
CSS** + **TypeScript types**. Components only ever see semantic names (`bg-surface`,
`text-verdict-nailed`), never raw colors or pixel values. Swapping the brand file
re-skins the whole app with zero component edits.

## Three token layers

| Layer | Example | Who sets it |
|---|---|---|
| **Primitive** | `--brand-9: oklch(0.62 0.17 35)` | Generated from the brand seed |
| **Semantic** | `--color-accent: var(--brand-9)`, `--color-surface: var(--gray-2)` | Base DESIGN.md (shared role → step map) |
| **Component** | `button` variants referencing semantic tokens | The component registry (04) |

Components reference semantic tokens. Semantic tokens reference primitives. Nothing skips a layer.

## Color: OKLCH 12-step scales

- **Why OKLCH:** it is perceptually uniform, so steps look evenly spaced. HSL scales
  drift purple in the light steps and go muddy in the dark ones.
- **The 12 steps have fixed roles (Radix model):** 1–2 app and subtle backgrounds; 3–5
  component backgrounds and states; 6–8 borders; **9 is the solid brand color (highest
  chroma)**; 10 is hover; 11 low-contrast text; 12 high-contrast text.
- **Generate, don't pick.** Candidate tools are `oklch-palette` (seed → 12 steps,
  CSS vars and a Tailwind preset) and OKChroma (contrast built into the math, APCA
  check). Evaluate both at build time.
- **Keep grays and status colors from a proven set** (Radix Colors), tinted toward the
  brand hue, and generate only the brand scale. Radix itself recommends this split.
- **Light and dark come from the same generator run**, not a hand-made second palette.

## Tailwind v4

- Use `@theme` for tokens that should become utilities, and `:root` for variables that
  shouldn't.
- For runtime theme switching, keep raw values in `:root` / `.dark` and map them
  through `@theme`. Before relying on `@theme inline`, test the dark-mode switch;
  sources disagree on whether it survives runtime switching.
- Add `@custom-variant dark (&:where(.dark, .dark *));` so the `dark:` variant follows the class.
- **Class names must be complete literal strings.** Never build one like
  `` `bg-${color}` ``. Conditional classes go through variants or `cn()`.
- Motion tokens (durations, springs) also live in the token layer, so CSS and Motion
  read the same values ([05](05-motion-and-celebration.md)).

## TypeScript — make the wrong thing fail to compile

- **Typed skin.** `GauntletSkin` (item 5 in ARCHITECTURE §4) is a typed object that the
  `brand.md` build step generates and validates. A missing tagline or an unknown motion
  temperament is a type error, not a runtime surprise.
- **Typed variants.** Use `tailwind-variants` for multi-slot components (RunView,
  ReportView, Verdict, and the Worst Day HUD). It has slots, compound variants and
  built-in merging, and it infers `VariantProps` types. Use CVA only for trivial
  single-element components, or skip it and stay on one library.
  - v4 caveat: tailwind-variants' responsive variants were removed. Use plain
    responsive prefixes inside the variant strings.
- **Domain-typed props, not style props.** Components take `band: 'absent' | 'gestured' |
  'landed' | 'nailed'`, not `color="green"`. The engine's vocabulary *is* the design
  API, which ties visual meaning to scoring meaning.
- **Only token-backed classes appear in variant files.** If `text-gray-500` shows up,
  the right token is missing or wasn't used. Lint catches both
  ([07](07-guardrails-and-verification.md)).
