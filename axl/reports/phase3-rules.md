# Phase 3–5 result: every tweak as rules, on the site

**1829 rules** shown on the site (635 measurable, 1194 questions), grouped Class › Element (**280 rows**), each backed by quote IDs.
25 rules had no source statement or public claim behind them and are **not shown** (listed below). 127 `axl:` measures are proposed in `axl/measures.md`; none is implemented yet (phase 4).

| Class | Rules | Measurable | Questions | Element rows |
|---|---|---|---|---|
| Type | 151 | 83 | 68 | 20 |
| Color & theming | 103 | 33 | 70 | 21 |
| Space & layout | 306 | 74 | 232 | 39 |
| Surface | 137 | 80 | 57 | 30 |
| Imagery | 134 | 1 | 133 | 14 |
| Motion | 155 | 63 | 92 | 24 |
| Interaction | 237 | 6 | 231 | 42 |
| Access | 173 | 105 | 68 | 31 |
| Performance | 175 | 150 | 25 | 21 |
| Search & metadata | 13 | 10 | 3 | 4 |
| Locale | 11 | 0 | 11 | 3 |
| Content | 159 | 30 | 129 | 28 |
| Process | 75 | 0 | 75 | 3 |

## What *polish* lights up

| Source | Rules linked | Evidence |
|---|---|---|
| OneRedOak | 72 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Impeccable | 132 | 121 links with quote IDs from its own polish statements; the rest via its definition quote |
| Taste-Skill | 19 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| ui-final-polish | 34 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Anthropic | 8 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Villalba | 31 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| UI Craft | 5 | 1 links with quote IDs from its own polish statements; the rest via its definition quote |
| OpenClaw | 12 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Compound Eng. | 0 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Feel Better | 15 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| Agent Skills Finder | 39 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| UI Skills | 9 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |
| better-web-ui | 9 | 0 links with quote IDs from its own polish statements; the rest via its definition quote |

## Not shown (no evidence on record)

- `aria:status/ask:63dfab`: Are status messages exposed with role status or an aria-live region?
- `page/ask:5352bb`: Is meaningful content kept in the HTML rather than in CSS generated content?
- `aria:table/ask:47ee2f`: Does the table have an empty state when it has no rows?
- `aria:table/ask:dbfb17`: Does selecting rows reveal bulk actions?
- `aria:dialog/ask:d8448b`: Does the modal have a clear close control?
- `aria:dialog/ask:82900e`: Is record detail shown in a side panel?
- `ui:accordion/ask:de2401`: Are disclosures built with native details and summary?
- `ui:accordion/ask:239c14`: Does every accordion behave consistently about whether one or several sections can be open?
- `aria:tablist/ask:35e065`: Is the active tab clearly distinguished from the others?
- `text:*/ask:331f78`: Does each section lead with its conclusion?
- `aria:list/ask:0a572c`: Are parallel items set as bullets rather than paragraphs?
- `page/ask:e6f77e`: Does the interface show a message when the user is offline?
- `aria:region/ask:dae770`: Do content containers use min-height rather than a fixed height?
- `page/lighthouse:render-blocking-insight`: Whole page render blocking insight (Lighthouse) is passes 
- `page/lighthouse:document-latency-insight`: Whole page document latency insight (Lighthouse) is passes 
- `page/lighthouse:cache-insight`: Whole page cache insight (Lighthouse) is passes 
- `page/lighthouse:legacy-javascript-insight`: Whole page legacy javascript insight (Lighthouse) is passes 
- `page/lighthouse:modern-http-insight`: Whole page modern http insight (Lighthouse) is passes 
- `page/lighthouse:bf-cache`: Whole page bf cache (Lighthouse) is passes 
- `page/ask:c1bf0e`: Does the page register a service worker?
- `page/axl:document-write-calls`: Whole page document write calls is 0
- `page/lighthouse:target-size`: Whole page target size (Lighthouse) is passes 
- `page/ask:04749b`: Does the page avoid front-end libraries with known vulnerabilities?
- `aria:link/ask:8fc2a6`: Do external links that open a new tab set rel=noopener?
- `aria:button/ask:c2dab5`: Do buttons use stronger typography than surrounding body text?

## How it was made

1. Every harvested statement got a permanent quote ID (`scripts/assign_ids.py`).
2. Agents expressed each tweak as rules (`data/rules_src/*.json`). A validator accepted only element IDs from ARIA / Open UI / the vocabulary, properties from Chromium's CSS list, WCAG 2.2 criteria, Lighthouse 13.5 audits or declared `axl:` measures, and quote IDs from that tweak's own statements.
3. Agents merged duplicate questions across areas (`data/rules_src/_questions.json`); a script checked that no question was dropped or invented.
4. `scripts/build_rules.py` merges rules by element + property (different values = one rule with a disagreement; the default is the value most statements give) and links every command definition to rules (`data/commands.json`).
