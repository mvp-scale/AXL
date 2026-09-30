# super polish

**198 rules · 60 measurable · 138 questions for a person or agent.**
Every rule is written in standard terms (ARIA roles, CSS properties, WCAG 2.2, Lighthouse); quote IDs look up the exact source statement on the AXL site.

## Rules

### Type

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 1 | Body text size is at least 16px (sources also say: 14px, 13px-14px, 17pt) | `text:body font-size >= 16px` | deslop:b4223e, deslop:d9e5d8, deslop:f6b6cc, impeccable:a2b590, impeccable:b3b1d9, impeccable:e6d3a0 +8 |
| 2 | Are low-priority labels and metadata visibly quieter than the headline and core message? | `text:caption ask "Are low-priority labels and metadata visibly quieter than the headline and core message?"` | claw-design:05d8d3, claw-design:5382f6, claw-design:674bc6, claw-design:729bad, claw-design:a55f9e, claw-design:bd9b4c +4 |
| 3 | Does the work keep the product's existing type system? | `text:* ask "Does the work keep the product's existing type system?"` | feel-better:2b36be, feel-better:98b55b, impeccable:da6546, ui-craft:3c6573 |
| 4 | Do display sizes shrink one step below 40rem? | `aria:heading ask "Do display sizes shrink one step below 40rem?"` | hallmark:892023 |
| 5 | Headings heading body weight gap is at least 300 (sources also say: 600) | `aria:heading axl:heading-body-weight-gap >= 300` | hallmark:bf8097, anthropic:3e8b34 |
| 6 | Headings heading body size ratio is at least 1.25 (sources also say: 3) | `aria:heading axl:heading-body-size-ratio >= 1.25` | impeccable:c77a42, anthropic:3e8b34 |
| 7 | Whole page hierarchy step ratio is at least 1.5 | `page axl:hierarchy-step-ratio >= 1.5` | ui-craft:b36822 |
| 8 | Can a viewer separate headline, evidence and footnote layers at a glance, with the eye landing on things in order of importance? | `page ask "Can a viewer separate headline, evidence and footnote layers at a glance, with the eye landing on things in order of importance?"` | claw-design:05d8d3, claw-design:1f1a14, claw-design:729bad, claw-design:decd57, deslop:3478de, ui-craft:4b5f21 |
| 9 | Body text lines are between 45 75 characters (sources also say: 65) | `text:body axl:chars-per-line between 45 75` | deslop:7f37db, deslop:cf0256, hallmark:2404b3, hallmark:31f7b5, hallmark:38f635, hallmark:d8592a +5 |
| 10 | All text uses between 2 3 typefaces (sources also say: 2, 2 3) | `text:* axl:distinct-font-families between 2 3` | deslop:7346e0, hallmark:6bae6c, hallmark:97e2b5, ui-craft:35600d, ui-craft:363ccb, anthropic:1f9f6e +4 |
| 11 | All text typeface is never "Inter, Roboto, Open Sans" (sources also say: Inter, Roboto, Open Sans, Times New Roman, Georgia, Garamond, Palatino) | `text:* font-family !contains "Inter, Roboto, Open Sans"` | anthropic:82ff46, deslop:8ce027, taste-skill:9b813d, taste-skill:b143dd, taste-skill:cb6237, anthropic:d65725 +4 |
| 12 | Body text typeface includes "Inter, Geist" (sources also say: Inter, Geist) | `text:body font-family contains "Inter, Geist"` | taste-skill:ed5b24, ui-craft:458e7f, ui-craft:f4239b |
| 13 | Does the page pair a distinctive display face with a separate body face? | `page ask "Does the page pair a distinctive display face with a separate body face?"` | deslop:7346e0, hallmark:263508, hallmark:d2a963, hallmark:db7a27, unslop:114f83, unslop:6a0102 +1 |
| 14 | Does the wordmark use a different display face than the body? | `aria:banner ask "Does the wordmark use a different display face than the body?"` | hallmark:9a2390, hallmark:a6f68f, hallmark:d7bf65 |
| 15 | All text number style includes tabular-nums | `text:* font-variant-numeric contains tabular-nums` | deslop:28d758, feel-better:04dde9, feel-better:f011fe, taste-skill:0d6ae9, ui-craft:0e3cd8, ui-craft:79ea78 +2 |
| 16 | Headings line wrapping is balance | `aria:heading text-wrap == balance` | feel-better:8a265a, vercel:1c1518, vercel:2b0eb0 |
| 17 | Are paragraphs separated by spacing or first-line indentation, but not both? | `text:body ask "Are paragraphs separated by spacing or first-line indentation, but not both?"` | impeccable:5f8f0b |
| 18 | Do font sizes follow one stated modular ratio? | `page ask "Do font sizes follow one stated modular ratio?"` | deslop:b4223e, hallmark:a7a2af |
| 19 | Are font sizes set in rem/em or from scale variables? | `text:* ask "Are font sizes set in rem/em or from scale variables?"` | claw-design:c709d2 |

### Color & theming

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 20 | Does the UI offer a higher-contrast colour scheme when the system Increase Contrast setting is on? | `media:forced-colors ask "Does the UI offer a higher-contrast colour scheme when the system Increase Contrast setting is on?"` | apple-hig:02dbe1, apple-hig:cc15ca |
| 21 | Is text placed over imagery kept readable with an overlay, scrim or backdrop? | `text:* ask "Is text placed over imagery kept readable with an overlay, scrim or backdrop?"` | deslop:aa2dad, taste-skill:0c0457, taste-skill:167905, taste-skill:2e074a |
| 22 | All text gray on colored background is 0 | `text:* axl:gray-on-colored-background == 0` | deslop:da5281, impeccable:5091ac, impeccable:a2a3e9, impeccable:eb0cee, ui-craft:4a4ea6 |
| 23 | Whole page raw color values is 0 | `page axl:raw-color-values == 0` | anthropic:a1a932, claw-design:71c9b4, hallmark:4f55d3, impeccable:8c6e68, shadcn:219aca, shadcn:2bc660 +3 |
| 24 | Are colour tokens named by role rather than by raw value? | `page ask "Are colour tokens named by role rather than by raw value?"` | deslop:963516, deslop:f147e4, hallmark:19cdeb, impeccable:2cdeda, impeccable:73f1bf, impeccable:c00b5b +4 |
| 25 | Do theme changes remap semantic tokens only, leaving primitive values untouched? | `page ask "Do theme changes remap semantic tokens only, leaving primitive values untouched?"` | deslop:33bad5, impeccable:8c6e68, ui-craft:5b92e0, ui-craft:6901e2 |
| 26 | Are system colours used where they already define the variants needed? | `page ask "Are system colours used where they already define the variants needed?"` | apple-hig:56955e |
| 27 | Are the strongest colour, weight and contrast reserved for the elements that matter most (primary action, headline, KPI)? | `page ask "Are the strongest colour, weight and contrast reserved for the elements that matter most (primary action, headline, KPI)?"` | claw-design:49fb14, claw-design:51e026, claw-design:e3817e, impeccable:ab2c7f, impeccable:cf7c3f |
| 28 | Are design tokens declared once as named CSS custom properties at :root? | `page ask "Are design tokens declared once as named CSS custom properties at :root?"` | anthropic:a1a932, hallmark:107394, hallmark:19f318, hallmark:4cb76d, hallmark:cb516e, shadcn:6c0381 |
| 29 | Does the work keep the brand's existing palette and color logic? | `page ask "Does the work keep the brand's existing palette and color logic?"` | impeccable:061c9c, taste-skill:520450, taste-skill:631852, taste-skill:a63ade, ui-craft:e56089, ui-craft:e6b74e |
| 30 | Do partner brand accents stay from overriding backgrounds and text colors? | `page ask "Do partner brand accents stay from overriding backgrounds and text colors?"` | openai:874eb8 |
| 31 | Are buttons ranked by importance rather than colored by meaning? | `aria:button ask "Are buttons ranked by importance rather than colored by meaning?"` | deslop:aa1545, deslop:ba7e05, deslop:f03fa4 |
| 32 | Is the loud red destructive treatment used only when destruction is the primary action of that surface? | `aria:alertdialog ask "Is the loud red destructive treatment used only when destruction is the primary action of that surface?"` | deslop:4e97f2, ui-craft:e67d29 |
| 33 | Does every CTA fill with an accent color? | `aria:button ask "Does every CTA fill with an accent color?"` | hallmark:6507dd |
| 34 | Does the error state use a distinct error color plus a non-color cue (icon, text or border)? | `state:invalid ask "Does the error state use a distinct error color plus a non-color cue (icon, text or border)?"` | hallmark:4763fe, nngroup:d4e818, nngroup:df18e6, nngroup:e75b2c, ui-craft:fd718d |
| 35 | Are shadows tinted to the background hue rather than pure black? | `ui:card ask "Are shadows tinted to the background hue rather than pure black?"` | taste-skill:00c36b, taste-skill:66c74c, taste-skill:cb5741, ui-craft:233a86, vercel:9c2217 |

### Space & layout

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 36 | Does the page render without loss at 320px up to very large screens (checking 320, 375, 414 and 768px)? | `page ask "Does the page render without loss at 320px up to very large screens (checking 320, 375, 414 and 768px)?"` | hallmark:0daf77, hallmark:cd26aa, hallmark:fa240e, impeccable:1ee491, hallmark:0daf77, hallmark:cd26aa +8 |
| 37 | Do text containers and flex children that may truncate handle long content with truncation, clamping or wrapping, with min-width 0 so children can shrink? | `text:* ask "Do text containers and flex children that may truncate handle long content with truncation, clamping or wrapping, with min-width 0 so children can shrink?"` | impeccable:0e5fee, impeccable:df0caa, ui-craft:0d608e, unslop:e5691d, vercel:c94a81, ui-craft:89e593 +1 |
| 38 | Do elements differ in visual weight by importance, so something still stands out and hierarchy is not eliminated? | `page ask "Do elements differ in visual weight by importance, so something still stands out and hierarchy is not eliminated?"` | impeccable:176733, impeccable:399113, taste-skill:fb3075 |
| 39 | Labels margin bottom is 4px (sources also say: 4px) | `text:label margin-bottom == 4px` | hallmark:b11a4e, ui-craft:a7ce9c |
| 40 | Are primary actions large and placed where the cursor or thumb already rests (at the bottom of the screen within thumb reach on mobile)? | `aria:button ask "Are primary actions large and placed where the cursor or thumb already rests (at the bottom of the screen within thumb reach on mobile)?"` | deslop:bc4b5d, impeccable:4d1e6b |
| 41 | Can a viewer identify the first thing to read and the primary goal within one second? | `page ask "Can a viewer identify the first thing to read and the primary goal within one second?"` | claw-design:4e2d8d, impeccable:399113, nngroup:996e1e, ui-craft:8b6cba, unslop:049bc1, unslop:2ff24e |
| 42 | Is spacing tighter within groups than between sections, so a rhythm is visible? | `page ask "Is spacing tighter within groups than between sections, so a rhythm is visible?"` | claw-design:5c43b9, claw-design:698d11, claw-design:bce1dd, claw-design:decd57, deslop:6e666b, hallmark:bb7df9 +6 |
| 43 | Body text width is at most 65ch (sources also say: 65ch-75ch) | `text:body max-width <= 65ch` | hallmark:d8592a, hallmark:e22fbe, taste-skill:40053d, taste-skill:4f8934, ui-craft:14cb50, ui-craft:600bf3 +2 |
| 44 | Main content padding is at least 24px | `aria:main padding >= 24px` | ui-craft:f1ccf0 |
| 45 | Main content gap is 16px | `aria:main gap == 16px` | ui-craft:f1ccf0 |
| 46 | Forms gap is 16px | `aria:form gap == 16px` | ui-craft:a7ce9c |
| 47 | Forms margin bottom is 48px | `aria:form margin-bottom == 48px` | ui-craft:a7ce9c |
| 48 | Do adjacent nesting levels use different spacing values? | `page ask "Do adjacent nesting levels use different spacing values?"` | ui-craft:a7ce9c, ui-craft:ab90a8 |
| 49 | Is the density of each view chosen to fit its use frequency and content complexity? | `page ask "Is the density of each view chosen to fit its use frequency and content complexity?"` | claw-design:0b07e1, claw-design:555d73, impeccable:94c06b, impeccable:d8744f |
| 50 | Does every major block have visible breathing room around it? | `page ask "Does every major block have visible breathing room around it?"` | claw-design:19a087, claw-design:bce1dd, claw-design:df22df, deslop:47fb0f, deslop:915287, impeccable:12453f +19 |
| 51 | Are cards replaced by border-top dividers or negative space where a card adds nothing, especially in dense layouts? | `ui:card ask "Are cards replaced by border-top dividers or negative space where a card adds nothing, especially in dense layouts?"` | hallmark:e018e1, taste-skill:00c36b, taste-skill:ba7104, taste-skill:ea3d67 |
| 52 | Main content grid template columns is 1fr — phones | `aria:main grid-template-columns == 1fr @media:narrow` | deslop:01850d, deslop:0d6a36, hallmark:f5257a, taste-skill:0e76ff, taste-skill:14d9d6, taste-skill:1d8719 +6 |
| 53 | Main content padding left is at least 16px — phones | `aria:main padding-left >= 16px @media:narrow` | taste-skill:0e76ff, taste-skill:1d8719, taste-skill:72ba55, taste-skill:c31498, taste-skill:fa1f9c |
| 54 | Does every multi-column layout collapse to a single column on small screens (below 60rem)? | `page ask "Does every multi-column layout collapse to a single column on small screens (below 60rem)?"` | hallmark:452bc3, hallmark:822b38, hallmark:b6841f, hallmark:e5fb2a, taste-skill:9eb9d1, taste-skill:22c95b +2 |
| 55 | Does the layout reduce columns when the font size increases? | `page ask "Does the layout reduce columns when the font size increases?"` | apple-hig:b7188d |
| 56 | Do blocks and every section's content share the same left and right edges, columns or baselines on a stable grid, including on tinted bands? | `page ask "Do blocks and every section's content share the same left and right edges, columns or baselines on a stable grid, including on tinted bands?"` | apple-hig:848212, claw-design:5d2f31, claw-design:78037a, claw-design:b3cb94, deslop:aaa17a, hallmark:27ea91 +8 |
| 57 | Are any misalignments intentional and explainable? | `page ask "Are any misalignments intentional and explainable?"` | claw-design:1b8093, claw-design:85e793 |
| 58 | Do shared elements in side-by-side cards or columns start at the same vertical position? | `page ask "Do shared elements in side-by-side cards or columns start at the same vertical position?"` | taste-skill:3f6c3f, taste-skill:dd1aa0 |
| 59 | Are icons, play buttons and button text optically centred, with 1px nudges where geometric centring looks off? | `ui:icon ask "Are icons, play buttons and button text optically centred, with 1px nudges where geometric centring looks off?"` | feel-better:e65f80, impeccable:2ba427, impeccable:df7672, taste-skill:b85594, ui-craft:d45ff3, vercel:d1711b |
| 60 | Is bottom padding slightly larger than top padding where that looks balanced? | `aria:button ask "Is bottom padding slightly larger than top padding where that looks balanced?"` | taste-skill:5caef9 |
| 61 | Do icon-leading buttons use slightly less padding on the icon side? | `aria:button ask "Do icon-leading buttons use slightly less padding on the icon side?"` | ui-craft:e741fb, feel-better:6791b4 |
| 62 | Are breakpoints written in rem so they respect the user's font size? | `page ask "Are breakpoints written in rem so they respect the user's font size?"` | hallmark:335182, hallmark:fe7701 |
| 63 | Are breakpoints placed where the content breaks rather than at device widths? | `page ask "Are breakpoints placed where the content breaks rather than at device widths?"` | deslop:97bb00, hallmark:5d1983, impeccable:2f9689, impeccable:658ec8, impeccable:a14c30, ui-craft:ea55ce |
| 64 | Is the centre navigation hidden below about 900px, leaving the brand and a CTA or hamburger? | `aria:navigation ask "Is the centre navigation hidden below about 900px, leaving the brand and a CTA or hamburger?"` | hallmark:d82077 |
| 65 | Does the interface adapt to smaller screens and size changes while keeping functionality and a recognisable layout? | `page ask "Does the interface adapt to smaller screens and size changes while keeping functionality and a recognisable layout?"` | apple-hig:4f8888, apple-hig:a43748, apple-hig:eb0181, oneredoak:77e13e |
| 66 | Does the page use the project's existing breakpoint system, with no magic widths? | `page ask "Does the page use the project's existing breakpoint system, with no magic widths?"` | impeccable:2f9689, ui-craft:a656c0 |

### Surface

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 67 | Do cards use subtle, soft, wide-spreading drop shadows? | `ui:card ask "Do cards use subtle, soft, wide-spreading drop shadows?"` | deslop:9021ec, hallmark:0343a8, hallmark:9f02fe, hallmark:9fafe3, hallmark:d73930, hallmark:d7bb9d +3 |
| 68 | Are shadows and elevation reserved for genuinely floating UI (menus, toasts, modals)? | `page ask "Are shadows and elevation reserved for genuinely floating UI (menus, toasts, modals)?"` | deslop:9021ec, ui-craft:ff748d |
| 69 | Cards shadow is none — dark mode | `ui:card box-shadow == none @media:dark` | deslop:ebf053, hallmark:595c22, ui-craft:c36c7a, ui-craft:c70abb |
| 70 | Does an open menu on a low-contrast surface have a hairline stroke and/or shadow pair to separate it from the page? | `aria:menu ask "Does an open menu on a low-contrast surface have a hairline stroke and/or shadow pair to separate it from the page?"` | ui-craft:b6180f |
| 71 | Icons come from at most 1 icon set(s) | `ui:icon axl:icon-sets <= 1` | deslop:9b3cf3, feel-better:2ba963, hallmark:0b9bd5, hallmark:2f31d3, impeccable:4ddb7a, impeccable:9864e3 +2 |
| 72 | Icons distinct stroke widths is at most 1 | `ui:icon axl:distinct-stroke-widths <= 1` | deslop:3214bb, deslop:7a8ed8, deslop:9b3cf3, feel-better:2ba963, feel-better:f32af7, hallmark:30c27d +1 |
| 73 | Icons distinct icon grids is at most 1 | `ui:icon axl:distinct-icon-grids <= 1` | deslop:0a3f4b, deslop:3214bb, deslop:9b3cf3, deslop:bd9fd7 |

### Imagery

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 74 | Are round shapes drawn slightly larger than square ones so they read as the same size? | `ui:icon ask "Are round shapes drawn slightly larger than square ones so they read as the same size?"` | deslop:080bbd |
| 75 | Is the image aspect ratio identical across every card in a grid? | `ui:card ask "Is the image aspect ratio identical across every card in a grid?"` | openai:2ebba0, ui-craft:c845e6 |
| 76 | Does the icon corner radius match the overall radius of the token set? | `ui:icon ask "Does the icon corner radius match the overall radius of the token set?"` | deslop:3db8c5, deslop:6ab8b0, deslop:763866, deslop:9b3cf3 |
| 77 | Do all icons carry the same optical weight and read as siblings from one family? | `ui:icon ask "Do all icons carry the same optical weight and read as siblings from one family?"` | deslop:080bbd, deslop:0a3f4b, deslop:21a07b, deslop:7aea64, deslop:aaa8b3, impeccable:20e51b +2 |
| 78 | Is the unmodified default icon set avoided (customised stroke and radius, or a distinctive set)? | `ui:icon ask "Is the unmodified default icon set avoided (customised stroke and radius, or a distinctive set)?"` | deslop:0bbee2, deslop:1fe7c1, deslop:2dd102, deslop:358f64, deslop:6ab8b0, deslop:82d665 +6 |
| 79 | Are icons from one chosen icon library rather than hand-rolled SVG, with only brand-critical icons drawn custom? | `ui:icon ask "Are icons from one chosen icon library rather than hand-rolled SVG, with only brand-critical icons drawn custom?"` | deslop:9d2a20, taste-skill:00e4ee, taste-skill:116931, taste-skill:132b07, taste-skill:135a81, taste-skill:9cba25 +2 |
| 80 | Are icons monochrome and outlined by default, with fill used only for the active state? | `ui:icon ask "Are icons monochrome and outlined by default, with fill used only for the active state?"` | feel-better:cf318c, openai:f3f36f |

### Motion

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 81 | Loading placeholders transition delay is 200ms | `ui:skeleton transition-delay == 200ms` | ui-craft:0ae78b, ui-craft:5a8559, ui-craft:96bf62, ui-craft:a52cf2, ui-craft:b71798, ui-craft:b75dc0 |
| 82 | Does a skeleton show one pulse or shimmer signal with no spinner on top? | `ui:skeleton ask "Does a skeleton show one pulse or shimmer signal with no spinner on top?"` | ui-craft:33d5eb |
| 83 | Hover transition property includes opacity | `state:hover transition-property contains opacity` | feel-better:0bcbf6, feel-better:8a62d7, feel-better:9c5b06, oneredoak:922c83, oneredoak:9620ce, ui-craft:b52fa2 +1 |
| 84 | Does every animation communicate or confirm a state, hierarchy or relationship? | `page ask "Does every animation communicate or confirm a state, hierarchy or relationship?"` | deslop:fec7dc, hallmark:548637, hallmark:663ab5, hallmark:91027b, hallmark:942a74, impeccable:0c9106 +12 |
| 85 | Does motion use custom cubic-bezier curves rather than browser default, linear or ease-in-out keywords? | `page ask "Does motion use custom cubic-bezier curves rather than browser default, linear or ease-in-out keywords?"` | deslop:6ccd09, taste-skill:153b5e, taste-skill:be97af, taste-skill:db4bca |
| 86 | Whole page easing includes cubic-bezier | `page transition-timing-function contains cubic-bezier` | deslop:6ccd09, hallmark:7e609c, hallmark:e34963, hallmark:eda437, taste-skill:153b5e, taste-skill:3c18a5 +5 |
| 87 | Is bounce or elastic easing avoided on functional UI? | `page ask "Is bounce or elastic easing avoided on functional UI?"` | hallmark:8ec61f, impeccable:9a17f9, impeccable:a2a04a, impeccable:a6f0f1, ui-craft:79a9ea, ui-craft:e56ae9 |
| 88 | Is spring easing reserved for primary actions? | `page ask "Is spring easing reserved for primary actions?"` | hallmark:8ec61f |
| 89 | Whole page transition property is never backdrop-filter | `page transition-property !contains backdrop-filter` | deslop:fcea90, feel-better:81762a, feel-better:c375b9, hallmark:3df8ba, hallmark:7a9a30, hallmark:86bdd5 +14 |
| 90 | Whole page will change includes transform | `page will-change contains transform` | taste-skill:16cc4a, taste-skill:8e4ee7 |
| 91 | Does the page use one orchestrated entrance instead of motion on every section? | `page ask "Does the page use one orchestrated entrance instead of motion on every section?"` | anthropic:5eef76, hallmark:8ec61f, hallmark:d464f5, hallmark:d7099f, impeccable:624c9f, impeccable:e232a9 |
| 92 | Would removing this animation lose the user no information? | `page ask "Would removing this animation lose the user no information?"` | hallmark:942a74, oneredoak:bb5095 |
| 93 | Whole page cta wobbles is at most 1 | `page axl:cta-wobbles <= 1` | hallmark:8ec61f, hallmark:bf9ab7 |

### Interaction

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 94 | Was the primary gesture tried with the target input method and completed? | `process ask "Was the primary gesture tried with the target input method and completed?"` | impeccable:053bba, impeccable:caee46 |
| 95 | Does every click-opened dropdown also show a hover or focus affordance? | `aria:combobox ask "Does every click-opened dropdown also show a hover or focus affordance?"` | hallmark:043aae |
| 96 | Is there exactly one primary action per view section? | `aria:button ask "Is there exactly one primary action per view section?"` | hallmark:d15e85, impeccable:52b4ae, taste-skill:420cbf, taste-skill:59ad17, taste-skill:ad4b83, ui-craft:4397e1 +4 |
| 97 | Does each card have at most one primary and one secondary action? | `ui:card ask "Does each card have at most one primary and one secondary action?"` | openai:06c554, openai:1b0d71, openai:345cfe |
| 98 | Do secondary actions look visibly weaker than the primary (outline, ghost or text link), with one filled and at most one ghost button per area? | `aria:button ask "Do secondary actions look visibly weaker than the primary (outline, ghost or text link), with one filled and at most one ghost button per area?"` | taste-skill:420cbf, taste-skill:de8e93, ui-craft:4dd61f, ui-craft:e67d29, ui-craft:e86fe3 |
| 99 | Are toolbar filter controls ghost buttons rather than solid primary buttons? | `aria:toolbar ask "Are toolbar filter controls ghost buttons rather than solid primary buttons?"` | ui-craft:92046a |
| 100 | Is there one CTA in the nav, visually distinct from plain links and the page's primary CTA? | `aria:navigation ask "Is there one CTA in the nav, visually distinct from plain links and the page's primary CTA?"` | ui-craft:8ece42 |
| 101 | Is the primary action visible before scrolling and unmistakable? | `page ask "Is the primary action visible before scrolling and unmistakable?"` | claw-design:2669f7, claw-design:74e6c0, claw-design:bdef1d, taste-skill:84661f |
| 102 | Are calls to action placed at natural decision points rather than repeated as filler? | `page ask "Are calls to action placed at natural decision points rather than repeated as filler?"` | claw-design:6a84bf, claw-design:c531ba |
| 103 | Are long menus chunked with a recommended default highlighted? | `aria:menu ask "Are long menus chunked with a recommended default highlighted?"` | deslop:c3d097, impeccable:e005dd |
| 104 | Is the error message shown inline directly below its field? | `state:invalid ask "Is the error message shown inline directly below its field?"` | deslop:0e74eb, nngroup:8a5394, taste-skill:1b6d3c, taste-skill:b24049, taste-skill:d6fccf, ui-craft:1b0b96 +2 |
| 105 | Does the error text stand out from the rest of the form so the user notices it quickly? | `state:invalid ask "Does the error text stand out from the rest of the form so the user notices it quickly?"` | nngroup:5de04b, nngroup:99c3aa, nngroup:d4e818 |
| 106 | Are format errors validated on blur or submit, not on every keystroke? | `aria:form ask "Are format errors validated on blur or submit, not on every keystroke?"` | deslop:0e74eb, govuk:168328, hallmark:0d49c7, nngroup:31e721, ui-craft:9864c1, webdev:c4a5b5 |
| 107 | Does the form validate the information the user gives (emails, required fields and formats) on the client? | `aria:form ask "Does the form validate the information the user gives (emails, required fields and formats) on the client?"` | govuk:3e18ef, taste-skill:97797c |
| 108 | Does every interactive component have designed default, hover, focus, active, disabled, loading and error states? | `page ask "Does every interactive component have designed default, hover, focus, active, disabled, loading and error states?"` | deslop:1ba250, deslop:434997, deslop:aa1545, hallmark:381ce7, impeccable:95ccbe, ui-craft:26a88b |
| 109 | Does every view with no data show a designed empty state with a reason and a next action? | `state:empty ask "Does every view with no data show a designed empty state with a reason and a next action?"` | deslop:6b5cc1, hallmark:4e26fd, impeccable:ab96ee, shadcn:265057, ui-craft:6aae3e, ui-craft:734f61 +3 |
| 110 | Does a loading skeleton match the final layout geometry? | `ui:skeleton ask "Does a loading skeleton match the final layout geometry?"` | deslop:e471a8, shadcn:440373, taste-skill:27c814, taste-skill:4fc428, taste-skill:5b4ea1, ui-craft:0ae78b +6 |
| 111 | Is a skeleton used instead of a generic centered spinner for content loading? | `ui:skeleton ask "Is a skeleton used instead of a generic centered spinner for content loading?"` | taste-skill:27c814, taste-skill:4fc428, taste-skill:5b4ea1, ui-craft:5a8559, ui-craft:b71798 |
| 112 | Does a load or skeleton that lasts past 5s escalate to a progress indicator or a timeout message with retry, rather than a skeleton or spinner that waits indefinitely? | `aria:progressbar ask "Does a load or skeleton that lasts past 5s escalate to a progress indicator or a timeout message with retry, rather than a skeleton or spinner that waits indefinitely?"` | ui-craft:a52cf2, ui-craft:c5ab6f |
| 113 | Does a long wait or long operation show truthful progress rather than invented progress? | `aria:progressbar ask "Does a long wait or long operation show truthful progress rather than invented progress?"` | deslop:e471a8, impeccable:46eea3, impeccable:9a6ecc |
| 114 | Does a thinking indicator escalate to progress within 2s? | `aria:status ask "Does a thinking indicator escalate to progress within 2s?"` | ui-craft:ae0e28 |
| 115 | Are toasts used only for transient messages, reserved for failures, hidden-effect actions and needed confirmations? | `ui:toast ask "Are toasts used only for transient messages, reserved for failures, hidden-effect actions and needed confirmations?"` | hallmark:0c4c14, hallmark:9adf9e, hallmark:db45cf, taste-skill:b24049, ui-craft:e31bc7 |
| 116 | Does every avatar have a fallback for when its image fails to load? | `ui:avatar ask "Does every avatar have a fallback for when its image fails to load?"` | shadcn:653c51 |
| 117 | Does upload state reflect the real upload status? | `ui:file ask "Does upload state reflect the real upload status?"` | shadcn:7ec57f |
| 118 | Does the form keep the user's valid data, entered fields (including the cart after a declined charge) and in-flight state when an error occurs? | `aria:form ask "Does the form keep the user's valid data, entered fields (including the cart after a declined charge) and in-flight state when an error occurs?"` | impeccable:a83073, ui-craft:11b4a5, ui-craft:3e4871, ui-craft:9e5de2 |
| 119 | Does the interface use familiar system gestures, with the simplest gesture for frequent actions and no custom multifinger or multihand gestures people must learn? | `page ask "Does the interface use familiar system gestures, with the simplest gesture for frequent actions and no custom multifinger or multihand gestures people must learn?"` | apple-hig:209972, apple-hig:c4ca83, apple-hig:dcc5d9 |
| 120 | Does Enter submit a focused single input (or the last control) and Cmd/Ctrl+Enter a textarea, matching platform shortcuts (Cmd+Enter on macOS)? | `aria:form ask "Does Enter submit a focused single input (or the last control) and Cmd/Ctrl+Enter a textarea, matching platform shortcuts (Cmd+Enter on macOS)?"` | ui-craft:21b944, vercel:951bd0, vercel:ac2719 |
| 121 | Do interactive elements use CSS transitions for state changes? | `page ask "Do interactive elements use CSS transitions for state changes?"` | feel-better:0bcbf6, feel-better:8a62d7, oneredoak:922c83 |
| 122 | Does every clickable card and image react on hover with more than a background colour change? | `page ask "Does every clickable card and image react on hover with more than a background colour change?"` | taste-skill:7b010f, taste-skill:ae894b |

### Access

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 123 | All text meets WCAG 1.4.3: contrast (minimum) | `text:* wcag:1.4.3 pass` | deslop:16a21f, deslop:63f18e, govuk:2abc9c, impeccable:1f2256, impeccable:570161, impeccable:dc1528 +3 |
| 124 | Buttons meet WCAG 1.4.3: contrast (minimum) | `aria:button wcag:1.4.3 pass` | taste-skill:3793ac, taste-skill:a47ec2, taste-skill:f64166 |
| 125 | Dark mode meets WCAG 1.4.3: contrast (minimum) | `media:dark wcag:1.4.3 pass` | apple-hig:9c8a8d, apple-hig:cc15ca, taste-skill:9deb18 |
| 126 | Is each invalid field marked aria-invalid=true and linked to its error message with aria-describedby? | `state:invalid ask "Is each invalid field marked aria-invalid=true and linked to its error message with aria-describedby?"` | hallmark:3a54f8, ui-craft:79dedf, ui-craft:ff144b |
| 127 | Captions & fine print meet WCAG 1.4.3: contrast (minimum) | `text:caption wcag:1.4.3 pass` | impeccable:eb0cee |
| 128 | Buttons meet WCAG 1.4.11: non-text contrast | `aria:button wcag:1.4.11 pass` | impeccable:a5e15b, ui-craft:e86fe3, wcag22:0ce239 |
| 129 | Whole page meets WCAG 1.4.10: reflow — phones | `page wcag:1.4.10 pass @media:narrow` | impeccable:1ee491 |
| 130 | Are existing accessibility wins preserved, including focus states, alt text, keyboard navigation and contrast? | `page ask "Are existing accessibility wins preserved, including focus states, alt text, keyboard navigation and contrast?"` | taste-skill:1917bb |
| 131 | Keyboard focus meets WCAG 2.4.7: focus visible | `state:focus-visible wcag:2.4.7 pass` | deslop:1c9511, deslop:49025d, hallmark:5d4280, hallmark:983923, hallmark:dc47bf, hallmark:f99500 +7 |
| 132 | Keyboard focus meets WCAG 1.4.1: use of color | `state:focus-visible wcag:1.4.1 pass` | apple-hig:d7d79e |
| 133 | Does the focus ring follow the element's border-radius? | `state:focus-visible ask "Does the focus ring follow the element's border-radius?"` | deslop:49025d, deslop:6c1aa5 |
| 134 | Invalid input meets WCAG 1.4.1: use of color | `state:invalid wcag:1.4.1 pass` | hallmark:4763fe, nngroup:e75b2c, ui-craft:fd718d |
| 135 | Does focus move to the offending field on error? | `state:invalid ask "Does focus move to the offending field on error?"` | ui-craft:e7b766, vercel:afe6a8 |
| 136 | Whole page meets WCAG 1.4.10: reflow (sources also say: 1920px, 400%) | `page wcag:1.4.10 pass` | hallmark:0daf77, hallmark:c22f82, hallmark:cd26aa, hallmark:fa240e, ui-craft:171f32, ui-craft:e47347 +4 |

### Performance

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 137 | All text color contrast (Lighthouse) is passes  | `text:* lighthouse:color-contrast pass` | deslop:4024d9, impeccable:0a9d8d, lighthouse:0b114c |
| 138 | Whole page total byte weight (Lighthouse) is passes  | `page lighthouse:total-byte-weight pass` | impeccable:5df1a9, impeccable:d09cef, lighthouse:1b6894, oneredoak:96d61c |
| 139 | Whole page unused css rules (Lighthouse) is passes  | `page lighthouse:unused-css-rules pass` | impeccable:902b24, impeccable:b3ee17, lighthouse:c15110, oneredoak:96d61c |
| 140 | Whole page mainthread work breakdown (Lighthouse) is passes  | `page lighthouse:mainthread-work-breakdown pass` | impeccable:5cfae1, impeccable:aa1358, impeccable:aa8105, impeccable:b9395b, impeccable:bd7d22, impeccable:f1ac88 +3 |
| 141 | Whole page font display insight (Lighthouse) is passes  | `page lighthouse:font-display-insight pass` | impeccable:2b9811, impeccable:cd2a34 |
| 142 | Was the actual bottleneck identified, fixed and measured, instead of optimizing what is not slow? | `page ask "Was the actual bottleneck identified, fixed and measured, instead of optimizing what is not slow?"` | impeccable:695ed8 |
| 143 | Are dependencies added only when the existing stack cannot express the effect? | `page ask "Are dependencies added only when the existing stack cannot express the effect?"` | impeccable:03aa2d |
| 144 | Are heavy resources lazy-initialized only when near the viewport? | `page ask "Are heavy resources lazy-initialized only when near the viewport?"` | impeccable:3260fc |
| 145 | Do icons come from an SVG sprite? | `page ask "Do icons come from an SVG sprite?"` | impeccable:177c52 |
| 146 | Buttons target size (Lighthouse) is passes  | `aria:button lighthouse:target-size pass` | axe:a40d91, deslop:bc4b5d, lighthouse:238ec5, vercel:59af63, vercel:865212, vercel:b7090f |
| 147 | Buttons interactive element affordance (Lighthouse) is passes  | `aria:button lighthouse:interactive-element-affordance pass` | claw-design:4a2832, claw-design:ca62e3, claw-design:d79958, deslop:6018dc |
| 148 | Loading placeholders cumulative layout shift (Lighthouse) is passes  | `ui:skeleton lighthouse:cumulative-layout-shift pass` | deslop:e471a8, ui-craft:0ae78b, ui-craft:5a8559, vercel:cdace4, vercel:f9b7a1 |
| 149 | Images have an explicit width and height | `aria:img lighthouse:unsized-images pass` | hallmark:2ac7c4, impeccable:a74e20, impeccable:ed3181, lighthouse:62c011, ui-craft:dc9a1e, vercel:366ea0 +1 |
| 150 | Images image aspect ratio (Lighthouse) is passes  | `aria:img lighthouse:image-aspect-ratio pass` | hallmark:66800f, hallmark:a2ecce, impeccable:ed3181, lighthouse:ddb4c3, openai:2ebba0, ui-craft:dc9a1e |
| 151 | Images image size responsive (Lighthouse) is passes  | `aria:img lighthouse:image-size-responsive pass` | impeccable:a4053c, impeccable:ed3181, lighthouse:c6c975, ui-craft:dc9a1e |
| 152 | Whole page non composited animations (Lighthouse) is passes  | `page lighthouse:non-composited-animations pass` | feel-better:120641, hallmark:389f22, impeccable:ec40b9, lighthouse:86c261, ui-craft:5bc502, vercel:c7d2b3 +1 |

### Search & metadata

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 153 | Images image alt (Lighthouse) is passes  | `aria:img lighthouse:image-alt pass` | axe:413366, impeccable:ed3181, impeccable:f29dd2, lighthouse:457f09, openai:66552e, taste-skill:a63982 |

### Content

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 154 | Is plain language used, with jargon translated and any unavoidable domain terms defined inline, by tooltip or on first use? | `text:* ask "Is plain language used, with jargon translated and any unavoidable domain terms defined inline, by tooltip or on first use?"` | impeccable:0a8fa1, impeccable:367c41, impeccable:7e41df, impeccable:c1a8e1, nngroup:5cd495, nngroup:9275ca +8 |
| 155 | Is the copy specific and written in the product's own language, not generic or whimsical? | `text:* ask "Is the copy specific and written in the product's own language, not generic or whimsical?"` | deslop:58f733, impeccable:0f5a96, taste-skill:0516d5, taste-skill:736a1c, ui-craft:8059ba |
| 156 | All text em dashes per paragraph is 0 (sources also say: 1) | `text:* axl:em-dashes-per-paragraph == 0` | deslop:58f733, taste-skill:49905d, taste-skill:54765f, taste-skill:c733d3, taste-skill:dbc108, taste-skill:eb7089 +7 |
| 157 | Is the copy written in the active voice? | `text:* ask "Is the copy written in the active voice?"` | anthropic:e0b017, taste-skill:34d464 |
| 158 | Do social-proof headings use natural wording such as Trusted by rather than Quietly trusted by? | `aria:heading ask "Do social-proof headings use natural wording such as Trusted by rather than Quietly trusted by?"` | taste-skill:6e965f |
| 159 | Do confirmation toasts name the thing that happened? | `ui:toast ask "Do confirmation toasts name the thing that happened?"` | ui-craft:8059ba |
| 160 | Does every empty state explain why it is empty and offer the next action? | `state:empty ask "Does every empty state explain why it is empty and offer the next action?"` | deslop:6b5cc1, hallmark:2cd968, hallmark:4e26fd, impeccable:ab96ee, ui-craft:01f776, ui-craft:65649d +2 |
| 161 | Whole page hardcoded colors is 0 | `page axl:hardcoded-colors == 0` | apple-hig:013628, claw-design:349c46, claw-design:d65a0c, deslop:03079a, hallmark:2840c9, hallmark:4f55d3 +4 |
| 162 | Whole page: all spacing sits on the scale (sources also say: 8px, 0) | `page axl:spacing-off-scale == 0` | claw-design:59f92d, deslop:6e666b, hallmark:a84d7a, impeccable:4b2dac, impeccable:b0cfe6, oneredoak:600431 +14 |
| 163 | All text uses at most 6 font sizes (sources also say: 5, 8) | `text:* axl:distinct-font-sizes <= 6` | deslop:b3159c, hallmark:f36af6, ui-craft:3db0ac, ui-craft:4522a2, hallmark:40775f, ui-craft:8f8b4c +1 |
| 164 | All text uses at most 3 font weights (sources also say: 2) | `text:* axl:distinct-font-weights <= 3` | impeccable:c4ef3d, ui-craft:8f8b4c, ui-craft:a4dfd3, ui-craft:880428 |
| 165 | Whole page oklch color share is at least 100% | `page axl:oklch-color-share >= 100%` | hallmark:4cb76d |
| 166 | Does the design hold up with short, average and very long user content and emoji? | `page ask "Does the design hold up with short, average and very long user content and emoji?"` | impeccable:00010c, vercel:f37715 |
| 167 | Does the design hold up with empty states, localization, zoom and dynamic content? | `page ask "Does the design hold up with empty states, localization, zoom and dynamic content?"` | impeccable:0e5fee, impeccable:587fc2, impeccable:636c8a, impeccable:df0caa, ui-craft:71a438 |
| 168 | Are existing copy, claims and product names preserved unless the user supplies replacements? | `page ask "Are existing copy, claims and product names preserved unless the user supplies replacements?"` | hallmark:b89941, impeccable:06b9b5, ui-craft:e6b74e, ui-craft:f6bd26 |
| 169 | Does every error say what went wrong (the specific cause when known) and give a next step such as how to fix it, retry or contact support, never dead-ending? | `state:invalid ask "Does every error say what went wrong (the specific cause when known) and give a next step such as how to fix it, retry or contact support, never dead-ending?"` | anthropic:ee3b05, deslop:c17b4d, impeccable:410f2b, impeccable:8ff610, nngroup:07c8f8, nngroup:12c78e +15 |
| 170 | Is one label used for each intent? | `aria:button ask "Is one label used for each intent?"` | taste-skill:ed2998 |
| 171 | Is one term used for each concept throughout, including either Sign in or Log in everywhere, never mixed? | `text:* ask "Is one term used for each concept throughout, including either Sign in or Log in everywhere, never mixed?"` | hallmark:f9eb36, impeccable:a3822c, impeccable:c10bf2, impeccable:ffb5b0, nngroup:df89e3, ui-craft:1db8f0 +3 |
| 172 | Do different actions such as delete, remove and archive keep distinct meanings without aliasing? | `text:* ask "Do different actions such as delete, remove and archive keep distinct meanings without aliasing?"` | ui-craft:274ea5, ui-craft:cf04eb |
| 173 | Icons include no emoji used as icons | `ui:icon axl:emoji-as-icons == 0` | claw-design:05f742, claw-design:4f1bfd, hallmark:0560d5, hallmark:0a360f, hallmark:2f31d3, hallmark:7c1abc +6 |
| 174 | Does a first-use state show the value and offer a first action or template? | `state:empty ask "Does a first-use state show the value and offer a first action or template?"` | impeccable:331c13, impeccable:90c53b, impeccable:ab96ee, ui-craft:f790be |
| 175 | Does loading text name the real operation? | `aria:status ask "Does loading text name the real operation?"` | impeccable:9a6ecc |
| 176 | Does exactly one element carry a memorable signature detail (one signature bet)? | `page ask "Does exactly one element carry a memorable signature detail (one signature bet)?"` | ui-craft:1134e2, ui-craft:9063c5, ui-craft:a77ec9 |
| 177 | Does the interface match neighboring mental models, terminology and save behaviour? | `page ask "Does the interface match neighboring mental models, terminology and save behaviour?"` | impeccable:960139 |
| 178 | Do icons match cultural convention? | `ui:icon ask "Do icons match cultural convention?"` | ui-craft:efc4c7 |
| 179 | Is every paragraph three sentences or fewer? | `text:body ask "Is every paragraph three sentences or fewer?"` | claw-design:3753ac, hallmark:712494 |

### Process

| # | Rule | Code | Sources (quote IDs) |
|---|---|---|---|
| 180 | Was the layout checked at desktop, tablet and mobile viewports, at every supported viewport including the user's actual one, with screenshots for every device class the app ships to? | `process ask "Was the layout checked at desktop, tablet and mobile viewports, at every supported viewport including the user's actual one, with screenshots for every device class the app ships to?"` | impeccable:1dafe0, impeccable:314102, impeccable:531fdb, impeccable:a14c30, impeccable:ee5ad7, impeccable:f175ea +8 |
| 181 | Are changes small and targeted at the named target, improving existing parts rather than rewriting them? | `process ask "Are changes small and targeted at the named target, improving existing parts rather than rewriting them?"` | impeccable:5e2493, taste-skill:281855, taste-skill:746292, taste-skill:79478a, taste-skill:d43e62 |
| 182 | Does the work stay inside what the existing system already owns, using existing tokens first and adding no new colors, fonts, radii or shadows? | `process ask "Does the work stay inside what the existing system already owns, using existing tokens first and adding no new colors, fonts, radii or shadows?"` | deslop:1654cd, hallmark:3739d7, hallmark:391795, hallmark:437803, hallmark:4c3829, hallmark:6e8479 +10 |
| 183 | Does the work stay in the project's existing tech stack and a single styling approach, with no second styling system added? | `process ask "Does the work stay in the project's existing tech stack and a single styling approach, with no second styling system added?"` | feel-better:3b39bf, govuk:6f492f, hallmark:802726, hallmark:ffd0f3, shadcn:e14f69, taste-skill:4e2fb9 +3 |
| 184 | Is a value promoted to a token only when it is reused, not for one-off exceptions? | `page ask "Is a value promoted to a token only when it is reused, not for one-off exceptions?"` | impeccable:6f9765, ui-craft:86dcac, ui-craft:ac32c0 |
| 185 | Are repeated components built once and shared rather than re-implemented? | `page ask "Are repeated components built once and shared rather than re-implemented?"` | hallmark:4a9130, hallmark:f4a4bc, impeccable:2ad43d, impeccable:8c16d5, impeccable:aa3ded, ui-craft:16e691 +1 |
| 186 | Is a generic component extracted only when used 3 or more times with the same intent, otherwise kept inline? | `page ask "Is a generic component extracted only when used 3 or more times with the same intent, otherwise kept inline?"` | impeccable:ef7f73, ui-craft:3b949d, impeccable:1a4656 |
| 187 | Are existing components and built-in variants used before custom markup or styles? | `page ask "Are existing components and built-in variants used before custom markup or styles?"` | shadcn:00e262, shadcn:05d991, shadcn:17760a, shadcn:1e0326, shadcn:265057, shadcn:2c3034 +20 |
| 188 | Was the work tested on real devices, at least one phone and one tablet where relevant? | `process ask "Was the work tested on real devices, at least one phone and one tablet where relevant?"` | impeccable:1bacbd, impeccable:58f045, impeccable:caee46, impeccable:db128f, impeccable:df4931, impeccable:f4beb0 +2 |
| 189 | Does the evidence say whether it came from an emulator or real hardware? | `process ask "Does the evidence say whether it came from an emulator or real hardware?"` | impeccable:1bacbd, impeccable:58f045 |
| 190 | Were no assumptions made about which devices people use? | `process ask "Were no assumptions made about which devices people use?"` | govuk:f3e5f2 |
| 191 | Is the target audited and findings reported before any edits? | `process ask "Is the target audited and findings reported before any edits?"` | hallmark:f7420a, impeccable:0eb6e3, impeccable:1c53d4, impeccable:a98a37, impeccable:e3ae02, ui-craft:3da1b7 |
| 192 | Is the design plan checked for uniqueness before code is written? | `process ask "Is the design plan checked for uniqueness before code is written?"` | anthropic:5a976e |
| 193 | Does each finding name the violated principle? | `process ask "Does each finding name the violated principle?"` | deslop:135dd3 |
| 194 | Does the change keep the existing brand identity recognizable? | `page ask "Does the change keep the existing brand identity recognizable?"` | anthropic:7be652, claw-design:794055, hallmark:aae68f, impeccable:1fa04c, impeccable:21f283, impeccable:6c3d98 +3 |
| 195 | Are existing files, routes and global stylesheets kept, with changes merged in rather than overwritten or deleted? | `process ask "Are existing files, routes and global stylesheets kept, with changes merged in rather than overwritten or deleted?"` | hallmark:52e047, hallmark:a37dcf, hallmark:b73df6, hallmark:ead376, hallmark:ffd0f3, ui-craft:13385b +1 |
| 196 | Are existing analytics events and the names or IDs tracking depends on left unchanged? | `process ask "Are existing analytics events and the names or IDs tracking depends on left unchanged?"` | taste-skill:5e9e1e |
| 197 | Is each screen's state list (empty, loading, error, partial, conflict, offline) marked designed, missing or not applicable? | `process ask "Is each screen's state list (empty, loading, error, partial, conflict, offline) marked designed, missing or not applicable?"` | impeccable:25267c, impeccable:8f5a67, taste-skill:1805c1, taste-skill:90d645, taste-skill:acbd19, ui-craft:21fa52 +8 |
| 198 | Does the interface follow established platform and framework conventions instead of inventing custom patterns? | `process ask "Does the interface follow established platform and framework conventions instead of inventing custom patterns?"` | hallmark:7a69ea, impeccable:0d25fc, impeccable:50eaa7, impeccable:6bbf30, impeccable:99e25d, impeccable:9ab767 +6 |

## Give it to your agent

Apply every rule above to the UI. Automatic rules must pass; answer each question rule with yes or a change. Don't redesign anything the rules don't cover.

## Check a site

```
axl check super-polish.axl.md https://yoursite.com
```
Reports PASS / FAIL / ASK per rule, with JSON for your agent. (A quick browser-console version is in the second tab; the CLI is the recommended way.)

## Definition

```axl
word: super polish
rules:
  - text:* wcag:1.4.3 pass
  - text:* lighthouse:color-contrast pass
  - aria:button wcag:1.4.3 pass
  - media:dark wcag:1.4.3 pass
  - media:forced-colors ask "Does the UI offer a higher-contrast colour scheme when the system Increase Contrast setting is on?"
  - text:* ask "Is text placed over imagery kept readable with an overlay, scrim or backdrop?"
  - aria:img lighthouse:image-alt pass
  - state:invalid ask "Is each invalid field marked aria-invalid=true and linked to its error message with aria-describedby?"
  - text:* ask "Is plain language used, with jargon translated and any unavoidable domain terms defined inline, by tooltip or on first use?"
  - text:body font-size >= 16px
  - process ask "Was the layout checked at desktop, tablet and mobile viewports, at every supported viewport including the user's actual one, with screenshots for every device class the app ships to?"
  - process ask "Are changes small and targeted at the named target, improving existing parts rather than rewriting them?"
  - text:caption ask "Are low-priority labels and metadata visibly quieter than the headline and core message?"
  - text:caption wcag:1.4.3 pass
  - text:* axl:gray-on-colored-background == 0
  - aria:button wcag:1.4.11 pass
  - page axl:raw-color-values == 0
  - page ask "Are colour tokens named by role rather than by raw value?"
  - page ask "Do theme changes remap semantic tokens only, leaving primitive values untouched?"
  - page ask "Are system colours used where they already define the variants needed?"
  - page ask "Are the strongest colour, weight and contrast reserved for the elements that matter most (primary action, headline, KPI)?"
  - text:* ask "Is the copy specific and written in the product's own language, not generic or whimsical?"
  - text:* axl:em-dashes-per-paragraph == 0
  - text:* ask "Is the copy written in the active voice?"
  - aria:heading ask "Do social-proof headings use natural wording such as Trusted by rather than Quietly trusted by?"
  - ui:toast ask "Do confirmation toasts name the thing that happened?"
  - state:empty ask "Does every empty state explain why it is empty and offer the next action?"
  - page axl:hardcoded-colors == 0
  - page axl:spacing-off-scale == 0
  - text:* axl:distinct-font-sizes <= 6
  - text:* axl:distinct-font-weights <= 3
  - page axl:oklch-color-share >= 100%
  - page ask "Are design tokens declared once as named CSS custom properties at :root?"
  - process ask "Does the work stay inside what the existing system already owns, using existing tokens first and adding no new colors, fonts, radii or shadows?"
  - process ask "Does the work stay in the project's existing tech stack and a single styling approach, with no second styling system added?"
  - page ask "Is a value promoted to a token only when it is reused, not for one-off exceptions?"
  - page ask "Are repeated components built once and shared rather than re-implemented?"
  - page ask "Is a generic component extracted only when used 3 or more times with the same intent, otherwise kept inline?"
  - page ask "Are existing components and built-in variants used before custom markup or styles?"
  - process ask "Was the work tested on real devices, at least one phone and one tablet where relevant?"
  - process ask "Does the evidence say whether it came from an emulator or real hardware?"
  - process ask "Was the primary gesture tried with the target input method and completed?"
  - process ask "Were no assumptions made about which devices people use?"
  - page ask "Does the page render without loss at 320px up to very large screens (checking 320, 375, 414 and 768px)?"
  - page wcag:1.4.10 pass @media:narrow
  - text:* ask "Do text containers and flex children that may truncate handle long content with truncation, clamping or wrapping, with min-width 0 so children can shrink?"
  - page ask "Does the design hold up with short, average and very long user content and emoji?"
  - page ask "Does the design hold up with empty states, localization, zoom and dynamic content?"
  - page lighthouse:total-byte-weight pass
  - page lighthouse:unused-css-rules pass
  - page lighthouse:mainthread-work-breakdown pass
  - page lighthouse:font-display-insight pass
  - page ask "Was the actual bottleneck identified, fixed and measured, instead of optimizing what is not slow?"
  - page ask "Are dependencies added only when the existing stack cannot express the effect?"
  - page ask "Are heavy resources lazy-initialized only when near the viewport?"
  - page ask "Do icons come from an SVG sprite?"
  - process ask "Is the target audited and findings reported before any edits?"
  - process ask "Is the design plan checked for uniqueness before code is written?"
  - process ask "Does each finding name the violated principle?"
  - text:* ask "Does the work keep the product's existing type system?"
  - page ask "Does the work keep the brand's existing palette and color logic?"
  - page ask "Does the change keep the existing brand identity recognizable?"
  - process ask "Are existing files, routes and global stylesheets kept, with changes merged in rather than overwritten or deleted?"
  - page ask "Are existing copy, claims and product names preserved unless the user supplies replacements?"
  - page ask "Are existing accessibility wins preserved, including focus states, alt text, keyboard navigation and contrast?"
  - process ask "Are existing analytics events and the names or IDs tracking depends on left unchanged?"
  - page ask "Do partner brand accents stay from overriding backgrounds and text colors?"
  - state:invalid ask "Does every error say what went wrong (the specific cause when known) and give a next step such as how to fix it, retry or contact support, never dead-ending?"
  - aria:button ask "Is one label used for each intent?"
  - text:* ask "Is one term used for each concept throughout, including either Sign in or Log in everywhere, never mixed?"
  - text:* ask "Do different actions such as delete, remove and archive keep distinct meanings without aliasing?"
  - ui:icon axl:emoji-as-icons == 0
  - page ask "Do elements differ in visual weight by importance, so something still stands out and hierarchy is not eliminated?"
  - state:focus-visible wcag:2.4.7 pass
  - state:focus-visible wcag:1.4.1 pass
  - state:focus-visible ask "Does the focus ring follow the element's border-radius?"
  - aria:combobox ask "Does every click-opened dropdown also show a hover or focus affordance?"
  - text:label margin-bottom == 4px
  - aria:button lighthouse:target-size pass
  - aria:button ask "Are primary actions large and placed where the cursor or thumb already rests (at the bottom of the screen within thumb reach on mobile)?"
  - aria:button ask "Is there exactly one primary action per view section?"
  - ui:card ask "Does each card have at most one primary and one secondary action?"
  - aria:button ask "Do secondary actions look visibly weaker than the primary (outline, ghost or text link), with one filled and at most one ghost button per area?"
  - aria:button lighthouse:interactive-element-affordance pass
  - aria:button ask "Are buttons ranked by importance rather than colored by meaning?"
  - aria:alertdialog ask "Is the loud red destructive treatment used only when destruction is the primary action of that surface?"
  - aria:toolbar ask "Are toolbar filter controls ghost buttons rather than solid primary buttons?"
  - aria:navigation ask "Is there one CTA in the nav, visually distinct from plain links and the page's primary CTA?"
  - page ask "Is the primary action visible before scrolling and unmistakable?"
  - page ask "Can a viewer identify the first thing to read and the primary goal within one second?"
  - page ask "Are calls to action placed at natural decision points rather than repeated as filler?"
  - aria:button ask "Does every CTA fill with an accent color?"
  - aria:menu ask "Are long menus chunked with a recommended default highlighted?"
  - state:invalid wcag:1.4.1 pass
  - state:invalid ask "Does the error state use a distinct error color plus a non-color cue (icon, text or border)?"
  - state:invalid ask "Is the error message shown inline directly below its field?"
  - state:invalid ask "Does the error text stand out from the rest of the form so the user notices it quickly?"
  - state:invalid ask "Does focus move to the offending field on error?"
  - aria:form ask "Are format errors validated on blur or submit, not on every keystroke?"
  - aria:form ask "Does the form validate the information the user gives (emails, required fields and formats) on the client?"
  - page ask "Does every interactive component have designed default, hover, focus, active, disabled, loading and error states?"
  - process ask "Is each screen's state list (empty, loading, error, partial, conflict, offline) marked designed, missing or not applicable?"
  - state:empty ask "Does every view with no data show a designed empty state with a reason and a next action?"
  - state:empty ask "Does a first-use state show the value and offer a first action or template?"
  - ui:skeleton ask "Does a loading skeleton match the final layout geometry?"
  - ui:skeleton lighthouse:cumulative-layout-shift pass
  - ui:skeleton transition-delay == 200ms
  - ui:skeleton ask "Does a skeleton show one pulse or shimmer signal with no spinner on top?"
  - ui:skeleton ask "Is a skeleton used instead of a generic centered spinner for content loading?"
  - aria:progressbar ask "Does a load or skeleton that lasts past 5s escalate to a progress indicator or a timeout message with retry, rather than a skeleton or spinner that waits indefinitely?"
  - aria:progressbar ask "Does a long wait or long operation show truthful progress rather than invented progress?"
  - aria:status ask "Does loading text name the real operation?"
  - aria:status ask "Does a thinking indicator escalate to progress within 2s?"
  - ui:toast ask "Are toasts used only for transient messages, reserved for failures, hidden-effect actions and needed confirmations?"
  - ui:avatar ask "Does every avatar have a fallback for when its image fails to load?"
  - ui:file ask "Does upload state reflect the real upload status?"
  - aria:form ask "Does the form keep the user's valid data, entered fields (including the cart after a declined charge) and in-flight state when an error occurs?"
  - page ask "Does exactly one element carry a memorable signature detail (one signature bet)?"
  - process ask "Does the interface follow established platform and framework conventions instead of inventing custom patterns?"
  - page ask "Does the interface use familiar system gestures, with the simplest gesture for frequent actions and no custom multifinger or multihand gestures people must learn?"
  - page ask "Does the interface match neighboring mental models, terminology and save behaviour?"
  - ui:icon ask "Do icons match cultural convention?"
  - aria:form ask "Does Enter submit a focused single input (or the last control) and Cmd/Ctrl+Enter a textarea, matching platform shortcuts (Cmd+Enter on macOS)?"
  - page ask "Is spacing tighter within groups than between sections, so a rhythm is visible?"
  - text:body max-width <= 65ch
  - aria:main padding >= 24px
  - aria:main gap == 16px
  - aria:form gap == 16px
  - aria:form margin-bottom == 48px
  - page ask "Do adjacent nesting levels use different spacing values?"
  - page ask "Is the density of each view chosen to fit its use frequency and content complexity?"
  - page ask "Does every major block have visible breathing room around it?"
  - ui:card ask "Are cards replaced by border-top dividers or negative space where a card adds nothing, especially in dense layouts?"
  - page wcag:1.4.10 pass
  - aria:main grid-template-columns == 1fr @media:narrow
  - aria:main padding-left >= 16px @media:narrow
  - page ask "Does every multi-column layout collapse to a single column on small screens (below 60rem)?"
  - page ask "Does the layout reduce columns when the font size increases?"
  - page ask "Do blocks and every section's content share the same left and right edges, columns or baselines on a stable grid, including on tinted bands?"
  - page ask "Are any misalignments intentional and explainable?"
  - page ask "Do shared elements in side-by-side cards or columns start at the same vertical position?"
  - ui:icon ask "Are icons, play buttons and button text optically centred, with 1px nudges where geometric centring looks off?"
  - aria:button ask "Is bottom padding slightly larger than top padding where that looks balanced?"
  - aria:button ask "Do icon-leading buttons use slightly less padding on the icon side?"
  - ui:icon ask "Are round shapes drawn slightly larger than square ones so they read as the same size?"
  - page ask "Are breakpoints written in rem so they respect the user's font size?"
  - page ask "Are breakpoints placed where the content breaks rather than at device widths?"
  - aria:heading ask "Do display sizes shrink one step below 40rem?"
  - aria:navigation ask "Is the centre navigation hidden below about 900px, leaving the brand and a CTA or hamburger?"
  - page ask "Does the interface adapt to smaller screens and size changes while keeping functionality and a recognisable layout?"
  - page ask "Does the page use the project's existing breakpoint system, with no magic widths?"
  - aria:img lighthouse:unsized-images pass
  - aria:img lighthouse:image-aspect-ratio pass
  - aria:img lighthouse:image-size-responsive pass
  - ui:card ask "Is the image aspect ratio identical across every card in a grid?"
  - state:hover transition-property contains opacity
  - page ask "Do interactive elements use CSS transitions for state changes?"
  - page ask "Does every clickable card and image react on hover with more than a background colour change?"
  - page ask "Does every animation communicate or confirm a state, hierarchy or relationship?"
  - page ask "Does motion use custom cubic-bezier curves rather than browser default, linear or ease-in-out keywords?"
  - page transition-timing-function contains cubic-bezier
  - page ask "Is bounce or elastic easing avoided on functional UI?"
  - page ask "Is spring easing reserved for primary actions?"
  - page transition-property !contains backdrop-filter
  - page lighthouse:non-composited-animations pass
  - page will-change contains transform
  - page ask "Does the page use one orchestrated entrance instead of motion on every section?"
  - page ask "Would removing this animation lose the user no information?"
  - page axl:cta-wobbles <= 1
  - ui:card ask "Do cards use subtle, soft, wide-spreading drop shadows?"
  - ui:card ask "Are shadows tinted to the background hue rather than pure black?"
  - page ask "Are shadows and elevation reserved for genuinely floating UI (menus, toasts, modals)?"
  - ui:card box-shadow == none @media:dark
  - aria:menu ask "Does an open menu on a low-contrast surface have a hairline stroke and/or shadow pair to separate it from the page?"
  - ui:icon axl:icon-sets <= 1
  - ui:icon axl:distinct-stroke-widths <= 1
  - ui:icon axl:distinct-icon-grids <= 1
  - ui:icon ask "Does the icon corner radius match the overall radius of the token set?"
  - ui:icon ask "Do all icons carry the same optical weight and read as siblings from one family?"
  - ui:icon ask "Is the unmodified default icon set avoided (customised stroke and radius, or a distinctive set)?"
  - ui:icon ask "Are icons from one chosen icon library rather than hand-rolled SVG, with only brand-critical icons drawn custom?"
  - ui:icon ask "Are icons monochrome and outlined by default, with fill used only for the active state?"
  - aria:heading axl:heading-body-weight-gap >= 300
  - aria:heading axl:heading-body-size-ratio >= 1.25
  - page axl:hierarchy-step-ratio >= 1.5
  - page ask "Can a viewer separate headline, evidence and footnote layers at a glance, with the eye landing on things in order of importance?"
  - text:body axl:chars-per-line between 45 75
  - text:* axl:distinct-font-families between 2 3
  - text:* font-family !contains "Inter, Roboto, Open Sans"
  - text:body font-family contains "Inter, Geist"
  - page ask "Does the page pair a distinctive display face with a separate body face?"
  - aria:banner ask "Does the wordmark use a different display face than the body?"
  - text:* font-variant-numeric contains tabular-nums
  - aria:heading text-wrap == balance
  - text:body ask "Is every paragraph three sentences or fewer?"
  - text:body ask "Are paragraphs separated by spacing or first-line indentation, but not both?"
  - page ask "Do font sizes follow one stated modular ratio?"
  - text:* ask "Are font sizes set in rem/em or from scale variables?"
```
