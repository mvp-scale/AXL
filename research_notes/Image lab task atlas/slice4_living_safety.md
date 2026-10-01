# Slice 4: Living systems and safety (domains 31–40)

Researcher notes for the image-task test bench. They follow Part 1 of `_spec.md`. Work done 2026-10-01. Everything was fetched in this session with `curl` against `huggingface.co/api/datasets/<id>?blobs=true` (licence, gated flag, file sizes), `datasets-server.huggingface.co/{splits,size,first-rows,statistics}` (rows and class counts) and raw files under 50 MB (`README.md`, `README.dataset.txt`, `data.yaml`, COCO JSON, YOLO `.txt`, CSV). For YOLO repos, the "negatives" count comes from counting **0-byte label files** in the blob listing. No logins, forms or downloads over 50 MB.

Evidence tags: [ROW] = seen in a fetched row or file. [CARD] = owner card, README or yaml. [PAPER]. [INFERRED]. [UNVERIFIED].

**Domain swaps:** none. Domain 37 (healthcare admin) had little real data, but fetches turned up two generator datasets (synthetic, rendered medical documents), so I kept it.

**Headline:** about 15 candidates pass the USE rule. The strongest are PKLot (parking), Oxford-IIIT Pet, Project-AgML plant seedlings, oil-palm ripeness and tree species, the AGRARIAN sheep/goat drone set, VincentGOURBIN PPE (vest and helmet), the keremberke forklift and construction-safety sets, the bike-helmet COCO set, the Medication Boxes COCO set, the Turki weapon set (it has real hard negatives), and the morzel85 synthetic medical-document benchmark (generator labels). Fire and smoke is the weak spot. The one dataset with good real negatives, D-Fire (9,838 "none" images per its README), has **no licence stated** anywhere I could fetch. FASDD is a single 3.4 GB archive. Synthetic wildfire sets are positives-only.

---

## 1. Task atlas

### D31 Agriculture and crops
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 31.1 | Pest / disease present on crop plant | "Is this crop plant healthy?" | yes / no | photo | FAO: up to 40% of global crop production is lost to pests each year; plant diseases cost over $220 bn ([FAO via DownToEarth](https://www.downtoearth.org.in/news/agriculture/at-least-40-global-crops-lost-to-pests-every-year-fao-77252)) |
| 31.2 | Seedling is crop or weed (spot-spraying) | "Which plant is this seedling?" | 4–6 of the 12 Aarhus species (e.g. maize, sugar beet, common wheat, charlock, fat hen, black-grass) | photo (top-down) | same FAO pest-loss figure; weeds are among the "pests" in IPPC usage [INFERRED] |
| 31.3 | Oil-palm bunch ripeness grading at the mill | "What ripeness grade is this fresh fruit bunch?" | unripe / ripe / overripe / empty / damaged | photo | Unripe fruit lowers oil extraction rate by 0.13% or more; a 0.13% OER drop is about RM 340 m to Malaysia ([PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7038324)) |
| 31.4 | Weed count in a maize field image | "How many weeds are visible?" | 0 / 1–2 / 3–5 / 6+ | photo | FAO pest-loss source above |
| 31.5 | Banana/mango ripeness | "Is this fruit ripe?" | yes / no (+ banana / mango) | photo | No dedicated source found |
| 31.6 | Insect pest species on trap/leaf | "Which pest is this?" | 4–6 species | photo | FAO source above (invasive insects at least $70 bn) |
| 31.7 | Crop field vs other land cover from satellite | "Is this tile annual cropland?" | yes / no | aerial | No source fetched |

### D32 Livestock and fisheries
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 32.1 | Herd composition from drone | "Are there goats in this image?" / "Which animal is most numerous?" | yes/no ; goat / sheep / none | aerial (drone) | No source found (flock counting for subsidy and insurance claims, [INFERRED]) |
| 32.2 | Flock headcount from drone | "How many sheep are visible?" | 0–5 / 6–10 / 11–20 / 21+ | aerial | No source found |
| 32.3 | Pig posture (welfare: lying vs standing) | "How many pigs in this pen image are standing?" / "Is any pig sitting?" | count bins ; yes/no | video frame (barn CCTV) | No source fetched |
| 32.4 | Fish species ID at landing or audit | "Which family is this fish?" | 4–6 families | photo (specimen) | No source fetched |
| 32.5 | Aquatic animal type in tank/aquarium | "Which animal is shown?" | fish / jellyfish / penguin / shark / stingray / starfish | photo | No source |
| 32.6 | Cattle present / count in pasture | "How many cattle?" | bins | aerial/photo | No source. **Gap** (no verified dataset) |

### D33 Forestry and environment
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 33.1 | Camera-trap species triage | "Which animal is in this camera-trap image?" | fox / bird / rodent / skunk / other | photo (trail camera, incl. IR night) | About 70% of camera-trap images are empty; manual review takes up to 5 s per image ([MegaDetector docs](https://megadetector.readthedocs.io/en/latest/getting-started.html)) |
| 33.2 | Camera-trap empty frame filter | "Is there an animal in this image?" | yes / no | photo | same source. **Gap**: the HF subset dropped the empty frames |
| 33.3 | Tree species in forest inventory | "Which tree species is this?" | European beech / silver fir / Norway spruce / sessile oak | photo | No source fetched |
| 33.4 | Wildfire smoke on horizon | "Is there wildfire smoke in this view?" | yes / no | photo (tower camera) | NFPA: in 2018 the US had 1.3 m fires and about $25 bn property loss ([NFPA via FireEngineering](https://www.fireengineering.com/fire-safety/nfpa-fire-loss-report/)) |
| 33.5 | Land-cover class of satellite tile | "What is the main land cover?" | forest / annual crop / pasture / river / residential / industrial | aerial | No source. EuroSAT is 64 px (trap) |
| 33.6 | Flooded area in aerial image | "Is any road flooded?" | yes / no | aerial | No source. FloodNet is a 12.8 GB single archive |

### D34 Workplace safety and PPE
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 34.1 | Hi-vis vest missing | "Is any worker without a safety vest?" | yes / no | photo / CCTV frame | OSHA's top-10 cited standards include eye/face PPE (1926.102, 1,665 violations) and respiratory protection ([Safety+Health / OSHA Top 10](https://safetyandhealthmagazine.com/articles/24670-fall-protection-again-leads-oshas-annual-top-10-list-of-most-frequently-cited-standards)) |
| 34.2 | Hard hat missing (non-Voxel51 source) | "Is any worker without a helmet?" | yes / no | photo | same OSHA Top-10 source |
| 34.3 | Pedestrian near forklift | "Is a person present together with the forklift?" | yes / no | photo | OSHA: about 85 forklift fatalities and 34,900 serious injuries a year; powered industrial trucks are #8 in OSHA's Top 10 ([NIOSH/CDC](https://Cdc.gov/niosh/docs/2001-109/pdfs/2001-109.pdf); [OSHA Top 10](https://safetyandhealthmagazine.com/articles/24670-fall-protection-again-leads-oshas-annual-top-10-list-of-most-frequently-cited-standards)) |
| 34.4 | Construction-site PPE audit (mask, gloves, vest, hat) | "Which PPE item is missing on someone?" | hardhat / mask / safety vest / none | photo | OSHA Top-10 source |
| 34.5 | Seat belt fastened (fleet driver) | "Is the occupant wearing a seat belt?" | yes / no | photo (in-cab) | NHTSA: seat belts saved about 14,955 lives in 2017 ([NHTSA](https://crashstats.nhtsa.dot.gov/Api/Public/Publication/812683)) |
| 34.6 | Person down / fall incident | "Is a person lying on the floor?" | yes / no | CCTV frame | Falls lead OSHA's most-cited list for 15 years ([OSHA Top 10](https://safetyandhealthmagazine.com/articles/24670-fall-protection-again-leads-oshas-annual-top-10-list-of-most-frequently-cited-standards)) |
| 34.7 | Smoking in no-smoking zone | "Is someone smoking?" | yes / no | photo | No source |

### D35 Fire, smoke and security video
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 35.1 | Fire or smoke in frame | "Is there fire or smoke in this image?" | yes / no | CCTV frame / photo | NFPA fire-loss report ([FireEngineering](https://www.fireengineering.com/fire-safety/nfpa-fire-loss-report/)) |
| 35.2 | Fire vs smoke only (alarm type) | "What is visible?" | fire only / smoke only / both / neither | photo | same |
| 35.3 | Weapon visible (CCTV) | "Is a weapon visible?" | yes / no | CCTV frame / photo | No regulator source fetched |
| 35.4 | Weapon type | "Which weapon is visible?" | gun / knife / none | photo | No source |
| 35.5 | Person lying in monitored space | see 34.6 | yes / no | CCTV | see 34.6 |
| 35.6 | Intrusion: person in restricted zone at night | "Is a person present?" | yes / no | CCTV | No source. **Gap** |

### D36 Traffic, parking and smart city
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 36.1 | Parking occupancy | "Is this parking lot more than half full?" / "How many vacant spaces are labelled?" | yes/no ; bins | CCTV frame | INRIX: US drivers spend 17 h/yr searching for parking, $72.7 bn total ([INRIX](https://inrix.com/press-releases/parking-pain-us/)) |
| 36.2 | Motorcyclist helmet compliance | "Is every rider wearing a helmet?" | yes / no | photo / CCTV | No source fetched |
| 36.3 | Vehicle class count (tolling, planning) | "Which vehicle class is most common?" | car / bus / truck | CCTV frame | No source |
| 36.4 | Traffic light state | "What colour is the light facing the camera?" | red / yellow / green | dashcam frame | No source |
| 36.5 | Traffic sign identification | "Which sign is this?" | stop / yield / no entry / speed limit … | photo | No source. **Gap** (GTSRB is tiny) |
| 36.6 | Road-user count from fisheye pole camera | "How many pedestrians are visible?" | bins | CCTV fisheye | No source |

### D37 Healthcare administration (documents only, no diagnosis)
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 37.1 | Route incoming medical page by document type | "What kind of document is this page?" | contact info / observation / vaccination history / report / survey / notes | scan / photo of page | No source fetched |
| 37.2 | Capture-quality triage | "How was this page captured?" | clean digital / photocopy / phone photo | scan / photo | No source |
| 37.3 | Page clipped / incomplete | "Is part of the page cut off?" | yes / no | photo | No source |
| 37.4 | Bill vs discharge summary | "Is this a hospital bill?" | yes / no | scan | No source |
| 37.5 | Insurance card / wristband field read | "Does the wristband show a date of birth?" | yes / no | photo | **Gap**. A generator is realistic |

### D38 Pharmacy
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 38.1 | Package vs package-insert sorting; import vs domestic licence | "Is this an outer carton or a leaflet?" ; "Is this an imported drug (licence prefix 輸)?" | carton / leaflet ; yes/no | scan (rendered PDF) | Similar labels/packaging is the most-reported factor in medication errors (16.6%); labelling, packaging and nomenclature play a role in about half of FDA MedWatch error reports ([ECRI/ISMP](https://home.ecri.org/blogs/ismp-alerts-and-articles-library/merp-annual-review-exposes-how-manufacturer-labeling-quality-issues-impact-medication-safety)) |
| 38.2 | Pill identity on tray | "Which product is this tablet?" | Cipro 500 / Ibuphil 600 / Ibuphil Cold / Xyzall 5 mg | photo | same ECRI/ISMP source |
| 38.3 | Count of medication boxes (dispensing check) | "How many medicine boxes are in the photo?" | 1 / 2 / 3 / 4+ | photo | same |
| 38.4 | Pill reference match | "Which shape/colour is this pill?" | — | photo | **Gap**: labels only via the NDC filename |
| 38.5 | Blister pack completeness | "Is any blister cavity empty?" | yes / no | photo | **Gap** |

### D39 Veterinary and pets
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 39.1 | Cat or dog (intake, listings) | "Is this a cat or a dog?" | cat / dog | photo | No source fetched |
| 39.2 | Breed for listing/insurance quote | "Which breed is this?" | 4–6 of 37 Oxford breeds | photo | No source fetched |
| 39.3 | Dog breed, fine-grained | "Which breed?" | 4–6 of 120 | photo | No source |
| 39.4 | Livestock welfare posture | see 32.3 | | | |
| 39.5 | Animal count in photo | "How many animals?" | bins | photo | **Gap** |

### D40 Laboratory and scientific (no diagnosis)
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| 40.1 | Harmful-algal-bloom taxon in water sample | "Is this phytoplankton cell Alexandrium?" / pick taxon | yes/no ; 4–6 taxa | microscopy | HABs cost many millions of dollars a year (e.g. $10.3 m Texas oyster loss in 2011) ([NOAA Fisheries](https://www.fisheries.noaa.gov/west-coast/science-data/hitting-us-where-it-hurts-untold-story-harmful-algal-blooms)) |
| 40.2 | Specimen tray count (biodiversity lab) | "How many beetles are in this tray image?" | 1–5 / 6–15 / 16–40 / 41+ | photo (lab) | No source fetched |
| 40.3 | Specimen genus/species (single specimen) | "Which genus is this beetle?" | 4–6 genera | photo (lab) | No source |
| 40.4 | Colony count on agar plate | "How many colonies?" | bins | photo | No source. GATED candidate |
| 40.5 | Pollen grain taxon | pick | | microscopy render | No source. SKIP candidate |

---

## 2. Dataset qualification cards

Format: fields 1–12 in order, with evidence tags inline (field 13). "Rows" are real fetched rows, with image bytes replaced by their pixel size.

### D31.1 — Project-AgML/crop_pest_disease_classification (rank 1)
1. Landing: https://huggingface.co/datasets/Project-AgML/crop_pest_disease_classification ; files: …/tree/main ; repo id `Project-AgML/crop_pest_disease_classification` [CARD]
2. Licence: `license: cc-by-4.0` (README YAML) [CARD]. Card says "indexed on https://project-agml.github.io/". Original: Mensah Kwabena et al. (CCMT dataset, Ghana) [CARD]. No research restriction stated.
3. Access: open (gated: False) [CARD]
4. Size: 8,427 MB total; configs `raw` (25,170 rows) and `augmented` (105,252 rows). Smallest shard is about 380 MB (`augmented/train-00012-of-00016.parquet`). Not a single archive, but no shard is under 50 MB, so sample via datasets-server [CARD]
5. Sample proof: `https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/crop_pest_disease_classification&config=raw&split=train` [ROW]
   - `{"image": 400x400, "label": 0, "crop": "Cashew"}`
   - `{"image": 400x400, "label": 0, "crop": "Cashew"}`
   - `{"image": 400x400, "label": 0, "crop": "Cashew"}`
6. Schema: `image` (Image); `label` ClassLabel of 18 names (anthracnose, bacterial blight, brown spot, fall armyworm, grasshoper, green mite, gumosis, healthy, leaf beetle, leaf blight, leaf curl, leaf miner, leaf spot, mosaic, red rust, septoria leaf spot, streak virus, verticulium wilt); `crop` string (Cashew/Cassava/Maize/Tomato) [ROW]
7. Label origin: human [INFERRED]. The source is a field-collected, expert-curated CCMT set, but the card does not describe annotation. UNVERIFIED quote.
8. Answer rule: healthy = yes iff `label == "healthy"`. Crop = `crop` column.
9. Classes (raw split, /statistics): healthy 3,235; septoria 2,743; bacterial blight 2,614; leaf blight 2,292; anthracnose 1,729; red rust 1,682 … fall armyworm 285. Crop: Cassava 7,508, Cashew 6,549, Tomato 5,792, Maize 5,321 [ROW]. **Real negatives: yes** (3,235 healthy) [ROW].
10. One label per image [ROW]. Use the `raw` config only; `augmented` holds synthetic augmentations [CARD].
11. Risks: 400 px images (upscaling to 1536 softens them) [ROW]. Plant pathology is not human medical diagnosis, but **it overlaps the "plant leaf disease" family already used**. Same org (Project-AgML), different source dataset. The merge step should decide [INFERRED]. Duplicate photos in the source are UNVERIFIED.
12. Templates: (a) "Is this {crop} plant healthy?" yes/no. (b) "Which crop is this?" Cashew/Cassava/Maize/Tomato. (c) "Which problem is shown?" 4 options drawn from the same crop's labels.
Verdict: **USE** (provisional, origin inferred), confidence med. Flag the overlap with the used leaf-disease set.

### D31.2 — Project-AgML/plant_seedlings_aarhus (rank 1)
1. https://huggingface.co/datasets/Project-AgML/plant_seedlings_aarhus ; original https://vision.eng.au.dk/plant-seedlings-dataset/ [CARD]
2. `license: cc-by-sa-4.0` [CARD]. ShareAlike applies to derivatives. No testing restriction.
3. open [CARD]
4. 1,714.5 MB; 3 parquet shards, smallest 309.4 MB (`data/train-00000-of-00003.parquet`) [CARD]
5. Proof: `first-rows?dataset=Project-AgML/plant_seedlings_aarhus&config=default&split=train` [ROW]
   - `{"image": 426x426, "label": 9}`
   - `{"image": 629x629, "label": 9}`
   - `{"image": 404x404, "label": 9}` (9 = shepherds_purse)
6. `image`; `label` ClassLabel: black_grass, charlock, cleavers, common_chickweed, common_wheat, fat_hen, loose_silkybent, maize, scentless_mayweed, shepherds_purse, smallflowered_cranesbill, sugar_beet [ROW]
7. human [INFERRED]: plants were grown and photographed per species by Aarhus University. Card has no annotation section.
8. Species = `label`. Crop-or-weed: yes (crop) iff label ∈ {maize, common_wheat, sugar_beet} [INFERRED from species biology].
9. black_grass 309, charlock 452, cleavers 335, common_chickweed 713, common_wheat 253, fat_hen 538, loose_silkybent 762, maize 257, scentless_mayweed 607, shepherds_purse 274, smallflowered_cranesbill 576, sugar_beet 463 (total 5,539) [ROW]. Crop/weed negatives: 973 crop vs 4,566 weed images.
10. One species per image [CARD/ROW]
11. Variable size 400–630 px (some small) [ROW]. Widely used Kaggle set (training overlap likely) [INFERRED].
12. (a) "Which plant is this seedling?" 4 options. (b) "Is this seedling a crop?" yes/no. (c) "Is this seedling a grass-type weed (black-grass or loose silky-bent)?" yes/no.
Verdict: **USE** (med).

### D31.3 — Project-AgML/oil_palm_fruit_ripeness_classification (rank 1)
1. https://huggingface.co/datasets/Project-AgML/oil_palm_fruit_ripeness_classification ; source Zenodo https://doi.org/10.5281/zenodo.11114885 [CARD]
2. `license: cc-by-4.0` [CARD]
3. open
4. 1,165.7 MB; smallest shard 182.4 MB [CARD]
5. Proof: first-rows default/train [ROW]: `{"image":757x568,"label":1}`, `{"image":2400x3200,"label":1}`, `{"image":757x568,"label":1}` (1 = Empty)
6. `image`, `label` ClassLabel [Damaged, Empty, Overripe, Ripe, Unripe] [ROW]
7. human [INFERRED]: grading of outdoor Tenera FFB photos (MunirahRosbi Zenodo). UNVERIFIED quote.
8. grade = `label`
9. Damaged 15, Empty 12, Overripe 74, Ripe 201, Unripe 164 (466 total) [ROW]. Imbalanced. Use mainly Ripe/Unripe/Overripe.
10. one bunch per image [INFERRED]
11. Mixed resolutions (757 px to 3200 px) [ROW]. Small set.
12. (a) "What ripeness grade is this bunch?" unripe/ripe/overripe. (b) "Is this bunch ready to harvest (ripe)?" yes/no. (c) "Is this an empty or damaged bunch?" yes/no.
Verdict: **USE** (med).

### D31.4 — Project-AgML/maize_weed_detection (rank 1)
1. https://huggingface.co/datasets/Project-AgML/maize_weed_detection ; source Mendeley Data "Maize-Weed Image Dataset" (Olaniyi et al. 2022) [CARD]
2. `license: cc-by-4.0` [CARD]
3. open
4. 817 MB; 2 shards about 402/415 MB [CARD]
5. Proof [ROW]: row0 `objects.categories` [0,0,0,0,0,0,0,0,…+10], 1920x1080; row1 [0×8,…+8]; row2 [0×8,…+8]. Bboxes as [x,y,w,h].
6. `objects.bbox` list[list[float]]; `objects.categories` list ClassLabel [maize, weed] [ROW]
7. human [INFERRED] (Mendeley bbox set); card says "500 images with 5,764 bounding box annotations across 2 categories" [CARD]
8. weeds = count(categories == 1)
9. 2 classes. Per-image weed counts not computed; **zero-weed images UNVERIFIED** [UNVERIFIED]
10. multi-object; use count bins
11. 1920x1080 good. Small weeds may be tiny in frame [INFERRED].
12. (a) "How many weeds are labelled?" bins. (b) "Are there more maize plants than weeds?" yes/no. (c) "Is any weed present?" yes/no (only if negatives are confirmed).
Verdict: **MAYBE**. The yes/no needs a negatives check; the count is USE-able. Confidence med.

### D31.5 — darthraider/fruit-ripeness-detection-dataset
1. https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset
2. `license: apache-2.0` (YAML only) [CARD]
3. open
4. 390.9 MB; smallest `data/test-00000-of-00001.parquet` **35.5 MB** [CARD]
5. Proof [ROW]: `{"image":640x480,"label":0}` ×3 (0 = Raw_Banana)
6. `label` ClassLabel [Raw_Banana, Raw_Mango, Ripe_Banana, Ripe_Mango] [ROW]
7. UNVERIFIED (no provenance on the card)
8. ripe = label startswith "Ripe"
9. counts UNVERIFIED; 3,999 train / 1,000 test [ROW]
10. one per image [INFERRED]
11. Unknown provenance. Possibly scraped. Near the "fresh/rotten fruit" family already used.
12. ripe? yes/no; banana or mango; ripe banana vs raw banana.
Verdict: **MAYBE** (label origin unknown).

### D31.6 — EnmmmmOvO/insect-pest-dataset
1. https://huggingface.co/datasets/EnmmmmOvO/insect-pest-dataset. 2. `license: mit` [CARD]. 3. open. 4. 3,188 MB; smallest shard 299 MB. 5. [ROW] `{"image":342x190,"label":0}`, `{"image":330x247,"label":0}`, `{"image":240x213,"label":0}`. 6. `label` int64 **with no class names** [ROW]. 7. UNVERIFIED (looks like IP102, [INFERRED]). 8. Not computable without a name map. 9. 45,095/22,619/7,508 rows. 10. one per image. 11. **Tiny images (about 200–340 px)**. 12. n/a.
Verdict: **SKIP** (tiny images; unnamed labels).

### D31.7 — timm/eurosat-rgb (land cover; also serves D33.5)
1. https://huggingface.co/datasets/timm/eurosat-rgb. 2. `license: mit` [CARD] (paper arXiv:1709.00029). 3. open. 4. 92.1 MB; smallest **18.4 MB** test parquet. 5. [ROW] `{"image":64x64,"label":6,"image_id":"PermanentCrop_807"}`, `{"image":64x64,"label":0,"image_id":"AnnualCrop_889"}`, `{"image":64x64,"label":3,"image_id":"Highway_1169"}`. 6. label ClassLabel of 10 (AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial, Pasture, PermanentCrop, Residential, River, SeaLake). 7. human [INFERRED from paper, UNVERIFIED]. 8. = label. 9. AnnualCrop 1,791 … Pasture 1,195 (train) [ROW]. 10. one. 11. **64x64 px: tiny-image trap**. 12. n/a.
Verdict: **SKIP** (tiny).

### D32.1 — AGRARIAN/greek_sheep_goats_dataset (rank 1)
1. https://huggingface.co/datasets/AGRARIAN/greek_sheep_goats_dataset ; files …/tree/main (YOLO `train/`, `val/`, `data.yaml`)
2. `license: apache-2.0` [CARD]
3. open
4. 3,627.7 MB total, 7,205 files; individual label `.txt` files are about 0 MB and images about 0.5 MB each [CARD]. Not an archive, so files can be fetched one by one.
5. Proof: raw `train/labels/0058dd32-DJI_20250224121827_0005_D_2260_6.txt` [ROW]:
   - `0 0.0046205693651593 0.5696770439906462 0.0092411387303185 0.0727442369364713`
   - `0 0.0112021908022686 0.5921931173281253 0.0224043816045372 0.0914498978629926`
   - `0 0.0254046370612937 0.6091667726133015 0.0508092741225875 0.0866002820672277`
   - data.yaml: `names: ['goat', 'sheep']` [ROW]
6. YOLO lines: `class x_c y_c w h` normalised. Class 0 = goat, 1 = sheep.
7. human. Card: "**Manual Annotation:** Every image has been manually labeled… Label Studio was used" [CARD]
8. goats present = any line with class 0; majority = argmax count by class; none if the file is empty.
9. **Real negatives: yes**. 676 train + 214 val label files are 0 bytes (empty), 2,012 + 698 non-empty [ROW, blob listing].
10. Multi-animal. Use presence or count questions. Majority is ambiguous when counts tie, so drop ties.
11. Source is 450 drone frames cut into 8 **overlapping** 640x640 patches, so near-duplicates exist and the same animal can appear in two patches [CARD]. Animals are small. No people.
12. (a) "Are there goats in this image?" yes/no. (b) "Which animal is more numerous?" goat/sheep/none visible. (c) "How many animals?" 0 / 1–5 / 6–15 / 16+.
Verdict: **USE** (high).

### D32.2 — keremberke/aerial-sheep-object-detection (rank 1 for count)
1. https://huggingface.co/datasets/keremberke/aerial-sheep-object-detection ; Roboflow https://universe.roboflow.com/riis/aerial-sheep [CARD]
2. README.dataset.txt: "License: Public Domain" [CARD]. HF YAML has no licence field.
3. open
4. 451 MB; `data/train.zip` 393 MB; valid/test zips smaller (sizes not separately printed, UNVERIFIED). It is zip-based, but the datasets-server viewer works.
5. Proof first-rows default/train [ROW]: image_id 28 (600x600) 19 sheep boxes; image_id 1842 17 boxes; image_id 3386 20 boxes, all `category` 0.
6. `objects.{id, area, bbox[x,y,w,h], category∈[sheep]}` [ROW]
7. human [INFERRED] (Roboflow-annotated); README notes "augmentation was applied to create 3 versions of each source image" [CARD]
8. count = len(objects.category)
9. 1 class, 3,609/350/174 images. Negatives UNVERIFIED.
10. count question only
11. **3× augmented copies** inflate the set; dedupe by source. 600 px.
12. "How many sheep?" bins; "More than 10 sheep?" yes/no; "Is any sheep touching the image edge?" (from bbox, x=0 or x+w=600) yes/no.
Verdict: **USE** for counts (med). Dedupe augmentations first.

### D32.3 — anilbhujel/viewpoint-aware-pig-posture-recognition (rank 1)
1. https://huggingface.co/datasets/anilbhujel/viewpoint-aware-pig-posture-recognition ; code github.com/Anil-Bhujel/viewpoint-aware-pig-posture-recognition [CARD]
2. "released under the Creative Commons Attribution 4.0 (CC BY 4.0) license" [CARD]
3. open
4. 1,357 MB; `train.csv` 7.6 MB; images 0.08 MB and up each [CARD]
5. Proof: raw `viewpoint_aware_pig_posture_recognition/seenVP_test.csv` [ROW]:
   - `test_pen1_tur_cam2_20250920_174649_0000, pen1_tur_cam2_20250920_174649.jpg,1280,720,"[711.7,251.2,280.0,436.0]",0, …azimuth_deg 68.34…`
   - `…_0001, same image, "[378.5,506.0,409.0,210.0]",1, …`
   - `…_0002, same image, "[201.7,388.2,211.0,294.0]",1, …`
6. Columns: row_id, image_id, width, height, bbox [x,y,w,h], class_id, world_x/y, azimuth/elevation (deg, sin, cos), angle_valid, cam_pos_source, arrow_u/v. class_id: 0 Lateral_lying_left, 1 Lateral_lying_right, 2 Sitting, 3 Standing, 4 Sternal_lying [CARD]
7. human. "Pigs were annotated with bounding boxes and posture labels" [CARD]. Viewpoint angles are machine-computed (PnP) and should not be used as labels.
8. Group rows by image_id. standing_count = #class_id==3. any_sitting = exists class_id==2. lying = class_id ∈ {0,1,4}.
9. 5 classes. Per-class counts UNVERIFIED. 3,090 train / 3,000 test images (viewer).
10. Multi-pig per image. Use counts or presence, or crop a single bbox.
11. Fisheye overhead cameras distort the view. Unlabelled pigs possible [UNVERIFIED]. No people expected.
12. (a) "Is any pig standing?" yes/no. (b) "How many pigs are lying down?" bins. (c) "Most common posture?" lying / standing / sitting.
Verdict: **USE** (med; check per-image completeness of the labels).

### D32.4 — imageomics/fish-vista
1. https://huggingface.co/datasets/imageomics/fish-vista. 2. **No dataset-level licence on the card**. A per-row `license` column (e.g. "CC BY-NC") [ROW]. 3. open. 4. 11,896 MB; images about 0.1–32 MB each, individually fetchable; CSV configs. 5. [ROW] `{"filename":"INHS_FISH_107832.jpg","family":"Ictaluridae","standardized_species":"noturus nocturnus","license":"CC BY-NC"}`, `{"filename":"INHS_FISH_25132.jpg","family":"Cyprinidae","standardized_species":"notropis atherinoides","license":"CC BY-NC"}`, `{"filename":"INHS_FISH_40481.jpg","family":"Cyprinidae","standardized_species":"notropis texanus","license":"CC BY-NC"}`. 6. filename, family, standardized_species, source, owner, license, trait columns. 7. human (museum curation) [INFERRED]. 8. family/species = columns. 9. 628 train species [CARD]. 10. one fish per image. 11. NC per-image licences; museum specimens, not field catch. 12. family pick-one; "is it a catfish (Ictaluridae)?"; genus pick.
Verdict: **MAYBE** (no top-level licence; mixed NC).

### D32.5 — Francesco/aquarium-qlnqy (Roboflow 100)
1. https://huggingface.co/datasets/Francesco/aquarium-qlnqy. 2. YAML `license: cc` (no version); "Licensing Information: See original homepage" [CARD] → UNVERIFIED exact licence. 3. open. 4. 77.4 MB; `dataset.tar.gz` 38.7 MB, parquet per split (sizes UNVERIFIED). 5. [ROW] id 251: category [4] (puffin); id 253: [4,4,4]; id 102: [2×6] (jellyfish). 6. objects.{bbox, category ∈ aquarium, fish, jellyfish, penguin, puffin, shark, starfish, stingray}. 7. "annotations_creators: crowdsourced… Annotators are Roboflow users" [CARD] → human. 8. majority class. 9. 448/63/127. 10. multi-object; filter single-class images. 11. 640 px; aquarium visitor photos may contain people. 12. which animal; is a shark present; count jellyfish.
Verdict: **MAYBE** (licence version unverified).

### D33.1 — lila-bc-community/channel-islands-camera-traps (rank 1)
1. https://huggingface.co/datasets/lila-bc-community/channel-islands-camera-traps ; source https://lila.science/datasets/channel-islands-camera-traps/ [CARD]
2. "License: Community Data License Agreement — Permissive 1.0" (https://cdla.io/permissive-1-0/) [CARD]
3. open
4. 3,675 MB; 6 shards, smallest 415 MB [CARD]
5. Proof first-rows [ROW]: `{"image_id":"613dd021-…","width":1920,"height":1080,"objects":{"bbox":[[0,543,1773,504]],"category":[1]}}`; `{"image_id":"e8855688-…","objects":{"bbox":[[107,601,678,360]],"category":[1]}}`; `{"image_id":"4398456c-…","objects":{"bbox":[[118,566,527,304]],"category":[1]}}` (1 = fox)
6. objects.bbox [x,y,w,h], objects.category ∈ [bird, fox, other, rodent, skunk], objects.area
7. human (LILA bbox annotations, The Nature Conservancy) [CARD: "Camera-trap images with bounding-box annotations"]. Annotator details UNVERIFIED.
8. species = the unique category if all boxes share it
9. 5 classes; 11,996 images. **No negatives**: "Empty frames… and human labels… are excluded" [CARD]
10. Mostly one species per frame [INFERRED]. Drop mixed frames.
11. Night IR frames. Humans removed for privacy [CARD]. Foxes dominate (class balance UNVERIFIED).
12. "Which animal?" fox/bird/rodent/skunk/other; "Is the animal a fox?" yes/no (within positives only); "How many animals?" 1/2/3+.
Verdict: **USE** for pick-one species. **Not** for "empty vs animal" (33.2 → Gap).

### D33.3 — Project-AgML/tree_species_classification_slovak_normal_cropped (rank 1)
1. https://huggingface.co/datasets/Project-AgML/tree_species_classification_slovak_normal_cropped ; Zenodo https://doi.org/10.5281/zenodo.14228004 [CARD]
2. `license: cc-by-4.0` [CARD]
3. open
4. 2,431 MB; smallest shard 393.7 MB [CARD]
5. [ROW] `{"image":2480x3508,"label":0}` ×3 (European beech)
6. label ClassLabel [European beech, European silver fir, Norway spruce, Sessile oak]
7. human [INFERRED]. "real RGB images of tree species collected in natural field environments… during field surveys in June and August 2022" [CARD]
8. = label
9. beech 300, silver fir 337, Norway spruce 396, sessile oak 334 [ROW]. Balanced.
10. one tree per image ("cropped") [CARD name]
11. Very large images (2480x3508); downscale. Possible near-duplicates of the same tree [INFERRED].
12. species 4-way; "Is this a conifer?" yes/no (fir, spruce); "Is this an oak?" yes/no.
Verdict: **USE** (med-high).

### D33.4 — Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset
1. https://huggingface.co/datasets/Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset. 2. **Conflict**: YAML `license: cc-by-nc-4.0`, but the body says "License: CC BY 4.0" [CARD]. 3. open. 4. 431 MB; per-file PNG about 2 MB, labels about 0 MB. 5. [ROW] `0 0.500619 0.286510 0.087871 0.142327`; `0 0.505569 0.224629 0.132426 0.216584`; `0 0.510520 0.341584 0.048267 0.163366`. 6. YOLO, class 0 (smoke/fire; data.yaml not fetched). 7. **generator** ("100% synthetic… computer-generated by the Simuletic pipeline") [CARD]. 8. smoke present = non-empty label. 9. **Positives only**: 239/239 label files non-empty [ROW, blob listing]. 10. one plume usually. 11. Synthetic look; NC ambiguity. 12. n/a for yes/no.
Verdict: **SKIP** for yes/no (positives-only); MAYBE as a positive pool to mix with D-Fire negatives.

### D34.1 / D34.2 — VincentGOURBIN/ppe-detection (rank 1)
1. https://huggingface.co/datasets/VincentGOURBIN/ppe-detection ; Roboflow https://universe.roboflow.com/vincentspace/ppe-detection-1-cniwr/dataset/2 [ROW data.yaml]
2. YAML `license: cc-by-4.0`; data.yaml `roboflow: license: CC BY 4.0` [CARD]
3. open
4. 174.3 MB, 7,431 files, individually fetchable (images about 0.05 MB, labels under 0.01 MB) [CARD]
5. Proof: raw `valid/labels/*.txt` [ROW]:
   - `12_Group_Group_12_…_101…txt`: `3 0.1796875 0.6703125 0.1890625 0.2984375 / 3 0.371875 0.5640625 …` 
   - `…_198…txt`: `3 0.2609375 0.53125 0.134375 0.5421875 / 3 0.40625 …`
   - `…_29…txt`: `3 0.109375 0.5765625 0.18125 0.4859375 … / 1 0.11…`
6. YOLO; classes `['helmet','no-helmet','no-vest','person','vest']` [ROW data.yaml]
7. human [INFERRED] (Roboflow project annotations). No annotation statement on the card.
8. 34.1: yes iff any line has class 2 (no-vest). 34.2: yes iff any line has class 1 (no-helmet).
9. Valid split (164 images, all fetched): has no-vest 69 / none 95; has no-helmet 31 / none 133 [ROW]. **Real negatives yes.** Train 3,447 / test 101.
10. Multi-person. Image-level "any" questions are clean.
11. **Faces**: filenames "12_Group_Group_…" look like WIDER FACE group photos [INFERRED], so personal data risk. 640x640. Not the Voxel51 hard-hat source.
12. (a) "Is any person without a safety vest?" yes/no. (b) "Is any person without a helmet?" yes/no. (c) "How many people are labelled?" bins (class 3).
Verdict: **USE** (med; origin inferred; face risk flagged).

### D34.2 alt — jhboyo/ppe-dataset
1. https://huggingface.co/datasets/jhboyo/ppe-dataset. 2. `license: mit` [CARD]. The data merges two Kaggle sets: andrewmvd/hard-hat-detection and snehilsanyal/construction-site-safety [CARD]. Upstream licences UNVERIFIED. 3. open. 4. 1,862 MB, 31,005 files. 5. Viewer shows only images [ROW: 416x415, 416x416, 416x415]; label rows not fetched. 6. classes helmet / head / vest [CARD]. 7. human [INFERRED]. 8. no-helmet = any "head". 9. Empty label files: 27+14+8 [ROW]; most images positive. 10. multi. 11. **The hard-hat-workers images are likely the same source as the used Voxel51 hard-hat-detection** [INFERRED]. 416 px. 12. —
Verdict: **SKIP** (duplicate of a used source, no rows pasted).

### D34.3 — keremberke/forklift-object-detection (rank 1)
1. https://huggingface.co/datasets/keremberke/forklift-object-detection ; Roboflow https://universe.roboflow.com/mohamed-traore-2ekkp/forklift-dsitv [CARD]
2. README.dataset.txt "License: CC BY 4.0" [CARD]
3. open
4. 20.4 MB total; `data/train.zip` 13.5 MB (valid/test smaller). Fully under 50 MB [CARD]
5. first-rows full/train [ROW]: `{image_id:278, 500x375, category:[0]}`; `{image_id:76, 450x343, category:[1,0], bbox:[[285,133,19.0,27.0],[5,0,434.9,339.2]]}`; `{image_id:46, 500x500, category:[1,0]}`
6. objects.{id, area, bbox, category ∈ [forklift, person]}
7. human. "exporting images from images.cv… and labeling them as an object detection dataset" [CARD]
8. person-near-forklift = yes iff any category==1 (person) and any category==0
9. 421 images (295/84/42). Negatives = forklift-only images such as image_id 278 [ROW]. Exact count UNVERIFIED.
10. image-level presence is clean
11. Small (about 450–500 px). Web images (images.cv), likely in training data. Operators' faces visible.
12. "Is a person present with the forklift?" yes/no; "How many forklifts?" 1/2/3+; "Is the forklift the largest object (area)?" yes/no.
Verdict: **USE** (med).

### D34.4 — keremberke/construction-safety-object-detection (rank 1)
1. https://huggingface.co/datasets/keremberke/construction-safety-object-detection ; Roboflow https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety [CARD]
2. README.dataset.txt "License: CC BY 4.0" [CARD]
3. open
4. 27.7 MB total; train.zip 22.3 MB [CARD]
5. first-rows full/train [ROW]: image_id 180 (416x416) 64 objects incl. categories 4 (hardhat), 7 (no-mask); image_id 109: [4,4,3,3,12,12,7,7,…]; image_id 242: [4,8,7,9] (hardhat, no-safety vest, no-mask, person)
6. category names: barricade, dumpster, excavators, gloves, hardhat, mask, no-hardhat, no-mask, no-safety vest, person, safety net, safety shoes, safety vest, dump truck, mini-van, truck, wheel loader [ROW]
7. human [INFERRED]. Frames come from YouTube videos and a cloned Roboflow project [CARD]
8. vest missing = any category 8; hat missing = any 6; mask missing = any 7
9. 307/57/34 images. Negatives per item UNVERIFIED (row 109 has no "no-safety vest", so they exist [ROW])
10. multi; image-level presence
11. **416 px** (soft at 1536). YouTube frames. Faces.
12. "Is anyone missing a safety vest?"; "Which item is missing: hardhat / mask / vest / none?" (only when exactly one 'no-' class); "Is heavy machinery present?" (excavators, wheel loader, dump truck).
Verdict: **USE** (med; small images).

### D34.5 — c3rl/seatbelt-detection-v2
1. https://huggingface.co/datasets/c3rl/seatbelt-detection-v2. 2. `license: apache-2.0` (README is YAML only) [CARD]. 3. open. 4. 3,190 MB; PNGs 0.6–2 MB each, in folders `seatbelt/`, `noseatbelt/`. 5. [ROW] `{"image":1024x1024,"label":0}` ×3 (0 = noseatbelt). 6. label ClassLabel [noseatbelt, seatbelt] from the folder name. 7. **UNVERIFIED**. 1024² PNGs with UUID names suggest generated images [INFERRED]. 8. = label. 9. noseatbelt 1,000 / seatbelt 1,500 [ROW]. 10. one. 11. Provenance unknown. Possibly synthetic faces. 12. seat belt yes/no.
Verdict: **MAYBE** (label/image origin undocumented).

### D34.6 / D35.5 — Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection
1. https://huggingface.co/datasets/Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection. 2. "License: CC BY 4.0" [CARD]. 3. open. 4. 171.8 MB; 112 PNGs about 1–2 MB. 5. Viewer shows images only [ROW: 1024x1024 ×3]. Label files not fetched. 6. bbox + 17 keypoints [CARD]. 7. generator ("Fully synthetic") [CARD]. 8. lying = class from label (UNVERIFIED). 9. Folder `laying_dataset` only, so **likely positives-only** [INFERRED]. 10. —. 11. Synthetic. Small. 12. —
Verdict: **SKIP / MAYBE** (no rows, likely positives-only).

### D34.7 — ccclllwww/smoking_classification
apache-2.0 [CARD]; 2,920 images; viewer cannot stream ("Cannot load the dataset split") [ROW]; no label file seen. **SKIP / UNVERIFIED**.

### D35.1 / D35.2 — badsaarow/d-fire (D-Fire mirror) (rank 1 on data, blocked on licence)
1. Mirror https://huggingface.co/datasets/badsaarow/d-fire ; owner https://github.com/gaiasd/DFireDataset [CARD]
2. **No licence** on the HF card, and the GitHub API returns `license: None`. The owner README states no licence. It asks for citation of Venâncio et al. 2022 [CARD]. Treat as UNVERIFIED (all rights reserved by default).
3. Mirror open. Owner downloads are on OneDrive plus a Kaggle copy (no login checked).
4. 4,208 MB; parquet shards up to 492.8 MB; per-image YOLO `train/labels/*.txt` (about 0 MB) are separately fetchable [CARD]
5. first-rows default/train [ROW]: `{"label": "", "filename": "AoF00000.jpg", image 1086x610}`; `{"label": "1 0.2162… 0.7391… 0.1369… 0.1505…", "filename": "AoF00001.jpg"}`; `{"label": "0 0.7672… 0.2889… 0.0368… 0.0546…", "filename": "AoF00002.jpg"}`
6. `label` = raw YOLO text (empty = no fire/smoke); `filename`. Class id mapping 0/1 = smoke/fire is **UNVERIFIED** (not on the fetched README).
7. human [INFERRED] (authors' manual bbox annotation per the paper, UNVERIFIED)
8. fire_or_smoke = label != "". Type = set of class ids.
9. Owner README: only fire 1,164; only smoke 5,867; fire and smoke 4,658; **none 9,838** [CARD]. Mirror label dir: 3,307 empty vs 3,914 non-empty files [ROW]. **Real negatives: yes.**
10. One image-level answer.
11. Surveillance and web images. Some negatives are deliberately confusing (sunsets, lamps) [INFERRED]. Licence is the blocker.
12. fire/smoke yes/no; fire-only / smoke-only / both / neither; "Is there more than one fire region?"
Verdict: **MAYBE** (fails "licence stated"). A human should email GAIA for terms. Strongest negatives in the slice.

### D35.1 alt — Vertex-Test/FireSmokeDataset (rank 2)
1. https://huggingface.co/datasets/Vertex-Test/FireSmokeDataset (identical byte-for-byte file list in `baizhanquan/firesafety-fire-smoke`) [CARD]
2. `license: apache-2.0` (README is YAML only) [CARD]. Upstream Roboflow licences UNVERIFIED.
3. open
4. 381.3 MB, 18,189 files, each ≤0.1 MB [CARD]
5. Proof (mirror `baizhanquan/firesafety-fire-smoke` label viewer) [ROW]: `0 0.20234375 0.7875 0.08671875 0.1265625`; `0 0.0890625 0.6796875 0.0359375 0.028125`; `0 0.15 0.68828125 0.04296875 0.03515625`
6. YOLO; `names: ['fire', 'smoke']` [ROW data.yaml]
7. **UNVERIFIED**. Filenames like `00000-3505762096_png.rf…` look like Stable-Diffusion outputs [INFERRED], so the images may be partly generated. Labels are Roboflow (human) [INFERRED].
8. yes iff the label file is non-empty
9. Empty label files: train 425, valid 39, test 19 (483 negatives vs 8,610 positives) [ROW]
10. image-level
11. **Possible AI-generated images**; low-res 640. Few negatives (5%).
12. same as D-Fire.
Verdict: **MAYBE** (label origin undocumented; few negatives).

### D35.1 alt — seawsurf/fire_smoke_dataset_fasdd_cv
`license: cc-by-4.0` [CARD]; **SINGLE ARCHIVE** `FASDD_CV.zip` 3,410.6 MB; viewer: "No (supported) data files found" [ROW]. **SKIP** (single archive trap).

### D35.3 / D35.4 — Turki-Alshuaibi/haris-weapon-detection-dataset-curated (rank 1)
1. https://huggingface.co/datasets/Turki-Alshuaibi/haris-weapon-detection-dataset-curated
2. `license: cc-by-4.0` (YAML only) [CARD]. Upstream sources include Roboflow exports and **UCF-Crime** (its licence is UNVERIFIED and may be research-only).
3. open
4. 2,683 MB, 23,049 files; individual images and labels [CARD]
5. Proof (label viewer) [ROW]: `0 0.642249 0.448207 0.080718 0.086321`; `0 0.393479 0.528552 0.033081 0.037185`; `0 0.526465 0.466135 0.039697 0.034529`
6. YOLO; data.yaml `names: ['gun','knife']`, with comments listing sources ds_1…ds_9 incl. "ds_9_hardneg: 534 images — UCF-Crime hard negatives (empty labels)" [ROW]
7. human [INFERRED] (merged Roboflow annotations). Not stated.
8. weapon = non-empty label. Type = class set ({0} gun, {1} knife).
9. **Real negatives: yes.** Empty label files 2,072 train + 710 val; non-empty 7,650 + 1,091 [ROW]
10. image-level. Drop images with both classes for the pick-one.
11. CCTV and staged scenes; faces present. UCF-Crime terms. Sensitive content (violence).
12. "Is a weapon visible?" yes/no; "gun / knife / none"; "How many weapons?" 1/2/3+.
Verdict: **USE** (med). Flag the UCF-Crime licence for human check. Consider excluding ds_9 frames if the licence is restrictive.

### D35.3 alt — Subh775/WeaponDetection
cc-by-4.0, a derivative of Roboflow "weapon-detection-m7tpo" [CARD]; 583 MB; smallest validation parquet 74.2 MB; rows [ROW]: `{416x416, category:[19]}` (handgun), `{416x416, category:[25]}` (rifle), `{1024x683, category:[25]}`; 29 messy classes (weapons, Guns, guns, pistol, pistols…). Negatives UNVERIFIED. **MAYBE** (class mess; no negatives verified).

### D35.3 alt — jsalazar/US-Real-time-gun-detection-in-CCTV…
`license: cc-by-nc-4.0`; zips (smallest `Unity/split-500.zip` 68.3 MB > 50 MB); viewer images only [ROW 1920x1080]. **MAYBE** (NC; no label rows).

### D36.1 — dronefreak/PKLot (rank 1)
1. https://huggingface.co/datasets/dronefreak/PKLot ; owner https://web.inf.ufpr.br/vri/databases/parking-lot-database/ ; paper https://doi.org/10.1016/j.eswa.2015.02.009 [CARD]
2. "Unofficial redistribution… under the original CC BY 4.0 license" (`license: cc-by-4.0`) [CARD]
3. open
4. 3,909.7 MB; per-image JPG and YOLO txt; `data/images/train/metadata.jsonl` 15.5 MB holds all train labels [CARD]
5. first-rows default/train [ROW]: `{"file_name":"PUCPR_2012-09-11_15_16_58.jpg","objects":{"bbox":[[278,185,46,45],[310,185,45,48],…+91],"categories":[1,0,1,0,1,1,0,0,…+91]}}`; `PUCPR_2012-09-11_15_27_08.jpg` same layout; `PUCPR_2012-09-11_15_29_29.jpg` same layout
6. file_name; objects.bbox (COCO px); objects.categories int (0 = vacant, 1 = occupied per data.yaml and card) [ROW]
7. human. "Every frame has an XML descriptor marking each parking space and whether it is occupied" [CARD]
8. occupied_frac = mean(categories). "more than half full" = occupied_frac > 0.5. vacant_count = #0.
9. 693,755 labelled spaces; 8,346 / 1,981 / 2,089 images. Both classes are in every frame [ROW/CARD]
10. One answer per image for aggregate questions.
11. Card warns: fixed cameras, near-identical frames, 25,773 unlabelled spaces left as background [CARD]. Cars are far away, so plates are not readable [INFERRED]. 1280x720. Very well known (training overlap likely).
12. (a) "Is the lot more than half full?" yes/no. (b) "About how many spaces are free?" 0–10 / 11–30 / 31–60 / 61+. (c) "Which camera view (PUCPR / UFPR04 / UFPR05)?" from the filename prefix.
Verdict: **USE** (high).

### D36.2 — cute-face/bike-helmet-dataset (COCO part) (rank 1)
1. https://huggingface.co/datasets/cute-face/bike-helmet-dataset
2. `license: cc-by-4.0` (YAML). The README gives CC BY 4.0 for the VOC part and "Unknown / Web Collection" for the Google/harvested folders [CARD]. Use only the root COCO and `helmet_voc` parts.
3. open
4. 773.4 MB; `valid/_annotations.coco.json` (127 images) is small [ROW]
5. Proof (valid COCO JSON) [ROW]: ann `{id:1,image_id:0,category_id:2,bbox:[137,3,84,70]}`; `{id:2,image_id:1,category_id:1,bbox:[144,17,48,105]}`; `{id:3,image_id:1,category_id:1,bbox:[114,52,38,85]}`
6. COCO categories: 0 rider-helmet-bike (super), 1 "With Helmet", 2 "Without Helmet" [ROW]
7. human [INFERRED] (Roboflow export)
8. all helmeted = no annotation with category 2
9. Valid: only-with 74, only-without 38, both 15 [ROW]. **Negatives yes.**
10. Pick images with a single category for clean pick-one.
11. **416 px**; rider faces. The viewer's `label` column is the split name, not a label (do not use it).
12. "Is every rider wearing a helmet?"; "How many riders without helmet?"; "with / without / mixed".
Verdict: **USE** (med; small images).

### D36.3 — Francesco/vehicles-q0x2v
1. https://huggingface.co/datasets/Francesco/vehicles-q0x2v. 2. YAML `license: cc`, "See original homepage" [CARD] → version UNVERIFIED. 3. open. 4. 440 MB; `dataset.tar.gz` 219.6 MB + parquet per split (sizes UNVERIFIED). 5. [ROW] id 2529: categories [11,5,1,9,5,5]; id 187: [12,10,9,5]; id 1280: [10,10,9,5,10,9]. 6. 13 classes (big bus, big truck, bus-l-, bus-s-, car, mid truck, small bus, small truck, truck-l/m/s/xl) [ROW]. 7. "annotations_creators: crowdsourced… Roboflow users" [CARD]. 8. majority of coarse classes (bus*, truck*, car). 9. 2,634/458/966. 10. multi. 11. Overlapping class taxonomy. 640 px. 12. majority class; any bus?; count trucks.
Verdict: **MAYBE** (licence version).

### D36.4 — dronefreak/LISA-Traffic-Lights
`license: cc-by-nc-sa-4.0` [CARD]; 5,058 MB per-file; rows [ROW]: `dayClip1--00000.jpg` bbox [[349,222,6,16],[423,260,6,13]] categories [0,0]; `--00001` [[349,224,6,13],[423,260,6,13]] [0,0]; `--00002` [[349,220,6,16],[424,259,6,13]] [0,0]. Class names not in the fetched data.yaml (UNVERIFIED). Lights are **6–16 px**. **MAYBE** (NC-SA; tiny objects; class map unverified).

### D36.6 — Voxel51/fisheye8k
Card: "License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0"; "Two researchers/annotators manually labelled over 10,000 frames" [CARD]; labels in `samples.json` 39.4 MB (not fetched); viewer images only [ROW 1240x1088]. **MAYBE** (NC-SA; label rows not pasted).

### D36.5 — GTSRB (tanganke/gtsrb, bazyl/GTSRB GPL-3.0)
Found in search only [CARD tags]. Known tiny crops. Not carded further. → Gap.

### D36.x — emb-ai/traffic-sign-bench
odbl [CARD]; rows are SUMO map scenes (`pdd_code`, `scene_kind`, `net_path`) [ROW], **not photos**. **SKIP** (no image of a sign).

### D37.1 / D37.2 / D37.3 — morzel85/synthetic-medical-document-recognition-benchmark (rank 1)
1. https://huggingface.co/datasets/morzel85/synthetic-medical-document-recognition-benchmark ; files …/tree/main/data/png
2. `license: cc-by-4.0` [CARD]. "intended for software development and benchmarking, not for clinical use" [CARD]
3. open
4. 31,211 MB total; 7,384 PNGs (23,853 MB); smallest PNG 0.08 MB; `data/manifest.json` about 0 MB [CARD]
5. Proof: the generator values are in the filenames (blob listing) and the FHIR JSON [ROW]:
   - `data/png/synthetic_Adam_Hirthe_1ce276e5_clinical_timeline_type_1_p_10_of_13_dpi_300_clear_ver_1.png`
   - `…_clinical_timeline_type_1_p_11_of_13_dpi_300_clear_ver_1.png`
   - `…_clinical_timeline_type_1_p_12_of_13_dpi_300_clear_ver_1.png`
   - manifest: `"file_counts": {"html":150,"pdf":2100,"png":7384,…}` [ROW]; viewer rows: image 2550x3301 ×3 [ROW]
6. Filename grammar [CARD]: `<patient>_<category>_type_<n>[_p_<i>_of_<n>]_dpi_300_<variant>_ver_<k>`. variant tokens: `clear`, `photocopy_{str,rot,mis…}`, `photo_{ske,sta,cli,mis…}`. `cli` = "Clipped: part of the page extends beyond the image boundary"; `ske` = skewed photograph. type_1/2/3 = date style (US numeric / abbreviated month / ISO) [CARD]
7. **generator**. "synthetic… medical records rendered as documents… Every degraded page is derived from its corresponding clear page" [CARD]
8. 37.1 category = filename token before `_type_`. 37.2 capture = clear / photocopy / photo token. 37.3 clipped = `cli` in tokens. Date style = type_n.
9. Categories seen in clear pages: contact_form, contact_info, notes, observation, report, survey, vaccination_history, diagnostic, clinical_timeline, email (per card) [ROW/CARD]. 13 variant configs × 568 rows each [ROW]. Negatives for clipped: the clear/str/ske variants.
10. one answer per page
11. Only **5 synthetic patients**, so templates repeat; "synthetic" watermarks give shortcuts [CARD]. Names are synthetic. Large 300-dpi pages. **"diagnostic" pages contain clinical content**, so ask only admin questions (no diagnosis).
12. (a) "What kind of document is this page?" contact info / observation / vaccination history / survey / notes / report. (b) "How was this page captured?" clean / photocopy / photo. (c) "Which date format does the page use?" 08/24/2026 / Aug 24, 2026 / 2026-08-24.
Verdict: **USE** (high).

### D37.4 — hmnshudhmn24/noisy-medical-document-images-ocr
1. https://huggingface.co/datasets/hmnshudhmn24/noisy-medical-document-images-ocr. 2. **No licence field** [CARD]. 3. open. 4. 316 MB; images 0.19 MB+; `discharge_summaries_ground_truth.csv` 0.7 MB [CARD]. 5. [ROW] viewer `{"image":1654x2339,"label":0}` ×3 (bills); CSV row `med_doc_discharge_summary_200001_noisy.jpg,discharge_summary,"{ "hospital": { "name": "Christian Medical College (CMC)", …`. 6. label ClassLabel [bills, discharge_summaries]; CSV filename, document_type, json_data. 7. generator ("Generated with ReportLab… fully synthetic") [CARD]. 8. = label; hospital name from json. 9. bills 500 / discharge 500 [ROW]. 10. one. 11. Uses **real hospital names** (e.g. CMC) on fake documents. Licence missing. 12. bill?; hospital name pick-one; total-amount bins.
Verdict: **MAYBE** (no licence).

### D37.4 alt — RootCauseAnalytics/synthetic-australian-medical-documents-sample
cc-by-nc-4.0 [CARD]; 23.7 MB; PDFs (render needed); `ground_truth.csv` [ROW]: `1,prescription,AUS-TRN-0001,0001_prescription_DEPRESSION_GAD_Edwards.pdf,…`; `2,pathology_request,AUS-TRN-0002,…`; `3,pathology_report,AUS-TRN-0003,…`; generator [CARD: "every entity is synthetic"]. Doc types: prescription, pathology request/report, physiotherapy assessment, imaging report, referral letter, consent… **MAYBE** (NC; sales sample; carries diagnosis fields, so use only document-type and admin fields).

### D37.x — Ronysalem/medical-forms-dataset
No licence; 8 images; rows contain **real clinical notes** ("RE Cataract DOV") [ROW]. **SKIP** (privacy, diagnosis content).

### D38.1 — twinkle-ai/tw-drug-labels-vision (rank 1)
1. https://huggingface.co/datasets/twinkle-ai/tw-drug-labels-vision ; source TFDA open data (data.gov.tw) [CARD]
2. "**License:** CC BY 4.0" [CARD]
3. open
4. 12,513 MB; parquet shards 147–1,954 MB (smallest `data/train-00007-of-00008.parquet` 147 MB); `sample.json` 0.01 MB [CARD]. The two shard sets (…of-00008 and …of-00018) may overlap; which one the config uses is UNVERIFIED.
5. first-rows [ROW]: `{images:[744x1053,744x1053], license_id:"內衛成製字第000039號", drug_name_en:"RIVANOL SOLUTION 0.2%", dosage_form:"外用液劑", strength:"0.2%", source_type:"leaflet"}`; `{images:[1053x744], license_id:"內衛成製字第000040號", drug_name_en:"Hydrogen Peroxide Solution 3%", strength:"3%", active_ingredients:[{name:"HYDROGEN PEROXIDE", amount:"30mg/ml"}]}`; `{images:[744x1053], license_id:"內衛成製字第000044號", drug_name_en:"Liquor Cresolis Saponatus", strength:"50%"}`
6. images (list of WebP pages, 90 dpi); 17 text fields (license_id, names zh/en, dosage_form, strength, active_ingredients, indications…, package, manufacturer, marketing_holder, `source_type` ∈ {leaflet, carton}, source_urls) [ROW/CARD]
7. **mixed**. `source_type` and `license_id` come from the TFDA registry spreadsheet (human/administrative) [CARD]. The other 16 fields were "抽取" (extracted) from the PDFs with OCR clean-up mentioned, so **machine** [CARD].
8. carton/leaflet = `source_type`. Imported = `license_id` contains "輸" (licence-number convention, [INFERRED]). Do NOT trust dosage_form or strength as Tier A.
9. source_type: leaflet 26,574 / carton 15,630 in the stats sample [ROW]; card says 21,959 cartons of 44,663 [CARD]
10. one record per drug document (multi-page). Use the first page.
11. 90 dpi (about 750x1050). Chinese text. Machine-extracted fields. Public regulatory docs (no PII).
12. (a) "Is this an outer carton or a package leaflet?" (b) "Is this drug imported?" yes/no (from licence prefix). (c) "Which licence-type prefix is printed?" 衛部藥製 / 衛部藥輸 / 內衛成製 / other.
Verdict: **USE for (a)–(c) only** (registry-derived); **MAYBE** for any extracted field. Confidence med.

### D38.2 — LibreYOLO/pills-sxdht (Roboflow 100)
1. https://huggingface.co/datasets/LibreYOLO/pills-sxdht ; Roboflow https://universe.roboflow.com/roboflow-100/pills-sxdht [CARD]
2. "License: CC BY 4.0" (README.dataset.txt and data.yaml) [CARD]
3. open
4. 24.6 MB total, 907 files [CARD]
5. Proof: raw `test/labels/*.txt` [ROW]: `20210702_161114…txt: 7 0.49765625 0.453125 0.13515625 0.1296875`; `20210702_161207…txt: 6 0.47890625 0.53046875 0.18359375 0.21875`; `20210702_161707…txt: 4 0.4875 0.515625 0.1421875 0.221875`
6. names: Cipro 500, Ibuphil 600 mg, Ibuphil Cold 400-60, Xyzall 5mg, blue, pink, red, white [ROW]
7. human [INFERRED] ("Provided by a Roboflow user", RF100) [CARD]
8. product = class name if class ∈ 0–3; colour if 4–7
9. 316/90/45 images; no empty label files (no negatives) [ROW]
10. Single pill per image in the rows seen.
11. **Taxonomy mixes product names and colours**, so a pill gets a colour label OR a product label, never both. Small images (≤0.2 MB).
12. "What colour is this pill?" blue/pink/red/white (only colour-labelled images); "Which product?" 4 names (only product-labelled images); "How many pills?"
Verdict: **USE** (med), restricted to the two clean sub-tasks.

### D38.3 — ApyHTML19/Medication_Boxes_Arabe_Latin (rank 1)
1. https://huggingface.co/datasets/ApyHTML19/Medication_Boxes_Arabe_Latin
2. `license: mit` [CARD]
3. open
4. 91.8 MB; `annotations/instances_val.json` small (<1 MB) [ROW]
5. Proof (instances_val.json) [ROW]: `{id:1,image_id:1,category_id:1,bbox:[287.99,144.8,135.73,71.22],area:9222}`; `{id:2,image_id:2,category_id:1,bbox:[190.62,262.78,147.0,160.43]}`; `{id:12,image_id:7,category_id:1,bbox:[578.15,357.83,212.1,269.43]}`; images have `source`, `original_split`, `original_file`
6. COCO, one category `medicine_box` [ROW]
7. human [INFERRED]. Original annotations were "YLO-seg 4-point polygons" and "COCO polygons (24 drug classes merged)" [CARD]
8. count = #annotations per image_id
9. 676 images / 1,027 instances (train 540/806, val 68/121, test 68/100) [CARD]. Every image has at least 1 box (no zero-count images).
10. count question
11. Arabic/French text. Real product boxes. 640 px and up.
12. "How many medicine boxes?" 1/2/3/4+; "Is more than one box shown?" yes/no; "Which source: Arabic-French or medicine_packv2?" (from `source`).
Verdict: **USE** (med).

### D38.4 — Pjshana/pill-reference-images
No licence [CARD]; 4,392 JPGs 1024x896 [ROW]. The only "label" is the NDC in the filename (e.g. `00002-3228-30_RXNAVIMAGE10_391E1C80.jpg`) [ROW]. Shape/colour needs an external NLM RxNav lookup. **MAYBE** (no licence; labels external; NLM RxImage is a US government source, terms UNVERIFIED).

### D38.x — wony98/healtheat-pill-yolo
apache-2.0 on the card, but "원본 데이터는 AI Hub / 코드잇 Kaggle 출처이므로 해당 약관 함께 따름" (original AI Hub / Kaggle terms also apply) [CARD]. AI Hub normally requires an account, so **GATED** (upstream terms). Rows [ROW]: `0 0.251537 0.752344 0.296107 0.231250`; `1 0.750512 0.716016 0.314549 0.238281`; `4 0.740779 0.256641 0.299180 0.342969`.

### D38.5 — ABINSHA/blister_data
No licence, no README, image-only rows (343x165, 40x159) [ROW]. **SKIP**.

### D39.1 / D39.2 — timm/oxford-iiit-pet (rank 1)
1. https://huggingface.co/datasets/timm/oxford-iiit-pet ; original (Parkhi et al. 2012) [PAPER, UNVERIFIED link]
2. `license: cc-by-sa-4.0` [CARD]
3. open
4. 790.3 MB; train parquet 377.6 MB, test 412.7 MB [CARD]
5. first-rows [ROW]: `{"image":389x500,"label":20,"image_id":"Maine_Coon_204","label_cat_dog":0}`; `{"image":333x500,"label":1,"image_id":"american_bulldog_138","label_cat_dog":1}`; `{"image":500x375,"label":18,"image_id":"keeshond_112","label_cat_dog":1}`
6. label (37 breeds), image_id, label_cat_dog [cat, dog] [ROW]
7. human [INFERRED/PAPER, UNVERIFIED quote]
8. cat/dog = label_cat_dog; breed = label
9. Train: cat 1,188 / dog 2,492; about 100 per breed (bombay 96, egyptian_mau 93, …) [ROW]
10. one pet per image (mostly)
11. About 500 px (moderate). **Very likely in model training data.** Owners sometimes appear in the photo.
12. cat or dog; breed 4-way (same-species distractors); "Is this a long-haired cat breed (persian, maine_coon, birman, ragdoll)?" yes/no.
Verdict: **USE** (high). Note the overlap risk.

### D39.1 alt — microsoft/cats_vs_dogs
YAML `license: unknown` [CARD]; 721.7 MB; rows [ROW] `{500x375, labels:0}`, `{300x281, 0}`, `{489x500, 0}`; cat 11,741 / dog 11,669 [ROW]; "crowdsourced" (Asirra/Petfinder) [CARD]. **MAYBE** (licence unknown).

### D39.3 — Voxel51/StanfordDogs
"License: [More Information Needed]" [CARD]; labels in `samples.json` 7.0 MB (not parsed); viewer images only [ROW 333x500, 395x495, 500x298]. **MAYBE** (no licence; ImageNet-derived).

### D40.1 — sosiklab/NES-plankton-classifier-2022-dataset
1. https://huggingface.co/datasets/sosiklab/NES-plankton-classifier-2022-dataset. 2. "licensed under CC BY 4.0" [CARD]. 3. open. 4. 1,576 MB; shards up to 232.7 MB. 5. [ROW] `{"image":88x42,"label":0,"ifcb_roi_pid":"D20130825T135636_IFCB010_02229","classname":"Acanthoica_quattrospina"}`, `{96x50, …_IFCB010_01325, Acanthoica_quattrospina}`, `{88x68, …_IFCB101_01006, Acanthoica_quattrospina}`. 6. image, label, ifcb_roi_pid, classname. 7. human. "annotations_creators: expert-generated… human-verified using the IFCB Annotate tool" [CARD]. 8. = classname; HAB yes iff classname startswith "Alexandrium"/"Dinophysis"/"Pseudo-nitzschia" [INFERRED]. 9. e.g. Alexandrium_catenella 255, Guinardia_delicatula 1,600, detritus_transparent 609 [ROW]. 10. one cell per image. 11. **Tiny images (about 40–100 px): trap.** 12. —
Verdict: **SKIP** for this bench (tiny). An excellent label source otherwise.

### D40.1 alt — bloombio/phytoplankton-microscopy
cc-by-4.0, DOI 10.57967/hf/9967; "43 phytoplankton species across 10,433 high-resolution light microscopy images with bounding box annotations" [CARD]; 42,152 MB; smallest shard 42.7 MB (detection). `/first-rows` for config `classification` returned "Not found" [ROW error], so **no rows pasted**. **MAYBE / UNVERIFIED**. Next step: range-read the 42.7 MB detection shard footer.

### D40.2 / D40.3 — imageomics/2018-NEON-beetles (rank 1)
1. https://huggingface.co/datasets/imageomics/2018-NEON-beetles ; NEON https://www.neonscience.org/ [CARD]
2. `license: cc-by-sa-4.0` [CARD]
3. open
4. 5,866 MB; `BeetleMeasurements.csv` 19.5 MB; individual PNGs and group JPGs separately fetchable [CARD]
5. first-rows individual_specimens [ROW]: `{"image":128x207,"NEON_sampleID":"SERC_010.20180523.CHLAES.01","scientificName":"Chlaenius aestivus","siteID":"SERC","plotID":"SERC_010","individualImageFilePath":"individual_specimens/part_000/A00000001831_specimen_1.png","groupImageFilePath":"group_images/A00000001831.jpg"}`; same with `_specimen_10` (144x201); same with `_specimen_11` (123x195)
6. NEON_sampleID, scientificName, siteID, site_name, plotID, individualImageFilePath, groupImageFilePath
7. human. Group images were annotated in Notes from Nature ("group_images_resized… used for annotation in Notes from Nature") [CARD]. Species ID is from NEON taxonomists [INFERRED].
8. 40.2 tray count = number of individual_specimens rows sharing groupImageFilePath (e.g. A00000051605.jpg → 142; A00000046075.jpg → 1) [ROW stats]. 40.3 genus = first word of scientificName.
9. 577 group images; 11,654 individual specimens. Species e.g. Synuchus impunctatus 1,172, Pterostichus melanarius 364, Chlaenius aestivus 342 [ROW]. "Each image contains a collection of beetles of the same species" [CARD], so one species per tray.
10. Group image = one species and one count. Individual crops are **tiny (about 130x200 px)**, so use group images only.
11. Count completeness assumes every beetle was cropped [UNVERIFIED]. Ethanol-preserved specimens. No people.
12. (a) "How many beetles are in this tray?" bins. (b) "Which genus?" Pterostichus / Synuchus / Chlaenius / Carabus / Amara. (c) "Was this collected at a forest site?" No: site type needs an external map. Use "Are there more than 20 beetles?" yes/no instead.
Verdict: **USE** (med) for group-image count and genus.

### D40.4 — rotsl/colony-cfu-counting-coco
HF API `gated: manual`; datasets-server "not accessible without authentication" [ROW]. MIT on the card. **GATED**. A human must request access on https://huggingface.co/datasets/rotsl/colony-cfu-counting-coco.

### D40.5 — Etiiir/Pollen
cc-by-nc-4.0 [CARD]; rows are camera intrinsics/pose text (`131.250000 64.000000 64.000000 0.`) [ROW]; multi-view renders, 64 px. **SKIP**.

---

## 3. CSV

```csv
domain,task_id,task,dataset,landing_url,repo_id,licence,licence_quote_url,access,total_mb,smallest_fetch_mb,single_archive,sample_proof_url,rows_pasted,label_origin,answer_rule,has_negatives,classes,one_answer_per_image,personal_data_risk,verdict,confidence,unverified_fields
31,D31.1,crop healthy?,CCMT crop pest/disease (AgML),https://huggingface.co/datasets/Project-AgML/crop_pest_disease_classification,Project-AgML/crop_pest_disease_classification,CC-BY-4.0,https://huggingface.co/datasets/Project-AgML/crop_pest_disease_classification,open,8427,380,no,https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/crop_pest_disease_classification&config=raw&split=train,yes,human(inferred),yes iff label==healthy,yes (3235 healthy),18 labels x 4 crops,yes,none,USE,med,label_origin quote; overlap with used leaf-disease set
31,D31.2,seedling species / crop-or-weed,Aarhus plant seedlings,https://huggingface.co/datasets/Project-AgML/plant_seedlings_aarhus,Project-AgML/plant_seedlings_aarhus,CC-BY-SA-4.0,https://huggingface.co/datasets/Project-AgML/plant_seedlings_aarhus,open,1714.5,309.4,no,https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/plant_seedlings_aarhus&config=default&split=train,yes,human(inferred),label; crop iff in {maize;common_wheat;sugar_beet},yes (973 crop vs 4566 weed),12 species,yes,none,USE,med,label_origin quote
31,D31.3,oil palm FFB ripeness,Outdoor Tenera FFB (AgML),https://huggingface.co/datasets/Project-AgML/oil_palm_fruit_ripeness_classification,Project-AgML/oil_palm_fruit_ripeness_classification,CC-BY-4.0,https://huggingface.co/datasets/Project-AgML/oil_palm_fruit_ripeness_classification,open,1165.7,182.4,no,https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/oil_palm_fruit_ripeness_classification&config=default&split=train,yes,human(inferred),label,n/a (pick-one),Damaged15/Empty12/Overripe74/Ripe201/Unripe164,yes,none,USE,med,label_origin quote
31,D31.4,weed count maize field,Maize-Weed (AgML),https://huggingface.co/datasets/Project-AgML/maize_weed_detection,Project-AgML/maize_weed_detection,CC-BY-4.0,https://huggingface.co/datasets/Project-AgML/maize_weed_detection,open,817,402.3,no,https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/maize_weed_detection&config=default&split=train,yes,human(inferred),count(categories==1),UNVERIFIED,maize;weed,count only,none,MAYBE,med,zero-weed images; origin
31,D31.5,banana/mango ripe,fruit-ripeness-detection,https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset,darthraider/fruit-ripeness-detection-dataset,Apache-2.0 (yaml only),https://huggingface.co/datasets/darthraider/fruit-ripeness-detection-dataset,open,390.9,35.5,no,https://datasets-server.huggingface.co/first-rows?dataset=darthraider/fruit-ripeness-detection-dataset&config=default&split=train,yes,UNVERIFIED,label startswith Ripe,yes,4,yes,none,MAYBE,low,label origin; provenance
31,D31.6,insect pest species,insect-pest-dataset,https://huggingface.co/datasets/EnmmmmOvO/insect-pest-dataset,EnmmmmOvO/insect-pest-dataset,MIT,https://huggingface.co/datasets/EnmmmmOvO/insect-pest-dataset,open,3188,299.4,no,https://datasets-server.huggingface.co/first-rows?dataset=EnmmmmOvO/insect-pest-dataset&config=default&split=train,yes,UNVERIFIED,needs class-name map,n/a,unnamed ints,yes,none,SKIP,med,class names; origin
31,D31.7,land cover tile,EuroSAT RGB,https://huggingface.co/datasets/timm/eurosat-rgb,timm/eurosat-rgb,MIT,https://huggingface.co/datasets/timm/eurosat-rgb,open,92.1,18.4,no,https://datasets-server.huggingface.co/first-rows?dataset=timm/eurosat-rgb&config=default&split=train,yes,human(inferred),label,n/a,10,yes,none,SKIP,high,tiny 64px
32,D32.1,goats present / majority,Greek sheep & goats drone,https://huggingface.co/datasets/AGRARIAN/greek_sheep_goats_dataset,AGRARIAN/greek_sheep_goats_dataset,Apache-2.0,https://huggingface.co/datasets/AGRARIAN/greek_sheep_goats_dataset,open,3627.7,0.5,no,https://huggingface.co/datasets/AGRARIAN/greek_sheep_goats_dataset/resolve/main/train/labels/0058dd32-DJI_20250224121827_0005_D_2260_6.txt,yes,human,any class0 line => goats,yes (890 empty label files),goat;sheep,presence/count,none,USE,high,overlapping patches
32,D32.2,sheep count drone,Aerial Sheep (Roboflow),https://huggingface.co/datasets/keremberke/aerial-sheep-object-detection,keremberke/aerial-sheep-object-detection,Public Domain,https://huggingface.co/datasets/keremberke/aerial-sheep-object-detection/blob/main/README.dataset.txt,open,451,UNVERIFIED (<393),no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/aerial-sheep-object-detection&config=default&split=train,yes,human(inferred),len(objects.category),UNVERIFIED,sheep,count,none,USE,med,3x augmented copies; valid zip size
32,D32.3,pig posture counts,Viewpoint-aware pig posture,https://huggingface.co/datasets/anilbhujel/viewpoint-aware-pig-posture-recognition,anilbhujel/viewpoint-aware-pig-posture-recognition,CC-BY-4.0,https://huggingface.co/datasets/anilbhujel/viewpoint-aware-pig-posture-recognition,open,1356.9,0.08,no,https://huggingface.co/datasets/anilbhujel/viewpoint-aware-pig-posture-recognition/resolve/main/viewpoint_aware_pig_posture_recognition/seenVP_test.csv,yes,human,group by image_id; count class_id,yes (per class),5 postures,count/presence,none,USE,med,per-class counts; label completeness
32,D32.4,fish family/species,Fish-Vista,https://huggingface.co/datasets/imageomics/fish-vista,imageomics/fish-vista,none at dataset level (per-row e.g. CC BY-NC),https://huggingface.co/datasets/imageomics/fish-vista,open,11895.9,0.1,no,https://datasets-server.huggingface.co/first-rows?dataset=imageomics/fish-vista&config=species_classification&split=train,yes,human(inferred),family/standardized_species,n/a,628+ species,yes,none,MAYBE,med,dataset licence
32,D32.5,aquarium animal type,RF100 aquarium,https://huggingface.co/datasets/Francesco/aquarium-qlnqy,Francesco/aquarium-qlnqy,cc (version unstated),https://huggingface.co/datasets/Francesco/aquarium-qlnqy,open,77.4,38.7,no,https://datasets-server.huggingface.co/first-rows?dataset=Francesco/aquarium-qlnqy&config=default&split=train,yes,human (crowdsourced),majority category,n/a,8,filter single-class,low (visitors),MAYBE,med,licence version
33,D33.1,camera-trap species,Channel Islands camera traps (LILA subset),https://huggingface.co/datasets/lila-bc-community/channel-islands-camera-traps,lila-bc-community/channel-islands-camera-traps,CDLA-Permissive-1.0,https://huggingface.co/datasets/lila-bc-community/channel-islands-camera-traps,open,3675.4,415.2,no,https://datasets-server.huggingface.co/first-rows?dataset=lila-bc-community/channel-islands-camera-traps&config=default&split=train,yes,human,unique objects.category,no (empties removed),bird;fox;other;rodent;skunk,mostly,low (humans removed),USE,high,class balance
33,D33.3,tree species,Slovak tree species (AgML),https://huggingface.co/datasets/Project-AgML/tree_species_classification_slovak_normal_cropped,Project-AgML/tree_species_classification_slovak_normal_cropped,CC-BY-4.0,https://huggingface.co/datasets/Project-AgML/tree_species_classification_slovak_normal_cropped,open,2430.9,393.7,no,https://datasets-server.huggingface.co/first-rows?dataset=Project-AgML/tree_species_classification_slovak_normal_cropped&config=default&split=train,yes,human(inferred),label,n/a,beech300/fir337/spruce396/oak334,yes,none,USE,med,label_origin quote
33,D33.4,wildfire smoke yes/no,Simuletic long-distance wildfire,https://huggingface.co/datasets/Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset,Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset,CC-BY-NC-4.0 (yaml) vs CC BY 4.0 (text),https://huggingface.co/datasets/Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset,open,431.3,2.3,no,https://datasets-server.huggingface.co/first-rows?dataset=Simuletic/Long_Distance_Wildfire_Smoke_Detection_Dataset&config=default&split=train,yes,generator,non-empty label,no (239/239 positive),smoke,yes,none,SKIP,high,licence conflict
34,D34.1,no safety vest,PPE detection (VincentGOURBIN),https://huggingface.co/datasets/VincentGOURBIN/ppe-detection,VincentGOURBIN/ppe-detection,CC-BY-4.0,https://huggingface.co/datasets/VincentGOURBIN/ppe-detection/blob/main/data.yaml,open,174.3,0.05,no,https://huggingface.co/datasets/VincentGOURBIN/ppe-detection/tree/main/valid/labels,yes,human(inferred),any class2 (no-vest),yes (95/164 valid without),helmet;no-helmet;no-vest;person;vest,yes (image-level any),high (faces; WIDER-like group photos),USE,med,label_origin quote
34,D34.2,no helmet,PPE detection (VincentGOURBIN),https://huggingface.co/datasets/VincentGOURBIN/ppe-detection,VincentGOURBIN/ppe-detection,CC-BY-4.0,https://huggingface.co/datasets/VincentGOURBIN/ppe-detection/blob/main/data.yaml,open,174.3,0.05,no,https://huggingface.co/datasets/VincentGOURBIN/ppe-detection/tree/main/valid/labels,yes,human(inferred),any class1 (no-helmet),yes (133/164 valid without),same,yes,high (faces),USE,med,label_origin quote
34,D34.2b,no helmet (merged Kaggle),ppe-dataset (jhboyo),https://huggingface.co/datasets/jhboyo/ppe-dataset,jhboyo/ppe-dataset,MIT (upstream unverified),https://huggingface.co/datasets/jhboyo/ppe-dataset,open,1862,0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=jhboyo/ppe-dataset&config=default&split=train,no,human(inferred),any 'head',few (49 empty),helmet;head;vest,yes,med (faces),SKIP,med,dup of used hard-hat source; no label rows
34,D34.3,person with forklift,Forklift (Roboflow),https://huggingface.co/datasets/keremberke/forklift-object-detection,keremberke/forklift-object-detection,CC-BY-4.0,https://huggingface.co/datasets/keremberke/forklift-object-detection/blob/main/README.dataset.txt,open,20.4,13.5,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/forklift-object-detection&config=full&split=train,yes,human,any person and any forklift,yes (forklift-only images),forklift;person,yes,med (operators),USE,med,negative count
34,D34.4,construction PPE missing,Construction Site Safety (Roboflow),https://huggingface.co/datasets/keremberke/construction-safety-object-detection,keremberke/construction-safety-object-detection,CC-BY-4.0,https://huggingface.co/datasets/keremberke/construction-safety-object-detection/blob/main/README.dataset.txt,open,27.7,22.3,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/construction-safety-object-detection&config=full&split=train,yes,human(inferred),any no-* class,yes (per item),17,yes (image-level),med (faces; YouTube),USE,med,416px; per-item negative counts
34,D34.5,seat belt worn,seatbelt-detection-v2,https://huggingface.co/datasets/c3rl/seatbelt-detection-v2,c3rl/seatbelt-detection-v2,Apache-2.0 (yaml only),https://huggingface.co/datasets/c3rl/seatbelt-detection-v2,open,3190.3,0.61,no,https://datasets-server.huggingface.co/first-rows?dataset=c3rl/seatbelt-detection-v2&config=default&split=train,yes,UNVERIFIED (likely generated),label,yes (1000 no/1500 yes),2,yes,med (faces),MAYBE,low,image+label origin
34,D34.6,person lying,Simuletic CCTV fall,https://huggingface.co/datasets/Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection,Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection,CC-BY-4.0,https://huggingface.co/datasets/Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection,open,171.8,1.0,no,https://datasets-server.huggingface.co/first-rows?dataset=Simuletic/CCTV_Incident_Dataset_Fall_Lying_Down_Detection&config=default&split=train,no,generator,UNVERIFIED,likely no,laying,UNVERIFIED,none (synthetic),SKIP,med,label rows; negatives
34,D34.7,smoking,smoking_classification,https://huggingface.co/datasets/ccclllwww/smoking_classification,ccclllwww/smoking_classification,Apache-2.0,https://huggingface.co/datasets/ccclllwww/smoking_classification,open,1106.5,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=ccclllwww/smoking_classification&config=default&split=train,no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,high (faces),SKIP,low,labels
35,D35.1,fire or smoke yes/no,D-Fire (mirror),https://github.com/gaiasd/DFireDataset,badsaarow/d-fire,NONE STATED,https://github.com/gaiasd/DFireDataset,open (mirror),4208.1,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=badsaarow/d-fire&config=default&split=train,yes,human(inferred),label != '',yes (9838 none per owner),fire;smoke (id map unverified),yes,low,MAYBE,med,licence; class id map
35,D35.1b,fire or smoke yes/no,FireSmokeDataset (Vertex-Test),https://huggingface.co/datasets/Vertex-Test/FireSmokeDataset,Vertex-Test/FireSmokeDataset,Apache-2.0 (yaml only),https://huggingface.co/datasets/Vertex-Test/FireSmokeDataset,open,381.3,0.1,no,https://datasets-server.huggingface.co/first-rows?dataset=baizhanquan/firesafety-fire-smoke&config=default&split=train,yes,UNVERIFIED (Roboflow; some SD images),non-empty label,yes (483 empty),fire;smoke,yes,low,MAYBE,low,label/image origin
35,D35.1c,fire or smoke yes/no,FASDD_CV,https://huggingface.co/datasets/seawsurf/fire_smoke_dataset_fasdd_cv,seawsurf/fire_smoke_dataset_fasdd_cv,CC-BY-4.0,https://huggingface.co/datasets/seawsurf/fire_smoke_dataset_fasdd_cv,open,3410.6,3410.6,yes,https://datasets-server.huggingface.co/splits?dataset=seawsurf/fire_smoke_dataset_fasdd_cv,no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,low,SKIP,high,single archive
35,D35.3,weapon visible / gun vs knife,HARIS weapon detection curated,https://huggingface.co/datasets/Turki-Alshuaibi/haris-weapon-detection-dataset-curated,Turki-Alshuaibi/haris-weapon-detection-dataset-curated,CC-BY-4.0 (UCF-Crime upstream unverified),https://huggingface.co/datasets/Turki-Alshuaibi/haris-weapon-detection-dataset-curated,open,2683.2,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=Turki-Alshuaibi/haris-weapon-detection-dataset-curated&config=default&split=train,yes,human(inferred),non-empty label; class set,yes (2782 empty),gun;knife,yes,high (faces; violence),USE,med,upstream licences; origin quote
35,D35.3b,weapon type,WeaponDetection (Subh775),https://huggingface.co/datasets/Subh775/WeaponDetection,Subh775/WeaponDetection,CC-BY-4.0,https://huggingface.co/datasets/Subh775/WeaponDetection,open,583,74.2,no,https://datasets-server.huggingface.co/first-rows?dataset=Subh775/WeaponDetection&config=default&split=train,yes,human(inferred),category lookup,UNVERIFIED,29 messy,mostly,med,MAYBE,low,negatives; class merge
35,D35.3c,gun in CCTV,US Real-time gun detection CCTV,https://huggingface.co/datasets/jsalazar/US-Real-time-gun-detection-in-CCTV-An-open-problem-dataset,jsalazar/US-Real-time-gun-detection-in-CCTV-An-open-problem-dataset,CC-BY-NC-4.0,https://huggingface.co/datasets/jsalazar/US-Real-time-gun-detection-in-CCTV-An-open-problem-dataset,open,2718,68.3,no,https://datasets-server.huggingface.co/first-rows?dataset=jsalazar/US-Real-time-gun-detection-in-CCTV-An-open-problem-dataset&config=default&split=train,no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,high,MAYBE,low,labels; NC
36,D36.1,parking lot occupancy,PKLot (redistribution),https://web.inf.ufpr.br/vri/databases/parking-lot-database/,dronefreak/PKLot,CC-BY-4.0,https://huggingface.co/datasets/dronefreak/PKLot,open,3909.7,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=dronefreak/PKLot&config=default&split=train,yes,human,mean(categories)>0.5 etc.,yes (both classes every frame),vacant;occupied,yes (aggregate),low (distant cars),USE,high,none
36,D36.2,rider helmet,Bike helmet (cute-face COCO),https://huggingface.co/datasets/cute-face/bike-helmet-dataset,cute-face/bike-helmet-dataset,CC-BY-4.0 (COCO/VOC parts only),https://huggingface.co/datasets/cute-face/bike-helmet-dataset,open,773.4,0.1,no,https://huggingface.co/datasets/cute-face/bike-helmet-dataset/resolve/main/valid/_annotations.coco.json,yes,human(inferred),no category 2 => all helmeted,yes (74/127 valid all-helmeted),With Helmet;Without Helmet,mostly (15/127 mixed),med (faces),USE,med,416px; origin quote
36,D36.3,vehicle class,RF100 vehicles,https://huggingface.co/datasets/Francesco/vehicles-q0x2v,Francesco/vehicles-q0x2v,cc (version unstated),https://huggingface.co/datasets/Francesco/vehicles-q0x2v,open,440.4,UNVERIFIED,no,https://datasets-server.huggingface.co/first-rows?dataset=Francesco/vehicles-q0x2v&config=default&split=train,yes,human (crowdsourced),majority coarse class,n/a,13,no (multi),low,MAYBE,med,licence version
36,D36.4,traffic light state,LISA traffic lights,https://huggingface.co/datasets/dronefreak/LISA-Traffic-Lights,dronefreak/LISA-Traffic-Lights,CC-BY-NC-SA-4.0,https://huggingface.co/datasets/dronefreak/LISA-Traffic-Lights,open,5057.8,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=dronefreak/LISA-Traffic-Lights&config=default&split=train,yes,human,category lookup,UNVERIFIED,UNVERIFIED names,multi,low,MAYBE,low,class names; NC; tiny objects
36,D36.6,road-user count fisheye,FishEye8K (Voxel51),https://huggingface.co/datasets/Voxel51/fisheye8k,Voxel51/fisheye8k,CC-BY-NC-SA-4.0,https://huggingface.co/datasets/Voxel51/fisheye8k,open,14415.4,39.4,no,https://datasets-server.huggingface.co/first-rows?dataset=Voxel51/fisheye8k&config=default&split=train,no,human,count by class,UNVERIFIED,UNVERIFIED,multi,low,MAYBE,low,labels not pasted; NC
36,D36.x,traffic sign (map scenes),traffic-sign-bench,https://huggingface.co/datasets/emb-ai/traffic-sign-bench,emb-ai/traffic-sign-bench,ODbL,https://huggingface.co/datasets/emb-ai/traffic-sign-bench,open,626.7,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=emb-ai/traffic-sign-bench&config=catalog&split=train,yes,generator,n/a (map not photo),n/a,25 signs,n/a,none,SKIP,high,not a sign photo
37,D37.1,medical page document type,Synthetic Medical Document Recognition Benchmark,https://huggingface.co/datasets/morzel85/synthetic-medical-document-recognition-benchmark,morzel85/synthetic-medical-document-recognition-benchmark,CC-BY-4.0,https://huggingface.co/datasets/morzel85/synthetic-medical-document-recognition-benchmark,open,31211.3,0.08,no,https://huggingface.co/api/datasets/morzel85/synthetic-medical-document-recognition-benchmark?blobs=true,yes,generator,filename category token,n/a,~10 categories,yes,none (synthetic),USE,high,none
37,D37.2,capture type / clipped,Synthetic Medical Document Recognition Benchmark,https://huggingface.co/datasets/morzel85/synthetic-medical-document-recognition-benchmark,morzel85/synthetic-medical-document-recognition-benchmark,CC-BY-4.0,https://huggingface.co/datasets/morzel85/synthetic-medical-document-recognition-benchmark,open,31211.3,0.08,no,https://huggingface.co/api/datasets/morzel85/synthetic-medical-document-recognition-benchmark?blobs=true,yes,generator,variant token (clear/photocopy/photo; cli),yes,13 variants,yes,none,USE,high,none
37,D37.4,bill vs discharge summary,noisy medical document images,https://huggingface.co/datasets/hmnshudhmn24/noisy-medical-document-images-ocr,hmnshudhmn24/noisy-medical-document-images-ocr,NONE STATED,https://huggingface.co/datasets/hmnshudhmn24/noisy-medical-document-images-ocr,open,316.2,0.19,no,https://datasets-server.huggingface.co/first-rows?dataset=hmnshudhmn24/noisy-medical-document-images-ocr&config=default&split=train,yes,generator,label,yes (500/500),bills;discharge_summaries,yes,low (real hospital names),MAYBE,med,licence
37,D37.4b,medical doc type (AU),synthetic Australian medical docs sample,https://huggingface.co/datasets/RootCauseAnalytics/synthetic-australian-medical-documents-sample,RootCauseAnalytics/synthetic-australian-medical-documents-sample,CC-BY-NC-4.0,https://huggingface.co/datasets/RootCauseAnalytics/synthetic-australian-medical-documents-sample,open,23.7,0.004,no,https://huggingface.co/datasets/RootCauseAnalytics/synthetic-australian-medical-documents-sample/resolve/main/ground_truth.csv,yes,generator,document_type column,n/a,~10 doc types,yes,none (synthetic),MAYBE,med,NC; PDF render step
38,D38.1,carton vs leaflet / imported,TW drug labels vision (TFDA),https://huggingface.co/datasets/twinkle-ai/tw-drug-labels-vision,twinkle-ai/tw-drug-labels-vision,CC-BY-4.0,https://huggingface.co/datasets/twinkle-ai/tw-drug-labels-vision,open,12512.9,147,no,https://datasets-server.huggingface.co/first-rows?dataset=twinkle-ai/tw-drug-labels-vision&config=default&split=train,yes,mixed (registry human; text fields machine),source_type; license_id contains 輸,yes,carton;leaflet,yes,none,USE,med,shard-set duplication; import-prefix rule
38,D38.2,pill product / colour,RF100 pills,https://huggingface.co/datasets/LibreYOLO/pills-sxdht,LibreYOLO/pills-sxdht,CC-BY-4.0,https://huggingface.co/datasets/LibreYOLO/pills-sxdht/blob/main/data.yaml,open,24.6,0.001,no,https://huggingface.co/datasets/LibreYOLO/pills-sxdht/tree/main/test/labels,yes,human(inferred),class name lookup,n/a,4 products + 4 colours,yes,none,USE,med,origin quote
38,D38.3,count medicine boxes,Medication Boxes Arabic/Latin,https://huggingface.co/datasets/ApyHTML19/Medication_Boxes_Arabe_Latin,ApyHTML19/Medication_Boxes_Arabe_Latin,MIT,https://huggingface.co/datasets/ApyHTML19/Medication_Boxes_Arabe_Latin,open,91.8,0.5,no,https://huggingface.co/datasets/ApyHTML19/Medication_Boxes_Arabe_Latin/resolve/main/annotations/instances_val.json,yes,human(inferred),count annotations per image,no zero-box images,medicine_box,yes,low,USE,med,origin quote
38,D38.4,pill reference,pill-reference-images,https://huggingface.co/datasets/Pjshana/pill-reference-images,Pjshana/pill-reference-images,NONE STATED,https://huggingface.co/datasets/Pjshana/pill-reference-images,open,1023.9,0.17,no,https://datasets-server.huggingface.co/first-rows?dataset=Pjshana/pill-reference-images&config=default&split=train,no,external (NDC lookup),needs RxNav lookup,n/a,NDC,yes,none,MAYBE,low,licence; labels
38,D38.x,pill detection (KR),healtheat-pill-yolo,https://huggingface.co/datasets/wony98/healtheat-pill-yolo,wony98/healtheat-pill-yolo,Apache-2.0 + AI Hub terms,https://huggingface.co/datasets/wony98/healtheat-pill-yolo,login (upstream AI Hub),18793,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=wony98/healtheat-pill-yolo&config=default&split=train,yes,human(inferred),class lookup,UNVERIFIED,UNVERIFIED,multi,none,GATED,low,upstream terms
38,D38.5,blister,blister_data,https://huggingface.co/datasets/ABINSHA/blister_data,ABINSHA/blister_data,NONE STATED,https://huggingface.co/datasets/ABINSHA/blister_data,open,39.3,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=ABINSHA/blister_data&config=default&split=train,no,UNVERIFIED,n/a,n/a,n/a,n/a,none,SKIP,high,everything
39,D39.1,cat or dog / breed,Oxford-IIIT Pet (timm),https://huggingface.co/datasets/timm/oxford-iiit-pet,timm/oxford-iiit-pet,CC-BY-SA-4.0,https://huggingface.co/datasets/timm/oxford-iiit-pet,open,790.3,377.6,no,https://datasets-server.huggingface.co/first-rows?dataset=timm/oxford-iiit-pet&config=default&split=train,yes,human(paper),label_cat_dog; label,n/a (both classes),37 breeds; cat1188/dog2492,yes,low (owners),USE,high,label_origin quote
39,D39.1b,cat or dog,cats_vs_dogs (Asirra),https://huggingface.co/datasets/microsoft/cats_vs_dogs,microsoft/cats_vs_dogs,unknown,https://huggingface.co/datasets/microsoft/cats_vs_dogs,open,721.7,330.3,no,https://datasets-server.huggingface.co/first-rows?dataset=microsoft/cats_vs_dogs&config=default&split=train,yes,human (crowdsourced),labels,n/a,cat11741/dog11669,yes,low,MAYBE,med,licence
39,D39.3,dog breed 120,Stanford Dogs (Voxel51),https://huggingface.co/datasets/Voxel51/StanfordDogs,Voxel51/StanfordDogs,NONE STATED,https://huggingface.co/datasets/Voxel51/StanfordDogs,open,789.8,7.0,no,https://datasets-server.huggingface.co/first-rows?dataset=Voxel51/StanfordDogs&config=default&split=train,no,human(ImageNet),samples.json lookup,n/a,120,yes,low,MAYBE,low,licence; label rows
40,D40.1,plankton taxon,NES plankton IFCB,https://huggingface.co/datasets/sosiklab/NES-plankton-classifier-2022-dataset,sosiklab/NES-plankton-classifier-2022-dataset,CC-BY-4.0,https://huggingface.co/datasets/sosiklab/NES-plankton-classifier-2022-dataset,open,1576.4,UNVERIFIED (<232.7),no,https://datasets-server.huggingface.co/first-rows?dataset=sosiklab/NES-plankton-classifier-2022-dataset&config=default&split=train,yes,human (expert),classname,yes (detritus etc.),~100 taxa,yes,none,SKIP,high,tiny 40-100px
40,D40.1b,phytoplankton species,Bloombio phytoplankton microscopy,https://huggingface.co/datasets/bloombio/phytoplankton-microscopy,bloombio/phytoplankton-microscopy,CC-BY-4.0,https://huggingface.co/datasets/bloombio/phytoplankton-microscopy,open,42152.3,42.7,no,https://datasets-server.huggingface.co/first-rows?dataset=bloombio/phytoplankton-microscopy&config=classification&split=validation,no,UNVERIFIED,species column,UNVERIFIED,43 species,UNVERIFIED,none,MAYBE,low,rows; schema; origin
40,D40.2,beetle tray count / genus,NEON 2018 beetles,https://huggingface.co/datasets/imageomics/2018-NEON-beetles,imageomics/2018-NEON-beetles,CC-BY-SA-4.0,https://huggingface.co/datasets/imageomics/2018-NEON-beetles,open,5866.1,19.5,no,https://datasets-server.huggingface.co/first-rows?dataset=imageomics/2018-NEON-beetles&config=individual_specimens&split=train,yes,human,rows per groupImageFilePath; genus=first word,n/a,many species,yes (one species per tray),none,USE,med,count completeness
40,D40.4,colony count,colony-cfu-counting-coco,https://huggingface.co/datasets/rotsl/colony-cfu-counting-coco,rotsl/colony-cfu-counting-coco,MIT,https://huggingface.co/datasets/rotsl/colony-cfu-counting-coco,manual approval,287.1,UNVERIFIED,no,https://datasets-server.huggingface.co/splits?dataset=rotsl/colony-cfu-counting-coco,no,UNVERIFIED,count annotations,UNVERIFIED,UNVERIFIED,UNVERIFIED,none,GATED,low,all labels
40,D40.5,pollen taxon,Pollen (renders),https://huggingface.co/datasets/Etiiir/Pollen,Etiiir/Pollen,CC-BY-NC-4.0,https://huggingface.co/datasets/Etiiir/Pollen,open,211.1,0.001,no,https://datasets-server.huggingface.co/first-rows?dataset=Etiiir/Pollen&config=default&split=train,yes,generator(render),folder name,n/a,many,yes,none,SKIP,med,tiny 64px; NC
```

---

## Part C. Question-expansion recipes (USE candidates)

Rules for every dataset below. Tier C items always carry `label_origin: model` and are scored in a separate column. They are never merged into Tier A/B scores. They count only when a second, different model family independently gives the same answer. The model under test never writes questions. The most useful Tier C outputs are paraphrases of the Tier A question, harder same-category distractors (e.g. look-alike breeds or species), and natural-language variety ("Would a site inspector flag this photo?" mapped back to the Tier A rule).

**Project-AgML/crop_pest_disease_classification (D31.1).** A: healthy yes/no; problem label. B: (1) crop identity from `crop`; (2) "Is the problem caused by an insect (fall armyworm, grasshoper, green mite, leaf beetle, leaf miner) or a disease?" via a fixed lookup; (3) "Which of these problems does NOT occur on {crop}?" from the crop×label co-occurrence table; (4) pairwise "Are these two images the same crop?". C: symptom wording, distractors from the same crop.

**Project-AgML/plant_seedlings_aarhus (D31.2).** A: species. B: (1) crop vs weed; (2) grass-like (black_grass, loose_silkybent, common_wheat, maize) vs broadleaf; (3) "Which of these species is NOT a crop?"; (4) monocot/dicot lookup. C: farmer-style paraphrase ("Should the sprayer hit this plant?").

**Project-AgML/oil_palm_fruit_ripeness_classification (D31.3).** A: grade. B: (1) harvest-ready (Ripe) yes/no; (2) reject at mill (Damaged/Empty) yes/no; (3) "Is it past ripe?" (Overripe) yes/no. C: grader paraphrases.

**AGRARIAN/greek_sheep_goats_dataset (D32.1).** A: goats present; majority. B: (1) total animal count bins; (2) "Are there more than N sheep?"; (3) "Is any animal at the image edge?" (bbox x_c±w/2 near 0 or 1); (4) "Is the largest animal a goat?" (by w·h); (5) empty patch yes/no. C: herder wording.

**keremberke/aerial-sheep-object-detection (D32.2).** A: count. B: (1) >10 yes/no; (2) any sheep touching the edge; (3) largest-sheep quadrant (top-left/…) from bbox centre. C: none needed.

**anilbhujel/viewpoint-aware-pig-posture-recognition (D32.3).** A: posture per bbox; per-image counts. B: (1) any standing; (2) count lying (0,1,4); (3) majority posture; (4) "Are more pigs lying than standing?"; (5) which camera type (turret/orb) from the image_id token. C: welfare-inspector phrasing.

**lila-bc-community/channel-islands-camera-traps (D33.1).** A: species. B: (1) count bins; (2) "Is the animal in the left or right half?" (bbox centre); (3) "Is it a mammal?" (fox/rodent/skunk vs bird); (4) "Does the animal fill more than a quarter of the frame?" (area/(W·H)). C: ranger phrasing; distractor species from the same island list.

**Project-AgML/tree_species_classification_slovak_normal_cropped (D33.3).** A: species. B: (1) conifer vs broadleaf; (2) "Which of these is NOT shown?" (3 absent species plus the true one); (3) genus-level lookup. C: forester paraphrase.

**VincentGOURBIN/ppe-detection (D34.1/34.2).** A: no-vest, no-helmet. B: (1) person count bins (class 3); (2) "Are all helmeted persons also vested?" (count helmet ≥ person and no no-vest); (3) "How many people lack a helmet?"; (4) "Which item is missing: helmet / vest / both / neither?". C: safety-officer wording.

**keremberke/forklift-object-detection (D34.3).** A: person with forklift. B: (1) forklift count; (2) "Is the person closer to the left or right of the forklift?" (centre x); (3) "Is the forklift larger than the person?" (area). C: incident-report phrasing.

**keremberke/construction-safety-object-detection (D34.4).** A: per-item missing. B: (1) machinery present (excavators, wheel loader, dump truck); (2) count persons; (3) "Which of these is NOT present: barricade / dumpster / safety net / gloves?"; (4) more hardhats than no-hardhats?. C: inspector wording.

**Turki-Alshuaibi/haris-weapon-detection-dataset-curated (D35.3).** A: weapon yes/no; gun/knife. B: (1) weapon count; (2) "Is the weapon in the upper half?" (y_c); (3) "Is the weapon larger than 5% of the frame?". C: guard paraphrase. Keep severity judgements out of Tier C.

**dronefreak/PKLot (D36.1).** A: per-space occupancy. B: (1) more than half full; (2) free-space bins; (3) camera id from filename; (4) "Are there more vacant than occupied spaces?"; (5) full lot (zero vacant) yes/no. C: driver phrasing ("Will I find a space?" mapped to free > 0).

**cute-face/bike-helmet-dataset (D36.2).** A: all helmeted. B: (1) rider count; (2) riders without helmet count; (3) with / without / mixed. C: traffic-police phrasing.

**morzel85/synthetic-medical-document-recognition-benchmark (D37.1–37.3).** A: category, capture type, clipped. B: (1) page i of n ("Is this the first page?" from `p_1_of_n`); (2) multi-page document yes/no; (3) date format (type_n); (4) skewed yes/no (`ske`); (5) stained yes/no (`sta`). Also exact fields (patient birth date, organisation name) from the FHIR JSON, as generator truth. C: routing-clerk wording. Never ask about diagnoses.

**twinkle-ai/tw-drug-labels-vision (D38.1).** A: source_type; licence prefix. B: (1) imported vs domestic; (2) number of pages (len(images)); (3) "Is this a multi-panel carton?" (len>1 and carton). C: Text fields (drug name, strength) are machine-extracted, so they are Tier C only (`label_origin: machine`, kept separate).

**LibreYOLO/pills-sxdht (D38.2).** A: product or colour. B: (1) pill count; (2) "Is it an Ibuphil product?"; (3) "Which of these products is NOT shown?". C: pharmacist paraphrase.

**ApyHTML19/Medication_Boxes_Arabe_Latin (D38.3).** A: box count. B: (1) more than one box; (2) largest box position (left/right); (3) source subset; (4) "Does any box cover more than 20% of the image?". C: language-of-text questions (unverified).

**timm/oxford-iiit-pet (D39.1/39.2).** A: species, breed. B: (1) "Which of these is NOT a cat breed?"; (2) same-species 4-way distractors; (3) long-haired cat yes/no lookup; (4) terrier group yes/no lookup. C: adoption-listing phrasing; harder look-alike distractors (american_pit_bull_terrier vs staffordshire_bull_terrier).

**imageomics/2018-NEON-beetles (D40.2/40.3).** A: tray count, species. B: (1) >20 beetles; (2) genus; (3) NEON site code from siteID (pick 4); (4) "Are all specimens one species?" (always yes, so use as a sanity control). C: curator phrasing.

---

## 4. Gaps

| task | why no acceptable dataset | generator realistic? how |
|---|---|---|
| D31.6 insect pest species | Only candidate is tiny and has unnamed labels | Partly. Render museum-style insect images? Not realistic; photos are needed. Check IP102 owner page or iNaturalist research-grade exports (licence per photo). |
| D31.7 / D33.5 land cover | EuroSAT is 64 px | No for real imagery. Higher-res options (e.g. BigEarthNet patches) not checked. |
| D32.6 cattle count | No candidate verified | No. Needs drone photos. |
| D33.2 camera-trap empty vs animal | HF LILA subset dropped empty frames | No generator. The full LILA Channel Islands metadata JSON (with `empty`) on lila.science is the likely fix (not fetched). |
| D33.6 flooded road | FloodNet is a 12.8 GB single archive | No. |
| D34.6 / D35.5 person lying | Only synthetic positives | Yes. A 3D/CCTV renderer (pose → standing/lying label) gives generator truth; Simuletic shows it is feasible. |
| D34.7 smoking | No labels fetched | No (people photos). |
| D35.1 fire/smoke with clean licence | D-Fire has negatives but no licence; FASDD is a single archive | Partly. Synthetic fire/smoke composites exist but look artificial. Better: ask GAIA about D-Fire terms. |
| D35.6 intrusion | Not searched in depth | Yes. Render empty vs person-present CCTV scenes. |
| D36.4 traffic light colour | LISA is NC-SA with tiny lights | Yes. Draw or render a traffic light with a known lit lamp at a large scale. |
| D36.5 traffic sign | GTSRB crops are tiny | Yes. Paste vector sign templates (public-domain MUTCD/Vienna signs) onto street photos at large size. Label = template id. |
| D37.5 wristband / insurance card | None | Yes. HTML/PDF template generator with fake values (as morzel85 does). |
| D38.4 pill imprint/shape/colour | Labels need an external NDC lookup | Partly. NLM RxImage plus the RxNav API gives shape/colour/imprint as authority data (licence check needed). Rendering pills is possible but low-realism. |
| D38.5 blister empty cavity | None usable | Yes. Simple 2D/3D render of a blister grid with N empty cavities is realistic enough for counting. |
| D39.5 animal count | None | No (use COCO-style sets outside this slice). |
| D40.1 HAB taxon at usable resolution | NES images are tiny; bloombio has no rows | No generator. Fetch bloombio detection shard footer (42.7 MB) next. |
| D40.4 colony count | Only candidate GATED | Yes. Synthetic agar plates with drawn colonies (count = generator value) are realistic and common in the literature [INFERRED]. |
| D40 lab instrument reading | Not in slice data; gauges sit in slice 3 | Yes (gauge/needle rendering). |

---

## 5. Cannot verify

- **D-Fire licence**: neither the GitHub repo (API `license: None`) nor the HF mirror states one. The class-id map (0 = smoke, 1 = fire) was not found on the fetched README.
- **Label-origin quotes** for Project-AgML sets (seedlings, crop pest, oil palm, maize weed, tree species): the cards only cite the source. Annotation method not quoted.
- **Oxford-IIIT Pet** label origin: from the paper, not fetched.
- **Roboflow-derived sets** (VincentGOURBIN PPE, keremberke, cute-face, LibreYOLO pills, Turki weapons): no annotation statement beyond "Provided by a Roboflow user".
- **Turki weapons**: UCF-Crime upstream licence not checked.
- **Vertex-Test FireSmoke**: whether images are AI-generated (inferred from SD-style filenames).
- **c3rl seatbelt**: image provenance.
- **bloombio phytoplankton**: `/first-rows` returned "Not found". No rows. The schema is not seen.
- **Voxel51 fisheye8k / StanfordDogs**: labels sit in `samples.json` (39.4 MB / 7.0 MB), not parsed.
- **LISA traffic lights**: class names for ids 0..n.
- **keremberke aerial-sheep / construction-safety / forklift**: per-zip sizes of the valid/test splits (only the train zip size printed). Negatives per item.
- **tw-drug-labels-vision**: whether the two parquet shard sets (…of-00008, …of-00018) duplicate each other. The "輸 = imported" licence-prefix rule comes from TFDA naming convention [INFERRED], not a fetched page.
- **Value sources**: most "why it matters" lines use secondary reporting of FAO/NFPA/OSHA/NHTSA/INRIX/ISMP figures (links above). Domains 32, 36.2–36.6, 37, 39 and 40.2–40.5 have **no source**.
- **rotsl colony counting**: GATED (manual approval). Nothing inspected.
