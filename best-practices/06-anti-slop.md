# 06 — Anti-Slop Standard

## Bottom line

AI UI defaults to the statistical middle: Inter, purple gradients, a centered hero with
three cards, and colors spread timidly. The remedy is to **name a direction before any
code**, **ban the known defaults**, and **require a few deliberate choices**. Anything a
machine can check moves into lint ([07](07-guardrails-and-verification.md)); this file
keeps the taste rules that need judgment.

## Banned by default

A brand can use any of these only with a written reason in `brand.md`.

**Type**
- Inter, Roboto, Arial, Open Sans, Lato, system-ui as the *display* face
- Space Grotesk (the model's fallback once Inter is banned)
- A single font family used for everything
- Timid scale steps (14/16/18). Use real contrast between sizes

**Color**
- A purple or blue gradient on white or near-black
- **The 2026 "anti-slop" tell:** a warm cream background + a serif display face
  (Instrument Serif, Fraunces) + a sage or forest-green accent. It's what you get by
  swapping one default for another
- Colors spread evenly with no dominant one
- Pure `#000` / `#fff` surfaces with untinted grays
- Gradient text as decoration

**Layout**
- A centered hero, then three feature cards, then a CTA band
- Every section in the same rounded card with the same shadow
- Uniform spacing everywhere, with no rhythm and no tension
- Pill badges and "✨ New" chips as decoration

**Surface & detail**
- Glassmorphism as the default surface
- Emoji used as icons
- Generic stock illustrations or blob backgrounds
- Mixed icon sets, or icons used where a word would read better

**Motion**
- Fade-up on every element as it scrolls in
- Hover-scale on every card
- Spinners where a latency choreography belongs ([05](05-motion-and-celebration.md))

**Copy**
- "Unlock your potential", "Supercharge", "Seamless", "Elevate", "Revolutionize"
- Generic empty states ("Nothing here yet!"). Write each one in the brand voice

## Required choices (every brand)

1. **A named aesthetic family** and three adjectives ([02](02-brand-md.md)).
2. **A distinctive display face paired with a refined body face.** Pick with intent,
   and look past the usual places: editorial serifs, grotesques with character,
   mono for data.
3. **One dominant color with sharp accents.** For inspiration, look at IDE themes,
   print, sport, signage, and cultural aesthetics, not other SaaS sites.
4. **Backgrounds with atmosphere:** texture, grain, a tinted ground, or a structural
   grid. Never a flat default gray.
5. **One signature element** per brand that nobody else has.
6. **Hierarchy through contrast.** Size, weight and space do the work before color does.
7. **Data looks like instruments.** Scores, beats and the mountain are designed
   visualizations, not stat cards.

## The gut check (run on every screen)

- Could this screen be a different product's with the logo swapped? If yes, it's slop.
- Does it match the three adjectives, and avoid the three anti-adjectives?
- What is the one thing a user remembers from this screen?
- Is the most important thing visually the most important?

## Anti-slop toolkits (researched Sept 2026)

The key warning comes from the Unslop playbook: **every anti-slop effort fails by
replacing one default look with another.** That's why no toolkit is allowed to *choose*
our look. `brand.md` chooses it, and the toolkits only give taste and run checks.

| Toolkit | Type | What it does | Use |
|---|---|---|---|
| **Anthropic `frontend-design`** | Taste | Commit to an aesthetic direction and answer purpose/tone before writing CSS; bans default fonts | **Base taste layer**, adopted |
| **Impeccable** (Paul Bakaus) 4.0 | Taste + checks | 23 commands (`/impeccable critique` scores out of 40 and lists slop; `polish`, `animate`); 4px grid, OKLCH, fluid type, AA; brand vs product modes; Live mode detector | **Critique + polish passes**, strongest candidate. Pilot it |
| **Hallmark** (Nutlope / Together AI) | Generator + audit | 21 themes, 57 slop gates, an audit mode that returns a punch list with no edits | **Audit mode only.** Its themes would fight our brand files, and HN reactions were mixed |
| **Unslop UI** playbook | Audit | Findings with file:line references; never suggests a palette or font; catches the default shadcn/Tailwind look | Worth folding its checklist into `/design-review` |
| **design-taste-frontend** | Taste | Dials for variance, motion and density | Skip. It overlaps with `motion-temperament` / `density` in `brand.md` |
| **shadcn/skills** (`npx skills add https://github.com/shadcn-ui/ui --skill shadcn`) | Correct usage | Semantic colors, correct Base UI APIs, FieldGroup/ToggleGroup patterns | **Adopted.** It covers correctness, not taste |

**Rule: one taste skill only** (ours, `gauntlet-design`, built on `frontend-design`'s
principles). Multiple taste skills give Claude conflicting direction. The others are used
as **critics**, never as generators. Pilot before adopting: run Impeccable critique and
Hallmark audit on the existing Founder's Gauntlet UI, and keep whichever one finds real
problems.

## Sources of the standard

Anthropic's `frontend-design` skill and the Claude Cookbook's "prompting for frontend
aesthetics" (the ~400-token prompt), the community `frontend-design-deslop` skill, and
the Adpharm recipe: DESIGN.md + a named aesthetic family + 2–3 references + iterate
rather than re-prompt. See [SOURCES](SOURCES.md).
