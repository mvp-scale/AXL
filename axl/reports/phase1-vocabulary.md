# Phase 1: vocabulary for review

How rules are grouped and named on screen. **Element names** are what you'll see as rows under each class; the IDs are the standard terms underneath.

## Classes (top level, from the standards)

| Class | Standard it follows |
|---|---|
| Type | CSS Fonts 4, CSS Text 3 |
| Color & theming | CSS Color 4/5, prefers-color-scheme |
| Space & layout | CSS Box Model, Sizing, Flexbox, Grid |
| Surface | CSS Backgrounds & Borders 3 |
| Imagery | CSS Images, Filter Effects |
| Motion | CSS Transitions, CSS Animations |
| Access | WCAG 2.2 |
| Performance | Lighthouse performance, Core Web Vitals |
| Search & metadata | Lighthouse SEO |
| Locale | CSS Writing Modes, Logical Properties |
| Content | none: AXL questions (ask) |
| Process | none: AXL questions (ask) |
| Sound & haptics *(staged)* | Web Audio, Vibration API |

## Elements (the rows), grouped by ARIA's own role categories

| Family | Row name | Standard ID | Found on a page by |
|---|---|---|---|
| Landmarks & navigation | **Navigation** | `aria:navigation` | nav, [role=navigation] |
| Landmarks & navigation | **Page header** | `aria:banner` | body > header, [role=banner] |
| Landmarks & navigation | **Page footer** | `aria:contentinfo` | body > footer, [role=contentinfo] |
| Landmarks & navigation | **Main content** | `aria:main` | main, [role=main] |
| Landmarks & navigation | **Search** | `aria:search` | search, [role=search], input[type=search] |
| Landmarks & navigation | **Breadcrumbs** | `ui:breadcrumb` | nav[aria-label*=readcrumb], .breadcrumb |
| Landmarks & navigation | **Tabs** | `aria:tablist` | [role=tablist] |
| Landmarks & navigation | **Menus** | `aria:menu` | [role=menu], [role=menubar] |
| Document structure | **Display text** | `text:display` | text in the page's largest size band (hero headlines) |
| Document structure | **Headings** | `aria:heading` | h1–h6, [role=heading] |
| Document structure | **Body text** | `text:body` | running text: p, li, td, dd in the page's most common size band |
| Document structure | **Labels** | `text:label` | label, legend, th, small UI text |
| Document structure | **Captions & fine print** | `text:caption` | figcaption, small, text below the body size band |
| Document structure | **Code** | `text:code` | code, pre, kbd |
| Document structure | **All text** | `text:*` | every element with rendered text |
| Document structure | **Links** | `aria:link` | a[href], [role=link] |
| Document structure | **Lists** | `aria:list` | ul, ol, [role=list] |
| Document structure | **Tables** | `aria:table` | table, [role=table], [role=grid] |
| Document structure | **Images** | `aria:img` | img, picture, svg[role=img], [role=img] |
| Document structure | **Icons** | `ui:icon` | small svg/img/glyph beside text or alone in a control |
| Document structure | **Figures & media** | `aria:figure` | figure, video, audio, [role=figure] |
| Document structure | **Charts** | `ui:chart` | svg charts, canvas, [role=graphics-document] |
| Widgets & forms | **Buttons** | `aria:button` | button, [role=button], input[type=submit] |
| Widgets & forms | **Text fields** | `aria:textbox` | input (text types), textarea, [role=textbox] |
| Widgets & forms | **Checkboxes & radios** | `aria:checkbox` | input[type=checkbox|radio], [role=checkbox|radio] |
| Widgets & forms | **Select menus** | `aria:combobox` | select, [role=combobox], [role=listbox] |
| Widgets & forms | **Switches** | `aria:switch` | [role=switch] |
| Widgets & forms | **Sliders** | `aria:slider` | input[type=range], [role=slider] |
| Widgets & forms | **Forms** | `aria:form` | form, [role=form] |
| Widgets & forms | **File uploads** | `ui:file` | input[type=file] |
| Live regions & feedback | **Alerts & errors** | `aria:alert` | [role=alert], [aria-live=assertive] |
| Live regions & feedback | **Status messages** | `aria:status` | [role=status], output, [aria-live=polite] |
| Live regions & feedback | **Toasts** | `ui:toast` | transient status popups |
| Live regions & feedback | **Progress** | `aria:progressbar` | progress, [role=progressbar] |
| Live regions & feedback | **Loading placeholders** | `ui:skeleton` | .skeleton, [aria-busy=true] placeholders |
| Live regions & feedback | **Tooltips** | `aria:tooltip` | [role=tooltip], [title] |
| Windows | **Dialogs** | `aria:dialog` | dialog, [role=dialog] |
| Windows | **Confirmations** | `aria:alertdialog` | [role=alertdialog] |
| Components | **Cards** | `ui:card` | bordered/elevated boxes grouping one item |
| Components | **Badges & tags** | `ui:badge` | small labelled pills |
| Components | **Avatars** | `ui:avatar` | round person images or initials |
| Components | **Carousels** | `ui:carousel` | horizontally scrolling item sets |
| Components | **Accordions & disclosures** | `ui:accordion` | details/summary, [aria-expanded] sections |
| Components | **Popovers & menus** | `ui:popup` | [popover], floating panels |
| States | **Hover** | `state:hover` | :hover |
| States | **Keyboard focus** | `state:focus-visible` | :focus-visible |
| States | **Pressed** | `state:active` | :active, [aria-pressed=true] |
| States | **Disabled** | `state:disabled` | :disabled, [aria-disabled=true] |
| States | **Invalid input** | `state:invalid` | :invalid, [aria-invalid=true] |
| States | **Loading** | `state:busy` | [aria-busy=true] |
| States | **Empty states** | `state:empty` | views with no items (list/table with zero rows) |
| States | **Selected** | `state:selected` | [aria-selected=true], [aria-current] |
| Contexts | **Dark mode** | `media:dark` | prefers-color-scheme: dark |
| Contexts | **Phones** | `media:narrow` | width <= 390px |
| Contexts | **Reduced motion** | `media:reduced-motion` | prefers-reduced-motion: reduce |
| Contexts | **High contrast mode** | `media:forced-colors` | forced-colors: active |
| Contexts | **Print** | `media:print` | print |
| Whole page | **Whole page** | `page` | the document |
| Off the page | **How the work is done** | `process` | not on the page: team or agent process |

## How a rule reads

| On screen | Code underneath |
|---|---|
| All text uses at most 6 font sizes | `text:* axl:distinct-font-sizes <= 6` |
| Body text size is at least 16px | `text:body font-size >= 16px` |
| Text fields size is at least 16px — phones | `aria:textbox font-size >= 16px @media:narrow` |
| Headings line height is at most 1.2 | `aria:heading line-height <= 1.2` |
| Whole page: all spacing sits on the scale | `page axl:spacing-off-scale == 0` |
| Icons include no emoji used as icons | `ui:icon axl:emoji-as-icons == 0` |
| Images have an explicit width and height | `aria:img lighthouse:unsized-images pass` |
| Buttons meet WCAG 2.5.8: target size | `aria:button wcag:2.5.8 pass` |
| Hover transition time is at most 200ms | `state:hover transition-duration <= 200ms` |
| Does every error say what went wrong and how to fix it? | `state:invalid ask "Does every error say what went wrong and how to fix it?"` |

Sources checked: ARIA role names against WAI-ARIA 1.2 (W3C Rec. 2023) + 1.3 draft (Sep 2026); `ui:` names against Open UI's component research list; type roles against Material Web's type-scale tokens. Lists saved in `data/standards/`.