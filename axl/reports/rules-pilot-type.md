# Type — rules for review

123 tweaks → **22 rules**, 93 settings. Auto = a script can check it on any site. Ask = a yes/no question for a person or agent.

## Clear type hierarchy  `type.hierarchy`

Levels of text are told apart by size, weight and emphasis, so the reader sees what matters first.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | auto | font-size step ratio between heading and body >= 1.25x | 1.25x (impeccable); 1.5x (ui-craft) | Strengthen heading contrast |
| h2 | auto | font-weight heading weight differs clearly from body weight | 200 vs 800 (anthropic); 300 or 700+ (hallmark) | extreme weight and size contrast in type, Make differences decisive, not timid |
| body | ask | Is it obvious at a glance which text is the headline, which is supporting, and which is fine print? | — | hierarchy through weight, size and space rather , Order emphasis by importance, one dominant message on posters, Number-first hierarchy in metrics |
| display | ask | Is the headline type treated as a deliberate design element rather than a neutral label? | — | make headline type an active design element |
| h3 | ask | Does a large numeric headline figure come with a worded headline that completes it? | — | numeric hero paired with worded headline |

## Size scale  `type.size-scale`

Text sizes come from one small, consistent scale and scale sensibly across screen widths.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | font-size <= 6 distinct sizes | 5 sizes (hallmark); 4-6 steps (ui-craft); 6-8 sizes (deslop); ratio 1.25 (hallmark) | Use one fixed type scale |
| display | ask | Is one display scale chosen decisively rather than splitting the difference between sizes? | — | Pick one hero scale decisively |
| h1 | ask | Is display type sized with clamp() or a similar bounded method rather than vw alone? | — | Never use vw alone in font-size, responsive display type for marketing |
| mobile | ask | Do large type sizes shrink on small screens, with small sizes staying readable? | — | Shrink large type faster on mobile, Fluid type scale across viewports |

## Display size limits  `type.display-size`

Headline type is large enough to lead but never so large that it crowds the page.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | auto | font-size <= 5.5rem | 5.5rem (hallmark); 6rem (hallmark) | cap display size at 5.5rem, cap hero headline size, Keep headlines short at display size, Keep first heading restrained |
| display | auto | font-size display step >= 2.5x the next step | 2.5x to 4x (ui-craft) | Display step 2.5-4x above body step |
| page | ask | Does the main headline stay within three lines at common widths? | 3 lines (taste-skill); 2 lines (taste-skill) | Keep hero headline to 2-3 lines |
| card | ask | Does the main headline sit in a container wide enough that it does not wrap into a narrow stack? | — | Give hero headline a wide container |

## Minimum text size  `type.min-size`

Text is at least a minimum size for its role.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | font-size >= 16px | 16px (deslop, impeccable, ui-craft); 14px (deslop, hallmark, impeccable, taste-skill); 12px (impeccable) | Set body text to 16px |
| page | auto | font-size >= 18px for long-form reading | 18px (ui-craft) | Long-form body text 18px |
| input | auto | font-size >= 16px on mobile | 16px (ui-craft, vercel) | Inputs 16px minimum on mobile |
| button | auto | font-size between 14px 17px | 14-17px (ui-craft) | Button label size centered on whole pixels |
| small | ask | Is all text large enough to read comfortably at normal viewing distance, with no text that feels too small? | — | Keep text large and sparse, custom fonts must stay legible |

## Line height  `type.line-height`

Line height is set by text role: open for body copy, tight for large headings.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | line-height >= 1.5 | 1.5 (deslop, impeccable, oneredoak); 1.6 (taste-skill); 1.5-1.65 (ui-craft); 1.3 floor (impeccable) | Body line height 1.5 |
| h1 | auto | line-height <= 1.2 | 0.95-1.05 (hallmark); 1.05-1.2 (ui-craft); 1.1 minimum (taste-skill) | Tight heading line height, Reserve line height for italic descenders |
| label | auto | line-height between 1.3 1.4 | 1.3-1.4 (ui-craft) | Line height by text size |

## Line length  `type.line-length`

Lines of running text are kept to a comfortable number of characters.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | measure-ch between 45ch 75ch | 65ch (hallmark, taste-skill, ui-craft); 45-75ch (hallmark); 65-75ch (impeccable); 80ch max (anthropic) | Improve reading measure, Cap lines at 65 characters |
| page | ask | Is the main text column capped to a readable width rather than running the full page width? | — | Constrain content measure |

## Letter spacing  `type.letter-spacing`

Letter spacing is tuned per role: tighter for large type, looser for small caps, never crushed.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| display | auto | letter-spacing >= -0.04em | -0.02em (deslop, hallmark, impeccable); -0.03em (hallmark); -0.04em (impeccable, ui-craft); -0.06em (taste-skill) | Tune display tracking |
| label | auto | letter-spacing between 0.05em 0.14em for small caps labels | 0.08-0.14em (hallmark); 0.05em max on body (impeccable) | loosen tracking on small caps labels, Small monospaced labels with wide tracking |

## Font weights  `type.font-weight`

Few font weights are used, none too light, each with a clear job.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | font-weight-count <= 3 | 2 (ui-craft); 2-3 (impeccable, ui-craft); 4 (oneredoak, taste-skill) | Limit to few font weights, Use medium and semibold weights for subtle hiera |
| small | auto | font-weight >= 400 | — | Avoid light font weights |
| button | ask | Do button and action labels carry more weight than surrounding body text? | — | Strengthen action typography |

## Typeface choice and count  `type.typefaces`

Few typefaces are used, each chosen on purpose rather than by default.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | font-family-count <= 2 | 2 (anthropic, apple-hig, ui-craft); 3 (hallmark, ui-craft) | Use at most two typefaces |
| display | ask | Is any extra accent typeface limited to two places on the page? | — | limit outlier typeface to two slots, outlier face in at most two slots |
| h1 | ask | Is the main typeface a deliberate choice rather than an overused default (Inter, Roboto, Open Sans, Arial, system-ui)? | — | Replace generic default fonts |
| mobile | ask | If a native system font is used, is that a deliberate choice for a native feel? | — | use system font stack for native feel |
| label | ask | Does the font stack include a practical fallback for any commercial or custom face? | — | keep practical fallback font stack |

## Font pairing and style fit  `type.pairing`

Typefaces are paired by role and suit the kind of product.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| display | ask | Is a distinctive display face paired with a separate, plainer body face? | — | Pair display and body faces |
| h2 | ask | Are paired faces from clearly different classes rather than near-identical families? | — | Pair fonts from different classes |
| h1 | ask | Is the display face limited to headlines, with a neutral face for body text? | — | Limit display faces to headlines, Neutral sans for body, never display face |
| body | ask | Does the chosen type class match the brand adjectives, and was it tested in real mockups? | — | Match type class to brand adjectives, Test font pairs in real mockups |
| page | ask | Do the chosen faces hold up across every medium the design ships in? | — | Choose faces that hold across media |
| dashboard | ask | Do software or dashboard interfaces use sans-serif faces only? | — | Sans-serif pairings only for dashboards, Serif only for editorial designs |
| nav | ask | Is any serif use explicitly justified by the design brief? | — | Serif only when explicitly justified |
| card | ask | If the theme calls for a single style (rounded sans, lowercase sans), is it followed with no serif? | — | rounded sans only, lowercase sans display, no serif, Use monolithic heavy sans with visible grid line |

## Alignment and number layout  `type.alignment`

Text is aligned for easy scanning, and columns of numbers line up.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | justify == left aligned (no justified text without hyphenation) | — | Align to the left |
| h1 | ask | Is hyphenation on wherever text is justified in narrow columns? | — | Enable hyphenation for narrow columns |
| page | ask | Are the most important words at the start of headings and lines? | — | Front-load headings, left-align body (F-pattern) |
| table | auto | tabular-nums == on for aligned numbers | tabular-nums (vercel) | Use tabular numerals |

## Capitalization  `type.capitalization`

Case is used consistently: sentence case for headings, no all-caps body text.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | auto | all-caps == off for headings, nav and buttons | — | No all-caps on headings, nav, buttons, Use sentence case for headings, Sentence case headlines |
| body | auto | all-caps == off for running text | — | no all-caps or justified body text |
| label | ask | Are uppercase or mono labels reserved for small meta text? | — | mono uppercase labels for meta |
| display | ask | If headlines use a single case treatment (all lowercase or all caps), is it applied to every headline? | — | all-caps headlines, lowercase display headlines |

## Eyebrow labels and kickers  `type.eyebrows`

Small labels above headings are rationed and earn their place.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h2 | ask | Are eyebrow labels used on no more than one in three sections? | 1 per 3 sections (ui-craft) | Ration eyebrow labels, sparing eyebrow labels |
| page | ask | Is the page free of section eyebrows unless numbering is truly needed? | — | no section eyebrows or number kickers by default |
| h3 | ask | Are small numbered section labels and oversized index numerals avoided? | — | no tiny numbered section labels, giant faded numeral index behind section heads |

## Italics  `type.italics`

Italic is used only for inline emphasis in body text, never in headings.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | auto | italic == normal in headings | — | no italic headings, no italic emphasis, Avoid br-broken italic headline splits |
| body | auto | italic only for inline emphasis in running text | — | italics only for inline body emphasis |

## Headline emphasis  `type.headline-emphasis`

Emphasis inside a headline is sparing and made with weight, colour or the same family.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | ask | Is at most one word in a headline set apart in accent colour? | 1 word (hallmark) | one accent-colored verb in headline |
| h2 | ask | Is headline emphasis varied across sections rather than always one highlighted word? | — | vary headline emphasis |
| display | ask | Is emphasis within a headline made with weight or italic of the same family, not a different typeface? | — | Emphasize in headlines with same family, Emphasize headline words with same-font italic o |
| card | ask | Do highlighter bands behind text follow the text across line breaks? | — | clipped background text highlighter |
| nav | ask | Are bold, italic and highlight styles kept out of structural UI? | — | emphasis styling only in content areas |

## Text effects and rendering  `type.text-effects`

Text is rendered flat and clean, with decorative effects checked and font features set deliberately.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | ask | Is text flat (2D) without added shadows for contrast? | — | prefer flat 2D text, no shadows on text for contrast |
| h1 | ask | Is rotated or vertical text avoided unless the brief calls for it? | — | Avoid vertical rotated text |
| display | ask | Have decorative effects on text been checked for position and size? | — | verify decorative text effects position |
| image | ask | Are small images embedded inside headings avoided unless they are a deliberate design move? | — | Embed pill images inside headings |
| page | ask | Is antialiased text smoothing set without overriding the chosen font family? | — | Enable antialiased text rendering |
| button | ask | Is font synthesis off so missing weights show up during development? | — | Disable font synthesis |
| label | ask | Are OpenType features set on purpose (kerning on, ligatures off in UI)? | — | Enable OpenType features |
| link | ask | Do underlines take their offset and thickness from the font? | — | Underline offset and thickness from font metrics |

## Wrapping and truncation  `type.text-wrap`

Text wraps cleanly and is truncated only where the reader can still get the full content.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| h1 | auto | text-wrap == balance | — | Balance heading wrapping |
| body | auto | text-wrap == pretty | — | Prevent orphans in paragraphs |
| display | ask | Do long words in display text wrap instead of overflowing? | — | allow long words in headings to wrap |
| caption | ask | Is text-wrap balance and pretty skipped on very long text? | — | skip text-wrap balance and pretty on long text |
| card | ask | Is truncated text given a title tooltip and a set max width? | — | Truncate overflowing text with title tooltip |
| table | ask | Is truncation avoided in scrolling regions unless the full text opens elsewhere? | — | avoid truncating text in scroll regions |
| mobile | ask | Is truncation kept to a minimum as text size grows? | — | minimise truncation at larger text sizes |

## User text scaling  `type.user-scaling`

Text follows the reader's size and spacing settings and stays live text.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | ask | Can text be resized to 200 percent without loss of content, using relative units? | 200 percent (wcag22) | Support user font size setting |
| h1 | ask | Does content survive user overrides of line, paragraph, letter and word spacing? | 1.5x line, 2x paragraph, 0.12 letter, 0.16 word (deslop) | Survives user text spacing |
| image | ask | Is text shown as live text rather than as images of text? | — | Use live text, not images |

## Typographic punctuation  `type.punctuation`

Punctuation uses the proper characters.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | quotes-typographic == curly quotes and apostrophes | — | Use real typographic quotes |
| caption | ask | Are true ellipsis and dash characters used instead of three dots or double hyphens? | — | Use true ellipsis and dashes |
| label | ask | Are units, shortcuts and brand names kept together with non-breaking spaces? | — | Keep units with non-breaking space |
| nav | ask | Are middle-dot separators used sparingly? | — | Ration middle-dot separators |

## Font loading  `type.font-loading`

Web fonts load without invisible text or layout shift.  _(see perf.font-loading)_

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | auto | font-display in swap optional | swap (impeccable, taste-skill, vercel); optional (deslop, impeccable) | Set font-display swap |
| h1 | ask | Do fallback fonts match the web font metrics to avoid layout shift? | — | Match fallback font metrics |
| h2 | ask | Are critical fonts preloaded? | — | Preload critical fonts |
| h3 | ask | Are fonts subset to the characters and weights actually used? | — | Subset web fonts |
| display | ask | Are variable fonts used where several weights or widths are needed? | — | Use one variable font file |

## Page language  `type.page-language`

The page declares its language.  _(see access.page-language)_

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| page | auto | lang html has a valid lang attribute | — | Set page language |

## Text blocks  `type.text-blocks`

Paragraphs, headings and quotes are spaced and styled so blocks read easily.

| Setting | Check | Test / question | What sources say | Tweaks folded in |
|---|---|---|---|---|
| body | ask | Are long paragraphs broken up and paragraph boundaries marked in only one way? | — | Separate paragraphs |
| h2 | ask | Is there more space above a heading than below it? | — | Separate heading and body |
| h3 | ask | If a drop cap is used, is it styled to match the display face? | — | Drop cap on first paragraph |
| card | ask | Are pull quotes and blockquotes styled distinctly from body text? | — | Styled pull quotes, Accent-bordered serif blockquote |
| label | ask | Do mixed text sizes on one line share a baseline? | — | Align mixed text sizes on shared baseline |
| button | ask | Is text vertically centred in pills and buttons with trimmed half-leading? | — | Trim text box half-leading in pills and buttons |
