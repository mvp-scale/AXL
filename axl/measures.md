# AXL measures (`axl:`)

Measures no standard names (no CSS property, WCAG criterion or Lighthouse audit expresses them), proposed while expressing the harvested statements as rules.
Status: **proposed, not yet implemented**: a rule using one is *measurable*, not yet *checked automatically*. Each will be implemented once in `axl.py` and proven on Northstar (fails before, passes after) in phase 4; duplicates will be merged then.

| Measure | Definition | Class |
|---|---|---|
| `axl:above-fold-images-without-preload` | Count of img elements in the initial viewport that have no link rel=preload and are not the fetchpriority=high LCP element. | perf |
| `axl:accent-chroma` | Highest OKLCH chroma among accent colours on the page; unitless 0-0.4. | color |
| `axl:accent-coverage` | Share of the viewport area (first screen, each viewport) painted with accent-coloured fills, as a percentage; accent = non-neutral colour from the primary accent hue. | color |
| `axl:accent-hues` | Number of distinct accent hues on the page: hue of each non-neutral (OKLCH chroma >= 0.04) fill or text colour, clustered in 30-degree bins, excluding semantic status colours; count. | color |
| `axl:accent-in-violet-band` | Number of accent colours on the page with OKLCH hue between 250 and 320 degrees; count. | color |
| `axl:accent-words-per-heading` | Greatest number of words in any single heading coloured with the accent colour; unit: words. | type |
| `axl:all-pill-buttons` | 1 if every button on the page has a computed border-radius of at least 999px or 50%, otherwise 0. | surface |
| `axl:anchor-hue-shift-between-modes` | Largest OKLCH hue difference in degrees between the anchor (brand/accent) colour in light mode and in dark mode; degrees. | color |
| `axl:animated-blur-radius-max` | Largest blur radius in px, in filter or backdrop-filter, on any element while it animates. | perf |
| `axl:animated-gif-images` | Count of img elements whose source is an animated GIF. | perf |
| `axl:animation-primitives` | Count of distinct animation types (counter, hover-lift, marquee, etc.) running on the page; count. | motion |
| `axl:apca-lc` | Lowest APCA lightness contrast (Lc, absolute) of text against its background across the matched elements; Lc. | color |
| `axl:audio-contexts` | Count of AudioContext instances created by the page. | perf |
| `axl:autoplay-video-missing-attrs` | Count of video elements with autoplay that lack any of muted, loop or playsinline. | perf |
| `axl:backdrop-blur-containers` | Count of elements with a blurring backdrop-filter and a translucent background. | surface |
| `axl:backdrop-blur-on-scrolling` | Count of elements with a backdrop-filter that are neither position:fixed nor position:sticky. | surface |
| `axl:background-lightness` | OKLCH lightness of the page's computed background colour in light theme; percentage. | color |
| `axl:bg-without-color` | Number of style rules that set background-color without also setting color; count. | color |
| `axl:blink-marquee-elements` | Count of blink and marquee elements in the document; count. | motion |
| `axl:border-width-state-shift` | Largest difference in px between a field's default border-width and its border-width in hover, focus, error and disabled states. | surface |
| `axl:box-shadow-layers` | Largest number of comma-separated layers in the computed box-shadow of any matching element. | surface |
| `axl:buried-raster-count` | Count of raster background images sitting under a gradient wash of alpha above 0.9, or on an element with near-zero opacity. | surface |
| `axl:canvas-dpr-max` | Largest device-pixel-ratio a canvas renders at (canvas pixel width divided by CSS width). | perf |
| `axl:card-count` | Number of ui:card elements on the page. | surface |
| `axl:cdn-origins-without-preconnect` | Count of distinct third-party asset/CDN origins the page loads from that lack a link rel=preconnect. | perf |
| `axl:characters-per-heading` | Maximum, over heading elements, of the number of characters in the heading text. Unit: characters. | content |
| `axl:cliche-words` | Count of occurrences in rendered text of the words and phrases named by the source statements: elevate, seamless, unleash, next-gen, game-changer, delve, tapestry, leverage, synergy, robust, cutting-edge, revolutionary, revolutionize, unlock, supercharge, effortlessly, journey, ecosystem, platform, transform your. Unit: count. | content |
| `axl:color-saturation` | Highest HSL saturation among chromatic (non-neutral) fill and accent colours on the page; percentage. | color |
| `axl:colored-glow-shadows` | Number of box-shadow or text-shadow values that are a zero-offset chromatic halo, or any coloured blurred shadow on a dark background; count. | color |
| `axl:concentric-radius-error` | For every rounded element nested in a rounded parent, the absolute difference in px between the parent radius and (child radius + padding between them), ignoring pairs whose padding is over 24px; the maximum over the page. | surface |
| `axl:contrast-gain` | Contrast ratio of the matched state (hover, active, focus) minus contrast ratio of the same element at rest, text or boundary against its background; ratio points. | color |
| `axl:count-up-duration` | Duration of number count-up animations on the page; ms. | motion |
| `axl:cta-wobbles` | Count of call-to-action buttons with a wobble animation; page-wide; count. | motion |
| `axl:dark-scheme-declared` | 1 when the root declares color-scheme including dark (or a prefers-color-scheme: dark stylesheet exists), else 0. | color |
| `axl:dash-double-hyphen` | Count of "--" sequences in rendered text that should be an em dash or en dash; unit: count. | type |
| `axl:decorative-status-dots` | Count of live or status dots that are not bound to a real semantic state (an aria-live or status role region). Unit: count. | content |
| `axl:display-step-ratio` | Computed font-size of display text divided by the next-largest font-size in use on the page; unit: ratio (x). | type |
| `axl:distinct-border-radii` | Number of distinct computed border-radius values (px) across all elements with a non-zero radius on the page. | surface |
| `axl:distinct-icon-grids` | Number of distinct viewBox sizes across ui:icon SVG elements on the page. | surface |
| `axl:distinct-shadow-levels` | Number of distinct computed box-shadow values (other than none) used for elevation across the page. | surface |
| `axl:distinct-stroke-widths` | Number of distinct computed stroke-width values (px) across ui:icon elements on the page. | surface |
| `axl:document-write-calls` | Count of document.write calls executed while loading the page. | perf |
| `axl:eager-below-fold-images` | Count of img elements whose box starts below the initial viewport fold and lack loading=lazy. | perf |
| `axl:elevation-lightness-step` | In dark mode, the smallest difference in lightness (percentage points) between a surface and the surface one elevation level below it. | surface |
| `axl:ellipsis-three-dots` | Count of "..." (three periods) sequences in rendered text that should be the ellipsis character U+2026; unit: count. | type |
| `axl:em-dashes-per-paragraph` | Maximum, over paragraphs of rendered text, of the count of em dash characters (U+2014 or --). Unit: count. | content |
| `axl:emoji-count` | Number of emoji characters in the rendered text, markup and alt text of the matching elements. | surface |
| `axl:emoji-in-text` | Count of emoji characters in rendered text and alt text of the element (not counting emoji used as icons, which axl:emoji-as-icons measures). Unit: count. | content |
| `axl:empty-image-src` | Count of img elements whose src is empty, missing or a placeholder value, so they render as a broken-image box. Unit: count. | content |
| `axl:en-dash-separators` | Count of en dash characters (U+2013) in rendered text used as a separator, including date and number ranges. Unit: count. | content |
| `axl:exclamation-marks` | Count of exclamation marks in the rendered text of the element. Unit: count. | content |
| `axl:exit-to-enter-duration-ratio` | Exit animation duration divided by the enter duration of the same element; ratio. | motion |
| `axl:eyebrow-share-of-sections` | Number of uppercase tracked micro-labels (eyebrows) placed above section headings divided by the number of sections, the hero counting as one; unit: percent. | type |
| `axl:eyebrows-per-section` | Number of eyebrow labels (short text above a heading) divided by the number of page sections, hero counted as a section. Unit: ratio. | content |
| `axl:fixed-size-text-containers` | Count of elements containing text whose width or height is fixed in px (or overflow hidden with a fixed size), so the text cannot grow when its content gets longer. Unit: count. | content |
| `axl:flashes-per-second` | Maximum number of luminance flashes in any one second of rendered animation; count per second. | motion |
| `axl:font-size-vw-only` | Count of font-size declarations whose value is a bare vw length, with no rem/em/px term or clamp() bound; unit: count. | type |
| `axl:generic-labels` | Count of buttons whose visible label is one of: OK, Submit, Click here, Continue, Yes, No. Unit: count. | content |
| `axl:gradient-count` | Number of elements on the page whose computed background-image contains a gradient; count. | color |
| `axl:gradient-stops` | Maximum number of colour stops in any single CSS gradient (linear, radial, conic) found in computed background-image on the page; count. | color |
| `axl:gray-on-colored-background` | Number of text elements whose colour is a neutral gray (OKLCH chroma < 0.02) on a background of a chromatic colour (chroma >= 0.04); count. | color |
| `axl:h1-line-count` | Greatest number of rendered lines taken by the page h1 across the tested viewport widths; unit: lines. | type |
| `axl:h1-word-count` | Number of words in the page h1; unit: words. | type |
| `axl:hard-offset-shadows` | Count of elements with a box-shadow layer that has a non-zero offset and zero blur. | surface |
| `axl:hardcoded-colors` | Count of colour values (hex, rgb(), hsl(), oklch() literals or named colours) written in author CSS or inline styles outside custom-property definitions, i.e. not referenced through var(). Unit: count. | content |
| `axl:heading-body-size-ratio` | Computed font-size of the dominant heading (h1-h6, largest level in use) divided by the computed font-size of body text; unit: ratio (x). | type |
| `axl:heading-body-weight-gap` | Absolute difference between the computed font-weight of the dominant heading (most common h1-h6 weight) and of body text; unit: font-weight units (e.g. 300). | type |
| `axl:headings-crowded-above` | Count of headings (h1-h6) whose rendered space above (margin/padding plus gap to the previous block) does not exceed the rendered space below them; unit: count. | type |
| `axl:hero-version-labels` | Count of version or status labels such as V0.6, v2.0, BETA, ALPHA, EARLY ACCESS, INVITE-ONLY PREVIEW in the hero area. Unit: count. | content |
| `axl:hierarchy-step-ratio` | Smallest ratio between adjacent hierarchy levels (display, heading, body, caption) in their strongest signal (size, weight, contrast, surface area or position); unit: ratio (x). | type |
| `axl:icon-size-off-grid` | Count of ui:icon elements whose rendered size in px is not one of 16, 20, 24 or 32. | surface |
| `axl:icons-not-currentcolor` | Count of ui:icon elements whose computed fill and stroke are not currentColor (a single primary-CTA icon excepted). | surface |
| `axl:identical-shadow-count` | Largest number of elements on the page sharing the same computed box-shadow or drop-shadow value. | surface |
| `axl:inline-base64-images` | Count of base64 data: image URIs in HTML or CSS. | perf |
| `axl:lazy-loaded-lcp-element` | Count (0 or 1) of the page's largest-contentful-paint element carrying loading=lazy, for img or video. | perf |
| `axl:lcp-fetchpriority` | Value of the fetchpriority attribute on the page's LCP element (auto, high or low). | perf |
| `axl:marquees` | Count of horizontally scrolling looping text strips on the page; count. | motion |
| `axl:max-dom-depth` | Maximum element nesting depth in the document, as a count of levels. | perf |
| `axl:meta-labels` | Count of label or eyebrow texts of the form SECTION 01, QUESTION 05, 00 / INDEX, 01 / 4, 01 · About, 02 / Process, or ABOUT US used as a section label. Unit: count. | content |
| `axl:middle-dots-per-line` | Greatest number of middle-dot (U+00B7) separators in any single line of rendered text; unit: count. | type |
| `axl:missing-social-meta-tags` | Count of missing tags among og:image, og:title, og:description and twitter:card in the head. | perf |
| `axl:mutation-response-time` | Milliseconds for POST, PATCH and DELETE requests to complete, worst case, measured in the page. | perf |
| `axl:nested-cards` | Count of ui:card elements that have another ui:card as an ancestor, across the page. | surface |
| `axl:nested-radius-larger-than-parent` | Count of rounded elements whose border-radius is larger than their rounded parent's border-radius. | surface |
| `axl:neutral-chroma` | Lowest OKLCH chroma among neutral colours (surface, border, ink) on the matched elements, where neutral means chroma < 0.04; unitless. | color |
| `axl:non-inline-svg-icons` | Count of ui:icon elements that are not inline <svg> (img src references, icon fonts, package components). | surface |
| `axl:non-woff2-fonts` | Count of web font files whose format is not woff2. | perf |
| `axl:null-literals` | Count of visible text values that are N/A, null, undefined or NaN. Unit: count. | content |
| `axl:oklch-color-share` | Share of colour declarations in author CSS written with oklch(). Unit: percent. | content |
| `axl:oklch-colors` | Share of declared colour values written in oklch() (a hex fallback does not count against); percentage. | color |
| `axl:persistent-will-change-elements` | Count of elements whose computed will-change is not auto while no animation or transition is running on them. | perf |
| `axl:physical-direction-properties` | Count of declarations in the page's stylesheets that use a physical direction property (margin-left, margin-right, padding-left, padding-right, border-left, border-right, left, right) where a logical equivalent exists. Computed on the whole page; unit is a count. | layout |
| `axl:placeholder-text` | Count of occurrences in rendered text of placeholder copy: lorem ipsum or other placeholder Latin, and generic placeholder names such as John Doe, Jane Smith, Acme Corp. Unit: count. | content |
| `axl:purple-blue-gradients` | Number of gradients on the page whose stops span purple/indigo/violet (OKLCH hue 250-320) to blue, cyan, pink or magenta; count. | color |
| `axl:quotes-typographic` | Share of quotation marks and apostrophes in rendered text that are typographic (curly) rather than straight ASCII; unit: percent. | type |
| `axl:raster-icons` | Count of ui:icon elements that are raster images (png, jpg, webp, gif) rather than SVG. | surface |
| `axl:raw-color-values` | Number of colour literals (hex, rgb, hsl, oklch) used in style rules outside custom-property (token) definitions; count. | color |
| `axl:raw-timestamps` | Count of visible text values that are raw machine timestamps (Unix epoch numbers, unformatted ISO strings). Unit: count. | content |
| `axl:real-images` | Count of non-decorative img, picture and video elements that show real content (alt text present and not a placeholder). Unit: count. | content |
| `axl:rendered-items` | Count of item rows (li, tr or role listitem/row) present in the DOM within one list or table. | perf |
| `axl:request-debounce` | Milliseconds a text field waits after the last keystroke before it sends its request. | perf |
| `axl:rows-with-top-and-bottom-borders` | Count of list items or table rows whose computed border-top-width and border-bottom-width are both above 0. | surface |
| `axl:scroll-cues` | Count of scroll cue elements: text such as Scroll to explore or Swipe down, scroll arrow icons, and bouncing chevrons. Unit: count. | content |
| `axl:scroll-event-listeners` | Count of scroll event listeners registered on window, document or scrolling elements. | perf |
| `axl:scroll-reveals-per-section` | Count of scroll-triggered reveal animations within each section; count. | motion |
| `axl:separator-dots-per-line` | Maximum, over text lines, of the count of middle dot separator characters (U+00B7) in the line. Unit: count. | content |
| `axl:series-luminance-gap` | Smallest OKLCH lightness difference between adjacent series colours in a chart; percentage points. | color |
| `axl:shadow-max-alpha` | Largest alpha (0-1) of any colour in any computed box-shadow layer on the page. | surface |
| `axl:skeleton-show-delay` | Milliseconds between a loading state starting and its skeleton placeholder becoming visible, per ui:skeleton. | perf |
| `axl:soft-shadows` | Count of box-shadow layers with a non-zero blur radius on the matching elements. | surface |
| `axl:spelled-out-numbers` | Count of numbers written out as words (for example five, two hundred forty-five) in rendered text where a numeral would be used. Unit: count. | content |
| `axl:split-text-elements` | Count of per-character or per-word wrapper spans generated inside the element (text splitting). | perf |
| `axl:stagger-delay` | Delay between consecutive sibling animation-delay values in a staggered sequence; ms. | motion |
| `axl:stagger-total-duration` | Sum of staggered delays across one sequence; page-wide; ms. | motion |
| `axl:staggered-entrances-per-section` | Count of staggered entrance sequences within each section; count. | motion |
| `axl:static-blur-radius-max` | Largest blur radius in px, in filter or backdrop-filter, on any element at rest. | perf |
| `axl:substrate-modes` | Number of distinct light/dark background substrates used by top-level page sections (light if OKLCH L >= 60%, else dark); count. | color |
| `axl:theme-color-match` | 1 when <meta name=theme-color> equals the page background colour (per colour scheme), else 0. | color |
| `axl:third-party-asset-urls` | Count of image, logo, video, icon and font URLs that point to a different origin than the page. | perf |
| `axl:translation-space-budget` | Smallest, over elements with text, of (available inline size of the container / inline size of the text as rendered) minus 1, as a percentage: the spare room left for longer translations. | content |
| `axl:translucent-fills` | Count of matching elements whose computed background-color has alpha below 1. | surface |
| `axl:unglued-units` | Count of number-plus-unit pairs (e.g. 10 MB, 5 min) in rendered text separated by an ordinary space instead of a non-breaking space U+00A0; unit: count. | type |
| `axl:unitless-line-height` | Share of text elements whose line-height is declared without a unit; unit: percent. | type |
| `axl:unused-font-files` | Count of web font files (family + weight) downloaded but never used by rendered text. | perf |
| `axl:varied-grid-cells` | For every multi-cell grid or bento on the page, the number of cells whose background is an image, gradient, pattern or tint rather than plain surface colour; the minimum over all such grids. | surface |
| `axl:videos-without-poster` | Count of video elements with no poster attribute. | perf |
| `axl:words-per-heading` | Maximum, over heading elements, of the number of words in the heading text. Unit: words. | content |
