# Design System Kickstart

Status: **PARKED.** Don't start until the prerequisites below are met. This is the
execution checklist; the reasoning behind each step is in the linked docs.

## The system: 1 input, 1 kit, 3 gates

| # | Control | Stops |
|---|---|---|
| 1 | **Brand file** (`brand.md`), the only thing a gauntlet writes | Generic, undirected design |
| 2 | **Shared UI kit** (`gauntlet-ui`): tokens + components + motion | Inconsistency between apps |
| 3 | **Lint gate** (CI) | Drift, one-off hacks |
| 4 | **Screenshot gate** (CI) | Regressions; one app breaking another |
| 5 | **Review gate** (`/design-review`) | Slop and flat flows that lint can't catch |

The principle: taste goes in one place, and rules go in the build.

## Prerequisites (architecture first)

- [x] `ARCHITECTURE.md` reviewed and revised (v3): one standalone monorepo with the engine
      ported into `packages/engine` (§3), and §5's "no visual redesign" superseded (see
      [09](09-control-plane-monorepo.md)).
- [ ] Monorepo scaffold exists: `apps/`, `packages/`, a workspace tool, and a CI pipeline.
- [ ] At least one app (Founder's Gauntlet) builds and deploys from this repo.

## Phase 1: Brand file + base design (control 1)

- [ ] Write the base `packages/design-system/DESIGN.md` using the Google DESIGN.md format → [01](01-design-md.md)
- [ ] Define the `brand.md` schema and the brand-brief interview → [02](02-brand-md.md)
- [ ] Write Founder's Gauntlet `brand.md` as the first real brand
- [ ] Wire `npx @google/design.md lint` into CI
- **Done when:** the Founder's brand file passes lint and you've approved it.

## Phase 2: Shared UI kit (control 2)

- [ ] Token generator: seed → OKLCH 12-step scales → Tailwind v4 `@theme` + TS `GauntletSkin` → [03](03-tokens-and-typescript.md)
- [ ] Choose a component base: shadcn on Base UI, from our own registry (`extends: none`). First verify the single-source claims → [04](04-component-systems.md)
- [ ] Build the game components: `Verdict`, `BeatTrack`, `RecordButton`, `LatencyStage`, `ClimbMountain`, `WorstDayHUD`, `Celebration`
- [ ] Motion tokens + the moment catalog + `MotionConfig reducedMotion="user"` → [05](05-motion-and-celebration.md)
- [ ] **Specimen page** route in every app (type, colors, verdicts, components, moments)
- **Done when:** you approve the Founder's specimen page, and swapping in a test brand re-skins it with zero component edits.

## Phase 3: Lint gate (control 3)

- [ ] Shared ESLint preset: `better-tailwindcss` (no arbitrary values, no raw palette colors, no unknown classes) + `@shadcn/lint` (no restyle, no inline styles) → [07](07-guardrails-and-verification.md)
- [ ] Stylelint rule rejecting raw colors outside the token files
- [ ] CI check that the lint plugin is actually active (it switches off silently)
- [ ] Escape hatch that requires a written reason
- **Done when:** a deliberate `bg-blue-500` fails CI with a message naming the right token.

## Phase 4: Screenshot gate (control 4)

- [ ] Playwright baselines: every app × light/dark × 375/1440, including the specimen page
- [ ] Baselines generated in the CI container; animations frozen, dynamic content masked
- [ ] Playwright MCP set up so Claude can check its own screenshots during development
- **Done when:** a change to `gauntlet-ui` shows diffs for every app in one PR.

## Phase 5: Review gate (control 5)

- [ ] `gauntlet-design` skill (taste + build order; points to these docs) → [08](08-claude-workflow.md)
- [ ] `design-review` agent + `/design-review` command, with anti-slop + celebration audits → [06](06-anti-slop.md)
- [ ] Pilot Impeccable critique and Hallmark audit on the Founder's UI; keep whichever finds real issues
- [ ] Add pointers to `CLAUDE.md` (about 10 lines)
- **Done when:** the review catches a planted slop pattern (e.g. an Inter hero with three cards).

## Proof it works

- [ ] Take a second gauntlet (Management) from idea to Rev1 by writing **only** `brand.md` + content, with all 5 gates green.
