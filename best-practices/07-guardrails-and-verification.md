# 07 — Guardrails and Verification

## Bottom line

**Move deterministic rules out of prompts and into CI.** Agents ignore guidance, but they
can't get past a failing build. Lint errors that name the replacement token make agents
fix themselves inside the same loop (Evil Martians, "the design system as a compiler").
Then close the visual loop: Claude must *see* what it built, at real screen widths,
against committed baselines.

## Layer 1 — Lint (fails the build)

| Rule | Tool | Catches |
|---|---|---|
| No arbitrary values (`p-[13px]`, `text-[#fff]`) | `eslint-plugin-better-tailwindcss` → `no-restricted-classes` | Values that bypass tokens |
| No raw palette colors (`bg-blue-500`) | same, regex + a message naming the semantic token | Off-brand color |
| No unknown classes | `better-tailwindcss/no-unknown-classes` | Typos, hallucinated utilities |
| No restyling components via `className` / inline styles | `@shadcn/lint` (`no-restyle`, `no-raw-colors`, `no-inline-styles`, `require-static-classes`) | Agents patching a component instead of using its variants. It suggests valid variants (`size="sm"`) |
| Static class strings only | `require-static-classes` / review | Dynamically built classes that Tailwind can't detect |
| Raw colors in CSS files | Stylelint `declaration-property-value-disallowed-list` (regex) | Hex/rgb values outside the token files |
| Tokens in sync | `npx @google/design.md lint` + a check that the generated files are fresh | A stale DESIGN.md, contrast failures |

Notes from teams that have run these setups:
- **Escape hatch with a reason.** An exception requires a stated reason (e.g. a
  `designSystemException="…"` prop or a lint-disable with a justification) so it stays
  visible.
- **Ratchet baseline.** When adopting on existing code, record the current violation
  count; it can only go down.
- **Monorepo:** set `settings["better-tailwindcss"].cwd` per app. Plugins switch off
  **silently** when they can't resolve Tailwind, so CI must assert that the plugin is active.

## Layer 2 — Visual verification (Claude sees its own work)

- **Playwright MCP** gives Claude a real browser (`claude mcp add playwright npx
  '@playwright/mcp@latest'`).
- **Define "verified" explicitly.** Otherwise an agent with a screenshot tool will
  still declare a broken page done. Our definition: the screenshot is checked at
  **375px and 1440px**, in light and dark, with every celebration moment shown in
  its final state, and passes the [06](06-anti-slop.md) gut check.
- **Measure, don't eyeball.** Use Playwright `evaluate` to check computed font family,
  size and color against the tokens.

## Layer 3 — Regression baselines (CI)

- Playwright `toHaveScreenshot` for each screen × brand × theme × width.
- **Generate baselines in the same container image CI uses.** Commit them, and never
  update one without looking at the diff.
- **Keep them deterministic:** mask dynamic content, freeze animations (reduced-motion
  mode plus the Motion test config), and use fixed fonts. Fix flakiness at the source;
  never raise the tolerance.

## Layer 4 — Design review agent

Pattern: OneRedOak's `design-review` workflow. It has a principles checklist, a
reviewer subagent, a CLAUDE.md snippet and a `/design-review` command. Its phases:
interaction flows → responsiveness → visual polish → accessibility → robustness →
code health. We add two phases of our own:
- **Anti-slop audit** against [06](06-anti-slop.md).
- **Celebration audit:** does each moment in the [05](05-motion-and-celebration.md)
  catalog fire on the right event, and does it degrade cleanly under reduced motion?

It runs before any UI PR merges and reports its findings with screenshots.
