# Phase 2 pilot: Type as Class › Element › Rules

123 tweaks → **16 element rows**, **56 measurable rules**, **86 questions**. ● = lights up when you pick *polish*; "polish: n of 13" = how many of the 13 sources that define polish ask for something in that row.

## ○ Navigation · 1 rule  `aria:navigation`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Navigation capitalization is never uppercase<br>`aria:navigation text-transform !contains uppercase` | uppercase: ui-craft (1) |  |

## ● Page header · 1 rule · polish: 1 of 13  `aria:banner`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Does the wordmark use a display face distinct from the body face?<br>`aria:banner ask "Does the wordmark use a display face distinct from the body face?"` | yes: hallmark (3) | 1 |

## ○ Main content · 1 rule  `aria:main`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Main content width is at most 64rem<br>`aria:main max-width <= 64rem` | max-w-4xl or max-w-5xl: taste-skill (1) |  |

## ○ Display text · 18 rules  `text:display`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Display text headline lines is at most 3<br>`text:display axl:headline-lines <= 3` | 3: taste-skill (6); 2: taste-skill (1) |  |
| Display text headline words is between 5 and 10<br>`text:display axl:headline-words between 5 and 10` | 5-10: taste-skill (1) |  |
| Display text size is at most 5.5rem<br>`text:display font-size <= 5.5rem` | 5.5rem: hallmark (1); 6rem: hallmark (1) |  |
| Display text style is normal<br>`text:display font-style == normal` | normal: hallmark (1); yes: hallmark (1) |  |
| Display text number style includes tabular-nums<br>`text:display font-variant-numeric contains tabular-nums` | tabular-nums: hallmark (1) |  |
| Display text letter spacing is at most -0.02em<br>`text:display letter-spacing <= -0.02em` | -0.02em: deslop, hallmark, taste-skill, ui-craft (6); -0.04em: hallmark, impeccable, taste-skill, ui-craft (5); -0.025em: hallmark (2); -0.03em: hallmark, taste-skill (2) |  |
| Display text line height is at least 1.05<br>`text:display line-height >= 1.05` | 1.05: hallmark, ui-craft (2); 1: taste-skill (1); yes: taste-skill (1); 1.1: taste-skill (1); 0.95: hallmark (1) |  |
| Display text width is at least 64rem<br>`text:display max-width >= 64rem` | max-w-5xl, max-w-6xl or w-full: taste-skill (1) |  |
| Is the hero layout off-centre rather than a dead-centre stack?<br>`text:display ask "Is the hero layout off-centre rather than a dead-centre stack?"` | yes: hallmark (1) |  |
| Is the hero headline short (2-3 lines, words cut rather than lines added) and, when it is a long full sentence or sits beside a large hero asset with over 6 words, set below text-7xl rather than at display size?<br>`text:display ask "Is the hero headline short (2-3 lines, words cut rather than lines added) and, when it is a long full sentence or sits beside a large hero asset with over 6 words, set below text-7xl rather than at display size?"` | yes: deslop, impeccable, taste-skill (9) |  |
| Is the hero's large numeric figure paired with a worded headline, never standing alone?<br>`text:display ask "Is the hero's large numeric figure paired with a worded headline, never standing alone?"` | yes: hallmark (2) |  |
| Do display headers wrap inside long words (overflow-wrap: anywhere, min-width: 0)?<br>`text:display ask "Do display headers wrap inside long words (overflow-wrap: anywhere, min-width: 0)?"` | yes: hallmark (2) |  |
| Is the headline type treatment an active part of the design rather than a neutral vehicle for the content?<br>`text:display ask "Is the headline type treatment an active part of the design rather than a neutral vehicle for the content?"` | yes: anthropic (1) |  |
| Is a giant section-index numeral set beside or behind the heading at 6-10% opacity ink or in the signal ink?<br>`text:display ask "Is a giant section-index numeral set beside or behind the heading at 6-10% opacity ink or in the signal ink?"` | yes: hallmark (1) |  |
| Does display type carry the voice with decisive contrast, and shrink faster than small type on small screens (e.g. 72px desktop hero to 36px mobile while 16px body stays 16px)?<br>`text:display ask "Does display type carry the voice with decisive contrast, and shrink faster than small type on small screens (e.g. 72px desktop hero to 36px mobile while 16px body stays 16px)?"` | yes: deslop, impeccable (2) |  |
| Is the display or decorative face limited to headlines and limited accents?<br>`text:display ask "Is the display or decorative face limited to headlines and limited accents?"` | yes: deslop (1) |  |
| Do massive headings embed small pill-shaped images inline?<br>`text:display ask "Do massive headings embed small pill-shaped images inline?"` | yes: taste-skill (1) |  |
| Is one hero scale chosen decisively rather than splitting the difference?<br>`text:display ask "Is one hero scale chosen decisively rather than splitting the difference?"` | yes: taste-skill (1) |  |

## ● Headings · 18 rules · polish: 2 of 13  `aria:heading`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Headings accent words per heading is at most 1<br>`aria:heading axl:accent-words-per-heading <= 1` | 1: hallmark (3) |  |
| Headings heading space ratio is at least 1<br>`aria:heading axl:heading-space-ratio >= 1` | 1: impeccable (1) |  |
| Headings style is normal<br>`aria:heading font-style == normal` | normal: hallmark (1); yes: hallmark (1) |  |
| Headings weight is at least 700<br>`aria:heading font-weight >= 700` | 700: hallmark (2); 800: anthropic (1); 500: ui-craft (1) | 1 |
| Headings capitalization is never uppercase<br>`aria:heading text-transform !contains uppercase` | uppercase: hallmark, ui-craft (5) |  |
| Headings line wrapping is balance<br>`aria:heading text-wrap == balance` | balance: feel-better, vercel (3) | 1 |
| Are headings clearly stronger than body text (bigger or heavier)?<br>`aria:heading ask "Are headings clearly stronger than body text (bigger or heavier)?"` | yes: claw-design, impeccable, oneredoak (6) | 1 |
| Does each section heading's alignment match the body it introduces?<br>`aria:heading ask "Does each section heading's alignment match the body it introduces?"` | yes: hallmark (1) |  |
| Is the one accent-coloured word in the headline a verb (never a noun), with the rest of the display text in ink colour?<br>`aria:heading ask "Is the one accent-coloured word in the headline a verb (never a noun), with the rest of the display text in ink colour?"` | yes: hallmark (4) |  |
| Is the verb underline drawn once and never animated again?<br>`aria:heading ask "Is the verb underline drawn once and never animated again?"` | yes: hallmark (2) |  |
| When an eyebrow is used, does the heading sit directly under it in the same column?<br>`aria:heading ask "When an eyebrow is used, does the heading sit directly under it in the same column?"` | yes: hallmark (2) |  |
| Is an emphasised headline word set in italic or bold of the same font rather than a different face?<br>`aria:heading ask "Is an emphasised headline word set in italic or bold of the same font rather than a different face?"` | yes: taste-skill, ui-craft (3) |  |
| Is headline emphasis varied (scale, drawn underline, colour-blocked line) rather than always one highlighted word?<br>`aria:heading ask "Is headline emphasis varied (scale, drawn underline, colour-blocked line) rather than always one highlighted word?"` | yes: hallmark (1) |  |
| Are section headings free of tiny numbered index labels?<br>`aria:heading ask "Are section headings free of tiny numbered index labels?"` | yes: impeccable (1) |  |
| Do headings put the most important words at the start?<br>`aria:heading ask "Do headings put the most important words at the start?"` | yes: deslop (1) |  |
| Are headings in sentence case rather than title case?<br>`aria:heading ask "Are headings in sentence case rather than title case?"` | yes: taste-skill, ui-craft (2) |  |
| Is the first heading restrained, with hierarchy from weight and color rather than massive scale?<br>`aria:heading ask "Is the first heading restrained, with hierarchy from weight and color rather than massive scale?"` | yes: taste-skill (1) |  |
| Do headlines read naturally, without br-broken italicised splits used as a default design move?<br>`aria:heading ask "Do headlines read naturally, without br-broken italicised splits used as a default design move?"` | yes: taste-skill (1) |  |

## ● Body text · 20 rules · polish: 2 of 13  `text:body`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Body text lines are at most 75 characters<br>`text:body axl:chars-per-line <= 75` | 75: deslop, hallmark, impeccable, ui-craft (12); 65: hallmark, impeccable, taste-skill, ui-craft (10); 45: deslop, hallmark, impeccable, ui-craft (8); 80: anthropic, deslop (2) | 1 |
| Body text color is never #000000<br>`text:body color !contains #000000` | #000000: taste-skill (1) |  |
| Body text size is at least 16px<br>`text:body font-size >= 16px` | 16px: deslop, hallmark, impeccable, ui-craft (7); 14px: deslop, hallmark, impeccable, taste-skill (5); 18px: ui-craft (1) |  |
| Body text weight is at least 400<br>`text:body font-weight >= 400` | 400: hallmark, ui-craft (4); yes: apple-hig (1); 500: ui-craft (1) |  |
| Body text hyphenation is auto<br>`text:body hyphens == auto` | auto: impeccable (1) |  |
| Body text letter spacing is at most 0.05em<br>`text:body letter-spacing <= 0.05em` | 0.05em: hallmark, impeccable (2) |  |
| Body text line height is at least 1.5<br>`text:body line-height >= 1.5` | 1.5: deslop, impeccable, oneredoak, ui-craft (4); 1.7: deslop, impeccable, oneredoak (3); 1.3: deslop, impeccable (2); 1.6: taste-skill (1) |  |
| Body text width is at most 65ch<br>`text:body max-width <= 65ch` | 65ch: hallmark, taste-skill, ui-craft (7); 75ch: impeccable (1) |  |
| Body text alignment is left<br>`text:body text-align == left` | left: deslop, impeccable, oneredoak (5) |  |
| Body text capitalization is never uppercase<br>`text:body text-transform !contains uppercase` | uppercase: hallmark (1) |  |
| Body text line wrapping is pretty<br>`text:body text-wrap == pretty` | pretty: feel-better (2); yes: feel-better, vercel (2) |  |
| Does body text of three or more lines have relaxed leading, more for wider lines and for serif than for sans-serif, even where height is limited?<br>`text:body ask "Does body text of three or more lines have relaxed leading, more for wider lines and for serif than for sans-serif, even where height is limited?"` | yes: anthropic, apple-hig, impeccable, taste-skill (5) |  |
| Are paragraphs longer than 3 sentences split into separate blocks?<br>`text:body ask "Are paragraphs longer than 3 sentences split into separate blocks?"` | 3 sentences: hallmark (1); yes: claw-design (1) | 1 |
| Is paragraph rhythm set by either paragraph spacing or first-line indentation, not both?<br>`text:body ask "Is paragraph rhythm set by either paragraph spacing or first-line indentation, not both?"` | yes: impeccable (1) | 1 |
| Are line lengths set in relative units (rem or ch) rather than fixed px?<br>`text:body ask "Are line lengths set in relative units (rem or ch) rather than fixed px?"` | yes: webdev (2) |  |
| Is text of 10 or more lines left on the browser's default wrapping, without pretty or balance?<br>`text:body ask "Is text of 10 or more lines left on the browser's default wrapping, without pretty or balance?"` | 10+ lines: feel-better (1) |  |
| Is italic used only for inline emphasis inside running body paragraphs?<br>`text:body ask "Is italic used only for inline emphasis inside running body paragraphs?"` | yes: hallmark (1) |  |
| Is body text free of justification unless hyphenation is enabled?<br>`text:body ask "Is body text free of justification unless hyphenation is enabled?"` | yes: hallmark (1) |  |
| Does the first paragraph open with a drop cap (floated first letter, 4.5em, line-height 0.85, in the display face)?<br>`text:body ask "Does the first paragraph open with a drop cap (floated first letter, 4.5em, line-height 0.85, in the display face)?"` | yes: ui-craft (1) |  |
| Is body set in a neutral sans (Inter or Geist) and never in a display font?<br>`text:body ask "Is body set in a neutral sans (Inter or Geist) and never in a display font?"` | yes: ui-craft (1) |  |

## ○ Labels · 5 rules  `text:label`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Labels typeface includes JetBrains Mono<br>`text:label font-family contains JetBrains Mono` | JetBrains Mono: hallmark (1) |  |
| Labels size is between 10px and 14px<br>`text:label font-size between 10px and 14px` | 10px to 14px: taste-skill (1) |  |
| Labels letter spacing is at least 0.05em<br>`text:label letter-spacing >= 0.05em` | 0.05em: taste-skill, ui-craft (3); 0.06em: hallmark, ui-craft (2); 0.08em: hallmark (1) |  |
| Labels line height is between 1.3 and 1.4<br>`text:label line-height between 1.3 and 1.4` | 1.3 to 1.4: ui-craft (1) |  |
| Labels capitalization is uppercase<br>`text:label text-transform == uppercase` | uppercase: hallmark (2) |  |

## ● All text · 51 rules · polish: 5 of 13  `text:*`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| All text uses at most 6 font sizes<br>`text:* axl:distinct-font-sizes <= 6` | 6: deslop, hallmark, ui-craft (4); 5: hallmark (1); 8: deslop (1); 4: impeccable (1); yes: openai (1) | 2 |
| All text uses at most 3 font weights<br>`text:* axl:distinct-font-weights <= 3` | 3: impeccable, ui-craft (2); 2: ui-craft (1); 4: oneredoak (1) |  |
| All text type step ratio is at least 1.25<br>`text:* axl:type-step-ratio >= 1.25` | 1.25: hallmark, impeccable (2); 3: anthropic (1); 2.5: ui-craft (1); 4: ui-craft (1) | 3 |
| All text background image includes gradient<br>`text:* background-image contains gradient` | gradient: hallmark (2) |  |
| All text typeface is never Inter<br>`text:* font-family !contains Inter` | Inter: anthropic, deslop, hallmark, taste-skill, ui-craft, unslop (11); Roboto: anthropic, deslop, hallmark, taste-skill, unslop (6); Open Sans: anthropic, deslop, hallmark, taste-skill (4); Arial: anthropic, deslop (3); Times New Roman: taste-skill (2); Georgia: taste-skill (2); yes: feel-better (1) |  |
| All text size is at least 10px<br>`text:* font-size >= 10px` | 10px: hallmark (1) |  |
| All text style is never italic<br>`text:* font-style !contains italic` | italic: hallmark (2); yes: impeccable (1) |  |
| All text number style includes tabular-nums<br>`text:* font-variant-numeric contains tabular-nums` | tabular-nums: deslop, feel-better, hallmark, impeccable, taste-skill, ui-craft, vercel (12) | 2 |
| All text keeps text visible while fonts load<br>`text:* lighthouse:font-display pass` | yes: deslop, impeccable, taste-skill, webdev (8) |  |
| All text movement is never rotate<br>`text:* transform !contains rotate` | rotate 90deg: taste-skill (1) |  |
| All text meets WCAG 1.4.12: text spacing<br>`text:* wcag:1.4.12 pass` | yes: axe, deslop, impeccable, wcag22 (4) |  |
| All text meets WCAG 1.4.4: text resizes to 200%<br>`text:* wcag:1.4.4 pass` | yes: apple-hig, wcag22 (2) |  |
| Is letter-spacing left unadjusted on CJK, Arabic, Devanagari and other non-Latin scripts?<br>`text:* ask "Is letter-spacing left unadjusted on CJK, Arabic, Devanagari and other non-Latin scripts?"` | yes: ui-craft (2) |  |
| Is all text, including custom fonts, large and sparse enough to read comfortably at normal viewing size without zoom?<br>`text:* ask "Is all text, including custom fonts, large and sparse enough to read comfortably at normal viewing size without zoom?"` | yes: apple-hig, taste-skill, ui-craft (7) |  |
| Are font sizes set as rem/em values or scale tokens, each piece of text mapping to a named type role, rather than ad-hoc pixels?<br>`text:* ask "Are font sizes set as rem/em values or scale tokens, each piece of text mapping to a named type role, rather than ad-hoc pixels?"` | yes: apple-hig, claw-design, hallmark, impeccable, oneredoak (6) | 2 |
| Is typography for the same role consistent across screens and states?<br>`text:* ask "Is typography for the same role consistent across screens and states?"` | yes: impeccable (2) | 2 |
| Are line-height declarations unitless?<br>`text:* ask "Are line-height declarations unitless?"` | yes: webdev (1) |  |
| Are thin weights paired with sizes larger than the recommended minimum?<br>`text:* ask "Are thin weights paired with sizes larger than the recommended minimum?"` | yes: apple-hig (1) |  |
| Does weight contrast between titles and body carry the hierarchy, using a limited set of weights with the heaviest (900, 700) stepped down one or two?<br>`text:* ask "Does weight contrast between titles and body carry the hierarchy, using a limited set of weights with the heaviest (900, 700) stepped down one or two?"` | yes: deslop, impeccable, oneredoak, ui-craft (5) |  |
| Does every additional typeface have a role that only it can perform?<br>`text:* ask "Does every additional typeface have a role that only it can perform?"` | yes: deslop, hallmark, impeccable (3) |  |
| Does text show in a fallback font with matched metrics, from a practical fallback stack, until the web font is ready, so it is never invisible and does not reflow?<br>`text:* ask "Does text show in a fallback font with matched metrics, from a practical fallback stack, until the web font is ready, so it is never invisible and does not reflow?"` | yes: deslop, feel-better, hallmark, impeccable, webdev (6) |  |
| Are critical fonts preloaded?<br>`text:* ask "Are critical fonts preloaded?"` | yes: vercel (2) |  |
| Are only the code points, scripts and weights in use shipped?<br>`text:* ask "Are only the code points, scripts and weights in use shipped?"` | yes: impeccable, ui-craft, vercel (4) |  |
| Is a variable font used?<br>`text:* ask "Is a variable font used?"` | yes: deslop (1) |  |
| Is antialiased font smoothing enabled without overriding the project's chosen font family?<br>`text:* ask "Is antialiased font smoothing enabled without overriding the project's chosen font family?"` | yes: feel-better (2) |  |
| Does text use typographic (curly) quotes and apostrophes instead of straight ASCII ones?<br>`text:* ask "Does text use typographic (curly) quotes and apostrophes instead of straight ASCII ones?"` | yes: hallmark, taste-skill, vercel (5) |  |
| Does text use the ellipsis character and true em and en dashes instead of ... and --?<br>`text:* ask "Does text use the ellipsis character and true em and en dashes instead of ... and --?"` | yes: hallmark, ui-craft, vercel (7) |  |
| Are units, shortcuts and brand names kept together with non-breaking spaces?<br>`text:* ask "Are units, shortcuts and brand names kept together with non-breaking spaces?"` | yes: hallmark, ui-craft, vercel (6) |  |
| Do text and layout follow the user's font-size setting, with no hard-coded fixed sizes and no font-size set with vw alone?<br>`text:* ask "Do text and layout follow the user's font-size setting, with no hard-coded fixed sizes and no font-size set with vw alone?"` | yes: apple-hig, impeccable, webdev (8) |  |
| Is core UI text live text rather than rasterized?<br>`text:* ask "Is core UI text live text rather than rasterized?"` | yes: impeccable (1) |  |
| Is the highlighter painted on the text itself with box-decoration-break: clone, and does every decorative text effect (highlighter band, accent stroke, underline) sit in the right position and size?<br>`text:* ask "Is the highlighter painted on the text itself with box-decoration-break: clone, and does every decorative text effect (highlighter band, accent stroke, underline) sit in the right position and size?"` | yes: hallmark (5) |  |
| Are headlines, body, buttons, nav and captions all lowercase, with only mono labels uppercase?<br>`text:* ask "Are headlines, body, buttons, nav and captions all lowercase, with only mono labels uppercase?"` | yes: hallmark (3) |  |
| Is the middle dot limited to one per metadata line and used only when it conveys semantic state?<br>`text:* ask "Is the middle dot limited to one per metadata line and used only when it conveys semantic state?"` | yes: taste-skill (2) |  |
| Does every truncated text container carry a title tooltip and a set max-width, with min-width 0 on flex children holding it?<br>`text:* ask "Does every truncated text container carry a title tooltip and a set max-width, with min-width 0 on flex children holding it?"` | yes: ui-craft (2) |  |
| Is truncation kept to a minimum at larger font sizes, and absent in scrollable regions unless people can open a separate view to read the rest?<br>`text:* ask "Is truncation kept to a minimum at larger font sizes, and absent in scrollable regions unless people can open a separate view to read the rest?"` | yes: apple-hig (2) |  |
| Is text flat 2D rather than 3D-transformed?<br>`text:* ask "Is text flat 2D rather than 3D-transformed?"` | yes: apple-hig (1) |  |
| Is text contrast achieved without adding shadows to the text?<br>`text:* ask "Is text contrast achieved without adding shadows to the text?"` | yes: apple-hig (1) |  |
| Is all text set in sans-serif (rounded where specified), with no serif display faces and no mono body text?<br>`text:* ask "Is all text set in sans-serif (rounded where specified), with no serif display faces and no mono body text?"` | yes: hallmark (2) |  |
| Is hierarchy built through weight, size and space rather than colour and boldness?<br>`text:* ask "Is hierarchy built through weight, size and space rather than colour and boldness?"` | yes: impeccable (1) |  |
| Are bold, italic and highlight styling used only within content areas, not for structural UI?<br>`text:* ask "Are bold, italic and highlight styling used only within content areas, not for structural UI?"` | yes: openai (1) |  |
| Do differing elements differ decisively rather than timidly (not 16px vs 18px, not gray vs slightly-grayer)?<br>`text:* ask "Do differing elements differ decisively rather than timidly (not 16px vs 18px, not gray vs slightly-grayer)?"` | yes: deslop (1) |  |
| Is typography a monolithic heavy sans-serif on a high-contrast light ground, with structural grids outlined by visible dividing lines?<br>`text:* ask "Is typography a monolithic heavy sans-serif on a high-contrast light ground, with structural grids outlined by visible dividing lines?"` | yes: taste-skill (1) |  |
| Are Medium (500) and SemiBold (600) weights used for subtle hierarchy beyond Regular (400) and Bold (700)?<br>`text:* ask "Are Medium (500) and SemiBold (600) weights used for subtle hierarchy beyond Regular (400) and Bold (700)?"` | yes: taste-skill (1) |  |
| Does every italic word with descenders have line-height of at least 1.1 and a bottom-padding reserve?<br>`text:* ask "Does every italic word with descenders have line-height of at least 1.1 and a bottom-padding reserve?"` | 1.1: taste-skill (1) |  |
| Are pull quotes serif, large (1.75-2.25em), in one accent color with a short rule above?<br>`text:* ask "Are pull quotes serif, large (1.75-2.25em), in one accent color with a short rule above?"` | 1.75-2.25em: ui-craft (1) |  |
| Is the blockquote set with an accent left border, serif italic and a max-width of 55ch?<br>`text:* ask "Is the blockquote set with an accent left border, serif italic and a max-width of 55ch?"` | 55ch: ui-craft (1) |  |
| Are OpenType features active where supported: discretionary ligatures off in UI, contextual alternates on for serif headlines, kerning always on?<br>`text:* ask "Are OpenType features active where supported: discretionary ligatures off in UI, contextual alternates on for serif headlines, kerning always on?"` | yes: ui-craft (1) |  |
| Do mixed text sizes on one line align to the shared baseline rather than to vertical centers?<br>`text:* ask "Do mixed text sizes on one line align to the shared baseline rather than to vertical centers?"` | yes: ui-craft (1) |  |
| Do metrics lead with the number in the hierarchy?<br>`text:* ask "Do metrics lead with the number in the hierarchy?"` | yes: ui-craft (1) |  |
| Is font-synthesis set to none so a missing weight or style fails visibly instead of rendering fake glyphs?<br>`text:* ask "Is font-synthesis set to none so a missing weight or style fails visibly instead of rendering fake glyphs?"` | yes: ui-craft (1) |  |
| Are text sizes smaller on smaller screens and larger on larger screens?<br>`text:* ask "Are text sizes smaller on smaller screens and larger on larger screens?"` | yes: webdev (1) |  |

## ○ Links · 1 rule  `aria:link`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Do underlines take their offset and thickness from the font's metrics (from-font)?<br>`aria:link ask "Do underlines take their offset and thickness from the font's metrics (from-font)?"` | yes: ui-craft (1) |  |

## ● Tables · 2 rules · polish: 2 of 13  `aria:table`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Tables capitalization is never uppercase<br>`aria:table text-transform !contains uppercase` | uppercase: ui-craft (2) |  |
| Are numbers right-aligned so decimals and magnitudes line up?<br>`aria:table ask "Are numbers right-aligned so decimals and magnitudes line up?"` | yes: deslop, oneredoak (2) | 2 |

## ○ Images · 2 rules  `aria:img`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Images meet WCAG 1.4.5: <br>`aria:img wcag:1.4.5 pass` | yes: wcag22 (1) |  |
| Images meet WCAG 1.4.9: <br>`aria:img wcag:1.4.9 pass` | yes: wcag22 (1) |  |

## ○ Icons · 1 rule  `ui:icon`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Are informative icons still easy to view at larger font sizes?<br>`ui:icon ask "Are informative icons still easy to view at larger font sizes?"` | yes: apple-hig (1) |  |

## ○ Buttons · 4 rules  `aria:button`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Buttons size is between 14px and 17px<br>`aria:button font-size between 14px and 17px` | 14-17px: ui-craft (1) |  |
| Buttons capitalization is never uppercase<br>`aria:button text-transform !contains uppercase` | uppercase: ui-craft (1) |  |
| Is button label typography clearly stronger than surrounding body text?<br>`aria:button ask "Is button label typography clearly stronger than surrounding body text?"` | — |  |
| Is the label visually centered in single-line buttons, pills and chips (height minus font size even, half-leading trimmed with text-box: trim-both cap alphabetic)?<br>`aria:button ask "Is the label visually centered in single-line buttons, pills and chips (height minus font size even, half-leading trimmed with text-box: trim-both cap alphabetic)?"` | yes: ui-craft (2) |  |

## ○ Text fields · 1 rule  `aria:textbox`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Text fields size is at least 16px — phones<br>`aria:textbox font-size >= 16px @media:narrow` | 16px: deslop, impeccable, ui-craft, vercel (5) |  |

## ● Whole page · 13 rules · polish: 2 of 13  `page`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Whole page uses at least 2 typefaces<br>`page axl:distinct-font-families >= 2` | 2: anthropic, hallmark, ui-craft (7); 3: deslop, hallmark (4); 1: anthropic, hallmark, impeccable (4); yes: apple-hig (1) | 1 |
| Whole page doesn't shift while loading (CLS)<br>`page lighthouse:cls pass` | yes: hallmark (1) |  |
| Whole page html has lang (Lighthouse) is passes <br>`page lighthouse:html-has-lang pass` | yes: axe, lighthouse (2) |  |
| Whole page html lang valid (Lighthouse) is passes <br>`page lighthouse:html-lang-valid pass` | yes: axe, lighthouse (3) |  |
| Whole page meets WCAG 3.1.1: page language<br>`page wcag:3.1.1 pass` | yes: wcag22 (1) |  |
| Whole page meets WCAG 3.1.2: <br>`page wcag:3.1.2 pass` | yes: wcag22 (1) |  |
| Does the eye land first on the headline, then the evidence, then the footnote, so the three layers can be told apart at a glance?<br>`page ask "Does the eye land first on the headline, then the evidence, then the footnote, so the three layers can be told apart at a glance?"` | yes: claw-design, deslop (5) | 1 |
| Does the page pair a distinctive display face with a separate body face from a different class (e.g. serif with sans, not two sans)?<br>`page ask "Does the page pair a distinctive display face with a separate body face from a different class (e.g. serif with sans, not two sans)?"` | yes: deslop, hallmark, unslop (9) | 1 |
| Is each typeface chosen deliberately, with a stated reason, rather than as an autopilot default?<br>`page ask "Is each typeface chosen deliberately, with a stated reason, rather than as an autopilot default?"` | yes: anthropic, deslop, hallmark, impeccable, taste-skill, ui-craft, unslop (14) |  |
| Are uppercase tracked eyebrow labels and number kickers absent or rationed (at most one per 3 sections), unless numbering was explicitly requested?<br>`page ask "Are uppercase tracked eyebrow labels and number kickers absent or rationed (at most one per 3 sections), unless numbering was explicitly requested?"` | yes: hallmark, impeccable (7); 1 per 3 sections: ui-craft (2) |  |
| Does one message, date or event title dominate the composition, so the core message is understood within three seconds?<br>`page ask "Does one message, date or event title dominate the composition, so the core message is understood within three seconds?"` | yes: claw-design (3) |  |
| Is serif used only where it is explicitly justified (creative or editorial designs), and never on dashboards or software UIs?<br>`page ask "Is serif used only where it is explicitly justified (creative or editorial designs), and never on dashboards or software UIs?"` | yes: taste-skill (4) |  |
| Is the outlier typeface used in at most two slots on the page?<br>`page ask "Is the outlier typeface used in at most two slots on the page?"` | 2: hallmark (2) |  |

## ○ How the work is done · 3 rules  `process`

| Rule (as shown) | What sources say (statements) | polish |
|---|---|---|
| Have font pairs been tested in mockups for real use cases (web, mobile, print)?<br>`process ask "Have font pairs been tested in mockups for real use cases (web, mobile, print)?"` | yes: deslop (1) |  |
| Does the chosen type class match the committed brand adjectives?<br>`process ask "Does the chosen type class match the committed brand adjectives?"` | yes: deslop (1) |  |
| For cross-channel work, are faces chosen and tested for all media, with licensing covering all uses and per-medium size adjustments documented?<br>`process ask "For cross-channel work, are faces chosen and tested for all media, with licensing covering all uses and per-medium size adjustments documented?"` | yes: deslop (1) |  |

## New `axl:` measures proposed

- `axl:type-step-ratio`: Largest ratio between adjacent distinct font-size steps among the dominant heading and body roles (computed font-size of the next larger role divided by the smaller), unitless, measured on h1-h6 and body text.
- `axl:heading-space-ratio`: For each heading, computed space above it (margin-top plus preceding sibling margin-bottom/padding) divided by space below it (margin-bottom plus following sibling margin-top), unitless, taking the minimum over all aria:heading elements.
- `axl:headline-lines`: Number of rendered lines of the page's hero headline (the h1 / largest display text): its rendered block height divided by its computed line-height, rounded, at each viewport width tested; unit: lines.
- `axl:headline-words`: Number of whitespace-separated words in the page's hero headline (the h1 / largest display text); unit: words.
- `axl:accent-words-per-heading`: For each heading (h1-h6), the number of words whose computed color differs from the heading's base ink color; the maximum over all headings; unit: words.