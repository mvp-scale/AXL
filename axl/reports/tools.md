# Tools used for receipts (Phase 5)

All versions pinned in `tools/package-lock.json`. Install: `cd axl/tools && npm ci`. Browser: Chromium via `CHROME_PATH` (default `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`).

| Tool | Version | Used for | Status |
|---|---|---|---|
| axe-core (via @axe-core/playwright) | 4.13.0 / 4.13.0 | WCAG 2.0–2.2 A/AA rules at 1440 and 375 px | used |
| Lighthouse | 13.5.0 | accessibility audits (failed-audit ids; the category score is not asserted) | used |
| Playwright `toHaveScreenshot` (@playwright/test) | 1.63.0 | visual change detection, baseline in `tools/visual/__snap__/` | used |
| Playwright `emulateMedia(reducedMotion)` | 1.63.0 | reduced-motion check on a motion fixture | used |
| Stylelint | 17.15.0 | no `outline:none`, no gradients, banned font families | used |
| `@google/design.md lint` | 0.4.0 | token contrast rule on `demo/DESIGN.*.md` | used (exists on npm at run time) |
| WCAG contrast check (`runners/contrast.js`) | in-repo | WCAG 2.x relative-luminance ratio | used |
| eslint-plugin-better-tailwindcss | 4.7.0 on npm | Tailwind class linting | **dropped**: the Northstar demo is plain CSS with no Tailwind classes, so there is nothing for it to check |
| APCA | not installed | perceptual contrast | **dropped**: WCAG 2.x is the normative threshold cited by the claims; APCA adds no claim in this pass |

Notes
- The Northstar base page had real faults (axe and Lighthouse agree): 11 low-contrast text nodes and a missing `<title>`; it also has `outline:none` on focus and a decorative gradient (Stylelint). `demo/after.html` applies the fix layer in `demo/fix.css`. Both are produced by `scripts/build_demo.py`.
- The base page has no CSS transitions, so the reduced-motion check runs on two fixtures (`demo/fixture-motion-*.html`): the base plus the legacy `motion` effect, without and with a `prefers-reduced-motion` guard.
- The `target-size` axe rule passes on both variants, so its receipt runs but does not discriminate (flagged `discriminates: false` on those claims).
