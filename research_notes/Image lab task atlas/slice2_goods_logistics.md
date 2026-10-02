# Slice 2: Goods, places and logistics (domains 11–20)

Researcher notes for the Image lab task atlas. They follow Part 1 of `_spec.md`. Every dataset fact below comes from a fetch made in this session (2026-10-01) using the HF Hub API (`/api/datasets/<id>?blobs=true`, `/tree`), the datasets-server (`/splits`, `/first-rows`, `/rows`, `/statistics`), raw READMEs, the GitHub raw/API, and the Zenodo records API. Tags: [ROW] = seen in a fetched row or annotation file; [CARD] = owner's README/card/record; [PAPER] = paper or project report; [INFERRED]; [UNVERIFIED].

**Domain swaps:** none made. Domains 14 (food-service hygiene) and 17 (last-mile proof) are nearly empty of usable open data, but the spec only allows swapping within the slice. I found no domain inside the slice with "far more" data to swap in. Both are reported honestly in Gaps with generator routes.

**Headline:** 9 candidates rated USE:
- D11.3 price-tag detection
- D12.3 Fashionpedia
- D12.4 ABO-Edit (white background)
- D13.4 grocery-images-5class
- D15.1 forklift person-present
- D15.2 cardboard box anomaly
- D19.1 CubiCasa5K-YOLO doors
- D20.1 TrashNet
- D11.5 RPC: MAYBE (label origin not verified)

Most others fail on licence or label origin, or have positives only.

---

## 1. Task atlas

Value reasons come from web-search result snippets. The URLs were returned by the search tool and I did not open them in full, so each sentence is tagged [UNVERIFIED-snippet] unless noted. "No source" means none was found or fetched.

### Domain 11: Retail shelves and merchandising
| # | Task | Typed question | Options | Image type | Value reason (source) |
|---|---|---|---|---|---|
| 11.1 | Out-of-stock gap | "Is there an empty facing (gap) on this shelf?" | yes/no | photo | IHL Group puts the global cost of inventory distortion at about $1.77T in 2025, of which about $1.2T is out-of-stocks [UNVERIFIED-snippet] ([IHL](https://www.ihlservices.com/product/inventory-distortion/); [Chain Store Age](https://chainstoreage.com/study-global-retail-losses-due-inventory-distortion-hit-177-trillion)) |
| 11.2 | Price-tag photo usable | "How readable is this price tag crop?" | invalid / medium-quality / high-quality | photo crop | Open Prices uses this exact class to triage crowd price photos before extraction ([OFF report](https://github.com/openfoodfacts/openfoodfacts-ai/blob/develop/docs/reports/2026-03-price-tag-classification.md)) [PAPER] |
| 11.3 | Shelf-edge label count | "How many price tags are visible?" | 0–2 / 3–5 / 6–10 / 11+ | photo | Same IHL source (label audits feed availability checks) [UNVERIFIED-snippet] |
| 11.4 | Discount flag on tag | "Does this price tag show a promotional/discounted price?" | yes/no | photo crop | No source fetched |
| 11.5 | Checkout basket count | "How many products are on the checkout tray?" | 3–4 / 5–6 / 7–8 / 9+ | photo (top-down) | RPC paper motivates automatic checkout (arXiv 1901.07249) [UNVERIFIED: abstract not fetched] |
| 11.6 | Planogram category block | "Which product category occupies this shelf?" | drinks / snacks / dairy / household / other | photo | No source fetched |

### Domain 12: E-commerce product listings and catalogues
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 12.1 | Category check of listing image | "What product type is shown?" | e.g. SHOES / CHAIR / LAMP / SOFA / HARDWARE / other | photo (catalogue) | No source fetched (catalogue mis-categorisation cost) |
| 12.2 | Colour attribute check | "What is the main colour of the product?" | 4–6 colour names | photo | No source fetched |
| 12.3 | Garment present in model shot | "Which of these garments is worn: dress / pants / skirt / shorts?" | 4 options | photo | No source fetched |
| 12.4 | Main-image compliance (white background) | "Is the product shown alone on a plain white background?" | yes/no | photo / render | No source fetched (marketplace main-image rules; not fetched) |
| 12.5 | View/angle check | "Is the product shown front-on or turned?" | front / three-quarter-or-other | render | No source |
| 12.6 | Product colour/size text vs image | (Tier C only) | n/a | photo | No source |

### Domain 13: Grocery and produce quality
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 13.1 | Fresh vs rotten | "Is this fruit/vegetable rotten?" | yes/no | photo | USDA ERS: average supermarket loss is 11.6% for 31 fresh vegetables and fresh-fruit shrink is 12.6% [UNVERIFIED-snippet] ([USDA ERS](https://ers.usda.gov/data-products/food-availability-per-capita-data-system/food-loss)) |
| 13.2 | Ripeness | "Is this banana/mango ripe or unripe?" | ripe / unripe (× banana / mango) | photo | Same USDA ERS source [UNVERIFIED-snippet] |
| 13.3 | Variety identification at till | "Which variety is this?" | e.g. Golden-Delicious / Granny-Smith / Pink-Lady … | photo (in-store) | No source fetched (PLU mis-keying) |
| 13.4 | Item identification | "Which grocery item is this?" | apple / banana / bread_roll / cheese / tomato | photo | No source |
| 13.5 | Bruise/defect grade | "Grade of this produce item?" | Extra / I / II | photo | No source (UNECE marketing standards, not fetched) |
| 13.6 | Date-label legible | "Is the use-by date legible?" | yes/no | photo | No source |

### Domain 14: Food service and restaurant hygiene
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 14.1 | Dish matches order | "Which dish is this?" | 2–6 of 101 Food-101 classes | photo | No source fetched |
| 14.2 | Glove / hairnet worn by food handler | "Is the food handler wearing gloves?" | yes/no | photo / CCTV frame | No source fetched |
| 14.3 | Plate waste | "How much of the meal is left?" | none / some / most | photo | No source fetched |
| 14.4 | Pest sighting | "Is a rodent or cockroach visible?" | yes/no | CCTV frame | No source |
| 14.5 | Kitchen surface clean | "Is the prep surface clear of debris?" | yes/no | photo | No source |

### Domain 15: Warehousing and inventory
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 15.1 | Pedestrian near forklift | "Is a person visible together with the forklift?" | yes/no | photo | OSHA, as cited in snippets: about 85 forklift deaths and about 34,900 serious injuries a year [UNVERIFIED-snippet] ([OSHA PIT material](https://obis.osha.gov/dte/grant_materials/fy09/sh-18794-09/power_industrial_trucks.pdf)) |
| 15.2 | Damaged carton | "Is this cardboard box damaged?" | yes/no | photo | No source fetched |
| 15.3 | Pallet count | "How many pallets are in view?" | 0 / 1 / 2–3 / 4+ | photo | No source |
| 15.4 | Boxes on pallet | "How many boxes on this pallet?" | ranges | photo / render | No source |
| 15.5 | Aisle obstruction | "Is the aisle blocked?" | yes/no | photo | Same OSHA source |

### Domain 16: Parcel, freight and container logistics
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 16.1 | Container defect type | "What defect is on this container?" | Dent / Rusty / Scratch / Deframe / Hole | photo | No source fetched |
| 16.2 | Container damaged | "Is this container damaged?" | yes/no | photo | No source |
| 16.3 | Parcel damaged | "Is this parcel damaged?" | yes/no | photo | No source |
| 16.4 | Container ID read | "What is the check digit / owner code?" | 4–6 options | photo | No source |
| 16.5 | Shipping-label barcode present | "Is a readable barcode visible?" | yes/no | photo | No source |

### Domain 17: Last-mile delivery proof
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 17.1 | Parcel visible at door | "Is a parcel visible in the delivery photo?" | yes/no | photo | SafeWise, as reported: about 104M packages stolen in 2024 (~$15B) [UNVERIFIED-snippet] ([RetailWire](https://retailwire.com/porch-pirates-holiday-season/)) |
| 17.2 | Placement | "Where was the parcel left?" | doorstep / mailbox / lobby / locker | photo | Same source |
| 17.3 | Photo usable | "Is the proof photo sharp enough to see the parcel?" | yes/no | photo | No source |
| 17.4 | House number visible | "Is a house number visible?" | yes/no | photo | No source |
| 17.5 | Person in photo (privacy) | "Does the photo contain a person?" | yes/no | photo | No source |

### Domain 18: Hospitality and room condition
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 18.1 | Room type tag for listing | "Which room is this?" | bedroom / bathroom / kitchen / livingroom / dining_room | photo | No source fetched |
| 18.2 | Amenity visible | "Is a towel visible?" (bathroom) | yes/no | photo | No source |
| 18.3 | Bed made | "Is the bed made?" | yes/no | photo | No source |
| 18.4 | Room tidy | "Is the room ready for the next guest?" | yes/no | photo | No source |
| 18.5 | Visible damage/stain | "Is there visible damage?" | yes/no | photo | No source |

### Domain 19: Real estate (exteriors, interiors, floorplans)
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 19.1 | Floorplan door count | "How many doors does this floorplan show?" | ranges | drawing (scan/raster) | NAR, as reported: 55% of buyers find floor plans "very useful" [UNVERIFIED-snippet] ([F8 summary of NAR](https://www.f8re.com/post/the-surprising-importance-of-floor-plans-in-the-home-search-process)) |
| 19.2 | Bedroom count from plan | "How many bedrooms?" | 1 / 2 / 3 / 4+ | drawing | Same source |
| 19.3 | Construction era of house | "When was this house built?" | pre-1940 / 1941–70 / 1971–90 / post-1990 | photo (street) | No source fetched |
| 19.4 | Architectural style | "Which style is this facade?" | 4–6 of 20 styles | photo / generated | No source |
| 19.5 | Interior room type | (same as 18.1) | | photo | |
| 19.6 | CAD symbol count | "How many doors/windows in this CAD sheet?" | ranges | drawing | No source |

### Domain 20: Facilities, cleaning and waste
| # | Task | Typed question | Options | Image type | Value reason |
|---|---|---|---|---|---|
| 20.1 | Recycling stream | "Which bin does this item go in?" | cardboard / glass / metal / paper / plastic / trash | photo | Recycling Partnership: California cities see about 20% average inbound contamination [UNVERIFIED-snippet] ([Resource Recycling](https://dev.resource-recycling.com/recycling/2020/05/05/west-coast-study-recycling-zeal-doesnt-erase-contamination/)) |
| 20.2 | Illegal dumping in aerial tile | "Is dumped waste visible in this tile?" | yes/no | aerial | No source fetched |
| 20.3 | Litter material | "What is the main litter item?" | bottle / can / cigarette / plastic bag / cup | photo | No source |
| 20.4 | Bin overflowing | "Is the bin overflowing?" | yes/no | photo | No source |
| 20.5 | Wet floor / spill | "Is there a spill on the floor?" | yes/no | photo | No source |

---

## 2. Dataset qualification cards

### D11.2: openfoodfacts/price-tag-classification (rank 1 for 11.2)
1. Landing: https://huggingface.co/datasets/openfoodfacts/price-tag-classification. Files: `/tree/main/data`. Repo id `openfoodfacts/price-tag-classification`.
2. Licence: **not stated** on the card. There is no licence tag and no licence line in the README [CARD]. The sibling repo price-tag-detection says the Open Prices images are CC-BY-SA 4.0 [CARD], so the same licence is likely here [INFERRED].
3. Access: open (gated: False) [CARD].
4. Size: 48.5 MB total. Smallest unit: `data/val-00000-of-00001.parquet` at 9.87 MB. Train is 38.62 MB [CARD].
5. Sample proof: `https://datasets-server.huggingface.co/first-rows?dataset=openfoodfacts/price-tag-classification&config=default&split=train` [ROW]
   - `{"image_id":"140623","width":449,"height":316,"meta":{"image_url":"https://prices.openfoodfacts.org/img/price-tags/000/140/000140623.webp","price_id":null,"proof_id":"64240"},"label":0}`
   - `{"image_id":"149058","width":719,"height":385,"meta":{...,"price_id":"193851","proof_id":"67203"},"label":2}`
   - `{"image_id":"167945","width":690,"height":355,"meta":{...,"price_id":"210866","proof_id":"77223"},"label":2}`
6. Schema [CARD]:
   - `image_id` str
   - `image` Image
   - `width`, `height` int
   - `meta{image_url, price_id, proof_id}`
   - `label` ClassLabel {0 invalid, 1 medium-quality, 2 high-quality}. Definitions: invalid = blurry, not a tag, or more than half truncated; medium = readable-ish or partly truncated; high = very low blur.
7. Label origin: human. The report describes building the set with Label Studio and Labelr, using tags "to filter in Label Studio interface" [PAPER: OFF report]. The exact annotator count is UNVERIFIED.
8. Answer rule: option = `label` name.
9. Classes: train has invalid 534, medium-quality 220, high-quality 893 (`/statistics`) [ROW]. Not a yes/no task.
10. Per-image fit: exactly one label per crop [CARD].
11. Risks:
    - Crops can be small: minimum height 38 px, and 56 train crops are under 137 px tall [ROW, statistics]. Filter to 300 px or more.
    - The label is a subjective blur grade, so expect some noise [INFERRED].
    - Low personal-data risk.
12. Templates:
    - "How readable is this price tag photo? (invalid / medium-quality / high-quality)"
    - "Is this crop usable for reading the price? (yes = medium or high / no = invalid)"
    - "Is more than half of the tag cut off or blurred? (yes = invalid)"
13. Verdict: **MAYBE**. Fails the "licence stated" test.

### D11.3: openfoodfacts/price-tag-detection (rank 1 for 11.3)
1. Landing: https://huggingface.co/datasets/openfoodfacts/price-tag-detection. Files: `/tree/main/data`.
2. Licence: "Just like the original images, the images in this dataset are licensed under the Creative Commons Attribution Share Alike license (CC-BY-SA 4.0)." (README) [CARD]. Research and testing are allowed; share-alike applies.
3. Access: open [CARD].
4. Size: 399.2 MB. Smallest unit: `data/val-00000-of-00001.parquet` at 44.16 MB (fits under the cap). Train is 355.08 MB [CARD].
5. Sample proof: `first-rows?dataset=openfoodfacts/price-tag-detection&config=default&split=train` [ROW]
   - `{"image_id":"6485","width":768,"height":1024,"objects":{"bbox":[[0.252,0.894,0.305,0.965],[0.235,0.969,0.280,1.0],[0.441,0.865,0.490,0.942],[0.657,0.886,0.698,0.963],[0.879,0.934,0.931,1.0]],"category_id":[0,0,0,0,0],"category_name":["price-tag"×5]}}`
   - `{"image_id":"12447","width":399,"height":568,"objects":{"bbox":[[0.103,0.166,0.910,1.0],[0.096,-1.3e-17,0.938,0.186]],"category_id":[0,0],"category_name":["price-tag","price-tag"]}}`
   - `{"image_id":"5744","width":766,"height":1024,"objects":{"bbox":[[0.139,0.725,0.226,0.906],[0.031,0.417,0.123,0.582],… (9+ boxes)],"category_id":[0,…]}}`
6. Schema:
   - `image_id`, `image`, `width`, `height`
   - `meta.image_url`
   - `objects.bbox`: list of [y_min, x_min, y_max, x_max], normalised
   - `objects.category_id` / `objects.category_name`: a single class, `price-tag` [CARD]
7. Label origin: human. "Images were collected from the Open Prices database and labeled manually." [CARD]
8. Answer rule: n = len(`objects.category_id`), mapped to a bin.
9. Classes: one class. Val has 247 images; image width is 301–1024 px [ROW, statistics]. Whether any image has zero tags is UNVERIFIED. This does not matter for the count-bin question.
10. Per-image fit: one count per image.
11. Risks:
    - Resized so the longest side is at most 1024 px [CARD]; heights go down to 200 px [ROW].
    - Crowd photos from shops may include shoppers' faces occasionally [INFERRED].
    - Boxes are clipped at the image edge (negative coordinates seen) [ROW].
12. Templates:
    - "How many price tags are visible? (0–2 / 3–5 / 6–10 / 11+)"
    - "Is there more than one price tag? (yes/no)"
    - "Is any price tag cut off at the image edge? (yes/no; a bbox coordinate ≤ 0 or ≥ 1)"
13. Verdict: **USE** (confidence med; the zero-tag negatives question is untested).

### D11.4: openfoodfacts/price-tag-extraction
1. https://huggingface.co/datasets/openfoodfacts/price-tag-extraction
2. Licence: none on the card [CARD].
3. Access: open.
4. Size: 12,947 MB. Smallest unit: val parquet, 180.20 MB.
5. Rows [ROW]:
   - `{"image_id":"125873","output":"{\"type\":\"PRODUCT\",\"prices\":[{\"price\":3.99,\"currency\":\"$\",\"price_per\":\"UNIT\",\"discount_type\":\"SALE\",\"price_is_discounted\":true,...`
   - `{"image_id":"96699","output":"{...\"price\":9.79,...\"barcode\":\"14201821\",\"product_name\":\"MB CHIVES ALL NATURAL\"...`
   - `{"image_id":"78683","output":"{...\"price\":4.99,\"currency\":\"EUR\"...\"price\":7.56,...\"price_per\":\"KILOGRAM\"...`
6. Schema: `output` JSON string (prices[], discount_type, barcode, product_name, category …) and `meta`.
7. Label origin: **machine**. "We then used Google Gemini 3 Flash … to extract the relevant information" [CARD].
8. A rule exists (`price_is_discounted`), but the labels are untrusted.
9–12. Not pursued.
13. Verdict: **SKIP**. Machine-labels trap and no licence. The card mentions a separate human "price-tag-extraction benchmark v2.0" on GitHub [CARD]. I did not fetch it; it is listed under Cannot verify.

### D11.5: benjamintli/retail-product-checkout (RPC mirror)
1. https://huggingface.co/datasets/benjamintli/retail-product-checkout. Original project: https://rpc-dataset.github.io/ (not fetched).
2. Licence: README says "The RPC dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)** license by the original authors." The YAML tag says `cc-by-nc-sa-2.0`, which conflicts [CARD]. Research and testing are allowed; commercial use is not.
3. Access: open.
4. Size: 15,279 MB. The smallest shard I listed is `data/validation-00000-of-00003.parquet` at 315.90 MB, which is over the 50 MB cap. Use `/rows` to sample [CARD].
5. Rows from `rows?...&split=validation&offset=0&length=100` [ROW]:
   - row 0: 1865×1865, n_objects 9, categories [45_instant_noodles, 70_dessert, 70_dessert, 75_drink, 75_drink, 100_milk, 56_dessert, 45_instant_noodles, 56_dessert]
   - row 1: 1865×1865, n_objects 9, [56_dessert, 45_instant_noodles, 45_instant_noodles, 75_drink, 75_drink, 70_dessert, 70_dessert, 56_dessert, 100_milk]
   - row 2: 1847×1847, n_objects 7, [7_puffed_food ×3, 147_candy, 88_alcohol ×3]
6. Schema:
   - `image`
   - `objects.bbox`: [x, y, w, h] in pixels
   - `objects.category`: ClassLabel over 200 SKUs named `<n>_<supercategory>` (puffed_food, dried_fruit, dried_food, instant_drink, instant_noodles, dessert, drink, milk, candy, alcohol …) [CARD]
   - Train split (53,739 rows): single-product exemplar shots. Val (6,000) and test (24,000): checkout trays [CARD, ROW].
7. Label origin: the card credits "data collection, annotation" to the original authors [CARD]. Whether it was human or machine-assisted is **UNVERIFIED** (the arXiv abstract fetch failed).
8. Answer rule: count = len(`objects.category`); supercategory = the suffix after `_`.
9. Objects per image in the first 100 val rows: 4:3, 5:31, 6:12, 7:24, 8:13, 9:17 [ROW].
10. One count per image.
11. Risks: no people; large images; NC licence; whether the product classes are Chinese-market SKUs is UNVERIFIED.
12. Templates:
    - "How many products are on the tray? (4–5 / 6–7 / 8–9 / 10+)"
    - "Is any alcohol product on the tray? (yes/no)"
    - "Which category has the most items? (drink / dessert / instant_noodles / other)"
13. Verdict: **MAYBE**. Label origin unverified. Upgrade to USE once the paper's annotation section confirms human labels.

### D11.1 / D11.6: shelfwise-by-form/SKUs_on_shelves_PL
1. https://huggingface.co/datasets/shelfwise-by-form/SKUs_on_shelves_PL
2. Licence: `license: cc-by-4.0` [CARD].
3. Access: open.
4. Size: `SKUs_on_shelves_PL.zip` is a **SINGLE ARCHIVE of 11,422.09 MB** [CARD].
5. The viewer shows images only, with no annotations (`features: [image]`). Rows were image placeholders only (1627×228, 466×612, 1725×1529) [ROW]. No annotation rows could be pasted.
6. COCO format: ~27k images, ~2M boxes, ~8k SKUs. It has `unreadable` and `unknown_product` auxiliary classes [CARD].
7. Origin: "annotated SKUs" [CARD]; human vs machine UNVERIFIED.
8–12. Not computable without the archive.
13. Verdict: **SKIP** (single-huge-archive trap). It is the most promising shelf dataset if a human fetches only the COCO JSON.

### D12.1 / D12.2: suvadityamuk/amazon-berkeley-objects (ABO mirror)
1. https://huggingface.co/datasets/suvadityamuk/amazon-berkeley-objects. Original: https://amazon-berkeley-objects.s3.amazonaws.com/index.html (not fetched).
2. Licence: "This work is licensed under the **Creative Commons Attribution 4.0 International Public License (CC BY 4.0)**". It adds: "Note: the source S3 bucket root also contains a `LICENSE-CC-BY-NC-4.0.txt` file, but the official ABO download page licenses the released archives under CC BY 4.0" [CARD]. Flag this ambiguity.
3. Access: open.
4. Size: 617,650 MB total. Smallest units by config [CARD]:
   - `listings/train-listings_1.json.parquet`: 12.09 MB (17 files, 197 MB)
   - `images_small/train-00023.parquet`: 60.5 MB (256 px images)
   - `images_original/train-00059.parquet`: 172.3 MB
5. Rows from `first-rows?...&config=listings&split=train` [ROW]:
   - `{"item_id":"B06X9STHNG","item_name_en":"Amazon-merk - vinden. Dames Leder Gesloten Teen Hakken,…","brand_en":"find.","product_type":"SHOES","color_en":"Veelkleurig Vrouw Blauw","country":"NL","main_image_id":"81iZlv3bjpL","node_paths":"['/Categorieën/Dames/Schoenen/Pumps']"}`
   - `{"item_id":"B07P8ML82R","item_name_en":"22\" Bottom Mount Drawer Slides, White Powder Coat, 10 Pairs","brand_en":"AmazonBasics","product_type":"HARDWARE","color_en":"White Powder Coat","country":"MX","main_image_id":"619y9YG9cnL"}`
   - `{"item_id":"B07H9GMYXS","item_name_en":"AmazonBasics PETG 3D Printer Filament, 1.75mm, 1 kg Spool…","product_type":"MECHANICAL_COMPONENTS","color_en":"Translucent Yellow","country":"AE","main_image_id":"81NP7qh2L6L"}`
   - images_small rows: `{"image_id":"00834536","height":256,"width":256,"path":"images/small/00/00834536.jpg"}` [ROW]
6. Schema:
   - listings: `item_id`, `item_name_en`, `brand_en`, `product_type` (catalogue enum), `color_en` (free text, multilingual), `main_image_id`, `other_image_ids`, `node_paths`, `raw_listing_json`
   - images: `image_id`, `path`, `height`, `width`
7. Label origin: catalogue metadata entered by Amazon/sellers. That makes it human, not model [INFERRED; not stated on card].
8. Answer rule: join `listings.main_image_id` to `images_*.image_id`; the option is `product_type`.
9. Class counts were not computed (the statistics endpoint was not run for the listings config) [UNVERIFIED].
10. One product per main image [INFERRED].
11. Risks:
    - The 256 px small images hit the tiny-image trap; use images_original.
    - `color_en` is free text in many languages, so it needs normalising.
    - Amazon catalogue images are likely in model training data.
12. Templates:
    - "What product type is shown? (SHOES / CHAIR / LAMP / SOFA / HARDWARE / other)"
    - "Is this product footwear? (yes/no)"
    - "Which brand family? (AmazonBasics / Rivet / Stone & Beam / other)"
13. Verdict: **MAYBE**. Image access only via ≥172 MB shards or the small 256 px images; label origin inferred.

### D12.3: detection-datasets/fashionpedia
1. https://huggingface.co/datasets/detection-datasets/fashionpedia. Home: fashionpedia.github.io (not fetched).
2. Licence: "Fashionpedia is licensed under a Creative Commons Attribution 4.0 International License." [CARD]
3. Access: open.
4. Size: 3,478.9 MB. Smallest unit: `data/val-00000-of-00001.parquet` at 84.85 MB, which is over the cap, so sample via `/rows` [CARD].
5. Rows from `first-rows?...&split=train` [ROW] (category ids index into the 46-name list):
   - `{"image_id":23,"width":682,"height":1024,"objects":{"bbox_id":[150311,150312,150313,150314],"category":[23,23,33,10],"bbox":[[445,910,505,983],[239,940,284,994],[298,282,386,352],[210,282,448,665]],"area":[1422,843,373,56375]}}` = shoe, shoe, neckline, dress
   - `{"image_id":25,…"category":[2,33,31,31,13,7,22,22,23,23],…}` = sweater, neckline, sleeve×2, glasses, shorts, sock×2, shoe×2
   - `{"image_id":26,…"category":[13,29,28,32,32,31,31,0,31,31,18,4,…+3]}`
6. Schema: `image_id`, `width`, `height`, `objects{bbox_id, category (ClassLabel, 46 names: 27 garments + 19 parts), bbox [x1,y1,x2,y2], area}` [CARD, ROW].
7. Label origin: human. The card says "an ontology built by fashion experts … a dataset … annotated with segmentation masks" [CARD]. Annotator detail is in the paper [UNVERIFIED].
8. Answer rule: the set of garment names in `objects.category`. For the 4-way question keep images where exactly one of {dress=10, pants=6, skirt=8, shorts=7} is present.
9. 46 classes; per-class counts not fetched [UNVERIFIED]. The pick-one question needs no negatives.
10. Several items per image. Filter as in rule 8 to get one clean answer.
11. Risks:
    - Every image shows a person, often a face; some are celebrity event photos [CARD], which brings identity risk. Do not ask identity questions.
    - Likely overlap with model training data.
12. Templates:
    - "Which garment is worn: dress / pants / skirt / shorts?"
    - "Is the person wearing glasses? (yes/no; category 13 present)"
    - "How many shoes are annotated? (0 / 1 / 2 / 3+)"
13. Verdict: **USE** (confidence med; the yes/no templates assume exhaustive annotation, which is UNVERIFIED, so keep yes/no as Tier B with caution).

### D12.4 / D12.5: amazon/ABO-Edit
1. https://huggingface.co/datasets/amazon/ABO-Edit
2. Licence: "In accordance with CC BY 4.0, **ABO-Edit** is derived from Amazon Berkeley Objects (ABO) and it is distributed under the same **CC BY 4.0** license" [CARD].
3. Access: open.
4. Size: 18,288.6 MB in Arrow files of about 505 MB each [CARD]. No unit under 50 MB; sample via `/rows`.
5. Rows from `first-rows?dataset=amazon/ABO-Edit&config=default&split=train` [ROW]:
   - `{"xsource_image":"<2560x2560>","xtarget_image":"<1024x1024>","simplified_rotation_prompt":"Rotate the object: front view with a top tilt rotation of 22 degrees.","x_source_image_id":"A13tp5lR-9L","product_type":"LAMP","task":"lifestyle_to_white_with_controlled_rotation","llm_object_category":"lamp"}`
   - `{…"simplified_rotation_prompt":"…front view with a top tilt rotation of 21 degrees.","x_source_image_id":"A1xXv0BmDgL","product_type":"CHAIR","llm_object_category":"Chair"}`
   - `{…"…top tilt rotation of 23 degrees.","x_source_image_id":"91g1BZxBl9L","product_type":"SOFA"}`
6. Schema:
   - `xsource_image`: lifestyle photo
   - `xtarget_image`: the "same product isolated on a white background with realistic shadow, rotated and tilted to a precisely specified angle" [CARD], rendered from ABO 3D assets (`ABO_glb_path`)
   - `product_type`: catalogue enum
   - `simplified_rotation_prompt`: generator angle
   - `full_editing_prompt`, `object_description`, `llm_object_category`: VLM-written, **machine**
7. Label origin: mixed. The white/lifestyle split is **generator**: target images are rendered from 3D assets; "target images from ABO 3D assets and pairing them with lifestyle sources" [CARD]. `product_type` is catalogue (human) [INFERRED]. The prompts and LLM category are machine [CARD: "VLM-generated editing prompts"].
8. Answer rules:
   - "white background?" = yes for `xtarget_image`, no for `xsource_image`
   - product type = `product_type`
   - tilt = the integer in `simplified_rotation_prompt`
9. Balanced 1:1 by construction (each row gives one yes and one no) [INFERRED]. Total row count not fetched [UNVERIFIED].
10. One answer per image.
11. Risks:
    - Lifestyle images (2560 px) may contain people [INFERRED].
    - The render style is easy to spot, so a model may answer the "white background" question from rendering cues rather than the background.
    - Do not use the `llm_*` or prompt fields for answers.
12. Templates:
    - "Is the product shown alone on a plain white background? (yes/no)"
    - "What product type is shown? (LAMP / CHAIR / SOFA / TABLE / other)"
    - (target only) "Is the top tilt about 20° or more? (yes/no)". Check the angle range first.
13. Verdict: **USE** for the white-background and product_type questions (confidence med). No shard is under 50 MB.

### D12.2 (alt): ashraq/fashion-product-images-small
1. https://huggingface.co/datasets/ashraq/fashion-product-images-small. Source: Kaggle paramaggarwal (not fetched).
2. Licence: **none on card** [CARD].
3. Open. 4. 271.5 MB in 2 shards of about 136 MB each.
5. Rows [ROW]:
   - `{"id":15970,"gender":"Men","masterCategory":"Apparel","subCategory":"Topwear","articleType":"Shirts","baseColour":"Navy Blue","season":"Fall","year":2011.0,"usage":"Casual","productDisplayName":"Turtle Check Men Navy Blue Shirt","image":"<60x80>"}`
   - `{"id":39386,…"articleType":"Jeans","baseColour":"Blue",…,"image":"<60x80>"}`
   - `{"id":59263,"gender":"Women","masterCategory":"Accessories","subCategory":"Watches","baseColour":"Silver",…"image":"<60x80>"}`
6–12. Metadata comes from the Myntra catalogue [INFERRED].
13. Verdict: **SKIP**. Images are 60×80 (tiny-image trap) and there is no licence.

### D13.1: Densu341/Fresh-rotten-fruit
1. https://huggingface.co/datasets/Densu341/Fresh-rotten-fruit
2. Licence: `license: openrail` only, with no text [CARD]. OpenRAIL is a model licence, so its fit for a dataset is unclear.
3. Open. 4. **SINGLE ARCHIVE**: `freshness_fruit.zip`, 3,053.59 MB [CARD].
5. Rows [ROW]: `{"image":"<470x386>","label":0}`, `{"image":"<382x422>","label":0}`, `{"image":"<448x426>","label":0}` (0 = freshapples).
6. `label`: ClassLabel with 22 names such as freshapples … rottentomato (including typos like "freshtamto" and "freshpatato") [ROW].
7. Origin UNVERIFIED (no card text).
8. Rule: yes if the label starts with `rotten`.
9. Train counts include freshapples 3215, rottenapples 4236, freshbanana 3360, rottenbanana 3832 … (30,357 total) [ROW, statistics]. Real negatives exist.
11. It very likely overlaps the already-used Project-AgML fresh/rotten set (both derive from the Kaggle "fresh and rotten" fruit set) [INFERRED].
13. Verdict: **SKIP** (single archive, unclear licence, likely duplicate of a used set).

### D13.1 (alt): jojogo9/freshness
- MIT [CARD]. 191.8 MB; test parquet is 38.19 MB.
- Rows: `{"image":"<100x100>","label":0}` ×3 [ROW].
- The README YAML lists `'0': rottenoranges` but the served features list `freshapples` first, so the label mapping conflicts [CARD vs ROW].
- Verdict: **SKIP** (100 px tiny-image trap and label-map conflict).

### D13.2: darthraider/fruit-ripeness-detection-dataset
1. https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset. Origin: Mendeley https://data.mendeley.com/datasets/y3649cmgg6/3 (not fetched).
2. Licence: `license: apache-2.0` in YAML [CARD]. The licence of the Mendeley original is UNVERIFIED.
3. Open. 4. 390.9 MB. Smallest unit: `data/test-00000-of-00001.parquet` at 35.48 MB [CARD].
5. Rows [ROW]: `{"image":"<640x480>","label":0}` ×3 (0 = Raw_Banana).
6. `label` ClassLabel: Raw_Banana, Raw_Mango, Ripe_Banana, Ripe_Mango [ROW].
7. Origin: "collected from Mendeley data … Initially the data was for training YOLO models" [CARD]. Human vs machine is UNVERIFIED.
8. Rule: ripe = label starts with `Ripe_`.
9. Test split has 250 per class (balanced) [ROW, statistics]. Real negatives (Raw_) exist.
10. One label per image. Original YOLO images may contain several fruits [INFERRED].
11. Indian market photos at 640×480 (borderline small). Possible near-duplicates from video-style capture [INFERRED].
12. Templates:
    - "Is this fruit ripe? (yes/no)"
    - "Which fruit is this? (banana / mango)"
    - "Which of the 4 classes applies?"
13. Verdict: **MAYBE** (label origin unverified; licence from mirror only).

### D13.3: GroceryStoreDataset (marcusklasson, GitHub)
1. https://github.com/marcusklasson/GroceryStoreDataset. Files: `dataset/train.txt`, `val.txt`, `test.txt`, `classes.csv`.
2. Licence: **none found**. The GitHub API `license` is null and the README has no licence line [CARD].
3. Open (public repo). 4. Total and repo size UNVERIFIED (API size was null). The annotation txt files are a few KB.
5. Rows from raw `dataset/test.txt` (2,485 lines) [ROW]:
   - `test/Fruit/Apple/Golden-Delicious/Golden-Delicious_001.jpg, 0, 0`
   - `test/Fruit/Apple/Golden-Delicious/Golden-Delicious_002.jpg, 0, 0`
   - `test/Fruit/Apple/Golden-Delicious/Golden-Delicious_003.jpg, 0, 0`
   - `classes.csv` rows: `Golden-Delicious,0,Apple,0,…`, `Granny-Smith,1,Apple,0,…`, `Pink-Lady,2,Apple,0,…`
6. Schema: path, fine class id (81), coarse class id (42). `classes.csv` maps id to name, plus iconic image and description paths [CARD].
7. Origin: smartphone photos taken in stores by the authors and labelled by folder (WACV 2019, arXiv 1901.00711) [CARD]. Human [INFERRED].
8. Rule: class name from `classes.csv[fine_id]`.
9. 5,125 images, 81 fine / 42 coarse classes [CARD].
10. One item type per image (several units of it may appear) [INFERRED].
11. Includes branded cartons (Arla, Oatly), so it is Swedish-market specific.
12. Templates:
    - "Which apple variety? (Golden-Delicious / Granny-Smith / Pink-Lady / Royal-Gala)"
    - "Which coarse class? (Apple / Banana / Milk / Yoghurt / …)"
    - "Is this a packaged (carton) item or loose produce?" (from the path `Fruit/`, `Vegetables/`, `Packages/`; folder names inferred from the path)
13. Verdict: **MAYBE** (no licence stated).

### D13.4: Primusvandalus/grocery-images-5class
1. https://huggingface.co/datasets/Primusvandalus/grocery-images-5class
2. Licence: `license: other`, `license_name: pexels`, `license_link: https://www.pexels.com/license/`. "[Pexels license](https://www.pexels.com/license/). They are redistributed …" [CARD].
3. Open. 4. 63.4 MB total as 1,343 individual JPGs (0.00–0.17 MB each), so per-file fetch works [CARD].
5. Rows [ROW]: `{"image":"<940x629>","label":0}`, `{"image":"<867x650>","label":0}`, `{"image":"<940x627>","label":0}` (0 = apple).
6. `label` ClassLabel: apple, banana, bread_roll, cheese, tomato.
7. Origin: human. "Images were gathered through the Pexels API in April 2026 and hand-labelled with a custom keyboard-driven dashboard; every accept/reject decision was logged, and a written rubric governed edge cases" [CARD].
8. Rule: option = label name.
9. Classes: apple 300, banana 260, bread_roll 260, cheese 260, tomato 260 [CARD].
10. One label per image, but stock photos may show mixed foods. The rubric handled edge cases [CARD].
11. Risks: Pexels stock photos may contain people; they are likely in web-scraped training data; business value is low.
12. Templates:
    - "Which grocery item is this? (5 options)"
    - "Is this a fruit? (yes = apple/banana; no = bread_roll/cheese)" (tomato is ambiguous, so exclude it)
    - "Is this a baked good? (yes/no)"
13. Verdict: **USE** (confidence high on provenance; low on business realism).

### D14.1: ethz/food101
1. https://huggingface.co/datasets/ethz/food101
2. Licence: "Any use beyond scientific fair use must be negociated with the respective picture owners according to the Foodspotting terms of use" [CARD].
3. Open. 4. 5,060 MB. The smallest shard is `validation-00001-of-00003.parquet` at 413.15 MB.
5. Rows [ROW]: `{"image":"<384x512>","label":6}`, `{"image":"<512x512>","label":6}`, `{"image":"<512x383>","label":6}` (6 = beignets).
6. `label`: 101 classes.
7. Origin:
   - Test labels "were verified by human annotators"
   - Train labels "were assigned automatically based on the Foodspotting dish taxonomy and were not manually reviewed" [CARD]
   - Use the validation/test split only.
8. Rule: label name.
9. 750 per class in train [ROW, statistics]; 250 per class in the test split [CARD].
10. One dish per image (by design).
11. Very likely in training data. Images are 512 px at most.
12. Templates:
    - "Which dish? (pick 4 of 101)"
    - "Is this a dessert? (needs a class grouping)"
    - "Is this pizza? (yes/no)"
13. Verdict: **MAYBE**. Fails the open-licence test (fair use only).

### D14.3: Voxel51/food-waste-dataset
- MIT [CARD]. 309.6 MB; `samples.json` is 16.57 MB.
- `annotations_creators: machine-generated` [CARD].
- Viewer rows were images only (1688×1126 ×3) [ROW].
- Verdict: **SKIP** (machine labels).

### D14.2: ybli/yolo-kitchen-hygiene-safety-detection
- The repo holds only a README pointing to data2.cn, a download link off-site [CARD]. Class: "Performing-Hand-Hygiene".
- Verdict: **SKIP** (mirror-with-no-images trap).

### D15.1: keremberke/forklift-object-detection
1. https://huggingface.co/datasets/keremberke/forklift-object-detection. Roboflow source: https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv/dataset/1
2. Licence: README "### License CC BY 4.0"; `README.dataset.txt`: "License: CC BY 4.0" [CARD].
3. Open. 4. 20.4 MB total. Smallest units: `data/test.zip` 2.77 MB, `valid.zip` 3.77 MB, `train.zip` 13.53 MB [CARD].
5. Rows from `first-rows?...&config=full&split=train` [ROW]:
   - `{"image_id":278,"width":500,"height":375,"objects":{"id":[586],"area":[120469],"bbox":[[3.0,28.0,420.12,286.75]],"category":[0]}}` (forklift only)
   - `{"image_id":76,"width":450,"height":343,"objects":{"id":[170,171],"bbox":[[285,133,19.02,27.03],[5,0,434.86,339.18]],"category":[1,0]}}` (person + forklift)
   - `{"image_id":46,"width":500,"height":500,"objects":{"id":[90,91],"bbox":[[232,110,129.64,148.91],[40,15,454.65,470.16]],"category":[1,0]}}`
6. Schema: `image_id`, `width`, `height`, `objects{id, area, bbox [x,y,w,h], category: 0 forklift, 1 person}`.
7. Origin: "created by exporting images from images.cv and labeling them as an object detection dataset" [CARD]. Human labelling in Roboflow [INFERRED].
8. Rule: yes if 1 ∈ `objects.category`.
9. Counted from all rows via `/rows` [ROW]:
   - train: person+forklift 158, forklift only 134, person only 2, neither 1
   - val: 39 / 44 / 1 / 0
   - test: 25 / 16 / 1 / 0
   - So there are **real negatives** (forklift with no person): 194 in total.
10. One yes/no per image. Restrict to images containing a forklift.
11. Risks:
    - Images are small (median about 450–500 px, min 130 px) [ROW, statistics], so filter to 400 px or more.
    - People are present (faces possible).
    - Web images from images.cv: watermarks and likely training-data overlap.
    - Exhaustiveness of person boxes is UNVERIFIED (a tiny distant person may be missed).
12. Templates:
    - "Is a person visible with the forklift? (yes/no)"
    - "How many forklifts are visible? (1 / 2 / 3+)"
    - "Does the forklift fill more than half the image? (bbox area / (w·h) > 0.5)"
13. Verdict: **USE** (confidence med).

### D15.2 / D16.3: Gabriel8/cardboard-box-anomaly-detection
1. https://huggingface.co/datasets/Gabriel8/cardboard-box-anomaly-detection. Files: `/tree/main/test/good`, `/test/bad`.
2. Licence: "Este dataset está sob a licença **CC BY-NC-SA-4.0**. Uso não comercial, com atribuição obrigatória e compartilhamento sob a mesma licença." [CARD] Non-commercial; research testing is allowed.
3. Open. 4. 2,042.9 MB. Individual JPGs of 1.4–5.3 MB each, so per-file fetch works [CARD].
5. Rows from `rows?...&split=test&offset=0&length=100` [ROW]: `{'image':'<3072x4080>','label':0}` (row 0), `{'image':'<4080x3072>','label':0}` (row 1), `{'image':'<3072x4080>','label':0}` (row 99). Label 0 = `bad` per ClassLabel names ["bad","good"] [ROW]. Example filenames from the tree: `test/good/cam1_box32_pos02_ver00_loc-b2.jpg`, `test/bad/cam1_box01_pos04_ver00_loc-chao.jpg` [CARD].
6. Schema:
   - `label` ClassLabel {bad, good}
   - The filename encodes camera, box id (1–43), position, version and location (`chao` = floor, `b1`/`b2` = conveyor belts) [CARD]
7. Origin: human. 43 physical boxes, "13 consideradas normais e 30 anômalas", photographed by the authors with support from Ondupress Embalagens [CARD]. The label is a per-box ground truth.
8. Rule: damaged = `label == bad` (or folder `test/bad`).
9. Test split: good 166, bad 386. Train has 1 good image [CARD]. **Real negatives exist.**
10. One label per image (one box per photo) [CARD].
11. Risks:
    - Many near-duplicate shots of the same 43 boxes, so sample one per box/position.
    - Very large 12 MP images (fine after downscale).
    - The defect type is not labelled.
    - No people.
12. Templates:
    - "Is this cardboard box damaged? (yes/no)"
    - "Is the box on a conveyor belt or the floor? (belt / floor; from `loc-`)"
    - "Which camera view?" (not useful; skip). Use instead: "Same box as reference image? (yes/no; box id)"
13. Verdict: **USE** (confidence high).

### D16.3: HassanBinAli/Damaged_Parcel_boxes
- MIT [CARD]. Parquets total 0.03 MB.
- Rows: `{"image":"/content/drive/MyDrive/fatima_fellowship/parcel_boxes/parcel_boxes_dents/1000_F_442627326_….jpg","label":0}` (three similar rows) [ROW]. The images are Google Drive paths only, and the filenames suggest stock photos.
- Verdict: **SKIP** (mirror-with-no-images).

### D16.3: Parcel3D (Zenodo 8032204)
- "Parcel3D – A Synthetic Dataset of Damaged and Intact Parcel Images with 2D and 3D Annotations". Licence id `other-nc`. Access open.
- Files: `parcel3d.zip`, **45,838.3 MB SINGLE ARCHIVE** [CARD: Zenodo API].
- No rows.
- Verdict: **SKIP** (single huge archive). It is the best fit for damaged-vs-intact parcels (with negatives) if a human pulls a subset.

### D16.1: howell0123/shipping_container
1. https://huggingface.co/datasets/howell0123/shipping_container
2. Licence: **none** [CARD].
3. Open. 4. 224.6 MB as a single parquet (`data/train-00000-of-00001.parquet`, 224.52 MB) plus `my_dataset.parquet` (0.08 MB) [CARD].
5. Rows [ROW]:
   - `{"images":"<1000x640>","messages":[{"role":"user","content":"What defect on the shipping container?"},{"role":"system","content":"Dent, Rusty, Scratch"}]}`
   - `{…"content":"Scratch"}`
   - `{…"content":"Rusty"}`
6. Schema: `images` and `messages[user question, system answer]`. The answer is a comma-separated set from {Deframe, Dent, Hole, Rusty, Scratch}.
7. Origin: UNVERIFIED (no card).
8. Rule: parse the answer into a set; for pick-one, keep single-defect rows.
9. Counted over all 1,016 rows [ROW]:
   - Single-defect rows: Rusty 367, Dent 133, Scratch 129, Deframe 46, Hole 14
   - Multi-defect rows: the rest, e.g. "Rusty, Scratch" 143
   - **No undamaged images** (positives only).
10. Use only the 689 single-label rows.
11. 1000×640 resolution. Possible container numbers in view (not personal).
12. Templates:
    - "Which defect: Dent / Rusty / Scratch / Deframe / Hole?"
    - "Is rust present? (yes/no, within the defect set)"
    - "How many defect types? (1 / 2 / 3)"
13. Verdict: **MAYBE** (no licence, unknown origin). It cannot support "is it damaged?" yes/no.

### D16.2: Guztavu/container-damage
- `gated: auto` (accept-terms gate). README returns 401 [CARD].
- Files: `bbox_dmg_mc.zip` 58.72 MB, `mask_dmg_mc.zip` 39.00 MB, `bbox_nodmg.zip` 241.29 MB. The no-damage zip suggests **real negatives** [CARD: file listing].
- Verdict: **GATED**. A human must open https://huggingface.co/datasets/Guztavu/container-damage, log in and accept the terms.

### D17.1: OliseNS/person-face-package-home-security-detection
1. https://huggingface.co/datasets/OliseNS/person-face-package-home-security-detection
2. Licence: `license: other`, `license_name: multi-source-aggregated-terms`. The LICENSE file says "This dataset aggregates images and annotations governed by multiple upstream licenses (Open Images, COCO, WIDER FACE, Roboflow Universe projects) and Meta SAM 3 terms." [CARD]
3. Open. 4. `dataset.zip` is a 22,658 MB single archive. A `sample/` folder holds 100 images [CARD].
5. Viewer rows show folder labels only: `{"image":"<640x640>","label":0}` ("images"), `{"image":"<1920x1920>","label":1}` ("run"), and another `label 1` [ROW]. These are not annotation rows. `sample/data.yaml`: `nc: 9, names: [person, face, vehicle, bike, bicycle, parcel, dog, cat, bird]` [ROW].
7. Origin: mixed or machine (SAM 3 terms suggest model-assisted boxes) [INFERRED].
11. Includes a `face` class and WIDER FACE images, so the personal-data risk is high.
13. Verdict: **SKIP** (single archive, likely machine labels, face data). No acceptable dataset for 17.x, so see Gaps.

### D18.1 / D19.5 / D18.2: Voxel51/IndoorSceneRecognition (MIT Indoor-67)
1. https://huggingface.co/datasets/Voxel51/IndoorSceneRecognition. Original: http://web.mit.edu/torralba/www/indoor.html (quoted via the keremberke mirror; not fetched directly).
2. Licence: conflict.
   - Voxel51 card: `license: mit` [CARD].
   - The keremberke/Roboflow mirror quotes the original page: "The images provided here are for research purposes only." [CARD]
3. Open. 4. 2,602.9 MB as 15,626 individual files. `samples.json` is 22.47 MB and was fetched in full [CARD].
5. Rows from `samples.json` [ROW]:
   - `{"filepath":"data/data_13/indoor_0339.jpg","tags":["train"],"ground_truth.label":"bedroom","polyline_labels":["picture","picture","bed crop","cushion","cushion","telephone","night tablr","lamp","carpet","wall","floor"]}`
   - `{"filepath":"data/data_13/legacy_sleighl.jpg","tags":["train"],"ground_truth.label":"bedroom","polyline_labels":["tablelamp","tablelamp","mirror","pot","bed","pillow","pillow","painting","chest of drawers","plant"]}`
   - `{"filepath":"data/data_13/int107.jpg","tags":["train"],"ground_truth.label":"bedroom","polyline_labels":["painting","lamp","sofa","pillow",…,"window","curtain"]}`
6. Schema:
   - `filepath`, `tags` (train/test)
   - `ground_truth.label`: one of 67 scene classes
   - `ground_truth_polylines.polylines[].label`: LabelMe object names, free text with typos; present on 2,737 of 15,620 images [ROW]
7. Origin: human (CVPR 2009 dataset; scene class by folder; LabelMe polygons) [CARD].
8. Rules:
   - room type = `ground_truth.label`
   - object present = any stripped polyline label in a synonym set
9. Counts [ROW]:
   - Room classes: kitchen 734, livingroom 706, bedroom 662, dining_room 274, bathroom 197 (15,620 total)
   - Bedroom polylines: bed 240 of 350 annotated bedrooms
   - Bathroom: towel 81, toilet 63, sink 71 of 197
   - Polygon annotation is **not exhaustive** (e.g. many bedrooms lack "bed"), so absence does not equal a negative.
10. One scene label per image.
11. Risks: old web images of mixed size (640–800 px seen); a known benchmark, so likely in training data; licence ambiguity.
12. Templates:
    - "Which room is this? (bedroom / bathroom / kitchen / livingroom / dining_room)"
    - "Is this a wet room (bathroom/kitchen) or a dry room? (yes/no)"
    - "Which object is annotated in this bedroom: bed / sofa / desk?" (positives only)
13. Verdict: **MAYBE** (licence conflict). 18.2 object presence: **SKIP for yes/no** (no reliable negatives).

### D18.1 (alt): keremberke/indoor-scene-classification
- Same MIT Indoor data, "resized416by416_70-20-10Split". The README says "### License MIT" and quotes the "research purposes only" original [CARD].
- 470.3 MB; `test.zip` is 46.53 MB.
- Rows [ROW]: `{"image_file_path":".../airport_inside/airport_inside_0001_jpg.rf.cbf9….jpg","image":"<416x416>","labels":25}` (×3, airport_inside).
- Train counts include kitchen 650, bedroom (present; truncated in output) … [ROW].
- Verdict: **MAYBE**. Same licence conflict, and the 416 px resize is borderline tiny. Prefer the Voxel51 originals.

### D19.1: v1nz/cubicasa5k-yolo (CubiCasa5K derivative)
1. https://huggingface.co/datasets/v1nz/cubicasa5k-yolo. Original: https://zenodo.org/records/2613548.
2. Licence:
   - Mirror: `license: cc-by-nc-4.0`, "Converted from CubiCase5K (CC BY-NC 4.0)" [CARD]
   - Zenodo record licence id: **cc-by-nc-sa-4.0** [CARD: Zenodo API]
   - The two conflict; treat it as **CC BY-NC-SA 4.0**. Non-commercial.
3. Open. 4. 1,762.8 MB as 9,261 files: label txt files of about 0 MB, PNGs of about 4.4 MB each, so per-file fetch works [CARD].
5. Rows from `first-rows` (one YOLO polygon line per row) [ROW]:
   - `0 0.535439 0.775000 0.449871 0.775000 0.449871 0.794565 0.462725 0.795109 0.462358 0.869565 0.378259 0.869565 …`
   - `0 0.310320 0.775000 0.310320 0.794565 0.314359 0.794565 0.314359 0.775000`
   - `0 0.098054 0.678804 0.098054 0.794565 0.158281 0.794565 0.158281 0.775000 0.111274 0.774457 0.111274 0.678804`
6. Schema: `labels/<split>/<id>.txt` holds lines of `class x1 y1 x2 y2 …` (normalised polygon). Classes: 0 wall, 1 door (opening polygon only), 2 window [CARD].
7. Origin: human polygons from the CubiCasa5K SVG annotation ("annotated into over 80 floorplan object categories … using polygons" [CARD: Zenodo]), automatically rasterised and traced back to polygons by the mirror author [CARD]. Classed as human (converted); conversion noise is possible.
8. Rule: doors = count of lines starting with `1 `; windows = count starting with `2 `.
9. 105,729 label lines in the viewer split [ROW]. Per-image door distribution not computed [UNVERIFIED].
10. One count per image. Multi-floor plans are possible (the original F1 only is used: "F1_scaled.png") [CARD].
11. Risks:
    - Finnish real-estate floorplans, no personal data.
    - Large PNGs.
    - The trace-back step may split or merge openings, so spot-check 20 images.
12. Templates:
    - "How many doors are drawn? (0–3 / 4–6 / 7–9 / 10+)"
    - "Are there more windows than doors? (yes/no)"
    - "How many windows? (bins)"
13. Verdict: **USE** (confidence med; conversion fidelity unverified).

### D19.2: CubiCasa5K original (Zenodo 2613548)
- CC BY-NC-SA 4.0, open. `cubicasa5k.zip` is a **5,469.5 MB SINGLE ARCHIVE** [CARD]. Room-type polygons (Bedroom, Kitchen …) exist only inside the archive SVGs [CARD: description; room names INFERRED].
- No rows.
- Verdict: **SKIP** (single archive). Bedroom count is the most valuable floorplan question; see Gaps.

### D19.2 (generator route): OldDelorean/FloorplanQA-Layouts
1. https://huggingface.co/datasets/OldDelorean/FloorplanQA-Layouts
2. Licence: "This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0)." [CARD]
3. Open. 4. 16.0 MB of 2,007 JSON files, each well under 1 MB [CARD].
5. Rows [ROW]:
   - `{"layout_id":0,"room_type":"bedroom","room_boundary":[{"x":0,"y":0},{"x":2.8,"y":0},{"x":2.8,"y":3.2},…],"openings":{"windows":[{"label":"window",…}],"doors":[{"label":"door",…}]},"objects":[{"label":"bed","points":[…]},…]}`
   - `{"layout_id":1,"room_type":"bedroom","room_boundary":[…3.0 x 3.5…],"openings":{"windows":[1],"doors":[1]},"objects":[{"label":"bed",…},{"label":"nightstand"…`
   - `{"layout_id":10,"room_type":"bedroom","room_boundary":[…4.58 x 3.51…],"openings":{"windows":[{"label":"window_1"…},{"label":"window_2"…}],"doors":[…]}}`
6. Schema: `layout_id`, `room_type`, `room_boundary` polygon (m), `walls`, `openings{windows, doors}`, `objects[{label, points}]`, `units` [ROW].
7. Origin: generator (600 synthetic each of kitchens, living rooms and bedrooms) plus 200 derived from HSSD-200 [CARD].
8. Rules: counts of windows/doors/objects; room area from the polygon.
9. room_type: bedroom 692, kitchen 622, living_room 600, bathroom 38, … [ROW, statistics].
10. One room per layout.
11. **No images**: we must render them (SVG). Single-room plans only.
12. Templates:
    - "How many windows? (1 / 2 / 3+)"
    - "Is the room larger than 12 m²? (yes/no)"
    - "Which room type? (bedroom / kitchen / living_room)"
13. Verdict: **MAYBE** (no images; it becomes USE once we render it ourselves as a generator task).

### D19.6: Voxel51/FloorPlanCAD
1. https://huggingface.co/datasets/Voxel51/FloorPlanCAD
2. Licence: conflict. YAML says `license: cc-by-sa-4.0`; the card body says "**License**: Creative Commons Attribution-NonCommercial 4.0 License" [CARD].
3. Open. 4. 454.2 MB as 5,314 PNG files (0.01–0.46 MB each). `samples.json` is 60.42 MB, over the cap, so only a 6 KB range was read [CARD].
5. Range-read of `samples.json` [ROW]: first sample `{"filepath":"data/0000-0003.png","ground_truth":{"_cls":"Detections","detections":[{"label":"wall","bounding_box":[0.3098,0.0,0.6902,0.7206],"mask":…}…`. Labels in the first 6 KB: wall, sliding_door, sliding_door, wall. Fewer than three full rows could be pasted (the mask base64 is large).
6. FiftyOne `Detections` with label (30 categories, e.g. wall, single_door, sliding_door, parking), bbox and mask [CARD].
7. Origin: described as converted from the original vector SVG annotations [CARD]. The original annotators are in the paper [UNVERIFIED].
13. Verdict: **MAYBE** (licence conflict, rows incomplete, full JSON exceeds the cap).

### D19.3: murai-lab/WorcesterMA_Housing_Facades
1. https://huggingface.co/datasets/murai-lab/WorcesterMA_Housing_Facades. Code: https://github.com/murai-lab/City-Transformers.
2. Licence: `license: mit`, but the card adds: "Confirm that all source imagery and registry data are cleared for redistribution before publishing externally." [CARD]
3. Open. 4. 14,162 MB as 22,953 individual JPGs (0.01–3.7 MB). `train/metadata_train.csv` is 2.55 MB [CARD].
5. Rows from `first-rows` (metadata CSV) [ROW]:
   - `{"file_name":"23712.jpg","pid":23712,"class_label":"class_3","year_built":1988.0,"location":"1 NARRAGANSETT AVE # 1B","url":"https://images.vgsi.com/photos2/WorcesterMAPhotos//\\00\\08\\70\\82.jpg"}`
   - `{"file_name":"37878.jpg","pid":37878,"class_label":"class_3","year_built":1987.0,"location":"1 WIGWAM HILL DR",…}`
   - `{"file_name":"37901.jpg","pid":37901,"class_label":"class_3","year_built":1986.0,"location":"10 TECONNETT PATH",…}`
6. Schema: `file_name`, `pid` (municipal property id), `class_label` (class_1..4), `year_built`, `location` (street address), `url` (assessor photo).
7. Origin: municipal assessor registry (`year_built`), binned into "Class 1: pre-1940, Class 2: 1941–1970, Class 3: 1971–1990, Class 4: post-1990" [CARD: GitHub README]. Administrative human record.
8. Rule: era = class_label mapping, or compute from `year_built`.
9. Train: class_1 11,254, class_2 4,958, class_3 2,967, class_4 1,288 [ROW, statistics] (imbalanced).
10. One label per image.
11. Risks:
    - Street addresses for every image. These are property data, not names, but the address plus photo can be linked to owners, so drop the `location` field.
    - Assessor photos may show people or cars.
    - Licence clearance doubt.
    - Construction year is only partly visible, so the task is hard.
12. Templates:
    - "When was this house built? (pre-1940 / 1941–70 / 1971–90 / post-1990)"
    - "Was it built before 1940? (yes/no)"
    - "Built after 1970? (yes/no)"
13. Verdict: **MAYBE**. The licence is self-flagged as uncertain, and there is address data.

### D19.4: Jonathandav/facade-styles
1. https://huggingface.co/datasets/Jonathandav/facade-styles
2. Licence: `license: mit` [CARD].
3. Open. 4. 357.2 MB: 1,000 PNG plates of about 0.46 MB each; `plate_manifest.parquet` is 0.07 MB [CARD].
5. Rows from `plate_manifest.parquet` (downloaded, 70 KB) [ROW]:
   - `{"plate_id":"ST01-000","style_name":"Bauhaus International","period":"1920-1940","view":"frontal","crop":"facade_detail","light":"overcast","setting":"street","condition":"weathered","storeys":2,"roofline":"flat roof with thin parapet","ornament_level":"none"}`
   - `{"plate_id":"ST01-001",…"view":"three_quarter","crop":"full_building","light":"morning","condition":"pristine","storeys":2}`
   - `{"plate_id":"ST01-002",…"view":"oblique","crop":"full_building","light":"midday","setting":"isolated","condition":"weathered","storeys":3}`
6. 25 columns: style_name (20 × 50), view (4 × 250), light (5 × 200), condition (pristine 565 / weathered 336 / under_restoration 99), storeys (1–21), material, roofline, … [ROW].
7. Origin: **generator via a text-to-image model**. "Every plate is generated from a sampled attribute specification"; acceptance was measured, but some attributes are left to "generator's discretion" [CARD]. This is not a deterministic drawing.
8. Rule: style = `style_name`; view = `view`.
9. Balanced by design.
11. Risks:
    - Diffusion output may not obey the spec (the card lists generator failures).
    - 512 px plates.
    - Style and material are 1:1 confounded.
12. Templates:
    - "Which style? (4 of 20)"
    - "Which camera view? (frontal / three_quarter / oblique / looking_up)"
    - "Is the building under restoration? (yes/no)"
13. Verdict: **MAYBE** (labels are prompt specs, not verified renders).

### D20.1: garythung/trashnet
1. https://huggingface.co/datasets/garythung/trashnet. GitHub: garythung/trashnet (not fetched).
2. Licence: `license: mit` [CARD].
3. Open. 4. 3,677 MB. Smallest unit: `dataset-resized.zip` at 42.83 MB (fits under the cap). `dataset-original.zip` is 3,634 MB [CARD].
5. Rows from `first-rows` [ROW]: `{"image":"<4032x3024>","label":0}` ×3 (0 = cardboard).
6. `label` ClassLabel: cardboard, glass, metal, paper, plastic, trash.
7. Origin: human. The authors photographed objects by class on a white background (a Stanford CS229 project) [INFERRED; the card has no text, so UNVERIFIED].
8. Rule: option = label name.
9. cardboard 806, glass 1002, metal 820, paper 1188, plastic 964, trash 274 (5,054) [ROW, statistics].
10. One object per image (by design).
11. Plain backgrounds (easy). Widely used, so likely in training data. No people.
12. Templates:
    - "Which recycling stream? (6 options)"
    - "Is this recyclable? (yes = not trash)"
    - "Is this a fibre item (paper/cardboard)? (yes/no)"
13. Verdict: **USE**. Confidence med: the label origin is inferred, the card text is empty and the licence comes from the YAML only.

### D20.2: DroneWaste (Zenodo 17045559)
1. https://zenodo.org/records/17045559. Files: `dronewaste_v1.0.json` (8.8 MB, fetched), `images.tar.gz` (3,882.5 MB).
2. Licence: `cc-by-4.0` [CARD: Zenodo API].
3. Open. 4. The images are a **SINGLE ARCHIVE of 3,882.5 MB**. The annotation JSON is 8.8 MB and separately fetchable [CARD].
5. Rows from the JSON [ROW]:
   - image: `{"id":1,"file_name":"site3_4.png","site":"site3","width":640,"height":640}`
   - annotation: `{"id":1,"image_id":23,"category_id":15,"iscrowd":0,"area":606.5,"bbox":[329.0,394.0,28.0,27.0]}`
   - category: `{"id":1,"name":"Rubble","supercategory":"pile_waste","ewc":"12.61 Soils"}`
6. COCO: images (with `site`), annotations (bbox and segmentation), categories (20 materials with European Waste Codes) [ROW].
7. Origin: "Each visible waste instance is annotated with a segmentation mask, a bounding box, and a waste category" [CARD]. Human vs tool-assisted is UNVERIFIED.
8. Rule: dumping present = the image has ≥1 annotation.
9. 4,993 tiles; only 1,171 have annotations, so there are about 3,822 **real negatives** [ROW]. Top classes: Pallets 1016, Textile 876, C&D materials 397, Scrap 394 [ROW].
10. Several items per tile. For pick-one, choose tiles with a single category.
11. Aerial 640×640 tiles from orthomosaics. Small objects (e.g. 28×27 px). No personal data.
12. Templates:
    - "Is dumped waste visible? (yes/no)"
    - "Which material: Pallets / Textile / Tyres / Scrap?"
    - "How many waste items? (0 / 1 / 2–3 / 4+)"
13. Verdict: **MAYBE**. Labels pass, but the images come only as a single 3.9 GB archive (trap). Note that the spec rejected xBD as "aerial only"; this one is also aerial.

### D20.3: TACO (pedropro/TACO, GitHub) with images via RandyHuynh5815/TACO-Waste-Recognition
1. https://github.com/pedropro/TACO. Annotations: `data/annotations.json` (fetched).
2. Licence: **not found**. GitHub `license` is null; `annotations.json` has `"licenses": []` and image `"license": None` [ROW]. Images are hosted on Flickr.
3. Open. 4. The annotation JSON is small (fetched in full, under 50 MB). The HF image mirror is 2,534.5 MB as 1,462 individual JPGs (0.09–5.4 MB) and has **no annotations** of its own (labels are just batch folders) [CARD/ROW].
5. Rows [ROW]:
   - image: `{'id':0,'width':1537,'height':2049,'file_name':'batch_1/000006.jpg','flickr_url':'https://farm66.staticflickr.com/65535/33978196618_e30a59e0a8_o.png'}`
   - annotations: `{'id':1,'image_id':0,'category_id':6,'area':403954.0,'bbox':[517,127,447,1322],'iscrowd':0}`, `{'id':2,'image_id':1,'category_id':18,'area':1071259.5,'bbox':[1,457,1429,1519]}`, `{'id':3,'image_id':1,'category_id':14,'area':99583.5,'bbox':[531,292,1006,672]}`
   - scene annotation: `{'image_id':0,'background_ids':[1]}`
6. Schema: COCO with 60 categories / 28 supercategories, plus `scene_annotations.background_ids` over scene_categories {Clean, Indoor Man-made, Pavement, Sand/Dirt/Pebbles, Trash, Vegetation, Water} [ROW].
7. Origin: human, via the TACO annotation website. Note that `annotations_unofficial.json` "have not yet been reviewed" [CARD]. Use only the official file.
8. Rules: material = supercategory of the annotation; background = scene id.
9. 1,500 images, 4,784 annotations. Objects per image: 1→610, 2→359, 3→179, 4→98, 5+→254. Supercategories: Plastic bag & wrapper 850, Cigarette 667, Unlabeled litter 517, Bottle 439 … [ROW]. **Every image contains litter** (positives only for "is litter present").
10. 610 images have exactly one object, which gives a clean pick-one.
11. Flickr photos (possible people). Licence unclear.
12. Templates:
    - "What is the litter item? (Bottle / Can / Cigarette / Plastic bag & wrapper / Cup)"
    - "What surface is it on? (Pavement / Vegetation / Sand-dirt / Water / Indoor)"
    - "How many litter items? (1 / 2 / 3–4 / 5+)"
13. Verdict: **MAYBE** (no licence stated).

### D20.4: Akhila-9849/Garbage_Bin_overflow_images
- CC BY 4.0 [CARD]. 111.8 MB, 1,974 flat JPGs.
- Rows are images only (640×640 ×3) [ROW]. No labels; all images are "overflowing" [CARD].
- Verdict: **SKIP** (positives only, no annotations).

### D20.1 (alt): steveharianto/waste-garbage-management-dataset
- MIT [CARD]. 789.8 MB, 10 classes (battery 944 … clothes 5,327) [ROW].
- Rows: `{"image":"<275x183>","label":0}`, `{"image":"<225x225>","label":0}` ×2 [ROW].
- Verdict: **SKIP** (tiny images; scraped; origin unknown).

---

## 3. CSV

```csv
domain,task_id,task,dataset,landing_url,repo_id,licence,licence_quote_url,access,total_mb,smallest_fetch_mb,single_archive,sample_proof_url,rows_pasted,label_origin,answer_rule,has_negatives,classes,one_answer_per_image,personal_data_risk,verdict,confidence,unverified_fields
11,D11.2,price tag readability,OFF price-tag-classification,https://huggingface.co/datasets/openfoodfacts/price-tag-classification,openfoodfacts/price-tag-classification,NOT STATED,https://huggingface.co/datasets/openfoodfacts/price-tag-classification,open,48.5,9.87,no,https://datasets-server.huggingface.co/first-rows?dataset=openfoodfacts/price-tag-classification&config=default&split=train,yes,human,label name,n/a,invalid 534/medium 220/high 893,yes,low,MAYBE,med,licence;annotator count
11,D11.3,price tag count,OFF price-tag-detection,https://huggingface.co/datasets/openfoodfacts/price-tag-detection,openfoodfacts/price-tag-detection,CC-BY-SA-4.0,https://huggingface.co/datasets/openfoodfacts/price-tag-detection,open,399.2,44.16,no,https://datasets-server.huggingface.co/first-rows?dataset=openfoodfacts/price-tag-detection&config=default&split=train,yes,human,len(objects.category_id) binned,unverified (count task),price-tag,yes,low,USE,med,zero-tag images
11,D11.4,discount flag,OFF price-tag-extraction,https://huggingface.co/datasets/openfoodfacts/price-tag-extraction,openfoodfacts/price-tag-extraction,NOT STATED,https://huggingface.co/datasets/openfoodfacts/price-tag-extraction,open,12947.2,180.2,no,https://datasets-server.huggingface.co/first-rows?dataset=openfoodfacts/price-tag-extraction&config=default&split=train,yes,machine,output.prices[].price_is_discounted,yes,JSON fields,yes,low,SKIP,high,
11,D11.5,checkout item count,RPC (benjamintli mirror),https://huggingface.co/datasets/benjamintli/retail-product-checkout,benjamintli/retail-product-checkout,CC BY-NC-SA 4.0 (tag says 2.0),https://huggingface.co/datasets/benjamintli/retail-product-checkout,open,15279.1,315.9,no,https://datasets-server.huggingface.co/rows?dataset=benjamintli/retail-product-checkout&config=default&split=validation&offset=0&length=100,yes,UNVERIFIED,len(objects.category) binned; supercategory suffix,n/a,200 SKUs/17 supercats,yes,low,MAYBE,med,label origin;licence version
11,D11.1,shelf gap / SKU,SKUs_on_shelves_PL,https://huggingface.co/datasets/shelfwise-by-form/SKUs_on_shelves_PL,shelfwise-by-form/SKUs_on_shelves_PL,CC-BY-4.0,https://huggingface.co/datasets/shelfwise-by-form/SKUs_on_shelves_PL,open,11422.6,11422.09,yes,https://datasets-server.huggingface.co/first-rows?dataset=shelfwise-by-form/SKUs_on_shelves_PL&config=default&split=train,no,UNVERIFIED,needs COCO json in archive,unknown,~8k SKUs,no,low,SKIP,high,label origin;schema
12,D12.1,product type,ABO (suvadityamuk mirror),https://huggingface.co/datasets/suvadityamuk/amazon-berkeley-objects,suvadityamuk/amazon-berkeley-objects,CC-BY-4.0 (bucket also has NC file),https://huggingface.co/datasets/suvadityamuk/amazon-berkeley-objects,open,617650.7,12.09 (listings) / 172.3 (original images),no,https://datasets-server.huggingface.co/first-rows?dataset=suvadityamuk/amazon-berkeley-objects&config=listings&split=train,yes,human (catalogue) inferred,product_type via main_image_id join,n/a,product_type enum,yes,low,MAYBE,med,class counts;label origin
12,D12.3,garment worn,Fashionpedia,https://huggingface.co/datasets/detection-datasets/fashionpedia,detection-datasets/fashionpedia,CC-BY-4.0,https://huggingface.co/datasets/detection-datasets/fashionpedia,open,3478.9,84.85,no,https://datasets-server.huggingface.co/first-rows?dataset=detection-datasets/fashionpedia&config=default&split=train,yes,human,exactly one of {dress pants skirt shorts} in objects.category,n/a (pick-one),46 classes,filterable,high (faces),USE,med,exhaustiveness;class counts
12,D12.4,white background main image,ABO-Edit,https://huggingface.co/datasets/amazon/ABO-Edit,amazon/ABO-Edit,CC-BY-4.0,https://huggingface.co/datasets/amazon/ABO-Edit,open,18288.6,505,no,https://datasets-server.huggingface.co/first-rows?dataset=amazon/ABO-Edit&config=default&split=train,yes,generator (target renders) + human product_type,xtarget=yes / xsource=no,yes,white/lifestyle; product_type,yes,low-med,USE,med,row count
12,D12.2,colour attribute,fashion-product-images-small,https://huggingface.co/datasets/ashraq/fashion-product-images-small,ashraq/fashion-product-images-small,NOT STATED,https://huggingface.co/datasets/ashraq/fashion-product-images-small,open,271.5,135.4,no,https://datasets-server.huggingface.co/first-rows?dataset=ashraq/fashion-product-images-small&config=default&split=train,yes,human inferred,baseColour,n/a,many,yes,low,SKIP,high,licence
13,D13.1,fresh vs rotten,Densu341 Fresh-rotten-fruit,https://huggingface.co/datasets/Densu341/Fresh-rotten-fruit,Densu341/Fresh-rotten-fruit,openrail (no text),https://huggingface.co/datasets/Densu341/Fresh-rotten-fruit,open,3053.6,3053.59,yes,https://datasets-server.huggingface.co/first-rows?dataset=Densu341/Fresh-rotten-fruit&config=default&split=train,yes,UNVERIFIED,label startswith rotten,yes,22 classes,yes,low,SKIP,high,origin;overlap with AgML
13,D13.1,fresh vs rotten,jojogo9 freshness,https://huggingface.co/datasets/jojogo9/freshness,jojogo9/freshness,MIT,https://huggingface.co/datasets/jojogo9/freshness,open,191.8,38.19,no,https://datasets-server.huggingface.co/first-rows?dataset=jojogo9/freshness&config=default&split=train,yes,UNVERIFIED,label startswith rotten,yes,6 classes,yes,low,SKIP,high,label map conflict
13,D13.2,ripeness,fruit-ripeness-detection-dataset,https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset,darthraider/fruit-ripeness-detection-dataset,Apache-2.0 (mirror),https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset,open,390.9,35.48,no,https://datasets-server.huggingface.co/first-rows?dataset=darthraider/fruit-ripeness-detection-dataset&config=default&split=train,yes,UNVERIFIED,label startswith Ripe_,yes,4 classes x250 (test),yes,low,MAYBE,med,label origin;upstream licence
13,D13.3,produce variety,GroceryStoreDataset,https://github.com/marcusklasson/GroceryStoreDataset,,NOT STATED,https://github.com/marcusklasson/GroceryStoreDataset,open,UNVERIFIED,<0.1 (txt),no,https://raw.githubusercontent.com/marcusklasson/GroceryStoreDataset/master/dataset/test.txt,yes,human inferred,classes.csv[fine_id],n/a,81 fine/42 coarse,yes,low,MAYBE,med,licence;total size
13,D13.4,grocery item,grocery-images-5class,https://huggingface.co/datasets/Primusvandalus/grocery-images-5class,Primusvandalus/grocery-images-5class,Pexels licence,https://huggingface.co/datasets/Primusvandalus/grocery-images-5class,open,63.4,0.17,no,https://datasets-server.huggingface.co/first-rows?dataset=Primusvandalus/grocery-images-5class&config=default&split=train,yes,human,label name,n/a,apple300/banana260/bread260/cheese260/tomato260,yes,low,USE,high,
14,D14.1,dish identity,Food-101,https://huggingface.co/datasets/ethz/food101,ethz/food101,fair use only (Foodspotting ToS),https://huggingface.co/datasets/ethz/food101,open,5060,413.15,no,https://datasets-server.huggingface.co/first-rows?dataset=ethz/food101&config=default&split=train,yes,human (val) / machine (train),label name,n/a,101x(750+250),yes,low,MAYBE,high,
14,D14.3,plate waste,Voxel51 food-waste,https://huggingface.co/datasets/Voxel51/food-waste-dataset,Voxel51/food-waste-dataset,MIT,https://huggingface.co/datasets/Voxel51/food-waste-dataset,open,309.6,16.57,no,https://datasets-server.huggingface.co/first-rows?dataset=Voxel51/food-waste-dataset&config=default&split=train,no,machine,n/a,n/a,n/a,n/a,low,SKIP,high,
14,D14.2,hand hygiene,ybli kitchen hygiene,https://huggingface.co/datasets/ybli/yolo-kitchen-hygiene-safety-detection,ybli/yolo-kitchen-hygiene-safety-detection,NOT STATED,,unknown (off-site),0,0,no,,no,UNVERIFIED,n/a,n/a,Performing-Hand-Hygiene,n/a,high,SKIP,high,everything
15,D15.1,person near forklift,keremberke forklift,https://huggingface.co/datasets/keremberke/forklift-object-detection,keremberke/forklift-object-detection,CC BY 4.0,https://huggingface.co/datasets/keremberke/forklift-object-detection,open,20.4,2.77,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/forklift-object-detection&config=full&split=train,yes,human inferred,yes if 1 in objects.category,yes (194 forklift-only),forklift/person,yes,med (people),USE,med,box exhaustiveness
15,D15.2,damaged carton,cardboard-box-anomaly-detection,https://huggingface.co/datasets/Gabriel8/cardboard-box-anomaly-detection,Gabriel8/cardboard-box-anomaly-detection,CC BY-NC-SA 4.0,https://huggingface.co/datasets/Gabriel8/cardboard-box-anomaly-detection,open,2042.9,1.42,no,https://datasets-server.huggingface.co/rows?dataset=Gabriel8/cardboard-box-anomaly-detection&config=default&split=test&offset=0&length=100,yes,human,label==bad,yes (166 good),bad 386/good 166,yes,low,USE,high,
16,D16.3,damaged parcel,HassanBinAli Damaged_Parcel_boxes,https://huggingface.co/datasets/HassanBinAli/Damaged_Parcel_boxes,HassanBinAli/Damaged_Parcel_boxes,MIT,https://huggingface.co/datasets/HassanBinAli/Damaged_Parcel_boxes,open,0.03,0.02,no,https://datasets-server.huggingface.co/first-rows?dataset=HassanBinAli/Damaged_Parcel_boxes&config=default&split=train,yes,UNVERIFIED,n/a (no images),unknown,5 ints,n/a,low,SKIP,high,
16,D16.3,damaged parcel,Parcel3D,https://zenodo.org/records/8032204,,other-nc,https://zenodo.org/records/8032204,open,45838.3,45838.3,yes,,no,generator,UNVERIFIED,yes (per title),damaged/intact,UNVERIFIED,low,SKIP,high,schema
16,D16.1,container defect type,howell0123 shipping_container,https://huggingface.co/datasets/howell0123/shipping_container,howell0123/shipping_container,NOT STATED,https://huggingface.co/datasets/howell0123/shipping_container,open,224.6,224.52,no,https://datasets-server.huggingface.co/rows?dataset=howell0123/shipping_container&config=default&split=train&offset=0&length=100,yes,UNVERIFIED,single-defect answer string,no (positives only),Rusty367/Dent133/Scratch129/Deframe46/Hole14 singles,filter singles,low,MAYBE,med,licence;origin
16,D16.2,container damaged,Guztavu container-damage,https://huggingface.co/datasets/Guztavu/container-damage,Guztavu/container-damage,UNVERIFIED,,login + accept terms,339,39,no,,no,UNVERIFIED,UNVERIFIED,likely (bbox_nodmg.zip),UNVERIFIED,UNVERIFIED,low,GATED,low,all
17,D17.1,parcel at door,OliseNS home-security,https://huggingface.co/datasets/OliseNS/person-face-package-home-security-detection,OliseNS/person-face-package-home-security-detection,multi-source aggregated terms,https://huggingface.co/datasets/OliseNS/person-face-package-home-security-detection/blob/main/LICENSE,open,22701.7,22658 (sample folder small),yes,https://huggingface.co/datasets/OliseNS/person-face-package-home-security-detection/raw/main/sample/data.yaml,no,machine-assisted inferred,class 5 present,UNVERIFIED,9 classes incl face,no,high,SKIP,med,label origin
18,D18.1,room type,MIT Indoor-67 (Voxel51),https://huggingface.co/datasets/Voxel51/IndoorSceneRecognition,Voxel51/IndoorSceneRecognition,MIT tag vs original research-only,https://huggingface.co/datasets/Voxel51/IndoorSceneRecognition,open,2602.9,22.47 (json) / per-image,no,https://huggingface.co/datasets/Voxel51/IndoorSceneRecognition/resolve/main/samples.json,yes,human,ground_truth.label,n/a,kitchen734/living706/bed662/dining274/bath197,yes,low,MAYBE,med,licence
18,D18.1,room type,keremberke indoor-scene,https://huggingface.co/datasets/keremberke/indoor-scene-classification,keremberke/indoor-scene-classification,MIT (quotes research-only),https://huggingface.co/datasets/keremberke/indoor-scene-classification,open,470.3,46.53,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/indoor-scene-classification&config=full&split=train,yes,human,labels name,n/a,67,yes,low,MAYBE,med,licence
19,D19.1,floorplan door count,cubicasa5k-yolo,https://huggingface.co/datasets/v1nz/cubicasa5k-yolo,v1nz/cubicasa5k-yolo,CC BY-NC 4.0 (Zenodo says BY-NC-SA 4.0),https://zenodo.org/records/2613548,open,1762.8,4.4 (one png+txt),no,https://datasets-server.huggingface.co/first-rows?dataset=v1nz/cubicasa5k-yolo&config=default&split=train,yes,human (auto-converted),count lines with class 1,n/a,wall/door/window,yes,low,USE,med,conversion fidelity;door distribution
19,D19.2,bedroom count,CubiCasa5K original,https://zenodo.org/records/2613548,,CC BY-NC-SA 4.0,https://zenodo.org/records/2613548,open,5469.5,5469.5,yes,,no,human,room polygons in SVG,n/a,80+ categories,yes,low,SKIP,high,
19,D19.2,room layout (generator),FloorplanQA-Layouts,https://huggingface.co/datasets/OldDelorean/FloorplanQA-Layouts,OldDelorean/FloorplanQA-Layouts,CC BY 4.0,https://huggingface.co/datasets/OldDelorean/FloorplanQA-Layouts,open,16,<0.1,no,https://datasets-server.huggingface.co/first-rows?dataset=OldDelorean/FloorplanQA-Layouts&config=default&split=train,yes,generator,len(openings.windows) etc,n/a,bedroom692/kitchen622/living600,yes,none,MAYBE,high,no images (must render)
19,D19.6,CAD symbol count,FloorPlanCAD (Voxel51),https://huggingface.co/datasets/Voxel51/FloorPlanCAD,Voxel51/FloorPlanCAD,CC-BY-SA tag vs BY-NC text,https://huggingface.co/datasets/Voxel51/FloorPlanCAD,open,454.2,0.46 (png) / 60.4 (json),no,https://huggingface.co/datasets/Voxel51/FloorPlanCAD/resolve/main/samples.json (range),no (partial),UNVERIFIED,count detections by label,n/a,30,yes,low,MAYBE,low,licence;origin;rows
19,D19.3,construction era,WorcesterMA_Housing_Facades,https://huggingface.co/datasets/murai-lab/WorcesterMA_Housing_Facades,murai-lab/WorcesterMA_Housing_Facades,MIT (card warns clearance unconfirmed),https://huggingface.co/datasets/murai-lab/WorcesterMA_Housing_Facades,open,14162,0.01-3.7 (per image),no,https://datasets-server.huggingface.co/first-rows?dataset=murai-lab/WorcesterMA_Housing_Facades&config=default&split=train,yes,human (registry),class_label or year_built bins,yes,c1 11254/c2 4958/c3 2967/c4 1288,yes,med (addresses),MAYBE,med,image rights
19,D19.4,architectural style,facade-styles,https://huggingface.co/datasets/Jonathandav/facade-styles,Jonathandav/facade-styles,MIT,https://huggingface.co/datasets/Jonathandav/facade-styles,open,357.2,0.07 (manifest) / 0.46 (png),no,https://huggingface.co/datasets/Jonathandav/facade-styles/resolve/main/plate_manifest.parquet,yes,generator (text-to-image spec),style_name / view,yes,20 styles x50,yes,none,MAYBE,med,render fidelity
20,D20.1,recycling stream,TrashNet,https://huggingface.co/datasets/garythung/trashnet,garythung/trashnet,MIT,https://huggingface.co/datasets/garythung/trashnet,open,3677,42.83,no,https://datasets-server.huggingface.co/first-rows?dataset=garythung/trashnet&config=default&split=train,yes,human inferred,label name,n/a,cb806/gl1002/me820/pa1188/pl964/tr274,yes,none,USE,med,label origin text
20,D20.2,illegal dumping (aerial),DroneWaste,https://zenodo.org/records/17045559,,CC BY 4.0,https://zenodo.org/records/17045559,open,3891.3,8.8 (json) / 3882.5 images,yes,https://zenodo.org/records/17045559/files/dronewaste_v1.0.json,yes,UNVERIFIED (annotated),image has >=1 annotation,yes (3822 empty),20 materials,filterable,none,MAYBE,med,annotator type
20,D20.3,litter material,TACO,https://github.com/pedropro/TACO,,NOT STATED,https://github.com/pedropro/TACO,open,UNVERIFIED,annotations json small; images per-file 0.1-5 MB,no,https://raw.githubusercontent.com/pedropro/TACO/master/data/annotations.json,yes,human,supercategory of single annotation,no for presence,60 cats/28 supercats,610 single-object,low-med,MAYBE,med,licence
20,D20.4,bin overflowing,Garbage_Bin_overflow_images,https://huggingface.co/datasets/Akhila-9849/Garbage_Bin_overflow_images,Akhila-9849/Garbage_Bin_overflow_images,CC BY 4.0,https://huggingface.co/datasets/Akhila-9849/Garbage_Bin_overflow_images,open,111.8,0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=Akhila-9849/Garbage_Bin_overflow_images&config=default&split=train,no (images only),none,n/a,no,none,n/a,low,SKIP,high,
20,D20.1,waste class 10,waste-garbage-management,https://huggingface.co/datasets/steveharianto/waste-garbage-management-dataset,steveharianto/waste-garbage-management-dataset,MIT,https://huggingface.co/datasets/steveharianto/waste-garbage-management-dataset,open,789.8,<0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=steveharianto/waste-garbage-management-dataset&config=default&split=train,yes,UNVERIFIED,label name,n/a,10 classes,yes,low,SKIP,high,origin
```

---

## Part C. Question-expansion recipes (USE candidates only)

General rules for all datasets:
- Tier C questions are always stored with `label_origin: model` and kept in a separate table and score column. They are never merged into Tier A/B accuracy.
- A second model from a different family must agree on the answer, or the item is dropped.
- The model under test never writes or validates questions.
- The most useful Tier C content: rewordings of Tier A/B questions, harder distractor options drawn from the same class list, and natural-language variety (shopper, auditor or driver voice).

### D11.3 price-tag-detection
- **A:** none directly (detection only). The count of boxes is effectively Tier A for counting because the boxes are human.
- **B:**
  - (1) count bins: n = len(category_id)
  - (2) "Is any tag cut off at the edge?": any bbox coordinate ≤ 0.001 or ≥ 0.999
  - (3) "Are the tags in a single row?": the spread of y-centres is under 0.1
  - (4) "Is the largest tag more than 10% of the image?": max (y2−y1)(x2−x1) > 0.1
  - (5) "More tags in the top or bottom half?": compare y-centre counts
- **C:** price-reading questions ("what is the price on the left-most tag?"). These are model-written and need dual-model agreement. Distractors: nearby prices.

### D12.3 Fashionpedia
- **A:** garment set present (the 27 garment classes).
- **B:**
  - (1) "Which of these is NOT worn?" with 3 present and 1 absent class. Only use absent classes, and caution because exhaustiveness is unverified.
  - (2) shoe count bins
  - (3) "Is the dress larger than the jacket?" by bbox area
  - (4) "Does the outfit include an accessory (bag, hat, glasses, watch, belt)?"
  - (5) "Topmost garment: hat vs glasses vs none"
- **C:** style/occasion wording and colour questions (untrusted). Never ask about the person's identity.

### D12.4 ABO-Edit
- **A:** white-background yes/no (generator); `product_type` (catalogue).
- **B:**
  - (1) "Is the tilt ≥ N°?" from `simplified_rotation_prompt` (target only)
  - (2) "Is this the lifestyle or the studio version of the product?"
  - (3) Pairing: "Is the product in image 1 the same type as …?" Not allowed, because the spec requires one image per question, so skip it.
  - (4) "Which product type is NOT shown: LAMP / CHAIR / SOFA / TABLE?" with 3 distractors from other rows
- **C:** material and colour questions (the `object_description` field is VLM-written, so it counts as Tier C at best).

### D13.4 grocery-images-5class
- **A:** item class.
- **B:**
  - (1) "fruit vs non-fruit" (apple/banana vs bread_roll/cheese)
  - (2) "baked good?"
  - (3) "dairy?"
  - (4) "Which is NOT shown?" with 1 true class and 3 others as options
- **C:** quantity ("how many bananas?"), ripeness and packaging questions (model-written, verified by a second model).

### D15.1 forklift
- **A:** person present (yes/no).
- **B:**
  - (1) forklift count bins
  - (2) person count bins
  - (3) "Is the person larger than 10% of the forklift's box area?"
  - (4) "Is the person to the left or right of the forklift?" by comparing bbox x-centres
  - (5) "Does the forklift fill more than half the frame?"
- **C:** "Is the forklift carrying a load?", "Is the operator seated?" (untrusted).

### D15.2 cardboard box anomaly
- **A:** damaged yes/no.
- **B:**
  - (1) "Floor or conveyor?" from `loc-`
  - (2) "Which conveyor, b1 or b2?" (low value)
  - (3) Restrict to each box's own images: "Is this the same box id as reference X?" This is single-image only if X is described in text, so skip it.
  - Keep B to (1).
- **C:** defect type ("crushed corner / tear / wet / open flap"). This is model-written and especially valuable, but it must be agreed by two models.

### D19.1 CubiCasa5K-YOLO
- **A:** door count, window count (human polygons).
- **B:**
  - (1) "More windows than doors?"
  - (2) wall-segment count bins
  - (3) "Is there a window on the top edge of the plan?": any class-2 polygon with min y < 0.1
  - (4) "Total openings (doors + windows) above 15?"
  - (5) "Which is most common: wall segments / doors / windows?"
- **C:** room-name reading (OCR-like: "Is there a sauna?"), which is common in Finnish plans. Untrusted.

### D20.1 TrashNet
- **A:** material class.
- **B:**
  - (1) recyclable vs trash
  - (2) fibre vs non-fibre
  - (3) "Is this item glass or plastic?" (hard pair)
  - (4) "Which stream is NOT correct for this item?" (3 wrong options + 1 right, inverted)
- **C:** object name ("is it a bottle, a can or a box?") and "is it crushed?" (untrusted).

---

## 4. Gaps

| Task | Why no acceptable dataset | Generator / drawn version realistic? How |
|---|---|---|
| D11.1 out-of-stock gap | SKU-110K rejected. SKUs_on_shelves_PL is an 11.4 GB single archive. No open labelled "empty facing" set was found on HF ("empty shelf" / "out-of-stock" searches returned nothing). | **Yes, medium realism.** Render shelves procedurally (Blender or Unity) with textured product boxes in a grid, delete k facings, and record which slots are empty. The answer is the generator value. Real-photo fidelity is limited, so prefer a human pulling only the COCO JSON from SKUs_on_shelves_PL. |
| D11.4 discount flag | Only machine (Gemini) labels. | **Yes, high.** Draw price-tag templates (HTML to PNG) with known price, unit price and a promo badge. Add camera noise. |
| D11.6 planogram category | None found. | Partly: from the same shelf renderer, assign category textures per shelf. |
| D12.2 colour | Only tiny 60×80 images; ABO colour is free text. | Partly: normalise ABO `color_en` to about 10 colours (Tier B-like, needs mapping), or render ABO 3D assets with a known material colour (generator). |
| D13.1 fresh vs rotten | The open sets are tiny, a single archive, or a duplicate of the used AgML set. | Not realistic to draw decay convincingly. Needs human photos. |
| D13.5 produce grade, D13.6 date legible | None found. | Date legibility: **yes**. Render date labels with controlled blur and occlusion; the answer is the blur level. |
| D14.2 gloves/hairnet, D14.4 pests, D14.5 surface clean | Only an off-site mirror (ybli). No open kitchen-hygiene set with negatives. | Gloves/hairnet: needs human photos, with faces as a privacy risk. Pest: compositing is possible but unrealistic. **Domain 14 is the weakest; consider replacing it in the merge.** |
| D14.3 plate waste | Machine labels only. | No. |
| D15.3 / D15.4 pallet and box counts | Nothing found (lettuce-pallets is hydroponics, not logistics). | **Yes, high.** The projectsim/warehouse-manipulation-and-states CC BY 4.0 assets (cardboard boxes, pallet_boxes GLBs; 33–37 MB each [CARD]) can be rendered in stacks with known counts. |
| D15.5 aisle obstruction | None. | Partly: render warehouse aisles with or without objects. |
| D16.2 container damaged yes/no | Guztavu is GATED; howell0123 is positives only with no licence. | No. A human should review the GATED repo. |
| D16.3 parcel damaged | Parcel3D is a 45.8 GB archive. | Parcel3D itself is synthetic (Blender, damaged vs intact), so the generator route is proven. A human could pull a subset, or we re-render using CBTex textures (Zenodo 8041823, CC BY 4.0, 1.47 GB zip). Gabriel8 cardboard covers the real-photo version. |
| D16.4 container ID / D16.5 barcode | Nothing qualified. | **Yes, high.** Generate ISO 6346 codes (owner code + serial + computed check digit) painted on container-like panels; generate Code128/QR labels on parcel textures. The answer comes from the generator values. |
| D17.1–D17.5 delivery proof | Only OliseNS (archive, machine-assisted, face data). | Partly. Composite parcel renders onto doorstep photos (needs CC0 doorstep backgrounds) for "parcel visible"; blur levels for "photo usable". Placement (doorstep/mailbox/locker) needs human photos. |
| D18.3 bed made, D18.4 tidy, D18.5 damage | None found. | Bed made / tidy: **medium**. 3D room render with cloth simulation states. Damage: no. |
| D18.2 amenity yes/no | MIT Indoor polygons are not exhaustive. | Use Tier B only for positives, or render bathrooms with or without towels. |
| D19.2 bedroom count | CubiCasa5K SVGs only inside a 5.4 GB archive. | **Yes, high.** Render FloorplanQA-Layouts JSON (CC BY 4.0) or procedural multi-room plans with room labels; the count comes from the generator. A human could also pull CubiCasa5K once. |
| D20.4 bin overflowing, D20.5 wet floor | Overflow set is positives only and unlabelled; no spill set found. | Spill: partly (decals on floor renders). Overflow: needs human photos with negatives. |

---

## 5. Cannot verify

- **Annotator details from papers:** RPC (arXiv 1901.07249) label origin; the Fashionpedia annotation protocol and exhaustiveness; the TrashNet collection method; the FloorPlanCAD annotators; the DroneWaste annotation method. The arXiv API query returned nothing from this machine.
- **Original-owner licence pages:** MIT Indoor (web.mit.edu), ABO official page, Food-101 ETH page, Mendeley ripeness dataset, Roboflow Universe pages, tacodataset.org. None were fetched; I relied on mirror cards.
- **Value-reason statistics** (IHL, OSHA, USDA ERS, Recycling Partnership, SafeWise, NAR): seen only as search-result snippets, not opened.
- **Guztavu/container-damage:** README returns 401 (gated). Contents are known only from the file listing.
- **Per-class counts not run:** ABO `product_type`, Fashionpedia categories, CubiCasa-YOLO door distribution, ABO-Edit row count.
- **openfoodfacts price-tag-extraction benchmark v2.0** (claimed human-validated, on GitHub): not fetched. It may make D11.4 viable.
- **Not checked:** devmandan/syn10k-huawei-barcodes (possible generator barcodes, CC BY 4.0 tag), 123metro/barcode-datasets, Fnhid/indory-waybill-ocr-640x480, UniDataPro/grocery-shelves (cc-by-nc-nd sample), Kos1976/9-facades-doors-windows-50-commercial.
- **GroceryStoreDataset** total size: the GitHub API returned null.
- **FloorPlanCAD samples.json** (60.4 MB) is over the cap; only a range was read.
