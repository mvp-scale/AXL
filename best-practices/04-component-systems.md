# 04 — Component Systems (research + recommendation)

## Bottom line

**Recommended:** use **shadcn/ui on Base UI primitives**, published through **our own
shadcn registry** (`gauntlet-ui`), started from a non-default style and fully re-tokened
from `brand.md`.

- We **own the source**: components are copied into the repo, not hidden in
  `node_modules`.
- Accessibility comes from Base UI.
- Agents already know the conventions, and shadcn ships agent skills for them.

The "shadcn look" that people call slop is only its *default* style and tokens. We
replace both.

## Landscape (as of Sept 2026)

| System | What it is | Distinctiveness | Verdict |
|---|---|---|---|
| **shadcn/ui** | Copy-in components, Tailwind v4, choice of Base UI / Radix / React Aria primitives. CLI v4 (Mar 2026) adds presets, `--diff`/`--dry-run`, agent skills | Default look is famously generic, but `shadcn create` has 8 named styles (Vega, Nova, Maia, Lyra, Mira, Luma, Sera, Rhea) that *rewrite component code*, and presets encode style + color + fonts + radius | **Use it**, as our base |
| **Base UI** (MUI; built by the original Radix team) | Unstyled, accessible primitives, v1.8 (Sept 2026), 37 components | Zero CSS, so it looks exactly like our tokens | **Use it**, underneath shadcn |
| **Radix Primitives / Themes** | Acquired by WorkOS; development has slowed (Combobox and multi-select lag). Themes repo last updated Apr 2026 | Themes has good tinted grays | Keep **Radix Colors** for grays; skip the components |
| **HeroUI** (ex-NextUI) | React Aria + Tailwind v4, polished out of the box | Strong look, but it's *theirs*, and you don't own the source | Don't use: brand lock-in |
| **Park UI** | Styled Ark UI on Panda or Tailwind | Good token system; smaller ecosystem | Viable alternative, not needed |
| **Tailwind Plus / Catalyst** | Tailwind Labs' paid kits | Excellent craft | **Closed to new customers** (Tailwind joined Shopify, 9 Sept 2026) |
| **React Aria Components** (Adobe) | The strongest accessibility primitives | Unstyled | Fallback if Base UI lacks a component |

Key insight from the research: all of these libraries now share the same foundations
(Tailwind v4, React 19, accessible primitives). **The library doesn't make the
look. Type, color, spacing and motion decisions do.** That's why the effort goes
into [02](02-brand-md.md), [03](03-tokens-and-typescript.md) and [05](05-motion-and-celebration.md).

## How we use shadcn

1. **Our own registry.** `packages/gauntlet-ui` publishes a `registry.json` with a
   `registry:style` using `"extends": "none"` (fully independent), plus `cssVars` in
   `theme` / `light` / `dark` scopes. Each gauntlet app installs components from *our*
   registry, not upstream.
2. **Pick a starting style per brand shape.** `shape: sharp` → Lyra (boxy, pairs with
   mono), `soft` → Maia, `compact` → Mira. It's only a starting point, since our tokens
   override it.
3. **Game components beyond shadcn's set** live in the same registry: `Verdict`,
   `BeatTrack`, `RecordButton`, `LatencyStage`, `ClimbMountain`, `WorstDayHUD`,
   `Celebration`. These are what make it a game rather than a dashboard.
4. **Known trap:** switching or re-applying a shadcn preset **rewrites component
   classes and wipes custom variants**. Set the preset once at init, then manage
   everything through our registry and tokens, never with `preset apply`.
5. **Upstream updates** come in through `shadcn add --diff` and are reviewed, never
   blindly overwritten.

## To verify before committing (single-source claims)

- That Base UI is the shadcn default since July 2026 (one source; check the changelog).
- The exact list of 8 styles (one third-party source).
- Whether the Tailwind Plus licenses we might already hold get updates.
