# The Late‑2026 High‑Retention UI/UX & Agentic Build Playbook

## Modern Playbook

The strongest modern products do **not** maximize visual novelty or raw time-on-site. They minimize the distance between **intent and value**, keep the system legible while work is happening, preserve the user’s context, make mistakes cheap to recover from, and reveal complexity only as the user becomes ready for it. That direction is consistent with cognitive-load research, evidence that excessive choice can reduce action, self-determination research emphasizing autonomy and competence, and goal-gradient research showing that visible progress can increase persistence as people approach a meaningful goal. citeturn14search3turn14search4turn15search3turn14search5

For the requested stack, this philosophy is now unusually practical. React 19 provides first-class pending, form-action, optimistic-state, and Suspense primitives; Tailwind v4 makes design tokens available as CSS variables and brings container queries into core; shadcn/ui explicitly gives teams editable “open code” with composable interfaces designed to be understandable by both humans and AI models; and Motion provides a modern animation layer without requiring animation to become the architecture of the application. citeturn1view0turn21view0turn21view1turn21view2turn2search11

The key mindset is:

> **Premium UX is not “more UI.” It is fewer moments in which the user has to stop, interpret the product, remember hidden state, wait without feedback, recover manually, or wonder what to do next.**

### The high-retention pattern library

| Technique | Psychology / retention mechanism | Stock experience | Superior late‑2026 conversion |
|---|---|---|---|
| **Intent-First Task Shell** | People have limited working-memory capacity; forcing them to parse unrelated information increases extraneous cognitive load. Large choice sets can also suppress action rather than improve it. citeturn14search3turn14search4 | User lands on a “dashboard” containing 12 cards, four charts, a sidebar with 18 destinations, notifications, tips, and secondary metrics. They must infer what matters. | The first viewport answers **“What am I trying to accomplish?”** One dominant task, one status summary, and one obvious next action appear first. Secondary analytics, history, settings, and advanced controls emerge contextually. |
| **Progressive Disclosure Architecture** | Complexity feels smaller when the user only has to reason about what is relevant to the current decision. This reduces cognitive load without removing power from experts. citeturn14search3turn14search4 | Every configuration option is shown in one long form or modal because “users might need it.” | Start with the minimum viable decision. Reveal dependent options only after an earlier choice makes them relevant. Put rare controls behind **Advanced**, expandable regions, contextual side panels, or command surfaces—not behind obscure navigation. |
| **Predictive State UI** | Good defaults reduce decision effort; preserving the ability to override them protects autonomy. Self-determination research associates autonomous rather than controlled motivation with healthier sustained engagement. citeturn15search3turn14search4 | Every visit begins from a generic state. Users repeatedly set the same filter, workspace, sort, date range, export format, or recipient. | Infer the likely starting state from the current object, previous choice, role, workflow stage, or recent context. Show **“Using your last choice: X”**, allow instant override, and never hide what the system inferred. Predict; do not trap. |
| **Optimistic + Reversible Interaction** | Immediate acknowledgement preserves perceived agency. Reversibility lowers the perceived cost of acting and turns fear of error into safe experimentation. React 19’s optimistic-state and action primitives directly support this interaction model. citeturn19search3turn1view0 | Click “Archive”; button locks; spinner appears; network request completes; page refreshes; user is uncertain whether the click worked. | The item visually archives immediately, an unobtrusive **Undo** appears, the mutation runs in the background, and failure restores the item with a precise explanation. Use pessimistic confirmation only when an operation is expensive or genuinely irreversible. |
| **Zero-Layout-Shift Staged Loading** | Unexpected movement disrupts spatial memory and can literally cause users to activate the wrong control. CLS exists specifically to measure visual instability. citeturn10view1turn20view8 | Entire page is replaced by a centered spinner. Then cards suddenly pop into different positions as requests finish. | Render the shell immediately, reserve final geometry, preserve navigation and headings, skeleton only the regions actually loading, progressively reveal independent data, and transition loaded content without reflow. |
| **Latency-Aware Feedback** | Classic human-factors thresholds distinguish near-instantaneous response, interruptions to conversational flow, and delays long enough that attention wanders; regardless of exact cutoff, users need stronger feedback as latency grows. citeturn9search16turn19search3 | The same spinner is used for a 100 ms mutation and a 40-second AI generation. | For tiny delays, acknowledge through local state change. For noticeable delays, expose pending state. For longer jobs, show meaningful stages—**Analyzing → Generating → Validating**—plus cancellation/backgrounding when technically possible. Never fake percentage completion. |
| **State Continuity & Intent Preservation** | Re-entering information and reconstructing context imposes memory and effort costs. WCAG 2.2 explicitly requires certain previously entered information in a process to be auto-populated or available for selection rather than repeatedly requested. citeturn11view2turn14search3 | Back navigation resets filters. A modal closes and loses work. Refresh destroys a draft. Switching tabs returns to the top of a 500-row table. | Autosave drafts, preserve selections and scroll position, encode useful state in URLs, restore interrupted work, retain unsent text, maintain filter state, and tell users **Saved** rather than making them wonder. |
| **Intelligent Empty States** | A blank surface gives a novice neither competence feedback nor a path toward the first success. Visible progress toward a meaningful goal can increase persistence. citeturn15search3turn14search5 | “No projects found.” A blank table and disabled toolbar. | Explain **why it is empty, what good looks like, and the fastest route to populated value**. Pre-fill a useful example when appropriate, offer import/connect/sample paths, and make the primary CTA accomplish the first meaningful unit of work rather than merely opening another blank form. |
| **Recovery-First Errors & Inline Validation** | Errors become frustrating when the user must diagnose both what failed and how to recover. WCAG requires identified errors to be described in text and, where known, correction suggestions to be provided. citeturn12view3 | “Something went wrong.” Form wipes several fields. User must retry the entire task. | Keep valid input, focus the exact problem, explain it in domain language, suggest a valid repair, and provide one-click retry. Distinguish **validation**, **permissions**, **connectivity**, **conflict**, and **server failure** instead of mapping everything to one red toast. |
| **Just-in-Time, Learn-by-Doing Onboarding** | Competence is motivational; large up-front tutorials ask novices to memorize concepts before those concepts have relevance. Cognitive-load theory argues against unnecessary simultaneous processing. citeturn15search3turn14search3 | Five-slide product tour before the user has seen their workspace; mandatory checklist describing every feature. | Let users perform a real, low-risk task immediately. Explain a feature at the moment it becomes useful. Replace “tour the interface” with **“complete your first valuable outcome.”** Advanced education appears when behavior indicates readiness. |
| **Semantic Micro-interactions** | Feedback improves visibility of system status; motion is most valuable when it explains causality, hierarchy, state transitions, or spatial relationships. Interaction-triggered animation also needs an accessible reduction path. citeturn19search3turn12view1turn0search35 | Every hover scales, glows, bounces, or springs because the product wants to “feel premium.” | Animate only semantic transitions: a saved item settling into place, expansion revealing its origin, a dragged object reaching its destination, an optimistic action entering its new state. Prefer compositor-friendly transforms/opacity and honor `prefers-reduced-motion`. citeturn0search31 |
| **Progressive Power & Adaptive Density** | Beginners and experts need different amounts of visible machinery. Progressive disclosure reduces initial complexity while preserving competence growth and autonomy. citeturn14search3turn15search3 | Either the UI permanently exposes every expert control or permanently dumbs down the experience for experienced users. | Keep the default surface calm, then unlock shortcuts, batch operations, advanced filters, compact density, command palette actions, saved views, templates, and automation as the user’s needs grow. Tailwind v4’s built-in container queries make component-level adaptive composition easier than breakpoint-only page design. citeturn21view1 |
| **Meaningful Progress & Mastery Loops** | Goal-gradient research found that effort can accelerate as consumers perceive themselves approaching a reward; SDT suggests that experiences supporting competence and autonomy are better foundations for sustained motivation than coercion. citeturn14search5turn15search3 | Artificial streaks, badges, confetti, and progress bars attached to behaviors that have little user value. | Visualize progress toward the **user’s desired outcome**: setup completeness that unlocks capability, workflow completion, skills mastered, records processed, money/time saved, issues resolved, or project readiness. Celebrate meaningful milestones, not arbitrary clicks. |
| **Attention-Safe Return Architecture** | Sustained engagement should preserve autonomy rather than manufacture interruption. WCAG even treats the ability to postpone/suppress interruptions as an important accessibility principle at its enhanced level. citeturn12view1turn15search3 | Every event becomes an email, badge, toast, push alert, banner, and activity-feed entry. | Classify signals as **urgent, actionable, informational, or ambient**. Bundle low-value events, let users tune channels, make alerts deep-link to the exact resolution state, and stop prompting after the user has already acted. |

### The distinction that matters: “smart” UI versus mysterious UI

A predictive interface should reduce work **without creating unexplained behavior**. For example, “We selected your usual workspace — Change” is superior to silently modifying scope. “Suggested from your last three exports” is superior to mysteriously preselecting a file format. Autonomy matters: predictive defaults should be visible, reversible, and easy to override. citeturn15search3turn19search3

Similarly, optimistic UI should not be confused with pretending a risky operation succeeded. React 19 makes optimistic rendering straightforward, but the design decision still depends on reversibility. A “favorite,” “rename,” “archive,” or reorder operation is a good candidate; an irreversible payment, permanent deletion, privileged security change, or legally significant submission generally deserves stronger confirmation and validation. WCAG’s guidance for consequential data submissions similarly emphasizes reversibility, checking, or confirmation. citeturn1view0turn12view3

### The anti-pattern blacklist

A premium application in 2026 should generally reject visual effects that do not improve comprehension: glass layers stacked on glass layers, permanent gradients used as hierarchy substitutes, huge animated hero sections inside work surfaces, scroll-jacking, gratuitous parallax, excessive spring motion, dashboard-card proliferation, repeated modal nesting, icon-only mystery navigation, and AI-generated “feature soup.”

The common failure is not that these techniques are inherently forbidden; it is that they consume perceptual and implementation budget **without shortening the user’s route to value**. The best litmus test is:

> **If removing the effect makes the user faster, more confident, or less distracted, remove it.**

## Performance and Accessibility Quality Gates

“Premium” must be measurable. A beautiful application that jumps while loading, loses drafts, hides focus, forces repeated data entry, or responds sluggishly is not premium.

Google’s current Core Web Vitals define the primary field metrics around loading, interaction responsiveness, and visual stability. A good field result means **LCP ≤ 2.5 seconds, INP ≤ 200 ms, and CLS ≤ 0.1 at the 75th percentile**, evaluated separately across relevant device classes. Google also recommends real-user monitoring because laboratory testing cannot reproduce the full distribution of real-world devices, networks, and behavior. citeturn20view8

The resulting product-level quality contract should look roughly like this:

| Dimension | Minimum ship gate | Premium internal target |
|---|---|---|
| **Visual stability** | CLS passes Core Web Vitals | Core application shell and primary action region should effectively not move after interaction; reserve asynchronous geometry before content arrives. citeturn10view1turn20view8 |
| **Interaction responsiveness** | INP ≤ 200 ms at field P75 | Every interaction acknowledges intent immediately, even when its business operation continues asynchronously. citeturn20view8turn19search3 |
| **Primary loading** | LCP ≤ 2.5 s at P75 | Shell, navigation, and task context arrive before secondary analytics or decoration. citeturn20view8 |
| **Loading UX** | No unexplained blank screens | Stable skeletons for known geometry; pending labels for local actions; meaningful stages for long-running AI/server tasks. web.dev recommends reserving space when asynchronous content will arrive so it does not unexpectedly shift surrounding content. citeturn10view1 |
| **Touch targets** | Meet WCAG 2.2’s 24×24 CSS px AA minimum or its spacing exceptions | Prefer approximately 44–48 px for frequently used touch actions where density permits; WCAG’s enhanced target-size criterion is 44×44 CSS px. citeturn12view0turn12view1 |
| **Keyboard/focus** | All actionable functionality is keyboard operable and focus is visible/not obscured | Focus order mirrors the conceptual task sequence; opening/closing overlays restores focus to its logical origin. WCAG 2.2 strengthens focus visibility and non-obscuration expectations. citeturn12view1 |
| **Drag interactions** | Do not require dragging as the only mechanism | Every drag interaction has a non-drag single-pointer alternative, as required by WCAG 2.2 AA. citeturn12view1 |
| **Forms** | Identified errors are textually explained | Preserve correct values, suggest fixes, auto-populate repeated information, and position recovery beside the failure. citeturn12view3turn11view2 |
| **Authentication** | Meet WCAG Accessible Authentication requirements | Support password managers, paste, passkeys or other mechanisms that do not require users to solve unnecessary cognitive tests. citeturn11view3 |
| **Motion** | Respect reduced-motion preferences | Motion communicates state, not decoration; layout-changing animation is avoided in favor of transform/opacity where possible. citeturn12view1turn10view1turn0search35 |
| **State durability** | No routine navigation should silently destroy unsaved intent | Draft persistence, URL-backed filters where appropriate, undo for cheap reversals, and explicit save/sync status. |

This is also why the requested implementation stack is a good fit. Tailwind v4 can centralize product tokens as runtime CSS variables and adapt components to their containers rather than only the viewport. shadcn/ui gives the coding agent the **actual source of the primitives**, instead of burying crucial behavior behind an opaque package abstraction. Its own documentation explicitly describes the approach as “Open Code,” composable, predictable, and AI-ready. citeturn21view0turn21view1turn21view2

A useful architectural rule is therefore:

**shadcn supplies primitives; your product supplies behavior. Tailwind supplies constraints; your product supplies hierarchy. Motion supplies continuity; your product supplies meaning. React supplies state machinery; your product supplies the state model.**

Do not let an AI agent interpret “use shadcn” as “assemble a generic shadcn dashboard.”

## Engagement Architecture

The most important retention system is not a component library. It is the **sequence in which the application creates value, teaches itself, proves competence, remembers context, and gives the user a reason to return**.

A high-performing journey can be modeled as:

**Promise Match → Frictionless Value Realization → Aha Moment → Progressive Onboarding → Mastery & Personalization → Sustained Delight Loop**

The goal is not to maximize activity at every stage. The goal is to increase the percentage of users who arrive at each successive stage **without confusion, wasted decisions, or coercion**.

| Journey stage | User’s internal question | Experience architecture | What to measure |
|---|---|---|---|
| **Promise Match** | “Am I in the right place?” | Match the vocabulary and promised outcome from acquisition directly to the first screen. Avoid an unrelated marketing-to-dashboard context switch. Ask only information required to produce initial value. | Entry-to-start rate, abandonment before first task, unnecessary-field completion time. |
| **Frictionless Value Realization** | “Can this solve my problem?” | Offer the smallest useful workflow possible. Import existing data where possible. Infer safe defaults. Delay account enrichment, integrations, preferences, and advanced setup unless essential. This follows the cognitive-load and choice-reduction logic behind progressive disclosure. citeturn14search3turn14search4 | **Time to First Value**, successful first-task rate, errors/retries before first success. |
| **Aha Moment** | “Oh — this is why I would keep this.” | Make the first differentiating result unmistakable. Show the transformation, time saved, insight discovered, automation performed, collaboration achieved, or uncertainty removed. Do not bury the payoff behind another navigation step. | Activation event completion and the relationship between activation and later return. |
| **Progressive Onboarding** | “What can I do next?” | Teach one adjacent capability at the moment it becomes relevant. Use contextual cues, meaningful checklist progress, sample content, and safe experimentation. Competence-supporting environments are consistent with stronger autonomous motivation. citeturn15search3 | Second/third meaningful action, time between milestones, help usage followed by success. |
| **Mastery & Personalization** | “Does this product now work *my* way?” | Remember preferences, let users create views/templates/automation, reveal expert shortcuts, support keyboard and batch workflows, and reduce repeated configuration. | Repeated-task time, custom-view/template adoption, shortcut/batch usage, return to saved state. |
| **Sustained Delight Loop** | “Why should I return now?” | Return triggers correspond to genuine changed value: a collaborator acted, work finished, an important threshold was reached, new information arrived, or the next meaningful milestone became available. | Meaningful return rate, task success on return, notification action rate, opt-out rate, long-term retention by activated cohort. |

### Narrative UX: give every screen a sentence structure

Every major work surface should communicate five things, ideally without explanatory prose:

**Context → Goal → Action → Consequence → Next Step**

For example, instead of:

> Projects  
> 14 cards  
> New Project

a narrative surface might communicate:

> **Q4 Launch**  
> 8 of 12 deliverables are ready. Two are blocked by approvals.  
> **Resolve approvals**  
> Once approved, the launch package can be generated.

The latter turns data into **orientation and momentum**. It does not merely show what exists; it explains why the current state matters and identifies a consequential action.

That is the core of Narrative UX: the interface continuously answers:

**Where am I? What changed? What matters now? What can I do? What will happen if I do it?**

Visibility of system status is one of the foundational usability principles behind this approach. citeturn19search3

### Progressive onboarding should continue after “onboarding”

A common mistake is treating onboarding as a one-time funnel before the “real application.” The better model is a **capability gradient**.

A new user sees the minimum system required for first value. After success, the application exposes an adjacent capability. Repeated use eventually reveals power-user functionality: batch actions, automation, keyboard shortcuts, saved workflows, collaboration controls, advanced analytics, APIs, or agentic operations.

This simultaneously serves two psychological needs: it avoids overwhelming beginners while letting experienced users experience increasing competence and control. That aligns with cognitive-load theory and self-determination theory rather than forcing one fixed complexity level on everyone. citeturn14search3turn15search3

### Build loops around mastery, not addiction

There is a meaningful distinction between **high retention** and **maximum engagement**.

The strongest long-term model is:

**Meaningful action → Visible outcome → Increased competence/context → Easier next action → Genuine reason to return**

not:

**Notification → anxiety → click → arbitrary reward → notification.**

Goal-gradient research supports making progress toward meaningful goals legible, while self-determination theory provides a stronger foundation for sustainable engagement through autonomy and competence. citeturn14search5turn15search3

That means a productivity product should be perfectly happy when a user accomplishes the job and leaves.

A high-retention product earns the **next session** rather than artificially extending the current one.

### A practical friction budget

For each important workflow, count four things:

| Friction type | Question to ask |
|---|---|
| **Decision friction** | How many times must the user stop and choose something before receiving value? |
| **Interpretation friction** | How often must they decode labels, icons, data, or unexplained system state? |
| **Interaction friction** | How many clicks, fields, page transitions, re-selections, or confirmations are truly necessary? |
| **Recovery friction** | After a mistake, timeout, disconnect, back navigation, refresh, or failed request, how much work must be reconstructed? |

Have the product team—and later the coding agent—reduce these before discussing polish.

This produces a useful formula for premium UX:

> **Experience quality ≈ useful outcome ÷ (decisions + waiting + uncertainty + repetition + recovery cost)**

That is not a scientific equation; it is an architectural heuristic for prioritization.

## Late‑2026 Agentic Orchestration

There is an important date-sensitive correction to the model examples in the brief. **GPT‑5.5 exists, but as of September 29, 2026 it is no longer OpenAI’s recommended frontier starting point for complex coding.** OpenAI’s current API documentation recommends **GPT‑6 Astra** for complex reasoning and coding, **GPT‑6 Sol** for balancing capability and cost, and **GPT‑6 Luna** for cost-sensitive high-volume workloads. The current docs list Astra with a roughly 1.05M-token context and computer-use, web-search, file-search, and function tools. citeturn20view2turn20view3

Anthropic introduced **Claude Opus 5.5** on September 22, 2026. Anthropic characterizes it as particularly strong on long, sprawling coding work and reports leading results on several of its agentic-coding evaluations; those benchmark claims should be treated as vendor-reported rather than neutral comparisons. citeturn20view4turn21view4turn21view5

Google introduced **Gemini 3.8 Flash** on September 2, 2026, explicitly positioning it for long-horizon coding and autonomous-agent workloads, with selectable effort levels for trading additional reasoning for efficiency. citeturn20view5

The practical implication is that the best late‑2026 workflow is **model-routed**, not model-loyal.

| Agent role | Recommended class | Job |
|---|---|---|
| **Product/UX Architect** | GPT‑6 Astra or Claude Opus 5.5 | Understand repository + product brief, model user journeys, challenge requirements, design state architecture, write acceptance criteria. citeturn20view3turn21view5 |
| **Implementation Lead** | Opus 5.5, GPT‑6 Astra/Sol | Execute multi-file vertical slices, migrations, component architecture, difficult interaction state, major refactors. citeturn20view3turn21view5 |
| **Parallel Subagent** | Gemini 3.8 Flash, GPT‑6 Sol/Luna, a faster Claude tier | Inspect routes, write tests, audit accessibility, generate fixture states, examine edge cases, perform inexpensive parallel work. Google explicitly targets Gemini 3.8 Flash at long-horizon agentic tasks at scale. citeturn20view5turn20view3 |
| **Visual execution environment** | Lovable / Cursor Design Mode / equivalent | Rapidly instantiate interaction concepts and component variants, then move successful designs into controlled repository workflows. Lovable supports conventional source-control workflows and can be driven through MCP. citeturn21view8turn21view9 |
| **Independent critic** | A different frontier model from the implementing model | Run task-based UX review, adversarial edge-case review, accessibility audit, code review, and performance critique without being psychologically anchored to its own implementation. |

Cursor is particularly compatible with this methodology because its current platform exposes **Planning, Design Mode, Agent Review, Rules, Skills, Subagents, Hooks, MCP, cloud agents, automated review, and rollout tooling** rather than requiring one monolithic chat loop. citeturn21view6turn21view7

Lovable is useful at a different layer: its documentation explicitly positions it for rapid application generation while allowing engineering teams to review and maintain generated code through GitHub, GitLab, or Bitbucket; its MCP server lets another agent drive Lovable as part of a larger orchestration workflow. citeturn21view8turn21view9

Current Windsurf-family tooling can be used under the same pattern: **plan → bounded edit → inspect diff → test → critique → merge**, rather than granting an agent permission to wander through the entire repository. Current documentation emphasizes reviewable agent changes and code-mapping/context mechanisms. citeturn6search11turn6search29

### The crucial orchestration rule

Do **not** prompt:

```text
Make this app more modern, premium, polished, and engaging.
Use shadcn and nice animations.
```

That request optimizes for things a model can cheaply demonstrate—cards, gradients, shadows, badges, animation—rather than things a user values.

Instead, prompt agents against an **Experience Contract**:

```text
Optimize in this order:

1. Task success
2. Time to first meaningful value
3. Cognitive load
4. Error prevention and recovery
5. State continuity
6. Interaction responsiveness
7. Accessibility
8. Visual hierarchy
9. Meaningful motion
10. Decorative polish

Do not add UI unless it reduces ambiguity, effort, waiting, or recovery cost.
Do not add generic dashboard cards.
Do not use animation unless it explains state or causality.
Preserve user intent across navigation, refresh, failure, and retries.
Every asynchronous action must have explicit pending, success, error,
and retry/recovery behavior.
```

That change in instructions is far more important than whether the executor happens to be Cursor, Lovable, Windsurf, Claude Code, Codex, or another IDE.

## Simple Five-Step Build Guide

The following pipeline is designed to be reusable at the beginning of essentially any high-tier web application. The critical principle is **do not ask the agent to design and build everything simultaneously**. Separate understanding, interaction architecture, implementation, delight, and verification.

**Step 1 — Establish the Experience Contract before writing UI**

Give the architecture model the existing app, requirements, screenshots, routes, or repository. Its first job is to understand **user intent**, not restyle components.

Use:

```text
You are the Principal UX Architect for this product.

Do not write implementation code yet.

Analyze this product around USER OUTCOMES, not existing screens.

Identify:
- the top 3 jobs users come here to accomplish;
- the earliest meaningful value moment for each job;
- the shortest path from entry to that value;
- unnecessary decisions, fields, screens, navigation, and confirmations;
- repeated information or repeated configuration;
- places where the user must remember hidden state;
- places where system state is ambiguous;
- destructive or risky actions that need confirmation versus reversible actions
  that should use Undo;
- abandonment points, dead ends, empty states, and error-recovery problems;
- which functionality belongs in the default UI versus progressive disclosure.

Create a friction map for each core flow using:
Decision Friction / Interpretation Friction / Interaction Friction /
Waiting Friction / Recovery Friction.

Then produce:
A. User Job Map
B. Value-Moment Map
C. Current Friction Audit
D. Proposed task-first information architecture
E. Ranked deletion/simplification list
F. UX acceptance criteria

Priority order:
task success > cognitive load > recovery > performance >
accessibility > visual polish.

Do not optimize for "more engagement."
Optimize for voluntary return because the product becomes more useful.
```

**Gate before proceeding:** you should be able to express each primary journey in one sentence:

> **User enters with X → performs Y → receives Z value.**

If the agent cannot do that, it does not understand the product well enough to generate the interface.

This architecture-first approach also maps well to Cursor’s explicit planning capabilities and to frontier models designed for longer end-to-end reasoning tasks. citeturn21view7turn20view3turn21view5


**Step 2 — Design the interaction/state architecture, not mockup screens**

Now make the agent describe every meaningful state. This is where mediocre AI-generated apps diverge from production products: generic generation tends to design the happy path, while mature UX is largely the handling of everything around it.

Use:

```text
Using the approved Experience Contract, create the interaction architecture.

For every core page, component, and user action, define:

STATE:
- initial
- loading
- empty
- partially populated
- success
- optimistic pending
- validation error
- server/network error
- permission denied
- stale/conflicting data
- offline/interrupted state where relevant

TRANSITION:
- what the user does
- what changes immediately
- what remains stable
- what runs asynchronously
- what happens on success
- what happens on failure
- how the user retries or reverses it

CONTINUITY:
- what survives refresh
- what survives back/forward navigation
- what belongs in the URL
- what is autosaved
- what scroll/filter/selection context is restored

DISCLOSURE:
- default-visible controls
- contextual controls
- expert/advanced controls
- keyboard/command-palette actions

For every screen, enforce:
Context -> Goal -> Primary Action -> Consequence -> Next Step.

Then output:
1. Route/task map
2. Component hierarchy
3. State-transition matrix
4. Loading/empty/error specification
5. Accessibility interaction specification
6. Instrumentation events
7. Performance budgets

Do not implement yet.
Flag any requirement that creates unnecessary user friction.
```

At this stage, define the product’s design tokens rather than asking the agent to improvise styling page by page. Tailwind v4’s CSS-first configuration and runtime theme variables are well suited to encoding those decisions, while shadcn’s editable source makes it feasible to customize behavior once and reuse it consistently. citeturn21view0turn21view2

A useful token contract is:

```text
Typography:
- display
- page title
- section title
- body
- supporting
- metadata

Spacing:
- dense control
- related group
- section
- page region

Surfaces:
- canvas
- raised
- overlay
- selected
- destructive

Interaction:
- default
- hover
- active
- focus-visible
- disabled
- pending
- success
- error

Motion:
- micro feedback
- state transition
- enter/exit
- layout continuity
- reduced-motion alternative
```

Do not let the agent invent arbitrary radii, shadows, padding, and motion duration inside individual components.


**Step 3 — Implement one complete vertical slice with production states**

Only now should the implementation agent modify code.

Do **not** say “build all pages.” Give it one complete user outcome and demand production behavior from entry through recovery.

Use:

```text
Implement the first vertical slice from the approved interaction architecture.

Stack:
- React 19
- Tailwind CSS v4
- shadcn/ui primitives where appropriate
- Motion only where motion communicates state or spatial continuity

Implementation rules:

1. Prefer semantic HTML and existing design-system primitives.
2. Do not create generic Card wrappers around every content region.
3. Use React's appropriate pending/action/optimistic patterns.
4. Reserve final layout dimensions before asynchronous content arrives.
5. Never block the full page when only one region is pending.
6. Preserve the user's input and context after recoverable errors.
7. Make reversible operations optimistic when safe and provide Undo.
8. Destructive irreversible actions require appropriate confirmation.
9. Every async action needs pending, success, error and retry behavior.
10. Every interactive control must work by keyboard.
11. Respect prefers-reduced-motion.
12. Avoid layout-triggering animation when transform/opacity can communicate
    the same transition.
13. Mobile is not a shrunk desktop layout; use component/container behavior.
14. Preserve useful filter/view/navigation state.
15. No decorative animation until the complete workflow is functional.

After implementation:
- run types/lint/tests;
- inspect all changed files;
- exercise every specified state;
- report deviations from the Experience Contract.

Do not start another feature until this vertical slice passes its UX gates.
```

React 19’s action-state and optimistic-state primitives are designed for precisely these pending/error/optimistic flows; Tailwind v4 has first-class container queries; and modern Motion guidance favors compositor-friendly animation strategies for performance-sensitive interfaces. citeturn1view0turn21view1turn0search31

This is where an agentic IDE becomes more than autocomplete. Cursor currently supports repository planning, review, skills/rules, subagents and cloud agents; Lovable can rapidly instantiate a working application while keeping code available to conventional engineering workflows. citeturn21view6turn21view8


**Step 4 — Add the retention and delight layer only after the task works**

Now ask a second pass to improve the experience without changing the fundamental IA unnecessarily.

Use:

```text
The workflow is functionally complete.

Act now as a Retention + Interaction Design specialist.

Improve USER SATISFACTION without adding engagement theater.

Audit the vertical slice for:

- time to first meaningful value;
- repeated decisions that can become transparent defaults;
- opportunities to preserve previous user choices;
- smart empty states that accelerate first success;
- contextual onboarding rather than tours;
- optimistic/reversible interactions;
- inline recovery instead of generic error toasts;
- meaningful progress toward the user's goal;
- keyboard acceleration for repeated workflows;
- contextual expert controls;
- state continuity after navigation and refresh;
- long-running operation feedback;
- opportunities for useful personalization;
- notification/interruption restraint;
- microinteractions that explain causality or state.

Motion rules:
Motion must communicate one of:
1. causality,
2. hierarchy,
3. spatial continuity,
4. system feedback,
5. completion.

If it does none of these, remove it.

For every proposed enhancement provide:
- user friction removed;
- expected user benefit;
- implementation cost;
- accessibility/performance risk;
- metric that could validate it.

Implement only high-value, low-regret improvements.
```

That instruction prevents the typical “polish pass” from degenerating into animation and visual noise. It deliberately connects delight to reduced uncertainty, competence, preserved context, and visible meaningful progress—the mechanisms better supported by usability and motivation research. citeturn19search3turn15search3turn14search5


**Step 5 — Put a different agent in charge of trying to break the experience**

Never let “the code compiles” be the final review.

Ideally, use a different frontier model from the one that implemented the feature. The implementation agent is already anchored to its own architecture; a fresh critic is more useful.

Use:

```text
You are now the adversarial UX, accessibility, and performance reviewer.

You did NOT design this implementation.
Your job is to find reasons a real user would become confused, slowed down,
lose trust, make a mistake, or abandon the workflow.

Run a task-based audit.

Test:

USABILITY
- first-time user with no product knowledge
- returning user with saved state
- expert trying to move quickly
- user who takes an unexpected but reasonable path

FAILURE
- slow network
- request timeout
- request rejection
- duplicate submission
- stale data / concurrency conflict
- browser refresh during work
- back and forward navigation
- failed optimistic mutation

CONTENT STATES
- zero records
- one record
- many records
- very long labels/content
- missing optional data

ACCESSIBILITY
- keyboard only
- focus order and focus restoration
- visible focus
- screen-reader semantics
- reduced motion
- zoom/reflow
- touch-target sizing
- alternatives to dragging

PERFORMANCE
- LCP
- INP
- CLS
- unnecessary client JavaScript
- serial requests that can be parallelized
- layout-triggering animation
- needless rerenders
- oversized media

RETENTION QUALITY
- unnecessary onboarding
- repeated decisions
- repeated data entry
- lost state
- dead-end empty states
- unexplained system state
- excessive alerts
- engagement dark patterns

For every finding assign:
P0 = blocks task or loses data
P1 = serious confusion/accessibility/performance problem
P2 = recurring friction
P3 = polish

Fix P0 and P1.
Then fix the highest-impact P2 issues.

Do not add visual decoration while unresolved friction remains.

At the end provide:
- before/after task path;
- remaining known friction;
- accessibility status;
- Web Vitals status;
- regression tests added;
- screenshots/state coverage;
- recommendation: SHIP / SHIP WITH KNOWN ISSUES / DO NOT SHIP.
```

The objective quality gates should include field Core Web Vitals—LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at P75—as well as WCAG 2.2 interaction requirements such as visible/unobscured focus, adequate targets, non-drag alternatives, useful error handling, and avoidance of unnecessary repeated entry. citeturn20view8turn12view0turn12view1turn11view2turn12view3

The final reusable orchestration loop is therefore:

> **Research intent → Model the states → Build one complete outcome → Add meaningful delight → Adversarially validate → Repeat**

And the durable master instruction for every project is:

```text
PRODUCT STANDARD

This product should feel premium because it removes work from the user,
not because it adds visual effects.

Optimize:
1. clarity of current context;
2. shortest path to meaningful value;
3. progressive disclosure of complexity;
4. immediate and truthful system feedback;
5. preservation of user intent and state;
6. safe optimism plus easy reversibility;
7. excellent empty/loading/error states;
8. fast recovery when anything goes wrong;
9. accessible interaction by default;
10. performance under real-world conditions;
11. mastery for returning users;
12. restrained, semantic motion;
13. transparent personalization;
14. respectful return triggers.

Every screen must make clear:
- Where am I?
- What matters right now?
- What can I do?
- What will happen?
- What should I do next?

Every async operation must define:
idle -> pending -> success -> error -> retry/recovery.

Every data surface must define:
loading -> empty -> partial -> populated -> stale/error.

Every destructive operation must answer:
Can this safely be made reversible?
If yes, prefer Undo over confirmation.

Every design choice must survive this question:
Does this reduce effort, uncertainty, waiting, repetition, or recovery cost?

If not, justify why it exists.

Do not:
- generate generic dashboard card grids;
- expose all options simultaneously;
- use animation as decoration;
- hide important state behind hover;
- erase user input after errors;
- make users repeatedly configure the same context;
- interrupt users merely to increase engagement;
- use novelty as a substitute for hierarchy;
- optimize screenshots at the expense of workflows.

A successful result should require less explanation after the redesign
than before it.
```

That is the practical late‑2026 shift: **frontier coding agents are now capable enough that generating interface code is no longer the hard part. The differentiator is the quality of the behavioral specification, state model, evaluation criteria, and feedback loop you place around the agent.** Current frontier offerings from OpenAI, Anthropic, and Google are explicitly optimized around increasingly long-horizon coding/agentic work, while environments such as Cursor and Lovable expose the planning, subagent, review, source-control, and MCP machinery needed to turn those models into controlled engineering systems. citeturn20view3turn21view5turn20view5turn21view6turn21view8turn21view9