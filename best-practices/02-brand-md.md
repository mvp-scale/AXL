# 02 — Per-Gauntlet `brand.md`

## Bottom line

A new gauntlet's entire visual identity is **one small file**. It holds a seed color,
two fonts, adjectives, a voice and the Worst Day tagline. Everything else derives from
the base `DESIGN.md` and the token build. That is what lets a Rev1 of any idea look
finished on day one.

## What a gauntlet authors

```yaml
# apps/management-gauntlet/brand.md — front matter (illustrative, not final schema)
name: Management Gauntlet
tagline: Can you survive your team's worst day?
adjectives: [steady, candid, under-pressure]   # exactly three — drives every taste call
anti-adjectives: [corporate, cheerful, soft]   # what it must NOT feel like
seed:
  brand: "oklch(0.62 0.17 35)"                 # one color; the 12-step scale is generated
  gray-tint: brand                             # grays tinted toward brand hue (Radix pattern)
type:
  display: "<distinctive display face>"        # see 06-anti-slop banned list
  body: "<refined text face>"
  mono: "<data/mono face>"
shape: sharp | soft | boxy                     # maps to a component style preset (04)
density: compact | comfortable
motion-temperament: crisp | bouncy | weighty   # selects a spring preset (05)
references: [2-3 real products/aesthetics this should rhyme with, and why]
```

Below the front matter is prose: the audience, what their worst day *feels* like, the
voice (sample good and bad copy), and the one memorable signature element for this brand.

## The brand brief (before the file)

Claude fills in the brief with the user before writing `brand.md`:

1. **Audience + worst day.** Who is in the room, and what is at stake?
2. **Three adjectives + three anti-adjectives.** Every later taste decision is
   checked against these.
3. **Aesthetic family**, named explicitly, e.g. "editorial broadsheet", "flight-deck
   instrument", "field notebook", "arcade boss fight". Unnamed direction drifts to the
   generic default.
4. **Two or three references** (real products or cultural sources), each with the
   specific thing being borrowed.
5. **One signature element**, the thing people will remember (e.g. the Climb mountain,
   a verdict stamp, a pressure gauge).

## Rules

- **The brand layer changes only brand values.** A brand can't change the spacing
  rhythm, verdict colors, component behavior or the moment catalog. That boundary is what keeps
  "different genre, same game" true.
- **Seed, don't hand-pick.** One brand color goes in; the generator produces the 12
  steps plus dark mode with contrast guaranteed ([03](03-tokens-and-typescript.md)).
  Hand-picked palettes are where contrast failures and muddy dark modes come from.
- **Contrast is validated at build time**, via `design.md lint` and the generator. It
  is never checked by eye.
