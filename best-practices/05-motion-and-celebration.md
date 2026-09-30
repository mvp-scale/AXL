# 05 — Motion and Celebrating the Flow

## Bottom line

Treat delight as a **system with a fixed catalog of moments**, not as effects sprinkled
around the app. Product code *announces state* (`beatLanded`, `verdict: nailed`); the
motion layer decides what that looks like. This is Duolingo's model: they bought a
motion studio (Hobbes, 2024) and run characters as Rive state machines driven by app
state. Spend the motion budget on a few big moments. Anthropic's frontend-design guidance
agrees: one well-choreographed moment beats scattered micro-interactions.

## The moment catalog (tied to the engine's real events)

| Moment | Engine event | Intent | Weight |
|---|---|---|---|
| **Ready** | Enter run | Ramp up tension without anxiety | Small |
| **Listening** | Recording | The mic feels alive; the voice *is* the interface | Continuous, subtle |
| **Thinking** | AI latency (grader running) | Make the wait feel like work being done: signals, then segments, then score, unfolding | Medium; this is the most-seen screen |
| **Beat landed** | Beat band `landed` | Quick acknowledgment | Small |
| **Nailed** | Band `nailed` | Earned punch | Medium |
| **Verdict reveal** | Report ready | Build trust: the evidence first, then the score | Large |
| **Climb** | Progress on mountain | Show how far you've come | Medium |
| **Survived the Worst Day** | Boss cleared | The peak moment; everything else stays quieter to leave room for it | **Largest, happens once** |
| **Fell short** | Boss lost | Productive, not punishing; point to the next rep | Medium, restrained |

Rule: **a new moment requires a new engine event.** Nothing animates just to animate.

## Stack

| Need | Tool | Why |
|---|---|---|
| Hover, focus, simple enter | **CSS** transitions on tokens | Free; start here |
| Screen-to-screen, shared element (Run → Report) | **View Transitions API** (Baseline since Oct 2025; React `<ViewTransition>` still Canary) | The browser handles continuity |
| Springs, gestures, exits, orchestration | **Motion** (formerly Framer Motion), `AnimatePresence`; `AnimateView` bridges to View Transitions (React 19.3+) | Interruptible springs that keep their velocity; exits that finish cleanly |
| Characters, mascot, rich celebration | **Rive** state machines, driven by state, with a strict input contract | A state-driven graph instead of hardcoded motion; swap the art per brand without code changes |

## Motion tokens

- **Durations:** `instant` (≈100ms), `fast` (≈150ms), `base` (≈250ms), `slow` (≈400ms),
  and `moment` for choreographed sequences.
- **Springs:** the brand's `motion-temperament` (crisp / bouncy / weighty) picks a
  `{ visualDuration, bounce }` preset. The same values feed `MotionConfig`,
  `AnimateView` and the CSS easings.
- **Stagger:** one shared value for list and evidence reveals.

## Rules

- **Choreograph; don't scatter.** One orchestrated sequence per moment, using staggered
  reveals, a clear order, and a clear final rest state.
- **Motion carries meaning.** Direction and weight encode the outcome: success rises
  and settles, a miss holds and redirects. Never play a generic bounce on everything.
- **Reduced motion is required.** Set `<MotionConfig reducedMotion="user">` explicitly
  at the root; don't assume it's the default. Add a `@media (prefers-reduced-motion)`
  block for View Transitions, since React won't do that for you. Replace large
  transforms with opacity changes. Anything that loops or autoplays needs a pause
  control (WCAG 2.2.2).
- **Performance:** pause offscreen Rive files, cache reused `.riv` files, and scope view
  transitions tightly (snapshots are costly on low-end phones).
- **Screenshot tests freeze motion** so baselines are deterministic ([07](07-guardrails-and-verification.md)).
