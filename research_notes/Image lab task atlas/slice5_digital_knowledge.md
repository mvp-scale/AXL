# Slice 5: Digital and knowledge work (domains 41–50)

Researched 2026-10-01. All dataset facts were fetched in this session from the Hugging Face Hub API (`/api/datasets/<id>?blobs=true`, `/tree`), datasets-server (`/splits`, `/first-rows`, `/rows`, `/statistics`, `/parquet`), raw GitHub files, or owner pages. No candidate had more than 50 MB downloaded. The largest single downloads were the Open Images val label CSV (28.4 MB), Pitt Ads `Topics.json` (2.3 MB), ChartBench `test.jsonl` (3.9 MB), a 400 KB range read of the VisDrone `samples.json`, and a 64 KB range read of the end of the ChartBench `test.zip`.

Evidence tags: [ROW] seen in a fetched row · [CARD] owner page, card or README · [PAPER] · [INFERRED] · [UNVERIFIED].

**Format note.** The output follows Part 1 of `_spec.md` exactly: atlas, cards, CSV, Gaps, Cannot verify, then Part C. The researcher template's three-section layout was not used because the spec's order is required.

**Domain swaps: none.** Domain 49 (customer service) has almost no open labelled data. I kept it rather than swap it, because its most valuable tasks can be drawn by a generator (see Gaps) and two tasks have USE data from Open Images.

**Strict-rating notes, applied throughout:**
- When the licence appears only on a third-party mirror and not on the owner's page, the candidate is rated MAYBE ("licence not from owner").
- A gated owner download with an open mirror is rated GATED. The mirror may hold the same data.
- Open Images "verified negative" rows (Confidence 0) are real human-checked negatives. When a label is simply absent, that is **not** a negative. Answer rules below use only explicit rows.

---

## 1. Task atlas

### D41: IT support and software screenshots
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D41.1 | Identify the application in a ticket screenshot | "Which application is shown in this screenshot?" | 4–6 app names (e.g. Excel, Word, PowerPoint, VS Code, PyCharm, MATLAB) | screenshot | Routing a ticket to the right resolver group is the main lever on cost. Tier-1 tickets cost about $6 and Tier-3 escalations can exceed $35 per ticket; average resolution is 82 h (vendor blog, secondary) — [unthread](https://unthread.io/blog/support-ticket-resolution-statistics/) |
| D41.2 | Identify the operating system | "Which operating system is this screenshot from?" | Windows / macOS / Linux | screenshot | Same routing value. OS decides the troubleshooting script — same source as D41.1 |
| D41.3 | Software category for queue routing | "What kind of software is open?" | Development / Creative / CAD / Scientific / Office / Operating system | screenshot | Same as D41.1 |
| D41.4 | Error dialog present | "Does the screenshot show an error or warning dialog?" | yes / no | screenshot | Same as D41.1. No dataset found (see Gaps) |
| D41.5 | Dark mode / theme | "Is the application in dark mode?" | yes / no | screenshot | No business source found. Low value, kept as a cheap generator task |

### D42: Web and mobile UI quality
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D42.1 | Screen type classification for QA coverage | "What type of screen is this?" | e.g. login / list / form / gallery / settings / tutorial | screenshot (mobile) | Apple Guideline 2.1 (app completeness) rejects incomplete or placeholder screens. Reviewers report it as the most common rejection group — [Apple App Review Guidelines PDF](https://developer.apple.com/support/downloads/terms/app-review-guidelines/App-Review-Guidelines-English-UK.pdf); [RevenueCat summary](https://revenuecat.com/blog/growth/the-ultimate-guide-to-app-store-rejections/) |
| D42.2 | Login / sign-up screen detection | "Is this a login or sign-up screen?" | yes / no | screenshot | Same as D42.1. Login flows must work for review, and a demo account is required |
| D42.3 | Website vertical | "Which kind of website is this?" | Travel / Shopping / Entertainment | screenshot (web, long) | Ad and compliance routing. No direct source found |
| D42.4 | Visual defect (overlap, truncation, occlusion) | "Does any text or component overlap or get cut off?" | yes / no | screenshot | 94.8% of the top 1M home pages have detectable WCAG failures — [WebAIM Million 2025](https://webaim.org/projects/million/2025) |
| D42.5 | Placeholder content left in UI | "Is placeholder text (e.g. 'Lorem ipsum') visible?" | yes / no | screenshot | Apple rejects apps with placeholder content (Guideline 2.1) — [Apple PDF](https://developer.apple.com/support/downloads/terms/app-review-guidelines/App-Review-Guidelines-English-UK.pdf) |
| D42.6 | Low-contrast text | "Is there text with insufficient contrast against its background?" | yes / no | screenshot | 79.1% of home pages have low-contrast text — [WebAIM Million 2025](https://webaim.org/projects/million/2025) |

### D43: Dashboards, charts and BI
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D43.1 | Chart type | "What type of chart is this?" | bar / line / pie / area / scatter / box (subset of 9) | rendered chart | Poor data quality costs organisations about $12.9M/yr (Gartner, via secondary page) — [Verato citing Gartner](https://verato.com/resources/gartner-dq) |
| D43.2 | Pairwise comparison check | "At <x>, is series A higher than series B?" | yes / no | rendered chart | Same as D43.1. Misread dashboards drive wrong decisions |
| D43.3 | Value-claim verification | "Does the chart show <series> at <x> = <value>?" | yes / no | rendered chart | Same as D43.1. This is the "does the slide match the number?" check |
| D43.4 | Do lines cross | "Do any lines intersect?" | yes / no | real chart (arXiv figure) | Same as D43.1 |
| D43.5 | Panel count | "How many subplots does this figure have?" | 1 / 2 / 3 / 4 / 5+ | real chart | Same as D43.1 |
| D43.6 | Max/min series | "Which series is the maximum?" | 2–6 legend names | rendered chart | Same as D43.1 |

### D44: Maps, satellite and drone imagery
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D44.1 | Post-flood scene triage | "Is this area flooded?" | yes / no | aerial (UAV) | FEMA uses aerial imagery for damage assessment and relief-funding decisions. Nearmap captured 57,000 sq mi of disaster areas in 2024 — [DroneLife](https://dronelife.com/2026/02/11/nearmap-and-new-light-deploy-fema-disaster-response-system/); [NOAA](https://oceanservice.noaa.gov/news/jul25/ngs-texas-flooding.html) |
| D44.2 | Road passability | "Is the entire road flooded?" | yes / no | aerial (UAV) | Same as D44.1 |
| D44.3 | Building count bucket | "How many buildings are visible?" | 0 / 1–3 / 4–6 / 7+ | aerial (UAV) | Same as D44.1 (exposure counting) |
| D44.4 | Land-use type | "What land use does this tile show?" | 4–6 of airport / port / parking / residential / industrial / farmland … | satellite | No source fetched. Common in insurance and site selection [UNVERIFIED] |
| D44.5 | Vehicle presence in drone frame | "Is there a truck in this image?" | yes / no | aerial (drone, oblique) | No source fetched |
| D44.6 | Rooftop solar present | "Does this roof have solar panels?" | yes / no | aerial | No source fetched. Gap |

### D45: Education (worksheets, handwriting, diagrams)
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D45.1 | Auto-mark multiple-choice worksheet item | "Which option correctly answers the question shown?" | 2–5 given choices | drawing / worksheet image | English teachers spend 9.4–9.7 h/week marking (DfE survey of 44,000 teachers, reported by SecEd) — [SecEd](https://www.sec-ed.co.uk/content/news/teachers-spend-nine-hours-a-week-marking-despite-lack-of-evidence-that-it-works) |
| D45.2 | Diagram comprehension item | "Which option answers the diagram question?" | 4 choices | textbook diagram | Same as D45.1 |
| D45.3 | Worksheet subject routing | "What subject is this worksheet item?" | natural science / language science / social science | worksheet image | Same as D45.1 |
| D45.4 | Yes/no worksheet item | "Answer this yes/no item" | yes / no | worksheet image | Same as D45.1 |
| D45.5 | Handwritten answer correct | "Does the handwritten answer equal <value>?" | yes / no | handwriting scan | Same as D45.1. No dataset (Gap) |

### D46: Publishing, media and archives
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D46.1 | Document category triage | "What kind of document is this page from?" | financial report / scientific article / law or regulation / government tender / manual / patent | scan/render | NARA aims to digitise 500M pages by FY2026 and holds more than 13 billion analog pages — [FedScoop](https://fedscoop.com/nara-targets-digitization-of-500-million-pages-by-2026-in-draft-strategic-plan/); [archives.gov](https://www.archives.gov/digitization) |
| D46.2 | Table present (routes to table extraction) | "Does this page contain a table?" | yes / no | scan/render | Same as D46.1 |
| D46.3 | Newspaper page content (photograph, map, advert) | "Does this newspaper page contain a photograph?" (or map / advertisement) | yes / no | historical scan | Same as D46.1 |
| D46.4 | Typeface group of early printed page | "Which typeface group is used on this page?" | antiqua / italic / textura / fraktur / schwabacher / rotunda … | photo of book page | Same as D46.1 (cataloguing) |
| D46.5 | Illustrated advert | "Does this advert contain an illustration?" | yes / no | newspaper crop | Same as D46.1 |
| D46.6 | Manuscript dating | "In which century was this manuscript written?" | 3–6 centuries | photo of manuscript | Same as D46.1 |
| D46.7 | Page orientation | "Is this page rotated?" | 0° / 90° / 180° / 270° | scan | Same as D46.1. Generator task |

### D47: Marketing and ad compliance
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D47.1 | Restricted-category ad | "Is this an ad for alcohol, gambling or tobacco/smoking?" | yes / no | ad image | Google restricts alcohol and gambling ads by certification and geography. Violations can suspend accounts — [Google Ads policy](https://support.google.com/adspolicy/answer/2684542); [summary](https://stubgroup.com/glossary/restricted-content-policy/) |
| D47.2 | Ad topic routing | "What is this ad selling?" | e.g. clothing / cars / beauty / soda / restaurant / electronics | ad image | Same as D47.1 |
| D47.3 | Image contains advertising | "Does this image contain advertising?" | yes / no | photo | Same as D47.1 |
| D47.4 | Sponsored-content disclosure visible | "Is an '#ad' / 'Sponsored' disclosure visible?" | yes / no | social post screenshot | FTC Endorsement Guides: disclosures must be "clear and conspicuous" and visual when the endorsement is visual (law-firm summary) — [Quarles](https://quarles.com/newsroom/publications/deciphering-the-ftcs-updated-guidance-for-advertisers) |
| D47.5 | Billboard present (OOH audit) | "Is there a billboard in this photo?" | yes / no | photo | No source fetched |

### D48: Fashion and beauty
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D48.1 | Attribute tagging: dress | "Is the person wearing a dress?" | yes / no | photo | Fashion return rates of 20–40%+ are driven by inaccurate product data (vendor blog) — [Bluestone PIM](https://www.bluestonepim.com/blog/how-fashion-retailers-reduce-returns-with-pim) |
| D48.2 | Main garment category | "What is the main garment in this photo?" | dress / pants / skirt / jacket / shirt / coat | photo | Same as D48.1 |
| D48.3 | Accessory present | "Is there a bag or wallet in the image?" | yes / no | photo | Same as D48.1 |
| D48.4 | Catalogue category | "Which product category is this?" | Apparel / Footwear / Accessories / Personal Care | product photo | Same as D48.1 |
| D48.5 | Cosmetics present | "Is there lipstick in the image?" | yes / no | photo | Same as D48.1 |

### D49: Customer service (photos of faults, error screens)
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D49.1 | Screenshot vs camera photo intake triage | "Is this image a screenshot?" | yes / no | mixed | Visual support cuts truck rolls by 15–47% (vendor) — [Grypp](https://grypp.io/visual-support-reduces-truck-rolls/) |
| D49.2 | Which device is in the photo | "Which device is shown?" | mobile phone / laptop / computer monitor | photo | Same as D49.1 |
| D49.3 | Photo usable for diagnosis | "Is this photo sharp enough to read?" | yes / no | photo | Same as D49.1. Generator task |
| D49.4 | Cracked screen | "Is the device screen cracked?" | yes / no | photo | Same as D49.1. Gap |
| D49.5 | Error message on device screen | "Is an error message displayed?" | yes / no | photo or screenshot | Same as D49.1. Gap |

### D50: Content moderation and brand safety
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D50.1 | Weapon present | "Does the image contain a weapon?" | yes / no | photo | No primary brand-safety source fetched (a GARM search returned nothing relevant) |
| D50.2 | Alcohol present | "Does the image show an alcoholic beverage?" | yes / no | photo | Google restricted-content policy — [Google Ads](https://support.google.com/adspolicy/answer/2684542) |
| D50.3 | Brand/logo visible | "Is a brand logo visible?" | yes / no | photo | Counterfeit trade is USD 467bn (2.3% of world imports); clothing, footwear and leather make up 62% of seizures — [OECD/EUIPO 2025](https://www.oecd.org/en/about/news/press-releases/2025/05/global-trade-in-fake-goods-reached-USD-467-billion-posing-risks-to-consumer-safety-and-compromising-intellectual-property.html) |
| D50.4 | Logo's industry | "Which industry does this logo's brand belong to?" | Food / Clothes / Necessities / Electronic / Transportation / Leisure | photo/crop | Same as D50.3 |
| D50.5 | Visible watermark (rights check) | "Does the image have a visible watermark?" | yes / no | photo | No source fetched |
| D50.6 | Counterfeit product | "Is this product counterfeit?" | yes / no | photo | OECD/EUIPO as D50.3. No open data (Gap) |

---

## 2. Dataset cards

### D41.1 / D41.2 / D41.3: ScreenSpot-Pro (rank 1). One dataset, three tasks
1. **Landing**: https://huggingface.co/datasets/likaixin/ScreenSpot-Pro · GitHub https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding · **Files**: https://huggingface.co/api/datasets/likaixin/ScreenSpot-Pro/tree/main/annotations · repo id `likaixin/ScreenSpot-Pro` [CARD]
2. **Licence**: HF card YAML `license: mit` [CARD]. GitHub LICENSE: "MIT License … Copyright (c) 2026 Kaixin Li" (https://raw.githubusercontent.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/main/LICENSE) [CARD]. No research restriction and no form.
3. **Access**: open (`gated: False`) [CARD]
4. **Size**: 1,619 files, 3,376 MB total. 26 annotation JSONs, one per app/OS; smallest `annotations/illustrator_windows.json` = 0.02 MB. Each screenshot is its own PNG (largest 22.9 MB). Not a single archive. [CARD]
5. **Sample-first proof**: `curl -L https://huggingface.co/datasets/likaixin/ScreenSpot-Pro/resolve/main/annotations/illustrator_windows.json` (31 entries) [ROW]
   - `{"img_filename": "illustrator_windows/screenshot_2024-11-29_17-39-25.png", "bbox": [2618, 193, 2790, 221], "instruction": "select ellipse tool", "id": "illustrator_windows_0", "application": "illustrator", "platform": "windows", "img_size": [5120, 1440], "ui_type": "text", "group": "Creative"}`
   - `{"img_filename": "illustrator_windows/screenshot_2024-11-29_17-42-44.png", "bbox": [2802, 623, 2868, 649], "instruction": "group the selected contents", "id": "illustrator_windows_1", "application": "illustrator", "platform": "windows", "img_size": [5120, 1440], "ui_type": "text", "group": "Creative"}`
   - `{"img_filename": "illustrator_windows/screenshot_2024-11-29_17-54-35.png", "bbox": [3632, 639, 3758, 662], "instruction": "don't use compression", "id": "illustrator_windows_2", "application": "illustrator", "platform": "windows", "img_size": [5120, 1440], "ui_type": "text", "group": "Creative"}`
6. **Schema**: `img_filename` str; `bbox` [x1,y1,x2,y2] target element; `instruction` str (grounding command, not used here); `application` str (app id); `platform` str (windows/macos/linux); `img_size` [w,h]; `ui_type` text/icon; `group` str (Dev/Creative/CAD/Scientific/Office/OS) [ROW]
7. **Label origin**: human. Annotators captured screenshots of real professional apps that they operate (the card's app table lists version and OS) [CARD]. The paper's annotation method was not read [UNVERIFIED]. `application`, `platform` and `group` are the capture context, not model output [INFERRED].
8. **Answer rule**: D41.1 answer = `application` (dedupe by `img_filename`). D41.2 answer = `platform`. D41.3 answer = `group`.
9. **Classes**: 23 apps + common_{windows,macos,linux}. Card table: VS Code, PyCharm, Android Studio, Quartus, VMware, Photoshop, Premiere, Illustrator, Blender, FL Studio, Unreal, DaVinci, AutoCAD, SolidWorks, Inventor, Vivado, MATLAB, Origin, Stata, EViews, Word, PowerPoint, Excel [CARD]. Each app appears on exactly one OS in the table [CARD], so D41.2 is confounded with app (see risks). Pick-one, so negatives are not applicable.
10. **Per-image fit**: one app per screenshot [INFERRED from per-app folders]. Several instructions point to the same image, so dedupe on `img_filename`.
11. **Risks**: very large images (5120×1440 and up); downscaling to 1536 px makes small text unreadable, but app identity survives [INFERRED]. Possible user names or file paths in screenshots [INFERRED]. ScreenSpot-Pro is a popular GUI benchmark, so contamination risk is high. OS is perfectly correlated with app, so D41.2 can be solved by app recognition; balance with the `common_*` OS screenshots.
12. **Templates**: "Which application is open? {Excel, Word, PowerPoint, VS Code}" · "Which OS is this screenshot from? {Windows, macOS, Linux}" · "Which category of software is shown? {Development, Creative, CAD, Scientific, Office, Operating system}".
- **Verdict**: USE (high).

### D42.1 / D42.2: Enrico (rank 1)
1. **Landing**: https://github.com/luileito/enrico · **Files**: https://raw.githubusercontent.com/luileito/enrico/master/design_topics.csv. Screenshots: http://userinterfaces.aalto.fi/enrico/resources/screenshots.zip, or HF mirror `Leonardo6/enrico` (https://huggingface.co/datasets/Leonardo6/enrico) [CARD]
2. **Licence**: GitHub LICENSE "MIT License · Copyright (c) 2020 Luis A. Leiva, Asutosh Hota, Antti Oulasvirta" (https://raw.githubusercontent.com/luileito/enrico/master/LICENSE) [CARD]. Mirror says apache-2.0 [CARD], which differs from the owner. Use the owner's MIT.
3. **Access**: open
4. **Size**: labels CSV 1,461 lines (<0.1 MB) [ROW]. Screenshots SINGLE ARCHIVE 110 MB (README) [CARD]. HF mirror parquet 125.8 MB [CARD]. Single images can be fetched through datasets-server `/rows` (signed image URL per row) [INFERRED]
5. **Sample-first proof**: `curl -L .../design_topics.csv | head` [ROW]
   - `screen_id,topic` / `50245,tutorial`
   - `320,list`
   - `39729,login`
   - Mirror rows also fetched (first-rows of `Leonardo6/enrico`): assistant answers "tutorial", "list", "login" with images 1080×1920, 1080×1920, 540×960 [ROW]
6. **Schema**: `screen_id` int (RICO screen id), `topic` str (one of 20 design topics) [ROW/CARD]
7. **Label origin**: human. "We have manually curated a random sample of 10k UIs from Rico … 1460 UIs classified according to 20 design topics" [CARD]. Screenshots come from RICO; the RICO *view-hierarchy annotations* were rejected as machine labels, but these topic labels are manual.
8. **Answer rule**: D42.1 answer = `topic` (restrict to a 4–6 option subset, e.g. {login, list, form, gallery, settings, tutorial}). D42.2: yes if `topic == "login"`, no otherwise.
9. **Classes** [CARD]: bare 76, dialer 6, camera 8, chat 11, editor 18, form 103, gallery 144, list 265, login 141, maps 9, mediaplayer 32, menu 79, modal 67, news 59, other 52, profile 63, search 35, settings 90, terms 39, tutorial 163. D42.2 has real negatives: 141 yes vs 1,319 no.
10. **Per-image fit**: one topic per screen [CARD]. Drop `other` and `bare`.
11. **Risks**: RICO apps date from about 2017, so the look is dated. Screens may hold user names or emails [INFERRED]. The categories are somewhat subjective, e.g. list vs news [INFERRED]. RICO is common in training data. 540×960 resolution is acceptable.
12. **Templates**: "What type of screen is this? {login, list, form, gallery, settings, tutorial}" · "Is this a login screen? {yes, no}" · "Is this an onboarding/tutorial screen? {yes, no}".
- **Verdict**: USE (high).

### D42.3: Multimodal-Mind2Web (rank 1)
1. https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web · repo `osunlp/Multimodal-Mind2Web` [CARD]
2. **Licence**: card YAML `license: openrail` [CARD]. OpenRAIL is a model-oriented licence; it is unclear how it applies to data [INFERRED].
3. **Access**: open
4. **Size**: 49 files, 13,577 MB. Smallest data shard about 217.7 MB [CARD]. Use `/rows` for single rows.
5. **Proof**: `/first-rows?dataset=osunlp/Multimodal-Mind2Web&config=default&split=train` [ROW]
   - `{"action_uid":"6c7a7082-…","website":"united","domain":"Travel","subdomain":"Airlines","confirmed_task":"rent a car in Brooklyn - Central, NY on from April 9 to April 15.","screenshot":1280x5429}`
   - `{"action_uid":"b64c2417-…","website":"united","domain":"Travel","subdomain":"Airlines", "operation":{"op":"TYPE","value":"Brooklyn Central"}, "screenshot":1280x5429}`
   - `{"action_uid":"dad6690b-…","website":"united","domain":"Travel","subdomain":"Airlines","operation":{"op":"CLICK"}, "screenshot":1280x5429}`
6. **Schema**: `website`, `domain`, `subdomain` str; `screenshot` image; HTML and action fields [ROW]
7. **Label origin**: human-chosen website taxonomy [INFERRED; paper not read, UNVERIFIED]
8. **Answer rule**: answer = `domain`.
9. **Classes** (test_website stats): Shopping 415, Travel 367, Entertainment 237 [ROW/statistics]
10. **Per-image fit**: one domain per site. Many near-identical screenshots per task, so sample one per `annotation_id`.
11. **Risks**: extremely tall screenshots (1280×5429) need cropping to the first viewport. Live-site content may include personal data [INFERRED].
12. **Templates**: "Which kind of website is this? {Travel, Shopping, Entertainment}" · "Which subdomain? {Airlines, Car rental, …}" · "Is this an airline website? {yes, no}"
- **Verdict**: MAYBE. It fails the label-origin check: the origin is inferred, not quoted, and the licence's fit for data is unclear.

### D42.4 (rejected candidate): zxy6654/multiwindow-gui-defect-benchmark
- https://huggingface.co/datasets/zxy6654/multiwindow-gui-defect-benchmark. Card is YAML-only (`license: cc-by-4.0`) and has no description [CARD]. 439 files, 92.5 MB. first-rows show image-only rows (507×900, 507×900, 640×1136) with **no label column** [ROW]. Label origin UNVERIFIED and no answer rule exists. **SKIP** (it fails the question-cannot-be-computed check).

### D43.1 / D43.2 / D43.3: ChartBench (rank 1)
1. https://huggingface.co/datasets/SincereX/ChartBench · repo `SincereX/ChartBench` · files `test.jsonl`, `data/test.zip` [CARD]
2. **Licence**: card YAML `license: mit` [CARD]. The card also carries an `extra_gated_prompt` ("You agree to not use the dataset to conduct experiments that cause harm to human subjects…"), but the API reports `gated: False` and files downloaded without login [CARD/ROW].
3. **Access**: open
4. **Size**: total 10,449 MB. `test.jsonl` 3.86 MB. Test images are a SINGLE ARCHIVE `data/test.zip` of 227.67 MB. A 64 KB tail range read found the zip end-of-central-directory: 10,552 entries, central directory 1.29 MB. Single images can therefore be pulled by HTTP range ("remote zip") [ROW]; the per-file extraction itself was not tested [UNVERIFIED].
5. **Proof**: downloaded `test.jsonl` (10,500 records) [ROW]
   - `{"id": 1000, "image": "./data/test/bar/horizontal_percent_stacked/chart_1/image.png", "type": {"chart": "bar", "image": "horizontal_percent_stacked", "task": "CR", "QA": "Acc+"}, "conversation": [{"label": "Yes", "query": "This graph is a bar chart, instead of others chart."}, {"label": "No", "query": "This graph is a others chart, instead of bar chart."}]}`
   - `{"id": 1001, … "task": "VE" …, "conversation": [{"label": "Yes", "query": "According to this chart, the percentage of Malaysia at Year 2022 is 5.78."}, {"label": "No", "query": "According to this chart, the percentage of Malaysia at Year 2022 is 14.80."}]}`
   - `{"id": 1002, … "task": "VC" …, "conversation": [{"label": "Yes", "query": "According to this chart, at Year 2016, the percentage of Philippines is higher than Vietnam."}, {"label": "No", "query": "According to this chart, at Year 2016, the percentage of Vietnam is higher than Philippines."}]}`
6. **Schema**: `id` int; `image` path inside the zip; `type.chart` (9 coarse types); `type.image` (42 subtypes); `type.task` ∈ {CR chart recognition, VE value extraction, VC value comparison, GC global conception, NQA numeric QA}; `conversation[]` = {`query` assertion, `label` Yes/No or a number for NQA} [ROW]
7. **Label origin**: generator. Charts are plotted from known data, and assertions are built from that data (paired true/false) [INFERRED from paired templates; paper not read, UNVERIFIED].
8. **Answer rule**: D43.1 answer = `type.chart` (choose 4–6 options from the 9). D43.2: take a `task=="VC"` record and pick either conversation item; answer = `label`. D43.3: same, with `task=="VE"`.
9. **Classes**: chart counts (records) bar 3250, line 1250, pie 1250, combination 1000, radar 1000, area 750, box 750, scatter 750, node_link 500. Tasks 2,100 each. Yes 8,456 / No 8,444, so real negatives are balanced by construction. 2,100 unique images [ROW]
10. **Per-image fit**: one chart type per image; each assertion has a single answer.
11. **Risks**: synthetic look. Data values were possibly LLM-generated [UNVERIFIED]. The "combination" type is ambiguous for chart-type questions, so exclude it. The CR assertion "instead of others chart" is odd phrasing, so build our own question from `type.chart`.
12. **Templates**: "What type of chart is this? {bar, line, pie, area, scatter, box}" · "At Year 2016, is Philippines higher than Vietnam? {yes, no}" · "Does the chart show Malaysia at Year 2022 = 5.78? {yes, no}".
- **Verdict**: USE (med; the archive is sampleable but per-file extraction was not tested).

### D43.2 / D43.6: FigureQA (rank 2)
1. Owner page https://www.microsoft.com/en-us/research/project/figureqa-dataset/ (download page shows "Agree & Download" plus a "Licensing" tab) [CARD]. Mirror `vikhyatk/figureqa` (https://huggingface.co/datasets/vikhyatk/figureqa)
2. **Licence**: owner requires click-through agreement; text not read [UNVERIFIED]. Mirror card has no licence [CARD].
3. **Access**: GATED at the owner (accept terms). The mirror is open but may be the same data.
4. **Size**: mirror 2,218 MB, smallest shard 321.4 MB [CARD]. Owner download "5.78 GB uncompressed" [CARD].
5. **Proof (mirror)** `/first-rows?dataset=vikhyatk/figureqa` [ROW]: row0 qa includes `{"question":"Is Pale Green the minimum?","answer":"No."}`, `{"question":"Is Light Green the high median?","answer":"Yes."}`; row1 `{"question":"Is Saddle Brown the minimum?","answer":"Yes."}`; row2 `{"question":"Is Navy Blue the maximum?","answer":"Yes."}`
6. **Schema (mirror)**: `image`, `qa[]{question, answer}`. The original's colour/value metadata is missing from the mirror [ROW]
7. **Label origin**: generator (synthetic plots with templated questions) [INFERRED]
8. **Answer rule**: answer = `qa[i].answer` (Yes./No.)
9. **Classes**: yes/no both present [ROW]; counts UNVERIFIED
10. **Per-image fit**: many questions per image; pick one.
11. **Risks**: colour-name reasoning only; widely used in training.
12. **Templates**: "Is <colour> the maximum?" · "Is <A> greater than <B>?" · "Is <colour> the low median?"
- **Verdict**: GATED (the owner requires agreement; the mirror has no licence).

### D43.6: DVQA (rank 3)
1. Owner https://github.com/kushalkafle/DVQA_dataset (Google Drive links) [CARD]. Mirror `vikhyatk/dvqa`.
2. **Licence**: no licence statement found in the owner README [UNVERIFIED]. Mirror has none.
3. **Access**: open (Google Drive / HF mirror)
4. **Size**: mirror 4,272.5 MB, shards about 473 MB each [CARD]
5. **Proof** (mirror first-rows) [ROW]: row0 `{"question":"Which bar has the largest value?","answer":"Soil."}`, `{"question":"Is the value of soil larger than essay?","answer":"Yes."}`; row1 `{"question":"Which object is the most preferred?","answer":"Land."}`; row2 `{"question":"Is the accuracy of the algorithm corps in the dataset iron smaller than … muscle in the dataset notice?","answer":"Yes."}`
6–8. `image`, `qa[]`. Generator-made bar charts [INFERRED]. Answer = `qa.answer`.
9–12. Max-bar questions are pick-one among bar labels. Risk: no licence. Template: "Which bar has the largest value? {<bar labels>}"
- **Verdict**: MAYBE (fails the licence check).

### D43.4 / D43.5: CharXiv (rank 1)
1. https://huggingface.co/datasets/princeton-nlp/CharXiv (owner org) · templates in https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/src/constants.py [CARD]
2. **Licence**: card YAML `license: cc-by-sa-4.0` [CARD]. Charts are arXiv figures whose copyright varies [INFERRED].
3. **Access**: open
4. **Size**: 375.9 MB total; `images.zip` 141.45 MB; `test.parquet` 91.67 MB. validation parquet size UNVERIFIED (<92 MB by elimination [INFERRED]). Single rows via `/rows`.
5. **Proof**: first-rows (validation) [ROW]
   - `{"figure_path":"images/0.jpg","num_subplots":2,"subplot_row":1,"subplot_col":2,"descriptive_q1":7,"descriptive_a1":"60","descriptive_q3":11,"descriptive_a3":"Yes","reasoning_q":"Which model shows a greater decline in accuracy from Session 1 to Session 9…","reasoning_a":"Joint-CNN"}` (image 1024×496)
   - `{"figure_path":"images/2.jpg","num_subplots":1,"descriptive_q1":2,"descriptive_a1":"W_H","descriptive_q2":8,"descriptive_a2":"0.1","descriptive_q3":7,"descriptive_a3":"0.12"}` (1024×760)
   - `{"figure_path":"images/3.jpg","num_subplots":2,"descriptive_q1":18,"descriptive_a1":"1 by 2","descriptive_q3":19,"descriptive_a3":"2"}` (1024×502)
6. **Schema**: `descriptive_qK` int = template id (1–19, e.g. 11 "Do any lines intersect?", 18 "layout of the subplots", 19 "number of subplots" [CARD constants.py]); `descriptive_aK` str answer; `num_subplots` int16; `reasoning_q/a` str [ROW]
7. **Label origin**: human. Answers are human-curated per the benchmark design [INFERRED; paper not read, UNVERIFIED].
8. **Answer rule**: D43.4: find K where `descriptive_qK == 11`; answer = `descriptive_aK` (Yes/No). D43.5: answer = `num_subplots` bucketed {1,2,3,4,5+}, or `descriptive_aK` where q=19.
9. **Classes**: Yes/No balance for q11 UNVERIFIED (row 0 shows "Yes"). Subplot counts include 1 and 2 [ROW].
10. **Per-image fit**: one answer per template per figure.
11. **Risks**: test-split answers may be withheld [UNVERIFIED], so use validation. Real arXiv figures are likely in pretraining.
12. **Templates**: "Do any lines intersect? {yes, no}" · "How many subplots? {1,2,3,4,5+}" · "What is the subplot layout? {1 by 1, 1 by 2, 2 by 2, …}"
- **Verdict**: USE (med; label origin is inferred from the benchmark design).

### D44.1 / D44.2 / D44.3: FloodNet Track 2 VQA (rank 1)
1. Owner https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021 (Google Drive) [CARD] · HF mirror https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF (DatasetNinja/Supervisely format)
2. **Licence**: mirror YAML `license: cc-by-sa-4.0` [CARD]. No licence line found in the owner README (grep for "licen") [UNVERIFIED].
3. **Access**: open
4. **Size**: mirror 12,310 MB; 1,448 train + 450 val + 450 test images, each with a per-image JSON (about 1 KB). Images about 7 MB each, 4000×3000 [CARD/ROW]
5. **Proof**: fetched `train_image/ann/*.json` [ROW]
   - `10170.JPG.json`: `{'Question': 'What is the overall condition of the given image?', 'Ground_Truth': 'non flooded', 'Question_Type': 'Condition_Recognition'}`, `{'Question': 'Is the entire road non flooded?', 'Ground_Truth': 'Yes', 'Question_Type': 'Yes_No'}`, `{'Question': 'How many buildings can be seen in this image?', 'Ground_Truth': 4, 'Question_Type': 'Simple_Counting'}`
   - `10171.JPG.json`: `{'Question': 'Is the entire road flooded?', 'Ground_Truth': 'No', 'Question_Type': 'Yes_No'}`, overall `'non flooded'`, building count 4
   - first-rows row 0: `{'Question': 'What is the overall condition of the given image?', 'Ground_Truth': 'flooded', 'Question_Type': 'Condition_Recognition'}` (3000×4000)
6. **Schema**: `tags[].value` = stringified dict {Question_ID, Question, Ground_Truth (str or int), Question_Type ∈ {Simple_Counting, Complex_Counting, Condition_Recognition, Yes_No}}; `size{height,width}` [ROW]
7. **Label origin**: human VQA annotation per the challenge README [CARD], which describes the question categories; the annotation method is UNVERIFIED. The `labelerLogin: inbox@datasetninja.com` field is the converter's account, not the annotator.
8. **Answer rule**: D44.1 answer = Ground_Truth of "What is the overall condition of the given image?" (flooded→yes). D44.2 answer = Ground_Truth of "Is the entire road flooded?" (invert for "…non flooded?"). D44.3 = bucket(Simple_Counting answer).
9. **Classes**: a 1-in-10 sample of 145 train images gave overall flooded 24 / non flooded 121. Road yes/no 50 yes-type and 39 no-type answers across both phrasings. Real negatives exist [ROW]
10. **Per-image fit**: one condition answer per image.
11. **Risks**: owner licence UNVERIFIED. Large images (4000×3000, fine to downscale). Class imbalance (about 17% flooded). Counting answers on dense scenes are noisy [INFERRED].
12. **Templates**: "Is this area flooded? {yes,no}" · "Is the entire road flooded? {yes,no}" · "How many buildings are visible? {0,1–3,4–6,7+}"
- **Verdict**: MAYBE (licence only on the mirror).

### D44.4: WHU-RS19 (rank 1)
1. Mirror https://huggingface.co/datasets/jonathan-roberts1/WHU-RS19. Owner page not found; card cites the paper https://hal.science/hal-00458685/document [CARD]
2. **Licence**: mirror YAML `cc-by-4.0`. The "Licensing Information" section only links the paper [CARD]. Owner licence UNVERIFIED. Google Earth imagery source [UNVERIFIED].
3. **Access**: open
4. **Size**: single parquet 113.33 MB [CARD]. `/rows` serves single images.
5. **Proof**: `/rows?offset=120,560,900` → `{'label': 2, 'image': '600x600'}` (bridge), `{'label': 10, 'image': '600x600'}` (mountain), `{'label': 17, 'image': '600x600'}` (river) [ROW]
6. **Schema**: `image`, `label` ClassLabel (19 names) [ROW]
7. **Label origin**: human (scene-class curation) [INFERRED]
8. **Answer rule**: answer = `label` name. Choose 4–6 visually distinct options.
9. **Classes**: 1,005 images; 50–61 per class (airport 55, beach 50, … viaduct 58) [statistics]
10. **Per-image fit**: one class per tile.
11. **Risks**: licence; 600 px tiles upscaled to 1536 is acceptable; widely used benchmark.
12. **Templates**: "What land use is shown? {airport, port, parking, residential, farmland, forest}" · "Is this an industrial area? {yes,no}" · "Water feature type? {river, pond, beach}"
- **Verdict**: MAYBE (licence not from owner).

### D44.5: VisDrone2019-DET (Voxel51 mirror)
1. Mirror https://huggingface.co/datasets/Voxel51/VisDrone2019-DET · owner https://github.com/VisDrone/VisDrone-Dataset [CARD]
2. **Licence**: **conflict**. Card YAML `cc-by-sa-3.0`, but the card text says "distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License … may not use this work for commercial purposes" [CARD]
3. **Access**: open
4. **Size**: 2,059.8 MB; 8,635 files; `samples.json` 118.49 MB (annotations); images as individual JPGs (e.g. 0.02 MB) [CARD]
5. **Proof**: HTTP range read of the first 400 KB of `samples.json` [ROW]
   - `{"filepath":"data/0000002_00005_d_0000014.jpg","tags":["train"],"wh":[960,540],"label_counts":{"car":39,"people":11,"van":6,"truck":1,"motor":8,"bicycle":3,"tricycle":1,"awning_tricycle":2,"pedestrians":11,"others":1,"ignore_regions":5}}`
   - `{"filepath":"data/0000002_00448_d_0000015.jpg","wh":[960,540],"label_counts":{"car":12,"van":1,"awning_tricycle":3,"motor":34,"bicycle":2,"pedestrians":24,"tricycle":1,"people":8,"others":1,"ignore_regions":9}}`
   - `{"filepath":"data/0000003_00231_d_0000016.jpg","wh":[960,540],"label_counts":{"car":16,"motor":1,"people":2,"pedestrians":10,"van":9,"tricycle":1,"ignore_regions":18}}` (counts summarised from `ground_truth.detections[].label`)
6. **Schema**: FiftyOne sample: `filepath`, `tags` (split), `metadata{width,height}`, `ground_truth.detections[]{label, bounding_box (rel xywh), truncation, occlusion}` [ROW]
7. **Label origin**: human boxes [INFERRED; owner paper not read]
8. **Answer rule**: yes if any detection `label == "truck"` (or bus), no otherwise.
9. **Classes**: pedestrians, people, bicycle, car, van, truck, tricycle, awning_tricycle, bus, motor, others, ignore_regions [ROW]. Negative frequency for truck/bus UNVERIFIED (2 of 3 sampled frames lack trucks).
10. **Per-image fit**: multi-object. Yes/no presence is clean, except where `ignore_regions` may hide objects; skip images with large ignore regions.
11. **Risks**: licence conflict (non-commercial). Pedestrians at street level, though faces are small. Tiny objects.
12. **Templates**: "Is there a truck? {yes,no}" · "Is there a bus? {yes,no}" · "Are there more cars than motorbikes? {yes,no}"
- **Verdict**: MAYBE (licence conflict; owner terms UNVERIFIED).

### D44.6 (rejected candidate): PatternNet `jonathan-roberts1/PatternNet`
- Has a `solar panel` class among 38 classes, but images are 256×256 [ROW] (tiny-image trap). Licence `other` [CARD]. **SKIP**.

### D45.1 / D45.3 / D45.4: ScienceQA (rank 1)
1. Owner https://github.com/lupantech/ScienceQA · HF `derek-thomas/ScienceQA` (linked from the owner README as the official HF copy) [CARD]
2. **Licence**: **conflict**. HF YAML `cc-by-sa-4.0` [CARD]. The owner README has an "MIT license" badge, then "This work is licensed under a [MIT License](http://creativecommons.org/licenses/by-nc-sa/4.0/)" and a CC BY-NC-SA 4.0 badge [CARD]. Treat it as CC BY-NC-SA 4.0 (non-commercial, fine for testing).
3. **Access**: open
4. **Size**: 626.5 MB; test parquet 122.39 MB (single file per split) [CARD]. `/rows` serves single items.
5. **Proof**: first-rows (train) [ROW]
   - `{"question":"Which of these states is farthest north?","choices":["West Virginia","Louisiana","Arizona","Oklahoma"],"answer":0,"task":"closed choice","grade":"grade2","subject":"social science","topic":"geography","skill":"Read a map: cardinal directions"}`
   - `{"question":"Identify the question that Tom and Justin's experiment can best answer.","choices":["Do ping pong balls stop rolling … 30° angle or a 45° angle?","Do ping pong balls travel farther … 45° angle?"],"answer":1,"subject":"natural science"}`
   - `{"question":"Identify the question that Kathleen and Bryant's experiment can best answer.","choices":["…wax or when it does not have a layer of wax?","…thin layer of wax or a thick layer of wax?"],"answer":0}`
6. **Schema**: `image` (nullable), `question`, `choices[]`, `answer` int8 index, `hint`, `task` (closed choice / yes or no / true-or false), `grade`, `subject`, `topic`, `category`, `skill`, `lecture`, `solution` [ROW]
7. **Label origin**: human (curriculum questions; the source curriculum is UNVERIFIED) [INFERRED]
8. **Answer rule**: D45.1 answer = `choices[answer]`. D45.3 answer = `subject`. D45.4: filter `task == "yes or no"`, answer = `choices[answer]`. Keep only rows with a non-null image.
9. **Classes** (test, 4,241 rows): subject natural 2,252 / language 1,100 / social 889. task closed choice 4,090, yes or no 113, true-or false 38 [statistics]. Image-bearing share UNVERIFIED.
10. **Per-image fit**: one answer per item.
11. **Risks**: licence conflict. Many items are answerable from text alone, so filter items whose `hint` is empty and the question requires the image [INFERRED]. Widely trained on. Small images [UNVERIFIED].
12. **Templates**: "Which choice answers the question? {choices}" · "What subject is this item? {natural science, language science, social science}" · "Which grade band? {1–3, 4–6, 7–9, 10–12}"
- **Verdict**: USE (med; licence conflict flagged, both licences allow research).

### D45.2: AI2D (lmms-lab copy)
1. `lmms-lab-encoder/ai2d` (https://huggingface.co/datasets/lmms-lab-encoder/ai2d) / `lmms-lab/ai2d`. Original AI2D (Allen AI) owner licence page not found [UNVERIFIED]
2. **Licence**: none on the card [CARD]. UNVERIFIED.
3. **Access**: open
4. **Size**: 139.5 MB; parquet shards 62.29 and 77.17 MB [CARD]
5. **Proof** [ROW]: `{"question":"which of these define dairy item","options":["c","D","b","a"],"answer":"1"}` (600×449); `{"question":"which of these define oil","options":["b","a","d","k"],"answer":"3"}`; `{"question":"According to the given food chain what would happen if phytoplankton decreases?","options":["Seal population will become extinct","Fish population would decrease.","Whale population would decrease.","Penguin population would increase."],"answer":"1"}` (576×396)
6–8. `question`, `options[4]`, `answer` (index as str). Label origin human [INFERRED]. Answer = `options[int(answer)]`.
9. Test 3,088. Answer index distribution 0:758, 1:802, 2:832, 3:696 [statistics]
10–12. One answer per item. Risks: no licence; very common benchmark. Template: "Which option answers the diagram question?"
- **Verdict**: MAYBE (licence).

### D46.1 / D46.2: DocLayNet (rank 1)
1. Owner https://github.com/DS4SD/DocLayNet · HF `docling-project/DocLayNet-v1.2` (owner org) and the smaller re-pack `pierreguillou/DocLayNet-base` [CARD]
2. **Licence**: owner LICENSE: "Community Data License Agreement – Permissive – Version 1.0 … grant(s) to You a worldwide, non-exclusive, irrevocable … right to: (a) Use Data; and (b) Publish Data" (https://raw.githubusercontent.com/DS4SD/DocLayNet/main/LICENSE) [CARD]. Permissive.
3. **Access**: open
4. **Size**: v1.2 39,770.6 MB, smallest shard 266.5 MB [CARD]. `pierreguillou/DocLayNet-base` converted parquet test = **187.2 MB**. `pierreguillou/DocLayNet-small` test parquet = **17.0 MB** but only 49 pages [/parquet endpoint]. Use `/rows` for single pages.
5. **Proof**: `/rows?dataset=pierreguillou/DocLayNet-base&config=DocLayNet_2022.08_processed_on_2023.01&split=test` [ROW]
   - `{'id':'0','doc_category':'financial_reports','collection':'ann_reports_00_04_fancy','original_filename':'OTC_NSANY_2004.pdf','page_no':17,'coco_width':1025,'coco_height':1025} categories=[9,9,9,9,9,9,9,9,9,4,4,4,5,5,5]`
   - `{'id':'1','doc_category':'financial_reports','original_filename':'NASDAQ_FFIN_2002.pdf','page_no':10} categories=[9 ×25…]`
   - `{'id':'2','doc_category':'manuals','collection':'manuals','original_filename':'IBM-i-s5445349.pdf','page_no':437} categories=[4,4]`
   - v1.2 first-rows also seen: `category_id [10,10,10,7,8,10,10,5,7]`, `metadata.doc_category "financi…"` [ROW]
6. **Schema** (base): `categories` list of ClassLabel {0 Caption, 1 Footnote, 2 Formula, 3 List-item, 4 Page-footer, 5 Page-header, 6 Picture, 7 Section-header, 8 Table, 9 Text, 10 Title}; `bboxes_block`; `doc_category` str; `collection`; `original_filename`; `page_no` [ROW]. (v1.2 uses `category_id` with a different id base [INFERRED].)
7. **Label origin**: human. "DocLayNet is hand-annotated by well-trained experts" and "Annotations are crowdsourced" [CARD v1.2]. `doc_category` is a source-collection label [INFERRED].
8. **Answer rule**: D46.1 answer = `doc_category`. D46.2: yes if 8 (Table) ∈ `categories`, no otherwise.
9. **Classes** (base test 499 pages): financial_reports 172, scientific_articles 103, laws_and_regulations 86, manuals 77, patents 32, government_tenders 29 [statistics]. Table yes/no counts UNVERIFIED, but rows 0–2 have no Table, so real negatives exist [ROW].
10. **Per-image fit**: one category per page. Table presence is unambiguous given full human labelling.
11. **Risks**: renders are 1025×1025. Real company names appear in public filings (low risk). DocLayNet is widely used in training.
12. **Templates**: "What kind of document is this page from? {financial report, scientific article, law/regulation, government tender, manual, patent}" · "Does the page contain a table? {yes,no}" · "Does the page contain a picture? {yes,no}"
- **Verdict**: USE (high).

### D46.3: LoC Beyond Words (rank 1)
1. https://huggingface.co/datasets/biglam/loc_beyond_words · files `data/val_20_percent.json` [CARD]
2. **Licence**: card YAML `license: cc0-1.0` [CARD]. biglam is a mirror; the LoC Labs original licence page was not fetched [UNVERIFIED]. The underlying Chronicling America pages are public-domain-era newspapers (WWI) [CARD].
3. **Access**: open
4. **Size**: 2,394 MB total; **COCO annotation JSON val 1.43 MB**, train 5.56 MB; validation parquet 238.31 MB; `images.zip` 1,193 MB. Image URLs inside the JSON point to `s3.amazonaws.com/ndnp-jpeg-surrogates/...` (one page each) [ROW]
5. **Proof**: downloaded `val_20_percent.json` (712 images, 9,931 annotations) [ROW]
   - image `{'file_name': '7.jpg', 'url': 'http://s3.amazonaws.com/ndnp-jpeg-surrogates/pst_davey_ver01/data/sn83045211/00237287678/1917110301/0875.jpg', 'height': 1134, 'width': 898, 'id': 7}`
   - annotation `{'id': 1790, 'bw_id': '5da8f595ebaf180001004056', 'image_id': 7, 'category_id': 1, 'bbox': [773, 68, 117, 408], 'area': 47736}`
   - annotation `{'id': 2186, 'bw_id': '5d98848aebaf180001003669', 'image_id': 7, 'category_id': 1, 'bbox': [552, 144, 110, 140], 'area': 15400}`
   - (first-rows train row 0: objects with `category_id` 0 and 6 on a 912×1330 page)
6. **Schema**: COCO `images[]{id,file_name,url,width,height}`, `annotations[]{image_id, category_id, bbox, area, bw_id}`, `categories` 0 Photograph, 1 Illustration, 2 Map, 3 Comics/Cartoon, 4 Editorial Cartoon, 5 Headline, 6 Advertisement [ROW]
7. **Label origin**: human, crowdsourced. "Volunteers marked seven types of visual content" [CARD]
8. **Answer rule**: yes if any annotation on the page has `category_id == k`, no otherwise.
9. **Classes** (val 712 pages, pages with ≥1 box): Photograph 489 yes / 223 no; Illustration 154/558; Map 32/680; Comics 109/603; Editorial cartoon 53/659; Headline 618/94; Advertisement 510/202 [ROW]. Real negatives exist, but see risk.
10. **Per-image fit**: multi-label page. The yes/no per class is clean if the marking is complete.
11. **Risks**: crowdsourcing may miss regions, so a "no" can be a missed mark. Use Photograph/Map/Comics, where misses are less likely [INFERRED]. Old scans at about 900×1300 px are low-res for small text. Old photos may show identifiable people (historical, not identified).
12. **Templates**: "Does this page contain a photograph? {yes,no}" · "Does it contain a map? {yes,no}" · "Which of these is NOT present? {photograph, map, advertisement, comic}"
- **Verdict**: USE (med; possible missed marks).

### D46.4: Early printed books font groups (rank 1)
1. https://huggingface.co/datasets/biglam/early_printed_books_font_detection. Mirror of Zenodo "Dataset of Pages from Early Printed Books with Multiple Font Groups" (DOI 10.5281/zenodo.33666…, truncated in card) [CARD]
2. **Licence**: card YAML `cc-by-nc-sa-4.0` [CARD]. Zenodo record not fetched [UNVERIFIED].
3. **Access**: open
4. **Size**: 44,768.8 MB; shards 438–592 MB [CARD]. Single pages via `/rows`.
5. **Proof**: first-rows [ROW]: `{"labels":[7]}` (fraktur, 1761×3221); `{"labels":[8]}` (schwabacher, 2000×2663); `{"labels":[11]}` (gotico_antiqua, 1137×1623)
6. **Schema**: `image`, `labels` list of ClassLabel {greek, antiqua, other_font, not_a_font, italic, rotunda, textura, fraktur, schwabacher, hebrew, bastarda, gotico_antiqua} [ROW]
7. **Label origin**: human: "each labelled by experts with the font group or groups used on the page"; YAML `annotations_creators: expert-generated` [CARD]
8. **Answer rule**: keep pages with `len(labels)==1`; answer = that label name.
9. **Classes**: test 4,554 pages; labels per page min 1, max 4, mean 1.11 [statistics]. Per-class counts UNVERIFIED.
10. **Per-image fit**: about 90% single-label [INFERRED from mean 1.11]. Filter on `len==1`.
11. **Risks**: non-commercial. Large images (fine). Fine-grained typography is hard. Little web overlap [INFERRED].
12. **Templates**: "Which typeface group is used? {antiqua, italic, textura, fraktur, schwabacher, rotunda}" · "Is this page set in a blackletter type? {yes,no}" · "Does the page contain Greek type? {yes,no}"
- **Verdict**: USE (med; Zenodo licence not confirmed).

### D46.5: biglam/illustrated_ads (rank 1)
1. https://huggingface.co/datasets/biglam/illustrated_ads [CARD]
2. **Licence**: YAML `cc0-1.0` [CARD]
3. **Access**: open
4. **Size**: **single parquet 48.05 MB** (whole dataset, under the cap) [CARD]
5. **Proof**: first-rows [ROW]
   - `{"file":"pst_fenske_ver02_data_sn84026497_00280776129_1880042101_0834_002_6_96.jpg","label":0,"pub_date":"1880-04-21","score":0.9609,"ocr":"H. II. IIASLKT & SOXN, Dealers in General Merchandise…","place_of_publication":"Tionesta, Pa.","image":388x395}`
   - `{"file":"scu_carlacox_ver01_…_007_6_93.jpg","label":0,"pub_date":"1870-04-14","place_of_publication":"Anderson Court House, S.C.","image":503x292}`
   - `{"file":"in_england_ver02_…_004_6_97.jpg","label":0,"pub_date":"1865-12-13","name":"The Indianapolis daily herald.","image":487x1665}`
6. **Schema**: `label` ClassLabel {text-only, illustrations}; `box` and `score` (Newspaper Navigator **detector** crop box and confidence, machine); `ocr` (machine); metadata [ROW]
7. **Label origin**: mixed. Crops are machine-located ("The adverts were located by Newspaper Navigator"), but the `label` is human: "annotations_creators: expert-generated", "Sampling and annotation used nnanno" [CARD]. The label we use is human.
8. **Answer rule**: yes if `label == 1` (illustrations).
9. **Classes**: 549 total; text-only 376, illustrations 173 [/rows count]
10. **Per-image fit**: one label per crop.
11. **Risks**: small crops (about 300–500 px), so they blur at 1536 (tiny-image risk). Card calls it "a realistic rather than clean example" [CARD].
12. **Templates**: "Does this advert contain an illustration? {yes,no}" · "Which decade? {1860s,1870s,1880s,1890s,1900}" (from `pub_date`) · "Text-only advert? {yes,no}"
- **Verdict**: USE (med; small images).

### D46.6: ICDAR 2021 historical document dating
1. https://huggingface.co/datasets/biglam/icdar2021-historical-document-dating [CARD]
2. **Licence**: YAML `cc-by-4.0` [CARD]. Owner (competition) licence UNVERIFIED.
3. **Access**: open
4. **Size**: 28,014 MB; shards 394–604 MB [CARD]
5. **Proof** [ROW]: `{"file_name":"0_1400_1430.jpg","date_start":1400,"date_end":1430,"date_span":30,"date_mid":1415.0}` (2639×3500); `{"file_name":"10000_1200_1299.jpg","date_start":1200,"date_end":1299,"date_span":99}`; `{"file_name":"10001_1445_1455.jpg","date_start":1445,"date_end":1455,"date_span":10}`
6–8. Date range fields. Label origin: archival catalogue metadata (human) [INFERRED]. Answer = century of `date_mid` when start and end fall in the same century.
9–11. Class balance UNVERIFIED. Very expert task.
12. "In which century was this written? {13th,14th,15th,16th}"
- **Verdict**: MAYBE (owner licence and label origin not verified).

### D47.1 / D47.2: Pitt Image Ads (PittAdsDB)
1. Owner https://people.cs.pitt.edu/~kovashka/ads/. Annotations mirror https://huggingface.co/datasets/Mindykkyan/PittadsDB-AdsPics (`image_annotations/image/Topics.json`, 2.31 MB). Images: owner GCS zips (`https://storage.googleapis.com/ads-dataset/subfolder-N.zip`, 591 MB–6.9 GB) or per-file mirror `dchen278/pitt-ads-full` (56,887 files) [CARD]
2. **Licence**: no licence found on the owner page or either mirror card [UNVERIFIED]
3. **Access**: open (direct GCS links in the owner readme) [CARD]
4. **Size**: Topics.json 2.31 MB. Per-image files in the `dchen278` mirror (0.01–58 MB). Owner zips are SINGLE ARCHIVES per subfolder [CARD]
5. **Proof**: downloaded Topics.json (64,340 keys) [ROW]: `7/62717.jpg ['27', '9', '27']` · `10/170741.png ['2', '2', '2']` · `0/80990.jpg ['9', '39', '9', '9', '9']`
6. **Schema**: key = `subfolder/image`; value = list of topic ids (or free text for "Other") from 3–5 annotators. `Topics_List.txt` maps ids, e.g. 1 restaurant, 2 chocolate, 6 alcohol, 9 cars, 17 beauty, 19 clothing, 29 gambling, 34 smoking_alcohol_abuse, 39 Unclear [ROW]
7. **Label origin**: human. "verified by human annotators on Amazon Mechanical Turk … we posed the same question to 3-5 different annotators" [CARD readme_images.txt]
8. **Answer rule**: majority topic = most common id with ≥2 votes. D47.1: yes if the majority ∈ {6 alcohol, 29 gambling}, plus 34 if anti-smoking PSAs are included; no if the majority is another topic. D47.2 answer = majority id → name.
9. **Classes**: agreement levels: 3 votes 38,032 · 2 votes 16,908 · 1 (no majority) 4,973 · 5: 3,295 · 4: 1,132. Majority counts: clothing 8,341, cars 7,051, beauty 5,826, soda 4,092, restaurant 4,090, chocolate 3,764, electronics 3,704, alcohol 2,807, … gambling 28 [ROW]. D47.1 has plenty of real negatives.
10. **Per-image fit**: drop images with no majority (4,973).
11. **Risks**: no licence. Copyrighted ads with celebrities (do not ask who). Mapping from the mirror's `images/0XX/` paths to `subfolder/name` keys is UNVERIFIED. Some images are tiny.
12. **Templates**: "What is this ad selling? {clothing, cars, beauty, soda, restaurant, electronics}" · "Is this an alcohol ad? {yes,no}" · "Is this a public-service ad (non-commercial)? {yes,no}" (topics 30–38)
- **Verdict**: MAYBE (fails the licence check).

### D47.3 / D47.5 / D48.5 / D49.1 / D49.2 / D50.1 / D50.2 / D50.3: Open Images V7 human-verified image-level labels (rank 1). Full card here; per-task rows below
1. **Landing**: https://storage.googleapis.com/openimages/web/factsfigures_v7.html · **Files**: https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv, https://storage.googleapis.com/openimages/v7/oidv7-class-descriptions.csv, https://storage.googleapis.com/openimages/2018_04/validation/validation-images-with-rotation.csv. Images: `https://open-images-dataset.s3.amazonaws.com/validation/<ImageID>.jpg` (checked: HTTP 200, 232,515 bytes for `041ec0633447b467`) [ROW]
2. **Licence**: "The annotations are licensed by Google LLC under CC BY 4.0 license. The images are listed as having a CC BY 2.0 license." Plus the caveat "we make no representations or warranties regarding the license status of each image" [CARD]
3. **Access**: open
4. **Size**: val human labels CSV **28.39 MB** (downloaded); test labels 93.6 MB (not fetched); class descriptions 0.50 MB; val image metadata 15.2 MB; images are one file each (about 0.2–1 MB) [ROW, Content-Length]
5. **Proof**: rows below per task (format `ImageID,Source,LabelName,Confidence`) [ROW]
6. **Schema**: `ImageID`; `Source` ∈ {verification, crowdsource-verification}; `LabelName` (MID, map via class descriptions); `Confidence` 1 = human-verified present, 0 = human-verified **absent** [ROW]
7. **Label origin**: human. Every val row is human verification (539,987 `verification` + 78,197 `crowdsource-verification`) [ROW]. Candidate labels to verify were machine-proposed [INFERRED], so negatives are hard negatives.
8. **Answer rule**: for class C: yes if a row (ImageID, C, 1) exists; no if a row (ImageID, C, 0) exists; **skip** if no row exists.
9. **Classes and balance** (val, 41,620 images; positives / verified negatives) [ROW]: Weapon 192/196 · Handgun 20/47 · Rifle 99/29 · Knife 83/19 · Firearm 93/87 · Alcoholic beverage 279/98 · Beer 96/70 · Wine 96/56 · Cocktail 153/80 · Brand 166/329 · Logo 79/9 · Advertising 110/97 · Billboard 32/9 · Poster 263/100 · Screenshot 116/330 · Mobile phone 119/46 · Laptop 77/59 · Computer monitor 88/52 · Lipstick 51/53 · Cosmetics 55/117 · Dress 788/217 · Handbag 71/59 · Sunglasses 134/102 · Cigarette 6/0 (too few) · "Nudity" class absent.
10. **Per-image fit**: presence yes/no is clean per class. For pick-one (D49.2) use images with exactly one positive among {Mobile phone, Laptop, Computer monitor} and no positive for the others. The others may be unverified, a risk.
11. **Risks**: Flickr photos of people (faces present; do not ask identity). The images-with-rotation CSV holds Flickr author names (exclude). Some original URLs are dead (use the S3 mirror). Open Images is heavily used in pretraining. Verification of a machine-proposed label can miss small objects.
12. **Templates**: "Does the image contain a weapon? {yes,no}" · "Is an alcoholic beverage shown? {yes,no}" · "Which device is shown? {mobile phone, laptop, computer monitor}"
- Rows per task [ROW]:
  - D50.1 Weapon `/m/083kb`: `041ec0633447b467,verification,/m/083kb,1.0` · `044a3e7c7b006202,verification,/m/083kb,1.0` · `01ff40138b875524,verification,/m/083kb,0.0`
  - D50.2 Alcoholic beverage `/m/012mj`: `00101a0160a05d31,verification,/m/012mj,1.0` · `009dfe7e81b732cb,verification,/m/012mj,1.0` · `01d160559286c930,verification,/m/012mj,0.0`
  - D50.3 Brand `/m/01cd9`: `02deba0102b5ce2a,verification,/m/01cd9,1.0` · `02f42085acfad7bc,verification,/m/01cd9,1.0` · `008e12a039f69f8a,verification,/m/01cd9,0.0`
  - D47.3 Advertising `/m/011s0`: `02f5d2bc887486c6,crowdsource-verification,/m/011s0,1` · `0349ccadeb208cbc,verification,/m/011s0,1.0` · `02f42085acfad7bc,verification,/m/011s0,0.0`
  - D47.5 Billboard `/m/01knjb`: `03c35bdfffbea53f,verification,/m/01knjb,1.0` · `083b651122889187,verification,/m/01knjb,1.0` · `2595ea3831d8da6a,verification,/m/01knjb,0.0`
  - D48.5 Lipstick `/m/06c7f7`: `05ae3737394ad03a,crowdsource-verification,/m/06c7f7,1` · `08f80f26c1d57ba1,crowdsource-verification,/m/06c7f7,1` · `01d715f1c31014df,verification,/m/06c7f7,0.0`
  - D49.1 Screenshot `/m/01zbnw`: `007f71665b0812a7,verification,/m/01zbnw,1.0` · `012dc31b561d4214,verification,/m/01zbnw,1.0` · `008e12a039f69f8a,verification,/m/01zbnw,0.0`
  - D49.2 Mobile phone `/m/050k8` / Laptop `/m/01c648` / Computer monitor `/m/02522`: `012dc31b561d4214,crowdsource-verification,/m/050k8,1` · `00a36f96e31731c4,crowdsource-verification,/m/01c648,1` · `00ec4ba83d648c33,verification,/m/02522,0.0`
- **Verdict**: USE (high) for D50.1, D50.2, D50.3, D47.3, D48.5, D49.1. USE (med) for D47.5 (only 9 negatives in val; add the test CSV) and D49.2 (pick-one exclusivity is partly unverified).

### D48.1 / D48.2 / D48.3: Fashionpedia (rank 1)
1. Owner https://fashionpedia.github.io/home/index.html · GitHub https://github.com/cvdfoundation/fashionpedia · HF `detection-datasets/fashionpedia` [CARD]
2. **Licence**: HF card: "Fashionpedia is licensed under a Creative Commons Attribution 4.0 International License" [CARD]. The owner home page has a "Terms of Use" link whose text could not be extracted [UNVERIFIED].
3. **Access**: open
4. **Size**: 3,478.9 MB; train shards about 480–490 MB; val split 1,158 images (via `/rows`) [CARD]
5. **Proof** (first-rows, train) [ROW]
   - `{"image_id":23,"width":682,"height":1024,"objects":{"category":[23,23,33,10],"bbox":[[445,910,505,983],…]}}` (shoe, shoe, neckline, dress)
   - `{"image_id":25,"width":683,"height":1024,"objects":{"category":[2,33,31,31,13,7,22,22,23,23]}}` (sweater, neckline, sleeve×2, glasses, shorts, sock×2, shoe×2)
   - `{"image_id":26,"width":1024,"height":683,"objects":{"category":[13,29,28,32,32,31,31,0,31,31,18,4,6,23,23]}}`
6. **Schema**: `objects.category` ClassLabel over 46 names (0 shirt/blouse … 10 dress, 13 glasses, 14 hat, 24 bag/wallet, 31 sleeve …), `bbox`, `area` [ROW]
7. **Label origin**: human: "a dataset with everyday and celebrity event fashion images annotated with segmentation masks…" (ontology "built by fashion experts") [CARD]
8. **Answer rule**: D48.1: yes if 10 ∈ categories, no otherwise. D48.3: yes if 24 ∈ categories. D48.2: among garment ids 0–12, if exactly one distinct id is present, answer = it.
9. **Classes** (val 1,158 images, by `/rows`): dress 506 (so 652 negatives), bag 205, hat 74, glasses 130, pants 313, skirt 162, jacket 179. Images with exactly one garment class: 496 [ROW]
10. **Per-image fit**: multi-object. Use the rules above. For D48.2 use the 496 single-garment images.
11. **Risks**: people and celebrities are visible (no identity questions). Exhaustive labelling is assumed for negatives [INFERRED]. Images about 1024 px.
12. **Templates**: "Is the person wearing a dress? {yes,no}" · "What is the main garment? {dress, pants, skirt, jacket, shirt/blouse, coat}" · "Is there a bag? {yes,no}"
- **Verdict**: USE (high).

### D48.4: Fashion Product Images (small) via `ashraq/fashion-product-images-small`
1. https://huggingface.co/datasets/ashraq/fashion-product-images-small; source "Data was obtained from https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small" [CARD]
2. **Licence**: none on the card; Kaggle not fetched (login wall) [UNVERIFIED]
3. **Access**: open mirror. Kaggle original requires login: GATED.
4. **Size**: 271.5 MB, 2 shards of about 136 MB [CARD]
5. **Proof** [ROW]: `{"id":15970,"gender":"Men","masterCategory":"Apparel","subCategory":"Topwear","articleType":"Shirts","baseColour":"Navy Blue","usage":"Casual"}` · `{"id":39386,…"masterCategory":"Apparel","articleType":"Jeans","baseColour":"Blue"}` · `{"id":59263,"gender":"Women","masterCategory":"Accessories","articleType":"Watches","baseColour":"Silver"}`
6–9. Catalogue fields (merchant-entered, human [INFERRED]). masterCategory: Apparel 21,361 / Accessories 11,244 / Footwear 9,197 / Personal Care 2,139 [statistics]
10–11. **Images are 60×80** [ROW], a tiny-image trap. `benitomartin/fashion-product-images-small-900x1200` has the same ids at 900×1200 [ROW], which is almost certainly upscaled from the same small images [INFERRED].
- **Verdict**: SKIP (tiny images, no licence). The full-resolution Kaggle original is GATED (login).

### D50.4: LogoDet-3K (`axonstan/LogoDet-3K`)
1. Owner https://github.com/Wangjing1551/LogoDet-3K-Dataset (Baidu Drive download) · mirror https://huggingface.co/datasets/axonstan/LogoDet-3K [CARD]
2. **Licence**: mirror `license: mit` [CARD]. No licence in the owner README [UNVERIFIED].
3. **Access**: open mirror
4. **Size**: 3,116.5 MB; test shards 311.7 and 313.2 MB [CARD]
5. **Proof** [ROW]: `{"industry_name":"Clothes","company_name":2020,"bbox":[22,68,366,448]}` (387×520) · `{"industry_name":"Necessities","company_name":1119,"bbox":[94,120,455,278]}` (509×368) · `{"industry_name":"Others","company_name":575,"bbox":[4,1,522,242]}` (522×393)
6–8. `industry_name` (9 super-categories), `company_name` ClassLabel (about 3,000 brands), `bbox`. The owner README says "about 200,000 manually annotated logo objects" [CARD], so labels are human. Answer = `industry_name`.
9. Test (31,731 rows): Food 10,670, Clothes 6,252, Necessities 4,966, Others 3,107, Transportation 2,093, Electronic 1,931, Leisure 1,136, Sports 788, Medical 788 [statistics]
10. One logo row per image here (rows look like one box per row) [INFERRED].
11. Risks: licence; brand identity is fine (not a person). May overlap with the already-used `logo-detection-dataset` [INFERRED].
12. "Which industry is this brand in? {Food, Clothes, Necessities, Electronic, Transportation, Leisure}"
- **Verdict**: MAYBE (licence only on the mirror).

### D50.5: Watermark-or-Not-20K
1. https://huggingface.co/datasets/prithivMLmods/Watermark-or-Not-20K [CARD]
2. **Licence**: `apache-2.0` [CARD]
3. **Access**: open
4. **Size**: 2,643 MB; smallest shard `dataset/0005.parquet` 74.14 MB [CARD]
5. **Proof** [ROW]: `{"label":0}` 528×350 · `{"label":0}` 509×350 · `{"label":0}` 525×350
6. `image`, `label` {0 No Watermark, 1 Watermark}
7. **Label origin**: UNVERIFIED. The card describes classes only, with no provenance [CARD]. Watermarks may have been synthetically added, which would make this generator data [UNVERIFIED].
9. 10,000 / 10,000 [statistics]
- **Verdict**: MAYBE (label origin unknown).

---

## 3. CSV

```csv
domain,task_id,task,dataset,landing_url,repo_id,licence,licence_quote_url,access,total_mb,smallest_fetch_mb,single_archive,sample_proof_url,rows_pasted,label_origin,answer_rule,has_negatives,classes,one_answer_per_image,personal_data_risk,verdict,confidence,unverified_fields
41,D41.1,Which application is shown,ScreenSpot-Pro,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro,likaixin/ScreenSpot-Pro,MIT,https://raw.githubusercontent.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/main/LICENSE,open,3376,0.02,no,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro/resolve/main/annotations/illustrator_windows.json,yes,human,answer=application (dedupe img_filename),n/a,23 apps + 3 OS-common,yes,low (paths/usernames possible),USE,high,paper annotation method
41,D41.2,Which OS,ScreenSpot-Pro,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro,likaixin/ScreenSpot-Pro,MIT,https://raw.githubusercontent.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/main/LICENSE,open,3376,0.02,no,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro/resolve/main/annotations/illustrator_windows.json,yes,human,answer=platform,n/a,windows/macos/linux,yes,low,USE,high,OS confounded with app
41,D41.3,Software category,ScreenSpot-Pro,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro,likaixin/ScreenSpot-Pro,MIT,https://raw.githubusercontent.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding/main/LICENSE,open,3376,0.02,no,https://huggingface.co/datasets/likaixin/ScreenSpot-Pro/resolve/main/annotations/illustrator_windows.json,yes,human,answer=group,n/a,Dev/Creative/CAD/Scientific/Office/OS,yes,low,USE,high,
42,D42.1,Screen type,Enrico,https://github.com/luileito/enrico,Leonardo6/enrico (mirror),MIT,https://raw.githubusercontent.com/luileito/enrico/master/LICENSE,open,236,0.05,yes (screenshots zip 110MB; per-row via /rows),https://raw.githubusercontent.com/luileito/enrico/master/design_topics.csv,yes,human,answer=topic,n/a,20 topics (list 265 … dialer 6),yes,low,USE,high,
42,D42.2,Is login screen,Enrico,https://github.com/luileito/enrico,Leonardo6/enrico (mirror),MIT,https://raw.githubusercontent.com/luileito/enrico/master/LICENSE,open,236,0.05,yes (110MB zip),https://raw.githubusercontent.com/luileito/enrico/master/design_topics.csv,yes,human,yes if topic==login,yes (141 vs 1319),login/other,yes,low,USE,high,
42,D42.3,Website vertical,Multimodal-Mind2Web,https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web,osunlp/Multimodal-Mind2Web,openrail,https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web,open,13577,217.7,no,https://datasets-server.huggingface.co/first-rows?dataset=osunlp/Multimodal-Mind2Web&config=default&split=train,yes,human (inferred),answer=domain,n/a,Travel/Shopping/Entertainment,yes,low-med,MAYBE,med,label origin; licence fit for data
42,D42.4,UI visual defect,multiwindow-gui-defect-benchmark,https://huggingface.co/datasets/zxy6654/multiwindow-gui-defect-benchmark,zxy6654/multiwindow-gui-defect-benchmark,cc-by-4.0,https://huggingface.co/datasets/zxy6654/multiwindow-gui-defect-benchmark,open,92.5,0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=zxy6654/multiwindow-gui-defect-benchmark&config=default&split=train,yes (image only),UNVERIFIED,cannot compute (no label column),unknown,none,unknown,low,SKIP,high,label origin; labels
43,D43.1,Chart type,ChartBench,https://huggingface.co/datasets/SincereX/ChartBench,SincereX/ChartBench,MIT,https://huggingface.co/datasets/SincereX/ChartBench,open,10449,3.86,yes (test.zip 227.7MB; range-readable),https://huggingface.co/datasets/SincereX/ChartBench/resolve/main/test.jsonl,yes,generator,answer=type.chart,n/a,bar/line/pie/combination/radar/area/box/scatter/node_link,yes,none,USE,med,per-file zip extraction; data-generation method
43,D43.2,Is A higher than B,ChartBench,https://huggingface.co/datasets/SincereX/ChartBench,SincereX/ChartBench,MIT,https://huggingface.co/datasets/SincereX/ChartBench,open,10449,3.86,yes (227.7MB range-readable),https://huggingface.co/datasets/SincereX/ChartBench/resolve/main/test.jsonl,yes,generator,task==VC; answer=conversation[i].label,yes (balanced pairs),Yes/No,yes,none,USE,med,
43,D43.2,Is A higher than B,FigureQA,https://www.microsoft.com/en-us/research/project/figureqa-dataset/,vikhyatk/figureqa (mirror),UNVERIFIED (click-through),https://www.microsoft.com/en-us/research/project/figureqa-dataset/download/,manual approval (agree & download),2218,321.4,no,https://datasets-server.huggingface.co/first-rows?dataset=vikhyatk/figureqa&config=default&split=train,yes,generator,answer=qa.answer,yes,Yes/No,yes,none,GATED,med,licence text
43,D43.3,Value-claim check,ChartBench,https://huggingface.co/datasets/SincereX/ChartBench,SincereX/ChartBench,MIT,https://huggingface.co/datasets/SincereX/ChartBench,open,10449,3.86,yes (227.7MB range-readable),https://huggingface.co/datasets/SincereX/ChartBench/resolve/main/test.jsonl,yes,generator,task==VE; answer=label,yes,Yes/No,yes,none,USE,med,
43,D43.4,Do any lines intersect,CharXiv,https://huggingface.co/datasets/princeton-nlp/CharXiv,princeton-nlp/CharXiv,cc-by-sa-4.0,https://huggingface.co/datasets/princeton-nlp/CharXiv,open,375.9,91.7,no,https://datasets-server.huggingface.co/first-rows?dataset=princeton-nlp/CharXiv&config=default&split=validation,yes,human (inferred),descriptive_qK==11 -> descriptive_aK,yes (balance unverified),Yes/No,yes,low,USE,med,label origin quote; q11 balance
43,D43.5,Number of subplots,CharXiv,https://huggingface.co/datasets/princeton-nlp/CharXiv,princeton-nlp/CharXiv,cc-by-sa-4.0,https://huggingface.co/datasets/princeton-nlp/CharXiv,open,375.9,91.7,no,https://datasets-server.huggingface.co/first-rows?dataset=princeton-nlp/CharXiv&config=default&split=validation,yes,human (inferred),bucket(num_subplots),n/a,1/2/3/4/5+,yes,low,USE,med,class counts
43,D43.6,Which series/bar is max,DVQA,https://github.com/kushalkafle/DVQA_dataset,vikhyatk/dvqa (mirror),UNVERIFIED,https://github.com/kushalkafle/DVQA_dataset,open,4272.5,473.3,no,https://datasets-server.huggingface.co/first-rows?dataset=vikhyatk/dvqa&config=default&split=train,yes,generator,answer=qa.answer for 'largest value' question,n/a,bar labels,yes,none,MAYBE,med,licence
43,D43.6,Which series is max,FigureQA,https://www.microsoft.com/en-us/research/project/figureqa-dataset/,vikhyatk/figureqa (mirror),UNVERIFIED (click-through),https://www.microsoft.com/en-us/research/project/figureqa-dataset/download/,manual approval,2218,321.4,no,https://datasets-server.huggingface.co/first-rows?dataset=vikhyatk/figureqa&config=default&split=train,yes,generator,yes/no 'Is X the maximum?',yes,colour names,yes,none,GATED,med,licence text
44,D44.1,Is area flooded,FloodNet Track 2,https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021,takara-ai/FloodNet_2021-Track_2_Dataset_HF,cc-by-sa-4.0 (mirror only),https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF,open,12310,0.001 (ann json); 7 (image),no,https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF/resolve/main/train_image/ann/10170.JPG.json,yes,human,overall condition == flooded,yes (~17% flooded),flooded/non flooded,yes,low,MAYBE,med,owner licence
44,D44.2,Is entire road flooded,FloodNet Track 2,https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021,takara-ai/FloodNet_2021-Track_2_Dataset_HF,cc-by-sa-4.0 (mirror only),https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF,open,12310,0.001,no,https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF/resolve/main/train_image/ann/10171.JPG.json,yes,human,Yes_No answer (invert for 'non flooded' phrasing),yes,Yes/No,yes,low,MAYBE,med,owner licence
44,D44.3,Building count bucket,FloodNet Track 2,https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021,takara-ai/FloodNet_2021-Track_2_Dataset_HF,cc-by-sa-4.0 (mirror only),https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF,open,12310,0.001,no,https://huggingface.co/datasets/takara-ai/FloodNet_2021-Track_2_Dataset_HF/resolve/main/train_image/ann/10170.JPG.json,yes,human,bucket(Simple_Counting),n/a,0/1-3/4-6/7+,yes,low,MAYBE,low,owner licence; count noise
44,D44.4,Land-use type,WHU-RS19,https://huggingface.co/datasets/jonathan-roberts1/WHU-RS19,jonathan-roberts1/WHU-RS19,cc-by-4.0 (mirror only),https://huggingface.co/datasets/jonathan-roberts1/WHU-RS19,open,113.3,113.3,no,https://datasets-server.huggingface.co/rows?dataset=jonathan-roberts1/WHU-RS19&config=default&split=train&offset=560&length=1,yes,human (inferred),answer=label,n/a,19 classes ~50 each,yes,none,MAYBE,med,owner licence; imagery rights
44,D44.5,Truck present (drone),VisDrone2019-DET,https://github.com/VisDrone/VisDrone-Dataset,Voxel51/VisDrone2019-DET,conflict: cc-by-sa-3.0 yaml vs CC BY-NC-SA 3.0 text,https://huggingface.co/datasets/Voxel51/VisDrone2019-DET,open,2059.8,0.02 (image); 118.5 (samples.json; range-readable),no,https://huggingface.co/datasets/Voxel51/VisDrone2019-DET/resolve/main/samples.json,yes,human (inferred),any detection label==truck,yes (unquantified),10 object classes,yes,med (pedestrians),MAYBE,med,owner licence; negatives count
44,D44.6,Rooftop solar,PatternNet,https://huggingface.co/datasets/jonathan-roberts1/PatternNet,jonathan-roberts1/PatternNet,other,https://huggingface.co/datasets/jonathan-roberts1/PatternNet,open,1422.1,697.6,no,https://datasets-server.huggingface.co/first-rows?dataset=jonathan-roberts1/PatternNet&config=default&split=train,yes,human (inferred),label==solar panel,yes,38 classes,yes,none,SKIP,high,tiny 256px images
45,D45.1,Auto-mark MCQ item,ScienceQA,https://github.com/lupantech/ScienceQA,derek-thomas/ScienceQA,conflict: CC BY-NC-SA 4.0 (owner) / cc-by-sa-4.0 (HF),https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md,open,626.5,122.4,no,https://datasets-server.huggingface.co/first-rows?dataset=derek-thomas/ScienceQA&config=default&split=train,yes,human (inferred),answer=choices[answer],n/a,2-5 choices,yes,none,USE,med,label origin quote; image share
45,D45.2,Diagram question,AI2D (lmms-lab),https://huggingface.co/datasets/lmms-lab-encoder/ai2d,lmms-lab-encoder/ai2d,UNVERIFIED,https://huggingface.co/datasets/lmms-lab-encoder/ai2d,open,139.5,62.3,no,https://datasets-server.huggingface.co/first-rows?dataset=lmms-lab-encoder/ai2d&config=default&split=test,yes,human (inferred),answer=options[int(answer)],n/a,4 options,yes,none,MAYBE,med,licence
45,D45.3,Worksheet subject,ScienceQA,https://github.com/lupantech/ScienceQA,derek-thomas/ScienceQA,conflict: CC BY-NC-SA 4.0 / cc-by-sa-4.0,https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md,open,626.5,122.4,no,https://datasets-server.huggingface.co/first-rows?dataset=derek-thomas/ScienceQA&config=default&split=train,yes,human,answer=subject,n/a,natural 2252/language 1100/social 889 (test),yes,none,USE,med,
45,D45.4,Yes/no worksheet item,ScienceQA,https://github.com/lupantech/ScienceQA,derek-thomas/ScienceQA,conflict: CC BY-NC-SA 4.0 / cc-by-sa-4.0,https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md,open,626.5,122.4,no,https://datasets-server.huggingface.co/first-rows?dataset=derek-thomas/ScienceQA&config=default&split=train,yes,human,task=='yes or no' -> choices[answer],yes (counts unverified),yes/no,yes,none,USE,low,yes/no balance; image share (113 test items)
46,D46.1,Document category,DocLayNet,https://github.com/DS4SD/DocLayNet,pierreguillou/DocLayNet-base; docling-project/DocLayNet-v1.2,CDLA-Permissive-1.0,https://raw.githubusercontent.com/DS4SD/DocLayNet/main/LICENSE,open,39770.6,17.0 (small test) / 187.2 (base test),no,https://datasets-server.huggingface.co/rows?dataset=pierreguillou/DocLayNet-base&config=DocLayNet_2022.08_processed_on_2023.01&split=test&offset=0&length=3,yes,human,answer=doc_category,n/a,6 categories (base test 499),yes,low,USE,high,
46,D46.2,Page has table,DocLayNet,https://github.com/DS4SD/DocLayNet,pierreguillou/DocLayNet-base,CDLA-Permissive-1.0,https://raw.githubusercontent.com/DS4SD/DocLayNet/main/LICENSE,open,39770.6,17.0,no,https://datasets-server.huggingface.co/rows?dataset=pierreguillou/DocLayNet-base&config=DocLayNet_2022.08_processed_on_2023.01&split=test&offset=0&length=3,yes,human,yes if 8 in categories,yes,11 layout classes,yes,low,USE,high,table counts
46,D46.3,Newspaper page has photo/map/ad,LoC Beyond Words,https://huggingface.co/datasets/biglam/loc_beyond_words,biglam/loc_beyond_words,cc0-1.0,https://huggingface.co/datasets/biglam/loc_beyond_words,open,2394.1,1.43,no,https://huggingface.co/datasets/biglam/loc_beyond_words/resolve/main/data/val_20_percent.json,yes,human (crowd),yes if any annotation category_id==k,yes (e.g. Photo 489/223),7 classes,yes,low (historic photos),USE,med,LoC original licence; missed marks
46,D46.4,Typeface group,Early printed books font groups,https://huggingface.co/datasets/biglam/early_printed_books_font_detection,biglam/early_printed_books_font_detection,cc-by-nc-sa-4.0,https://huggingface.co/datasets/biglam/early_printed_books_font_detection,open,44768.8,438.2,no,https://datasets-server.huggingface.co/first-rows?dataset=biglam/early_printed_books_font_detection&config=default&split=train,yes,human (expert),len(labels)==1 -> label,n/a,12 classes,mostly (mean 1.11),none,USE,med,Zenodo licence; per-class counts
46,D46.5,Illustrated advert,biglam/illustrated_ads,https://huggingface.co/datasets/biglam/illustrated_ads,biglam/illustrated_ads,cc0-1.0,https://huggingface.co/datasets/biglam/illustrated_ads,open,48.05,48.05,no,https://datasets-server.huggingface.co/first-rows?dataset=biglam/illustrated_ads&config=default&split=train,yes,mixed (human label on machine crops),yes if label==1,yes (376/173),text-only/illustrations,yes,none,USE,med,
46,D46.6,Manuscript century,ICDAR2021 document dating,https://huggingface.co/datasets/biglam/icdar2021-historical-document-dating,biglam/icdar2021-historical-document-dating,cc-by-4.0 (mirror),https://huggingface.co/datasets/biglam/icdar2021-historical-document-dating,open,28014,394,no,https://datasets-server.huggingface.co/first-rows?dataset=biglam/icdar2021-historical-document-dating&config=default&split=train,yes,human (inferred),century(date_mid) if same century,n/a,centuries,yes,none,MAYBE,low,owner licence; label origin
47,D47.1,Restricted-category ad,Pitt Image Ads,https://people.cs.pitt.edu/~kovashka/ads/,Mindykkyan/PittadsDB-AdsPics; dchen278/pitt-ads-full,UNVERIFIED,https://people.cs.pitt.edu/~kovashka/ads/,open,11881.7,2.31 (Topics.json); per-image ~0.01+,yes (owner zips per subfolder),https://huggingface.co/datasets/Mindykkyan/PittadsDB-AdsPics/resolve/main/image_annotations/image/Topics.json,yes,human (MTurk 3-5 votes),majority topic in {6 alcohol, 29 gambling},yes,39 topics,yes after majority filter,med (celebrities in ads),MAYBE,med,licence; mirror path mapping
47,D47.2,Ad topic,Pitt Image Ads,https://people.cs.pitt.edu/~kovashka/ads/,Mindykkyan/PittadsDB-AdsPics,UNVERIFIED,https://people.cs.pitt.edu/~kovashka/ads/,open,11881.7,2.31,yes,https://huggingface.co/datasets/Mindykkyan/PittadsDB-AdsPics/resolve/main/image_annotations/image/Topics.json,yes,human,majority topic id -> name,n/a,clothing 8341/cars 7051/beauty 5826…,yes after filter,med,MAYBE,med,licence
47,D47.3,Image contains advertising,Open Images V7 (human-verified labels),https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4 (val labels) + images,28.4 (labels); ~0.2 per image,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human (verification),Advertising conf 1 -> yes; 0 -> no; absent -> skip,yes (110/97),Advertising,yes,med (faces),USE,high,
47,D47.5,Billboard present,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Billboard conf 1/0,yes (32/9 val; few),Billboard,yes,med,USE,med,test-split counts
48,D48.1,Wearing a dress,Fashionpedia,https://fashionpedia.github.io/home/index.html,detection-datasets/fashionpedia,CC BY 4.0,https://huggingface.co/datasets/detection-datasets/fashionpedia,open,3478.9,~480 (shard); single rows via /rows,no,https://datasets-server.huggingface.co/first-rows?dataset=detection-datasets/fashionpedia&config=default&split=train,yes,human,yes if 10 in objects.category,yes (506/652 val),46 categories,yes,med (people/celebrities),USE,high,owner Terms of Use text
48,D48.2,Main garment,Fashionpedia,https://fashionpedia.github.io/home/index.html,detection-datasets/fashionpedia,CC BY 4.0,https://huggingface.co/datasets/detection-datasets/fashionpedia,open,3478.9,~480,no,https://datasets-server.huggingface.co/first-rows?dataset=detection-datasets/fashionpedia&config=default&split=train,yes,human,single distinct garment id 0-12 -> name,n/a,garments 0-12,496 of 1158 val,med,USE,high,
48,D48.3,Bag present,Fashionpedia,https://fashionpedia.github.io/home/index.html,detection-datasets/fashionpedia,CC BY 4.0,https://huggingface.co/datasets/detection-datasets/fashionpedia,open,3478.9,~480,no,https://datasets-server.huggingface.co/first-rows?dataset=detection-datasets/fashionpedia&config=default&split=train,yes,human,yes if 24 in categories,yes (205/953 val),bag/wallet,yes,med,USE,high,
48,D48.4,Catalogue category,Fashion Product Images small,https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small,ashraq/fashion-product-images-small,UNVERIFIED,https://huggingface.co/datasets/ashraq/fashion-product-images-small,open mirror / Kaggle login,271.5,135.4,no,https://datasets-server.huggingface.co/first-rows?dataset=ashraq/fashion-product-images-small&config=default&split=train,yes,human (catalogue; inferred),answer=masterCategory,n/a,Apparel/Accessories/Footwear/Personal Care,yes,low,SKIP,high,licence; tiny 60x80 images
48,D48.5,Lipstick present,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Lipstick conf 1/0,yes (51/53),Lipstick,yes,med (faces),USE,high,
49,D49.1,Is this a screenshot,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Screenshot conf 1/0,yes (116/330),Screenshot,yes,low,USE,high,
49,D49.2,Which device,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,exactly one positive among {Mobile phone, Laptop, Computer monitor},n/a,3 devices (119/77/88 pos),only after filter,med,USE,med,exclusivity of unverified classes
50,D50.1,Weapon present,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Weapon conf 1 -> yes; 0 -> no,yes (192/196),Weapon (+Handgun/Rifle/Knife),yes,med,USE,high,
50,D50.2,Alcohol present,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Alcoholic beverage conf 1/0,yes (279/98),Alcoholic beverage/Beer/Wine/Cocktail,yes,med,USE,high,
50,D50.3,Brand/logo visible,Open Images V7,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,,annotations CC BY 4.0; images CC BY 2.0,https://storage.googleapis.com/openimages/web/factsfigures_v7.html,open,28.4,28.4,no,https://storage.googleapis.com/openimages/v7/oidv7-val-annotations-human-imagelabels.csv,yes,human,Brand conf 1/0,yes (166/329),Brand (Logo 79/9),yes,med,USE,high,
50,D50.4,Logo industry,LogoDet-3K,https://github.com/Wangjing1551/LogoDet-3K-Dataset,axonstan/LogoDet-3K,MIT (mirror only),https://huggingface.co/datasets/axonstan/LogoDet-3K,open,3116.5,311.7,no,https://datasets-server.huggingface.co/first-rows?dataset=axonstan/LogoDet-3K&config=default&split=train,yes,human,answer=industry_name,n/a,9 industries (Food 10670 … Medical 788),yes,low,MAYBE,med,owner licence
50,D50.5,Visible watermark,Watermark-or-Not-20K,https://huggingface.co/datasets/prithivMLmods/Watermark-or-Not-20K,prithivMLmods/Watermark-or-Not-20K,apache-2.0,https://huggingface.co/datasets/prithivMLmods/Watermark-or-Not-20K,open,2643,74.1,no,https://datasets-server.huggingface.co/first-rows?dataset=prithivMLmods/Watermark-or-Not-20K&config=default&split=train,yes,UNVERIFIED,label==1,yes (10000/10000),No Watermark/Watermark,yes,low,MAYBE,med,label origin
```

---

## 4. Gaps (tasks with no acceptable dataset)

| task | why no data | drawn/generator version realistic? how |
|---|---|---|
| D41.4 Error dialog present | No open, human- or generator-labelled set of real error screenshots found on the HF Hub (searches: "screenshot error", "error message screenshot", "blue screen"). | **Yes, high realism.** Render native-looking dialogs (Windows/macOS/GTK themes via HTML/CSS or Qt) over real app screenshots from ScreenSpot-Pro (MIT). Label = whether a dialog was injected; option lists can add dialog type (error / warning / info / update prompt). Hard negatives: non-error modals. |
| D41.5 Dark mode | No labels found. | **Yes.** Render the same HTML app mock in light and dark CSS themes. Label = theme. Low value. |
| D42.4 Overlap/truncation defect | Only candidate (zxy6654) has no labels (SKIP). The OwlEyes/Nighthawk display-issue sets were not located on open hosts [UNVERIFIED]. | **Yes.** Take WebSight-style HTML or Enrico wireframes and inject a defect (negative margins, `overflow:hidden` truncation, z-index occlusion, missing image). Label = defect type or none. Screenshot with headless Chrome. |
| D42.5 Placeholder text | None. | **Yes.** Swap real strings for "Lorem ipsum" / "TODO" / "[Title]" in rendered HTML. Label known. |
| D42.6 Low-contrast text | None with labels. | **Yes, exact.** Render text with controlled foreground/background colours. Label = WCAG contrast ratio < 4.5:1, computed (generator). |
| D44.6 Rooftop solar | PatternNet is 256 px (SKIP). The Cyrille37 IGN set has only positive polygons (676 files, 29.8 MB, MIT); negatives UNVERIFIED. | **Partial.** Synthetic aerial is weak. Better: an owner dataset with negatives (e.g. Bradbury et al. Duke solar, licence UNVERIFIED), not checked. |
| D45.5 Handwritten answer correct | Handwriting candidates (MathWriting copies, CROHME copies, HumynLabs notes) were not probed; licences and labels UNVERIFIED. | **Yes.** Render worksheet items with handwriting fonts, or stroke data from MathWriting (if its licence allows) for answers. Label = whether the written answer equals the key (known at generation). |
| D46.7 Page rotated | Not needed as a dataset. | **Yes, exact.** Rotate DocLayNet pages (CDLA-Permissive) by 0/90/180/270. Label = rotation. |
| D47.4 Disclosure label visible | No dataset found. | **Yes.** Composite "#ad" / "Sponsored" / "Paid partnership" overlays at varied size, contrast and position onto CC images (Open Images). Label = present / absent, or "conspicuous" via size/contrast thresholds computed at generation. |
| D49.3 Photo usable (blur/dark) | No labelled set. | **Yes, exact.** Apply Gaussian/motion blur or underexposure with known parameters to Open Images device photos. Label = parameter above or below a threshold. |
| D49.4 Cracked screen | Only `34data/ai-generated-ecommerce-damaged-phone-screen` (AI-generated, text modality; not probed). Roboflow sets need login (GATED). | **Weak.** Overlaying crack textures on phone photos is feasible but looks artificial. A human photo set is needed. |
| D49.5 Error message on device screen | None. | **Yes.** Composite rendered error screens (D41.4 generator) into phone/monitor screen regions of Open Images photos via a homography. Label known. |
| D50.6 Counterfeit product | No open labelled data (only tiny unprobed HF uploads). The OECD shows the business value. | **No.** Counterfeit status is not visible from generator parameters. It needs brand-owner ground truth. |
| (D41.2 balance) | OS is confounded with app in ScreenSpot-Pro. | Add the `common_{windows,macos,linux}` screenshots, or render the same web page in three OS browser chromes. |

---

## 5. Cannot verify

- **FigureQA owner licence text.** It sits behind "Agree & Download" on the Microsoft page; not accepted. GATED.
- **DVQA, AI2D, Pitt Ads, LogoDet-3K, FloodNet and WHU-RS19 owner licences.** None was found on the owner README or page. The licences shown come from mirrors only.
- **Fashionpedia owner "Terms of Use".** The link text could not be extracted. The HF card says CC BY 4.0.
- **VisDrone owner terms.** The mirror card is self-contradictory (cc-by-sa-3.0 YAML vs NC-SA text).
- **Label-origin quotes from papers** (ScreenSpot-Pro, CharXiv, ChartBench, Mind2Web, ScienceQA). Papers were not read; marked [INFERRED].
- **ChartBench single-file extraction from `test.zip`.** The central directory is reachable by range read (10,552 entries), but extracting one PNG was not attempted.
- **Per-class counts** for the CharXiv q11 yes/no, the DocLayNet Table yes/no, the font-detection classes, and the ScienceQA yes/no image share.
- **Hateful Memes (Facebook)** was found as HF mirrors but not probed. The original requires accepting a licence, so it is likely GATED [UNVERIFIED].
- **The `dchen278/pitt-ads-full` path mapping** (`images/0XX/<id>`) to the owner annotation keys (`<subfolder>/<id>`) was not confirmed.
- **GitHub REST API** was blocked in this session (add_repo required). Licences were read via raw.githubusercontent.com instead.
- **Value sources.** Several are vendor or secondary (unthread, Bluestone PIM, Grypp, Verato citing Gartner, law-firm FTC summaries). No primary brand-safety source for weapons was found.

---

## Part C. Question expansion recipes (USE candidates)

**Rules for all datasets:**
- Tier C items always carry `label_origin: model` and are never mixed into Tier A or B scores.
- A Tier C item is kept only if a second, different-family model answers it the same way without seeing the first model's answer.
- The model under test never writes questions.
- The most useful Tier C work is rewording, harder distractors (visually confusable options) and natural-language variety (ticket-style phrasing).

### ScreenSpot-Pro (D41.1–3)
- **A**: application, platform, group per screenshot.
- **B**:
  1. "Which of these apps is NOT open?" — the 3 distractors come from other apps in the same `group`.
  2. "Is this a Creative app?" — `group == Creative`.
  3. "Is the screen wider than 3000 px?" — from `img_size` (a metadata check; use sparingly).
  4. "Does this screenshot contain the element '<instruction target>'?" — yes for the paired image. No only if that instruction belongs to another app's annotation file, so it is safe only across apps.
- **C**: ticket-style rewordings ("User says Excel is frozen. Is the screenshot from Excel?"); confusable distractors (Word vs Pages, PyCharm vs IntelliJ).

### Enrico (D42.1–2)
- **A**: topic.
- **B**:
  1. Yes/no per topic ("Is this a settings screen?").
  2. "Which is NOT this screen's type?" — 3 options from other topics.
  3. Group mapping: {login, form} → "input screen" yes/no.
- **C**: UX-review phrasing; distractors among adjacent topics (list vs news vs gallery).

### ChartBench (D43.1–3)
- **A**: type.chart, VC and VE assertion labels.
- **B**:
  1. Flip the pair: use the No assertion as the question; the answer is no.
  2. Coarse type: is it a "bar family" chart (bar / combination with bar)?
  3. Subtype pick-one from `type.image`, e.g. horizontal vs vertical stacked.
  4. NQA numeric answer bucketed into 3–4 ranges as pick-one.
- **C**: business phrasing ("Did Platform A outperform B in Month 5?"); distractor values near the true value.

### CharXiv (D43.4–5)
- **A**: descriptive answers for templates 11 (intersect) and 19 (subplot count).
- **B**:
  1. Layout pick-one (template 18).
  2. "Does the plot have a legend?" — no if the template 12 answer is "Not Applicable", yes otherwise.
  3. "Does it have a colorbar?" — the same rule on template 14/15.
  4. Trend pick-one (template 16) only where the answers are categorical.
- **C**: rewording; harder distractors for layout.

### ScienceQA (D45.1, 45.3, 45.4)
- **A**: choices[answer], subject, yes/no items.
- **B**:
  1. "Which option is NOT correct?" — pick one of the wrong choices as the answer when there are 3+ choices; the question phrasing must say this.
  2. Topic pick-one (`topic`, e.g. geography / physics / chemistry).
  3. Grade band from `grade`.
  4. Category yes/no ("Is this a map-reading item?" from `skill`).
- **C**: teacher-style rewording; plausible distractor answers written by a model (validated by a second model plus the original key).

### DocLayNet (D46.1–2)
- **A**: doc_category; table presence.
- **B**:
  1. Presence yes/no for Picture, Formula, Footnote, Title.
  2. "Which element is NOT on this page?" — from present and absent sets.
  3. "Are there more than N text blocks?" — count of id 9.
  4. "Is the table larger than the largest picture?" — compare bbox areas.
  5. Page count bucket from `num_pages` (metadata).
- **C**: archivist rewording; distractor categories (e.g. tender vs law).

### LoC Beyond Words (D46.3)
- **A**: presence per category.
- **B**:
  1. Counts: "How many photographs? {0, 1, 2, 3+}" from annotation counts.
  2. "Which is NOT present?" over {Photograph, Map, Comics, Advertisement}.
  3. "Is there more advertising area than photo area?" from summed `area`.
  4. Decade of issue from the URL date.
- **C**: research-librarian phrasing.

### Early printed books fonts (D46.4)
- **A**: single label.
- **B**:
  1. Blackletter family yes/no ({textura, rotunda, bastarda, schwabacher, fraktur} vs roman/italic).
  2. "Does the page mix 2+ font groups?" — `len(labels) > 1`.
  3. "Is Greek present?"
- **C**: limited value; rewording only.

### illustrated_ads (D46.5)
- **A**: label.
- **B**:
  1. Decade pick-one from `pub_date`.
  2. "Was this published in the 1880s or later?" yes/no.
  3. State pick-one from `place_of_publication`. This is metadata, not visible, so avoid it except as a control.
- **C**: rewording.

### Open Images V7 (D47.3, D47.5, D48.5, D49.1, D49.2, D50.1–3)
- **A**: explicit per-class 1/0 rows.
- **B**:
  1. Parent/child roll-up: Handgun/Rifle/Shotgun = 1 → Weapon yes. Use only explicit rows, and do not infer negatives through the hierarchy.
  2. "Which of these is present?" — exactly one verified positive and the other options verified 0 on the same image.
  3. "Which of these is NOT present?" — the inverse of 2.
  4. Brand-safety composite: "Does the image contain alcohol OR a weapon?" — yes if either is 1. No only if both are verified 0.
- **C**: moderation-policy phrasing ("Would this image violate a no-weapons ad policy?"). Model-written distractor classes are useful here.

### Fashionpedia (D48.1–3)
- **A**: category presence.
- **B**:
  1. Count shoes/sleeves bucketed.
  2. "Which accessory is present?" among {bag, hat, glasses, belt} — exactly one present.
  3. "Which garment is NOT worn?"
  4. "Is the dress the largest garment by area?" from `area`.
  5. Upper vs lower garment presence.
- **C**: catalogue-attribute phrasing ("Tag this listing: does it show a dress?"); confusable distractors (cardigan vs sweater, coat vs jacket).
