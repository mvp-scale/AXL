# Slice 3: Industry and infrastructure (domains 21–30)

Research date: 2026-10-01. All dataset facts come from live fetches made in this session: the HF Hub API (`/api/datasets/<id>?blobs=true`, `/tree`), datasets-server (`/splits`, `/first-rows`, `/rows`, `/statistics`, `/size`), raw annotation files under 50 MB, GitHub raw files, the Zenodo, Figshare and Mendeley public APIs, and the Kaggle public dataset API (no login). Evidence tags: [ROW] = seen in a fetched row or annotation file; [CARD] = read on the owner's page or HF card; [PAPER]; [INFERRED]; [UNVERIFIED].

**Rating policy (spec, applied strictly).** A candidate is rated `USE` only if it meets all of these:
- the licence is stated;
- access is open;
- rows were pasted;
- the label origin is human or generator, and that is shown by a [CARD] or [PAPER] quote;
- the answer rule needs no one to look at the image;
- for yes/no tasks, real negatives exist.

When the label origin is only [INFERRED] (for example, a Roboflow export with no annotation statement), the candidate is capped at `MAYBE` and the failed test is named.

**Domain swaps: none.** Domains 24 (aviation) and 29 (oil, gas and mining) are thin, and they are reported as such in Gaps. I did not find another domain with far more usable data. Most open manufacturing and inspection data falls inside domains 21, 22, 28 and 30, which are already in this slice.

---

## 1. Task atlas

Each value-reason source is either a page I found in this session or is marked "No source fetched". Where the source was only seen as a search-result snippet, it is tagged [UNVERIFIED-snippet].

### D21 Manufacturing quality (surfaces, assembly)
| id | task | typed question | options | image type | value reason (source) |
|---|---|---|---|---|---|
| D21.1 | Steel sheet defect screening | "Does this steel-sheet image show a surface defect?" | yes / no | photo (line-scan, 1600×256) | Cost of poor quality is often cited at 15–20% of sales revenue at many manufacturers (ASQ rule of thumb, quoted at [IISE "Measuring the cost of quality"](https://iise.org/details.aspx?id=22118)) [UNVERIFIED-snippet] |
| D21.2 | Steel defect class | "Which Severstal defect class is present?" | class 1 / 2 / 3 / 4 | photo | same as D21.1 |
| D21.3 | Molded/commutator part crack check | "Does this commutator surface show a crack or defect?" | yes / no | photo (grayscale) | same as D21.1. Kolektor's own end-of-line inspection is the data source [CARD] |
| D21.4 | Lumber surface grading: defect present | "Does this wood board surface show any defect (knot, crack, resin, etc.)?" | yes / no | photo (2800×1024) | Wood paper: "manual inspection rarely achieves 70% reliability" ([F1000Research 10:581](https://f1000research.com/articles/10-581/v2)) [PAPER] |
| D21.5 | Lumber defect type | "Which defect type is visible on this board?" | e.g. Live_Knot / Dead_Knot / Crack / Resin / … (2–6 chosen from the class list) | photo | same as D21.4 |
| D21.6 | Weld acceptance | "Is this weld acceptable (good weld) or not (bad weld/defect)?" | good / bad | photo | No source fetched |
| D21.7 | Assembly completeness (missing part, e.g. screw or clip) | "Is any required part missing from this assembly?" | yes / no | photo | No source fetched. No qualifying dataset (see Gaps) |

### D22 Electronics and PCB inspection
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D22.1 | Bare-PCB defect screening (AOI review) | "Does this bare PCB image contain a manufacturing defect?" | yes / no | scan (binarised CCD, 640×640) | DeepPCB card: images come from "a linear scan CCD" used for AOI [CARD]. No business-cost source fetched |
| D22.2 | Bare-PCB defect type | "Which defect type is present on this board?" | missing hole / mouse bite / open circuit / short / spur / spurious copper | photo (≈2.5–3k px) | No source fetched |
| D22.3 | Assembled-board defect type | "Which defect is shown: dry joint, incorrect installation, PCB damage, or short circuit?" | 4 options | photo (640×480) | No source fetched |
| D22.4 | Component presence | "Is a <component type> present on this board?" | yes / no | photo | No source fetched. No licensed dataset (see Gaps) |
| D22.5 | Solder joint quality | "Is this solder joint acceptable?" | yes / no | photo | No source fetched. Gap |

### D23 Automotive repair and parts
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D23.1 | Tyre condition check | "Is this tyre defective or in good condition?" | defective / good | photo | NHTSA counted 733 traffic deaths in 2016 where tyre malfunction contributed (reported in [Salon/Center for Public Integrity](https://www.salon.com/2018/11/18/federal-regulators-deflated-numbers-on-tire-related-crash-deaths_partner/)) [UNVERIFIED-snippet] |
| D23.2 | Pothole-type tyre/wheel damage triage | see D30.1 | | | UK drivers: tyres were the most common pothole repair, 4.2 M repairs ([Kwik Fit](https://www.kwik-fit.com/press/the-state-of-the-nations-roads)) [UNVERIFIED-snippet] |
| D23.3 | Vehicle make identification (parts lookup) | "Which make is this car?" | 4–6 makes | photo | No source fetched |
| D23.4 | Body damage present | "Is this vehicle damaged?" | yes / no | photo | Already covered by DrBimmer (used). CarDD rejected. No new candidate (see Gaps) |
| D23.5 | Dashboard warning light identification | "Which warning light is lit?" | 4–6 icons | photo | No source fetched. Gap, drawable |
| D23.6 | Brake-pad wear | "Is this brake pad below the wear limit?" | yes / no | photo | No source fetched. Gap |

### D24 Aviation and aerospace maintenance
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D24.1 | Aircraft type check (ramp/MRO paperwork vs aircraft) | "Which manufacturer built this aircraft?" or "Which family is this?" | 4–6 manufacturers/families | photo | No source fetched |
| D24.2 | Fuselage/skin corrosion or dent | "Does this skin panel show corrosion?" | yes / no | photo | No source fetched. Gap (generic corrosion data in D29.1) |
| D24.3 | Borescope blade damage | "Does this engine blade show damage?" | yes / no | video frame | No source fetched. Gap |
| D24.4 | Foreign object debris on apron/runway | "Is there foreign object debris in this image?" | yes / no | photo | No source fetched. Gap |
| D24.5 | Tyre/landing-gear wear | "Is this aircraft tyre worn to limit?" | yes / no | photo | No source fetched. Gap |

### D25 Rail and transit
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D25.1 | Rail-head defect type | "Which rail-head defect is visible?" | crack / spalling / squat / corrugation / break | photo | No source fetched |
| D25.2 | Track obstruction | "Is there an object on the track?" | yes / no | video frame | No source fetched. Gap |
| D25.3 | Missing fastener/clip | "Is any rail fastener missing?" | yes / no | photo | No source fetched. Gap |
| D25.4 | Overhead catenary fault | "Is the catenary dropper/insulator damaged?" | yes / no | photo | No source fetched. Gap |
| D25.5 | Platform/rolling-stock graffiti | "Does this car exterior have graffiti?" | yes / no | photo | No source fetched. dacl10k has a `Graffiti` class on bridges (D30.4) |

### D26 Construction progress and sites
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D26.1 | Site equipment type | "Which machine is shown: excavator, dump truck, or wheel loader?" | 3 options | photo | No source fetched |
| D26.2 | Concrete surface crack | "Does this concrete surface show a crack?" | yes / no | photo | see D30 (FHWA NBIS) |
| D26.3 | Rebar installed and visible | "Is rebar of type <straight-N> present?" | yes / no | photo | No source fetched |
| D26.4 | Construction stage | "Which stage: foundation / frame / enclosure / finishing?" | 4 | photo | No source fetched. Gap |
| D26.5 | PPE compliance | (covered by slice 4 / D34; Voxel51 hard-hat already used) | | | |

### D27 Utilities meters and gauges
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D27.1 | Analog gauge reading (bucketed) | "Which range is the needle in?" or "What does the gauge read?" | 4–6 numeric options | photo/render | No source fetched |
| D27.2 | Water meter reading | "Which value does this meter show?" | 4 numeric options (1 true + 3 distractors) | photo | No source fetched |
| D27.3 | Electricity meter reading | "Which reading is shown?" | 4 numeric options | photo | No source fetched |
| D27.4 | Meter type | "Is this a mechanical or LCD meter?" | mechanical / LCD | photo | No source fetched. Only candidate GATED |
| D27.5 | Gauge out of range | "Is the needle above X?" | yes / no | render | No source fetched. Derived from D27.1 |

### D28 Energy assets (solar, wind, power lines)
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D28.1 | PV cell EL defect check | "Is this solar cell defective?" | yes / no | EL image (300×300) | Cracks are "among the defects that can lead to the highest power losses" ([Sensors 2024, PMC10933771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10933771/)) [UNVERIFIED-snippet] |
| D28.2 | Broken insulator on line | "Is there a broken insulator in this image?" | yes / no | aerial (drone) | Weather-related outages are cited at $28 bn/yr in the US ([Oxmaint](https://oxmaint.com/industries/power-plant/power-line-inspection-robots-and-drones-transmission-and-distribution-maintenance-cmms), a vendor page) [UNVERIFIED-snippet] |
| D28.3 | Broken cable/conductor | "Is there a broken cable in this image?" | yes / no | aerial | same as D28.2 |
| D28.4 | Solar panel soiling/damage | "What condition: clean / dusty / bird-drop / snow / electrical damage / physical damage?" | 6 | photo | No source fetched |
| D28.5 | Wind turbine blade damage | "Does this blade show damage?" | yes / no | drone photo | No source fetched. Gap |
| D28.6 | Thermal hotspot | "Does this thermal image show a hotspot?" | yes / no | thermal aerial | No source fetched. Candidate unlabeled |

### D29 Oil, gas and mining inspection
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D29.1 | Corrosion on steel asset | "Which is shown: corrosion, crack, or slippage?" or "Is corrosion present?" | 3 / yes-no | photo | No source fetched |
| D29.2 | Pipe/sewer CCTV defect type | "Which defect: blockage, corrosion, or crack?" | 3 | video frame | No source fetched |
| D29.3 | Gas leak plume (OGI camera) | "Is a gas plume visible?" | yes / no | IR video frame | No source fetched. Positives-only candidate |
| D29.4 | Oil spill present | "Is there an oil spill?" | yes / no | aerial/SAR | Not probed |
| D29.5 | Conveyor belt damage (mining) | "Is the belt torn?" | yes / no | photo | Gap |

### D30 Roads, bridges and public infrastructure
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D30.1 | Pothole present | "Is there a pothole in this road image?" | yes / no | photo (vehicle/drone) | UK pothole repair bill £1.25 bn/yr ([Yorkshire Evening Post / RAC-Kwik Fit](https://www.yorkshireeveningpost.co.uk/lifestyle/cars/pothole-damage-cost-uk-drivers-ps125bn-in-vehicle-repairs-last-year-2524106)) [UNVERIFIED-snippet] |
| D30.2 | Road damage type | "Which damage type: longitudinal crack, transverse crack, alligator crack, pothole?" | 4 | photo | same as D30.1 |
| D30.3 | Pothole severity | "How severe is the pothole: none / low / medium / severe?" | 4 | photo | same as D30.1 |
| D30.4 | Bridge defect type | "Which damage is shown: spalling / rust / crack / efflorescence / exposed rebar / …?" | 2–6 | photo | US bridges must be inspected at least every 24 months under NBIS ([FHWA NBIS Q&A](https://www.fhwa.dot.gov/bridge/nbis2022/qanda/07.cfm)) [UNVERIFIED-snippet] |
| D30.5 | Concrete crack present | "Does this concrete surface show a crack?" | yes / no | photo | same as D30.4 |
| D30.6 | Exposed rebar present (urgent repair) | "Is exposed reinforcement visible?" | yes / no | photo | same as D30.4 |

---

## 2. Dataset cards

The candidates within each task are ranked best first.

### D21.1 / D21.2 — Severstal steel defects (Voxel51 mirror). Verdict **MAYBE** (licence unverified)
1. Landing: https://huggingface.co/datasets/Voxel51/severstal_steel_defects. Files: same URL `/tree/main`. Origin: https://www.kaggle.com/competitions/severstal-steel-defect-detection. Repo id `Voxel51/severstal_steel_defects` [CARD]
2. Licence: the HF card metadata has `license: None` [CARD]. The card says it was "released for a 2019 Kaggle competition by Severstal". The Kaggle competition rules could not be read: the Kaggle API returned `401 Unauthenticated`. **UNVERIFIED.** Competition data is often limited to competition or non-commercial use [INFERRED].
3. Access: open (HF, not gated) [CARD]
4. Size: 1,758 MB in 18,080 files. The smallest unit is one JPG (~0.2 MB). The annotations are in `samples.json` (25.3 MB) [CARD api]
5. Sample-first proof: HTTP range request into `https://huggingface.co/datasets/Voxel51/severstal_steel_defects/resolve/main/samples.json` (first 80 KB) [ROW]:
   - `{"filepath": "data/data_0/0002cc93b.jpg", "split": "train", "image_id": "0002cc93b.jpg", "has_defect": true, "defect_classes": [1], "metadata": {"width": 1600, "height": 256}}`
   - `{"filepath": "data/data_0/00031f466.jpg", "split": "train", "image_id": "00031f466.jpg", "has_defect": false, "defect_classes": [], ... "width": 1600, "height": 256}`
   - `{"filepath": "data/data_0/000418bfc.jpg", "split": "train", "image_id": "000418bfc.jpg", "has_defect": false, "defect_classes": [], ...}`
6. Schema: `has_defect` (bool); `defect_classes` (list of int 1–4); `ground_truth` (FiftyOne segmentation mask); `split`; `metadata.width/height` [ROW]
7. Label origin: human [INFERRED]. The card says the annotations were "originally provided as run-length encoded (RLE) masks in train.csv" by Severstal [CARD]. The annotation method is not stated.
8. Answer rule: D21.1 is yes if `has_defect == true`. D21.2 is the single value of `defect_classes` when its length is 1.
9. Classes and balance: 4 classes, with class 3 most common and class 2 rarest [CARD]. "Unlabeled (no-defect) images: ~11,408 (~63%)" [CARD]. **Real negatives: yes** [ROW, 3 of 4 sampled rows have `has_defect: false`]. The test split (5,506) has no public labels [CARD], so use `split == train` only.
10. Per-image fit: some images carry several classes. Filter on `len(defect_classes) == 1` for D21.2.
11. Risks: no personal data. Very wide aspect ratio (1600×256) [ROW], so it needs padding or tiling at 1536 px. Widely used Kaggle data, so overlap with model training data is likely [INFERRED]. Kaggle labels are known to be noisy [UNVERIFIED].
12. Templates: (a) "Does this steel sheet show a surface defect?" yes/no. (b) "Which defect class (1/2/3/4) is present?" (c) "How many distinct defect classes appear: 0 / 1 / 2+?"
13. Failed test: licence not verifiable.

### D21.3 — Kolektor Surface-Defect Dataset (KolektorSDD, box release). Verdict **USE**
1. Landing: https://www.vicos.si/resources/kolektorsdd/. HF: https://huggingface.co/datasets/Voxel51/Kolektor_Surface_Defect, repo id `Voxel51/Kolektor_Surface_Defect` [CARD]
2. Licence: "**License:** CC BY-NC-SA 4.0 (non-commercial; contact Danijel Skočaj for commercial use)" (HF card README) [CARD]. Research and testing use is allowed. Commercial use is not.
3. Access: open [CARD api, `gated=False`]
4. Size: 106.6 MB in 405 files. The smallest unit is one JPG (~0.27 MB). `samples.json` is 0.67 MB [CARD api]
5. Sample-first proof: fetched the full `.../resolve/main/samples.json` (0.67 MB) [ROW]:
   - `{"filepath": "data/Part0.jpg", "board_id": "kos01", "has_defect": false, "ground_truth": {"_cls": "Segmentation", mask…}}`
   - `{"filepath": "data/Part1.jpg", "board_id": "kos01", "has_defect": false, …}`
   - `{"filepath": "data/Part5.jpg", "board_id": "kos01", "has_defect": true, …}`
6. Schema: `filepath`; `board_id` (physical item kos01–kos50); `has_defect` (bool); `ground_truth` (box-filled mask) [ROW]
7. Label origin: **human**. Quote: "images provided and annotated by Kolektor Group d.o.o." [CARD]
8. Answer rule: yes if `has_defect == true`.
9. Classes and balance: 399 samples, 52 defective and 347 non-defective [ROW count and CARD table]. **Real negatives: yes.**
10. Per-image fit: one answer per image. Build balanced sets by sampling 52 negatives.
11. Risks: no personal data. Grayscale 500×~1250 px [CARD]. Defects are "microscopic fractures", so the task is hard when the image is downscaled [CARD]. Box-filled masks, not pixel-precise [CARD]. KolektorSDD is a well-known benchmark, so moderate overlap with training data is likely [INFERRED].
12. Templates: (a) "Does this commutator surface show a crack?" yes/no. (b) "Is this part acceptable for shipment?" yes/no (same rule). (c) "Of these 2 surfaces of board kos0N, which one shows the defect?" (multi-image, optional).
13. All fields have evidence. Confidence: high.

### D21.4 / D21.5 — Wood surface defects (Kodytek et al.) — `iluvvatar/wood_surface_defects`. Verdict **MAYBE** (label origin not quoted)
1. Landing: https://huggingface.co/datasets/iluvvatar/wood_surface_defects. Paper: https://f1000research.com/articles/10-581/v2 [CARD]
2. Licence: `license: cc-by-4.0` (HF card) [CARD]. The original release licence was not checked [UNVERIFIED].
3. Access: open.
4. Size: 2,202.9 MB as 5 parquet shards of ~440 MB each. Smallest unit: one shard of 439.65 MB. Single images can be fetched through datasets-server `/rows` image URLs [CARD api]
5. Sample-first proof: `https://datasets-server.huggingface.co/rows?dataset=iluvvatar/wood_surface_defects&config=default&split=train&offset=5000&length=40` and `/first-rows` [ROW]:
   - `{"id": 160300034, "objects": [{"bb": [0.5075, 0.564941, 0.027142, 0.051758], "label": "Dead_Knot"}]}`
   - `{"id": 122700050, "objects": [{"bb": [0.369822, 0.116211, 0.021071, 0.039062], "label": "Live_Knot"}]}`
   - `{"id": 153500047, "objects": []}` (2800×1024; a defect-free board)
6. Schema: `id` (int); `image`; `objects` (list of {`bb`: YOLO box, `label`: string}) [ROW]
7. Label origin: human [INFERRED]. Paper and card text found in this session do not state how the boxes were made. The paper describes manual sorting for filtering only [PAPER]. **UNVERIFIED.**
8. Answer rule: D21.4 is yes if `len(objects) > 0`. D21.5 is the unique `label` when all objects share one label.
9. Classes and balance: the full label list was not enumerated. Seen in rows: Dead_Knot, Live_Knot [ROW]. The `/statistics` histogram of objects per image has bin [0,2) = 7,210 of 20,276 [ROW-stats]. Empty images were 3/40 and 2/40 in two sampled windows [ROW]. **Real negatives: yes** (~5–7% [INFERRED from samples]).
10. Per-image fit: mean 2.17 objects per image [ROW-stats]. Filter to a single distinct label for D21.5.
11. Risks: no personal data. Images are 2800×1024 and JPEG quality 50 [CARD]. Small knots are only ~2–5% of the width [ROW].
12. Templates: (a) "Does this board surface show any defect?" yes/no. (b) "Which defect is present: Live_Knot / Dead_Knot / …?" (c) "Are there more than 2 defects?" yes/no.
13. Failed test: label origin not quoted. Upgrade to USE if the paper's annotation section confirms manual boxes.

### D21.6 — Welding Defect Object Detection (CC0) — `rikkarth/welding-defect-object-detection`. Verdict **MAYBE** (label origin)
1. Landing: https://huggingface.co/datasets/rikkarth/welding-defect-object-detection. Origin: https://www.kaggle.com/datasets/sukmaadhiwijaya/welding-defect-object-detection [CARD]
2. Licence: "under **CC0: Public Domain**" (HF card, citing Kaggle) [CARD]
3. Access: open.
4. Size: 104.1 MB in 4,066 files. Smallest unit: `coco/test.json` (0.056 MB) or one image [CARD api]
5. Sample-first proof: fetched `.../resolve/main/coco/test.json` [ROW]:
   - image `{"id": 1, "file_name": "02fd0af7-51ab46bb-c13_jpg.rf.7de08cd3…jpg", "width": 640, "height": 640}`
   - annotation `{"id": 1, "image_id": 1, "category_id": 3, "bbox": [115.5, 118.25, 80.0, 158.5]}`
   - annotation `{"id": 3, "image_id": 2, "category_id": 3, "bbox": [92.25, 391.5, 547.5, 103.0]}`
   - categories: `[{'id':1,'name':'Bad Weld'},{'id':2,'name':'Good Weld'},{'id':3,'name':'Defect'}]`
6. Schema: COCO `images`, `annotations` (`category_id`, `bbox`), and `categories` [ROW]
7. Label origin: UNVERIFIED. The mirror's COCO files were "generated from the YOLO labels" by a converter, which is format conversion and not labelling [CARD]. The original annotation method is not stated. The "rf." filenames show a Roboflow export [ROW].
8. Answer rule: "good" if the image's category set is exactly {Good Weld}. "bad" if the set contains Bad Weld or Defect and no Good Weld. Mixed images are excluded.
9. Classes and balance (test split, 126 images): {Good only} 56, {Bad+Defect} 20, {Bad} 19, {Bad+Good+Defect} 16, {Bad+Good} 8, {Defect} 7 [ROW computed]. This gives real negatives ("good").
10. Per-image fit: 24/126 test images are mixed. Use the filter above.
11. Risks: some images are screenshots or video frames (filenames such as "Screenshot-2022-…", "SampleV1_1_mp4") [ROW, sibling repo listing]. Images are 640×640 Roboflow resizes [ROW]. Roboflow augmentation duplicates are possible [UNVERIFIED].
12. Templates: (a) "Is this weld acceptable?" yes/no. (b) "Does the image show at least one weld defect?" yes/no. (c) "How many welds are marked good: 0 / 1 / 2+?"
13. Failed test: label origin not documented.

### D22.1 — DeepPCB (GitHub). Verdict **USE**
1. Landing and files: https://github.com/tangsanli5201/DeepPCB. Files under `PCBData/groupNNNNN/` [CARD]
2. Licence: `LICENSE` reads "MIT License, Copyright (c) 2018 tangsanli5201" [CARD]. The README also says "You can only use this dataset for research purpose." [CARD]. **Flag:** research-only wording conflicts with MIT. Testing in research is allowed.
3. Access: open (GitHub raw).
4. Size: total repo size UNVERIFIED (the GitHub API call failed). Smallest unit: one template JPG, e.g. `00041000_temp.jpg` = 22,557 bytes [ROW HEAD], plus one TXT annotation. 1,500 pairs [CARD]
5. Sample-first proof: `https://raw.githubusercontent.com/tangsanli5201/DeepPCB/master/PCBData/group00041/00041_not/00041000.txt` [ROW]:
   - `466 441 493 470 3`
   - `454 300 493 396 2`
   - `539 259 592 316 1`
   - `trainval.txt` row: `group20085/20085/20085000.jpg group20085/20085_not/20085000.txt` [ROW]
6. Schema: one TXT per tested image. Each line is `x1,y1,x2,y2,type` with type 1=open, 2=short, 3=mousebite, 4=spur, 5=copper, 6=pin-hole [CARD]. Each pair has `*_test.jpg` (defective) and `*_temp.jpg` (defect-free template) [CARD]
7. Label origin: **human** (with artificially added defects). Quotes: "We use the axis-aligned bounding box with a class ID for each defect… we annotate six common types" and "we manually argument some artificial defects on each tested image" [CARD]
8. Answer rule: `*_test.jpg` gives yes (every annotation file has ≥1 line). `*_temp.jpg` gives no; the card says these were "manually checked and cleaned" as defect-free [CARD].
9. Classes and balance: 1,500 test images (3–12 defects each) and 1,500 templates [CARD]. **Real negatives: yes** (templates) [CARD].
10. Per-image fit: one yes/no answer per image. Type questions need multi-label handling, so D22.2 should use HRIPCB.
11. Risks: no personal data. Binarised 640×640 images, so pairs are visually easy and "_temp"/"_test" filenames must be hidden. Artificial defects [CARD]. Widely used benchmark [INFERRED].
12. Templates: (a) "Does this PCB image contain a defect?" yes/no. (b) "Is there an open-circuit defect?" yes/no (type 1 present). (c) "How many defects: 1–3 / 4–7 / 8+?"
13. Total size UNVERIFIED.

### D22.2 — HRIPCB / PKU PCB defects (`RobotHuman/PCB_defect`). Verdict **MAYBE** (licence provenance)
1. Landing: https://huggingface.co/datasets/RobotHuman/PCB_defect. Origin: https://www.kaggle.com/datasets/akhatova/pcb-defects. Paper: arXiv:1901.08204 [CARD]
2. Licence: HF metadata `license: mit` [CARD]. The licence of the original Kaggle/PKU release was not fetched [UNVERIFIED]. This is a re-upload whose MIT claim is unproven.
3. Access: open.
4. Size: 960.5 MB in 1,388 files (693 JPG and 693 XML). Smallest unit: one XML (~2 KB) [CARD api]
5. Sample-first proof: datasets-server `/rows?dataset=RobotHuman/PCB_defect&config=default&split=train&offset=300` [ROW]:
   - `<filename>06_open_circuit_04.jpg</filename> <width>2868</width><height>2316</height> <object><name>open_circuit</name><bndbox><xmin>1411</xmin><ymin>692</ymin><xmax>1450</xmax><ymax>734</ymax>`
   - offset 600: `12_spurious_copper_07.jpg`, width 2529, 5× `spurious_copper`
   - offset 0: `<folder>Missing_hole</folder><filename>01_missing_hole_01.jpg</filename>`
6. Schema: Pascal VOC XML with `filename`, `size`, and per-object `name` and `bndbox` [ROW]
7. Label origin: generator-like/human. The card says defects were inserted with Photoshop into template boards ("Photoshop으로 결함을 삽입해 합성") [CARD]. Boxes come from the inserter [INFERRED].
8. Answer rule: the defect type is the single distinct `name` across the objects (also equal to the folder).
9. Classes and balance: 6 classes (missing_hole, mouse_bite, open_circuit, short, spur, spurious_copper) [ROW folders and CARD]. Counts per folder were not tallied [UNVERIFIED]. **Positives only.** Not usable for yes/no.
10. Per-image fit: one type per image (3–5 instances) [CARD].
11. Risks: tiny defects (~40 px) on ~2.8k px boards [ROW], so downscaling to 1536 px may lose them. Synthetic defects [CARD].
12. Templates: (a) "Which defect type is on this board?" (6 options). (b) "Is the defect a short or an open circuit?" (2-option subset). (c) "How many defects are marked: 3 / 4 / 5?"
13. Failed test: licence provenance.

### D22.3 — `keremberke/pcb-defect-segmentation` (Roboflow). Verdict **MAYBE** (label origin; positives only)
1. Landing: https://huggingface.co/datasets/keremberke/pcb-defect-segmentation. Origin: https://universe.roboflow.com/diplom-qz7q6/defects-2q87r/dataset/8 [CARD]
2. Licence: "### License CC BY 4.0" [CARD]
3. Access: open.
4. Size: 9.7 MB in total; `data/valid-mini.zip` is 0.155 MB [CARD api]
5. Sample-first proof: `/first-rows?...config=full&split=train` [ROW]:
   - `{"image_id": 107, "width": 640, "height": 480, "objects": {"category": [..7 objects..]}}` (categories truncated in the fetch)
   - `{"image_id": 95, "width": 640, "height": 480, "objects": {"id": [243, 244], "bbox": [[229.0,334.0,54.8,17.7],[310.0,264.0,258.36,60.24]], "category": [2, 2]}}`
   - `{"image_id": 100, ..., "objects": {"bbox": [[319.0,130.0,114.71,126.3]], "category": [1]}}`
6. Schema: `objects.category` is a ClassLabel with names [dry_joint, incorrect_installation, pcb_damage, short_circuit]; COCO bbox and segmentation [ROW]
7. Label origin: UNVERIFIED (Roboflow user project).
8. Answer rule: the single distinct `category` name per image.
9. Classes: 4 [ROW]. Counts UNVERIFIED. Positives only [INFERRED].
10. Per-image fit: mixed classes occur. Filter to a single class.
11. Risks: small dataset. The per-split row count could not be confirmed (the `/size` call returned 3 rows per split for the default config).
12. Templates: (a) "Which defect is shown?" (4). (b) "Is a short circuit present?" yes/no. (c) "Is there more than one defect?" yes/no.
13. Failed tests: label origin, counts.

### D23.1 — Tyre condition (Mendeley `bn7ch8tvyp`; HF `NMiriams/Good_Tires` + `NMiriams/Defective_Tires`). Verdict **USE** (confidence med)
1. Landing: https://data.mendeley.com/datasets/bn7ch8tvyp (Mendeley public API). HF: https://huggingface.co/datasets/NMiriams/Good_Tires and https://huggingface.co/datasets/NMiriams/Defective_Tires. Kaggle mirror: `warcoder/tyre-quality-classification` [CARD]
2. Licence: Mendeley "CC BY 4.0 — You can share, copy and modify this dataset so long as you give appropriate credit…" [CARD api]. Both HF repos have `license: cc-by-4.0` [CARD]. Kaggle: "Attribution 4.0 International (CC BY 4.0)" [CARD api]
3. Access: open.
4. Size: HF Good 1,254.7 MB (828 JPG) and Defective 1,663.1 MB (1,028 JPG). Smallest unit: one JPG (~1.5 MB average) [CARD api]. Kaggle total is 2,917,776,336 bytes [CARD api]
5. Sample-first proof: datasets-server `/first-rows` for both repos returns image-only rows [ROW]. The label is the repo, not a column. Row counts: Good_Tires train = 828, Defective_Tires train = 1,028 [ROW `/size`]. Mendeley description: "1854 digital tyres images, categorized into two classes: defective and good condition" [CARD]. **Note:** there are no per-row label columns. The rows pasted are image-only, and the label comes from which repo the row is in.
6. Schema: `image` only. Label = source repo (Good/Defective) [ROW]
7. Label origin: human. Quote: "The images are labelled based on their condition, i.e., whether the tyre is defective or in good condition." [CARD Mendeley]. The annotator is not named, but nothing indicates a machine.
8. Answer rule: "good" if the image comes from Good_Tires, "defective" if it comes from Defective_Tires.
9. Classes and balance: 828 good and 1,028 defective (1,856 total vs 1,854 on Mendeley, which is close to exact) [ROW and CARD]. **Real negatives: yes.**
10. Per-image fit: one tyre per image [CARD].
11. Risks: the defect type (crack, bulge, etc.) is not labelled. Large photos (~1.5 MB). The set is also on Kaggle, so training overlap is possible [INFERRED]. The 2-image difference against Mendeley is unexplained.
12. Templates: (a) "Is this tyre defective?" yes/no. (b) "Is this tyre safe to keep in service?" yes/no (same rule). (c) "Defective or good condition?" (2 options).
13. Confidence is med because the proof is repo-level, not row-level.

### D23.3 — Stanford Cars (`tanganke/stanford_cars`). Verdict **MAYBE** (no licence on card)
1. Landing: https://huggingface.co/datasets/tanganke/stanford_cars [CARD]
2. Licence: `license=None` on the card [CARD]. **UNVERIFIED.**
3. Access: open.
4. Size: 6,016.5 MB. Smallest unit: one parquet of ~470–540 MB. This includes corrupted variants (gaussian_noise, pixelate, …) [CARD api]
5. Sample-first proof: `/first-rows` gives `{"label": 0}` ×3 (all "AM General Hummer SUV 2000") [ROW]. Only one class was seen, so this proof is weak.
6. Schema: `image` and `label` (ClassLabel, 196 names such as "Acura RL Sedan 2012") [ROW]
7. Label origin: UNVERIFIED.
8. Answer rule: make = first token(s) of the label name, mapped via a make lookup.
9. Classes: 196 make/model/year names [ROW].
10. Per-image fit: one car per image [INFERRED].
11. Risks: license plates may be visible [INFERRED]. Very common benchmark, so training overlap is high [INFERRED].
12. Templates: "Which make?" (4–6 options), "Is this a sedan or an SUV?" (from the name), "Which model year?" (from the name).
13. Failed tests: licence, label origin.

### D24.1 — FGVC-Aircraft (`Voxel51/FGVC-Aircraft`). Verdict **MAYBE** (label origin; non-commercial)
1. Landing: https://huggingface.co/datasets/Voxel51/FGVC-Aircraft. Origin page cited on the card [CARD]
2. Licence: `license: other`. Quote: "Images in the benchmark are generously made available for non-commercial research purposes only by a number of airplane spotters… the original authors retain the copyright" [CARD]
3. Access: open.
4. Size: 2,775.5 MB in 10,006 files. Smallest unit: one JPG (~80 KB). `samples.json` is 8.2 MB [CARD api]
5. Sample-first proof: range request into `.../resolve/main/samples.json` [ROW]:
   - `{"filepath": "data/data_0/0034309.jpg", "width": 900, "height": 687, "variant": {"label": "DC-8"}, "family": {"label": "DC-8"}, "manufacturer": "Douglas Aircraft Company"}`
   - `{"filepath": "data/data_0/0034958.jpg", "variant": {"label": "737-200"}, "family": {"label": "Boeing 737"}, "manufacturer": "Boeing"}`
   - `{"filepath": "data/data_0/0037511.jpg", "variant": {"label": "DC-9-30"}, "family": {"label": "DC-9"}, "manufacturer": "McDonnell Douglas"}`
6. Schema: `variant.label` (102), `family.label` (70), `manufacturer` (41), `bounding_box` [ROW and CARD]
7. Label origin: UNVERIFIED (spotter-sourced, curated by the authors) [CARD wording].
8. Answer rule: answer = `manufacturer` (or `family.label`). Distractors come from other manufacturers.
9. Classes: 41 / 70 / 102 [CARD]. Balanced at about 100 per variant [CARD].
10. Per-image fit: one main aircraft per image [CARD].
11. Risks: the copyright banner strip at the bottom of images is noted in the original release [UNVERIFIED]. Registrations are visible, but they identify aircraft, not people. Very common benchmark, so overlap is high [INFERRED]. This is not a maintenance task as such.
12. Templates: "Which manufacturer?", "Which family?", "Is this a Boeing 737-family aircraft?" yes/no.
13. Failed test: label origin. The licence is restrictive.

### D25.1 — `Dhika/defect_rail`. Verdict **SKIP**
1. https://huggingface.co/datasets/Dhika/defect_rail (Roboflow "Railway Defect.v8i.clip") [CARD]
2. Licence: `license: unknown` [CARD]
3. Access: open. 4. Size: 6.3 MB, 761 JPG [CARD api]
5. Proof: `/rows` offsets 0/150/300 give `{"image":{"w":224,"h":224},"label":0}`, `{"…label":2}`, `{"…label":4}` [ROW]
6. Schema: `label` ClassLabel [corrugation, crack, putus, spalling, squat] [ROW]
7. Label origin: UNVERIFIED. 8. Rule: label name.
9. Train counts: corrugation 14, crack 100, putus 63, spalling 100, squat 100 [ROW-stats]. No negatives.
10. One label per image. 11. **Tiny 224×224 images** (trap). Unknown licence.
12. "Which rail defect?" (5). 13. Failed tests: licence, tiny images, label origin.

### D26.1 — Excavators/dump trucks/wheel loaders (`keremberke/excavator-detector`). Verdict **MAYBE** (label origin)
1. Landing: https://huggingface.co/datasets/keremberke/excavator-detector. Origin: https://universe.roboflow.com/mohamed-sabek-6zmr6/excavators-cwlh0/dataset/3 [CARD]
2. Licence: README.dataset.txt says "License: CC BY 4.0", and the card says "### License CC BY 4.0" [CARD]
3. Access: open.
4. Size: 193.4 MB; `data/valid-mini.zip` is 0.161 MB and `data/test.zip` is 10.3 MB [CARD api]
5. Proof: `/first-rows?config=full&split=train` [ROW]:
   - `{"image_id": 714, "width": 640, "height": 640, "objects": {"bbox": [[257,58,126,126],[168,0,86.5,75.5],[87,246,293,369]], "category": [1, 1, 2]}}`
   - `{"image_id": 1159, "objects": {"bbox": [[45,112,533.5,416.5]], "category": [0]}}`
   - `{"image_id": 1688, "objects": {"bbox": [[0,7,627.5,582]], "category": [2]}}`
6. Schema: `objects.category` ClassLabel [excavators, dump truck, wheel loader] [ROW]
7. Label origin: UNVERIFIED. The card says "The dataset is provided by Mohamed Sabek… 1,532 annotated examples of 'excavators'" [CARD], which does not say how the boxes were made.
8. Answer rule: the single distinct category per image.
9. Instance counts: 1,532 excavator, 1,269 dump truck, 1,080 wheel loader [CARD]. Image counts UNVERIFIED.
10. Mixed images exist (row 714). Filter to a single class.
11. Images are stretched to 640×640 [CARD], which distorts the aspect ratio.
12. "Which machine?" (3); "Is a dump truck present?" yes/no; "How many machines: 1 / 2 / 3+?"
13. Failed test: label origin.

### D26.2 / D30.5 — METU concrete crack images (`mohammadnajeeb/concrete_crack_images`). Verdict **SKIP** (tiny)
1. https://huggingface.co/datasets/mohammadnajeeb/concrete_crack_images [CARD]. 2. `license: cc-by-4.0` [CARD]. 3. open.
4. 244.9 MB as 3 zips; the smallest is `data/test.zip` at 49.06 MB [CARD api]
5. `/rows` offsets 0/12000/23000 give `{"image":{"w":227,"h":227},"label":0}`, `{…"label":1}`, `{…"label":1}` [ROW]
6. `label` ClassLabel [Negative, Positive] [ROW]. 7. UNVERIFIED.
8. Rule: yes if `Positive`. 9. 12,000 / 12,000 (train) [ROW-stats]. Real negatives exist.
10. One answer per image. 11. **227×227 px** (tiny-image trap).
12. "Does this concrete show a crack?" 13. Failed test: image size. Label origin is unknown.

### D26.3 — ROI-1555 rebar (`tsrobcvai/ROI-1555_…`). Verdict **MAYBE** (no licence)
1. https://huggingface.co/datasets/tsrobcvai/ROI-1555_Rebar_Detection_and_Instance_Segmentation_Dataset [CARD]. 2. `license=None` [CARD]. 3. open.
4. 586.5 MB; one labelme JSON is 0.06–0.6 MB [CARD api]
5. `/first-rows` (test) [ROW]: `{"version":"5.1.1","shapes":[{"label":"straight-6",...},{"label":"straight-8",...},{"label":"straight-4",...}]}`; `{"version":"5.1.1","shapes":[{"label":"straight-5"},{"label":"straight-6"},{"label":"straight-8"}…]}`; `{"version":"4.5.9","shapes":[{"label":"straight-9"},{"label":"straight-6"},{"label":"straight-11"}…]}`
6. labelme `shapes[].label`, polygon `points`, `imageWidth/Height` [ROW]. 7. Card: "fine-labeled bounding boxes and pixel-wise masks" [CARD]. Who labelled is UNVERIFIED.
8. Rule: count of shapes (rebar count). The meaning of the "straight-N" labels is UNVERIFIED (probably bar IDs, not types).
9. 1,555 images [CARD]. 10. Many bars per image, so this suits counting.
11. Large images (~2160 px) [ROW]. 12. "How many rebars: <5 / 5–10 / >10?"
13. Failed tests: licence, label semantics.

### D27.1 — Synthetic meter reading (`goodcoffee/Meter_Reading`). Verdict **USE**
1. Landing: https://huggingface.co/datasets/goodcoffee/Meter_Reading [CARD]
2. Licence: `license: apache-2.0` (the entire card body) [CARD]
3. Access: open.
4. Size: 2,449.3 MB (1,500 PNG + 1,502 JSON). Smallest units: one per-image JSON (~0.022 MB) and `test__vqa_dataset.json` (0.275 MB) [CARD api]
5. Proof: `/first-rows?dataset=goodcoffee/Meter_Reading&config=default&split=train` [ROW]:
   - `{"image_id": 1, "file_name": "data/v_0001_f_0000_rgba.png", "height": 1024, "width": 1024, "measurement_answer": "The result is -0.2", "range_answer": "The range is from 0 to 8", "minmax_answer": "The minimum value is 0 and the maximum value is 8"}`
   - `{"image_id": 2, "file_name": "data/v_0002_f_0000_rgba.png", "measurement_answer": "The result is -1.2", "range_answer": "The range is from -1 to 6"}`
   - `{"image_id": 3, "file_name": "data/v_0003_f_0000_rgba.png", "measurement_answer": "The result is -0.2", "range_answer": "The range is from 0 to 8"}`
   - per-image JSON: `{"category_name": "dial", "bbox": [636.0, 592.0, 207.0, 89.0], "camera_matrix": […], "camera_focal_length": 50.0, "synth_dial_value": -0.2, …}` [ROW]
6. Schema: `needle_bbox`, `casing_bbox`, `face_bbox`, the question/answer string pairs for measurement, range and min/max, and in the JSON `synth_dial_value` (float) [ROW]
7. Label origin: **generator**. The `synth_dial_value` field, `camera_matrix` and the render filenames (`v_0001_f_0000_rgba`) show the images were rendered from known values [ROW]. There is no card text beyond the licence.
8. Answer rule: true value = `synth_dial_value` (or a parse of `measurement_answer`). Pick-one = the true value plus 3 distractors at ±k × tick spacing within [min, max] from `range_answer`.
9. Classes: continuous values. 1,198 train and 302 test [ROW `/size`].
10. One gauge per image [ROW].
11. No personal data. 1024×1024 [ROW]. A reading of -0.2 on a 0–8 range [ROW] suggests the value may sit below the scale minimum, so check for clipping. Small (1,500 images). The first rows repeat the value -0.2, so value diversity is UNVERIFIED.
12. Templates: (a) "What does the gauge read?" (4 numeric options). (b) "What is the maximum on the scale?" (from `range_answer`). (c) "Is the reading above the midpoint of the scale?" yes/no.
13. Confidence: med (generator inferred from fields, not stated on the card).

### D27.1 alt — `moondream/synthetic-gauges-v6`. Verdict **MAYBE** (no licence)
1. https://huggingface.co/datasets/moondream/synthetic-gauges-v6. 2. The card has no licence field [CARD]. 3. open.
4. 20,578.5 MB in 45 parquets of ~459 MB each (smallest > 50 MB) [CARD api]
5. `/first-rows` (split `train_0`) [ROW]: facts `{"units": {"outer": {"value": 20.998997750987026, "labels": [{"value": 0…},{"value": 40…},{"value": 80…},{"value": 120…},{"value": 160…}]…}}}`; next rows have outer value 104.023… and 55.513…; image 923×1024.
6. `facts` JSON: units.outer.value, labels, ticks [ROW]. 7. Generator [ROW: exact float values and tick positions].
8. Rule: answer = `units.outer.value`. 9. 262,144 rows [ROW]. 10. One gauge, possibly dual scale.
11. Licence missing. 12. As for goodcoffee. 13. Failed test: licence.

### D27.2 — Water meter readings (`rsnogueira/Watermeter`). Verdict **MAYBE** (no licence)
1. https://huggingface.co/datasets/rsnogueira/Watermeter [CARD]. 2. No licence on the card (README is config only) [CARD]. 3. open.
4. 1,104.6 MB; `data.csv` is 0.289 MB [CARD api]
5. `/first-rows` and raw `data.csv` [ROW]: `id_53_value_595_825.jpg, 595.825, {polygon…}`; `id_553_value_65_475.jpg, 65.475, {polygon…}`; `id_407_value_21_86.jpg, 21.86, {polygon…}`
6. `photo_name`, `value` (float m³), `location` (polygon of the reading window) [ROW]. 7. UNVERIFIED (looks human-entered).
8. Rule: answer = `value`. Distractors are made by digit perturbation. 9. 1,244 rows [ROW].
10. One meter per image. 11. **The value is in the filename**, so files must be renamed. The licence and origin are unknown (likely a re-upload of a Kaggle set) [INFERRED]. 12. "What reading is shown?" (4 options); "Is the reading above 100 m³?"
13. Failed tests: licence, label origin.

### D27.2 alt — `UniDataPro/water-meters`. Verdict **MAYBE** (preview of a commercial set; NC-ND)
1. https://huggingface.co/datasets/UniDataPro/water-meters. 2. `license: cc-by-nc-nd-4.0`. The card says "This is a limited preview… To access the full dataset, please contact us" [CARD]. 3. open (60-image preview).
4. 17.3 MB; `water meters.csv` is 0.005 MB [CARD api]. 5. Rows not fetched (`/first-rows` returned 500). **UNVERIFIED** rows. 6–12: UNVERIFIED.
13. Failed test: no rows pasted. Preview only.

### D27.3 — `Praekelt/ElectricityMeterReadings1o4`. Verdict **MAYBE** (no licence)
1. https://huggingface.co/datasets/Praekelt/ElectricityMeterReadings1o4. 2. `license=None` [CARD]. 3. open. 4. 44.2 MB in a single parquet (under 50 MB, fetchable) [CARD api]
5. `/first-rows` gives `{"reading": "93809.4"}`, `{"reading": "87972.4"}`, `{"reading": "41365.5"}` [ROW]
6. `image` and `reading` (string). 7. UNVERIFIED. 8. Rule: answer = `reading`. 9. 165 rows [ROW].
10. One meter per image [INFERRED]. 11. Possible household/location context in images [INFERRED]. 12. "Which reading?" (4 options).
13. Failed tests: licence, origin.

### D27.4 — `utilitimetersai/Annotated-Mechanical-And-LCD-Utility-Meter-Dials-Dataset`. Verdict **GATED**
`gated=manual`, `license: cc-by-nc-4.0`; `/splits` returns 401 [CARD api]. A person must request access at https://huggingface.co/datasets/utilitimetersai/Annotated-Mechanical-And-LCD-Utility-Meter-Dials-Dataset. Also `Mileeena/synthetic-analog-gauges` (`gated=auto`, cc-by-4.0, 2,545 MB, COCO annotations, a generator dataset) is GATED (login + accept).

### D28.1 — ELPV solar-cell EL (GitHub `zae-bayern/elpv-dataset`; HF `bardroh/elpv-el-defects`). Verdict **MAYBE** (label origin not quoted; 300 px)
1. Landing: https://github.com/zae-bayern/elpv-dataset. HF: https://huggingface.co/datasets/bardroh/elpv-el-defects. `mjphayes/elpv-dataset` claims MIT, which conflicts with upstream, so do not use it [CARD]
2. Licence: "All the images in this work are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License… For commercial use, please contact us" (GitHub README) [CARD]. `bardroh` card: `license: cc-by-nc-sa-4.0` [CARD]
3. Access: open.
4. Size: HF 90.3 MB as 3 parquets; the smallest is `validation` at 9.1 MB [CARD api]. Upstream `labels.csv` is small [ROW]
5. Proof: `https://raw.githubusercontent.com/zae-bayern/elpv-dataset/master/src/elpv_dataset/data/labels.csv` [ROW]:
   - `images/cell0001.png  1.0  mono`
   - `images/cell0002.png  1.0  mono`
   - `images/cell0004.png  0.0  mono`
   - HF `/rows`: `{"label": 1, "label4": "certainly_defective"}`, `{"label": 0, "label4": "functional"}`, both 300×300 [ROW]
6. Schema: upstream has path, defect probability ∈ {0, 1/3, 2/3, 1}, and type (mono/poly). HF has `label` (ok/defect) and `label4` [ROW]
7. Label origin: human [INFERRED]. The README says "Every image is annotated with a defect probability" without naming the annotator [CARD]. The probability levels look like a graded human rating [INFERRED].
8. Answer rule: yes if prob = 1.0, no if prob = 0.0. Drop 1/3 and 2/3 for a clean yes/no set. Pick-one: mono vs poly from `type`.
9. Classes (upstream, 2,624 total): prob 0.0 = 1,508, 0.333 = 295, 0.667 = 106, 1.0 = 715. Mono 1,074, poly 1,550 [ROW computed]. **Real negatives: yes.**
10. One cell per image.
11. **300×300 grayscale** [ROW-stats], close to the tiny-image trap, so flag it. No personal data. Known benchmark [INFERRED].
12. Templates: "Is this solar cell defective?" yes/no; "Is this a monocrystalline or polycrystalline cell?"; "How likely is a defect: functional / possibly / likely / certainly?" (4 options).
13. Failed test: label origin not quoted. Upgrade if the paper (Buerhop-Lutz et al. 2018 / Deitsch et al. 2019) confirms expert labelling. Not fetched.

### D28.2 / D28.3 — Powerline components and faults (`docmhvr/powerline-components-and-faults`). Verdict **USE**
1. Landing: https://huggingface.co/datasets/docmhvr/powerline-components-and-faults. GitHub: https://github.com/docmhvr/UAV-Based-Powerline-Problem-Inspection-Using-Machine-Learning [CARD]
2. Licence: "This dataset is provided under the [MIT License]" (README body). The YAML metadata licence is empty [CARD]
3. Access: open.
4. Size: 122.2 MB. Smallest units: `test` parquet 2.29 MB and `validation` 4.56 MB [CARD api]
5. Proof: `/first-rows?…split=train` [ROW]:
   - `{"bboxes": [[289.97, 88.20, 435.88, 321.69]], "labels": [0]}`
   - `{"bboxes": [7 boxes], "labels": [1, 3, 3, 4, 4, 4, 0]}`
   - `{"bboxes": [9 boxes], "labels": [1, 1, 1, 1, 3, 1, 3, 3, 4]}`
6. Schema: `labels` is a sequence of ClassLabel [Broken Cable, Broken Insulator, Cable, Insulators, Tower, Vegetation]; `bboxes` in pixel xyxy [ROW]
7. Label origin: **human**. Quote: "Data was collected using DJI Mini drone and manually compiled and annotated using Roboflow." [CARD]
8. Answer rule: D28.2 is yes if 1 ∈ labels (Broken Insulator), no if 3 ∈ labels and 1 ∉ labels. D28.3 is yes if 0 ∈ labels.
9. Balance (all 1,794 train rows scanned via `/rows`): has broken insulator 663; insulators with none broken 830; no insulator 301. Broken cable 907 vs none 887 [ROW computed]. **Real negatives: yes.**
10. Per-image fit: many objects per image (mean 8.0 [ROW-stats]), but yes/no presence is well defined.
11. Images are all 640×640 [ROW-stats], which is low-ish for 1536 px. Roboflow exports often include augmented copies, so near-duplicates are possible [UNVERIFIED]. No people expected.
12. Templates: (a) "Is there a broken insulator?" yes/no. (b) "Is there a broken cable?" yes/no. (c) "Which is present: vegetation encroachment, broken cable, or neither?"
13. Confidence: med-high.

### D28.2 alt — `silera/broken-insulators-synthetic-detection`. Verdict **MAYBE** (positives only)
1. https://huggingface.co/datasets/silera/broken-insulators-synthetic-detection. 2. `license: cc-by-4.0`; derivative of Roboflow "Defect Detection" (CC BY 4.0) [CARD]. 3. open.
4. 221.7 MB; `data/val/metadata.jsonl` is 0.006 MB [CARD api]
5. `/first-rows` [ROW]: `{"objects": {"bbox": [[280, 513, 58, 46]], "category": [1]}}`, `{"objects": {"bbox": [[296, 424, 59, 59]], "category": [1]}}`, `{"objects": {"bbox": [[240, 313, 89, 41]], "category": [1]}}`
6. `objects.bbox` and `objects.category` (int; names UNVERIFIED). 7. Generator ("Generated using Silera Studio") [CARD]. Whether the boxes are generator-exact is UNVERIFIED.
8. Rule: count boxes. 9. 162/41 rows [ROW]. Positives only [INFERRED from the title].
11. Synthetic look. 13. Failed test: no negatives.

### D28.4 — `metalmerge/solar-panel-inspection`. Verdict **MAYBE** (no licence)
1. https://huggingface.co/datasets/metalmerge/solar-panel-inspection. 2. No licence or README [CARD]. 3. open. 4. 247.8 MB; the unit is one image [CARD api].
5. Proof is a folder listing (folder = label) from `/api/datasets/...` [ROW]: `Faulty_solar_panel_Train/Bird-drop` 99, `…/Clean` 99, `…/Dusty` 99, `…/Snow-Covered` 98, `…/Electrical-damage` 82, `…/Physical-Damage` 55, plus Validation/Test folders. There are no per-row labels; the viewer shows only 5 test rows.
7. UNVERIFIED (looks web-scraped) [INFERRED]. 8. Rule: answer = folder name. 9. Clean is a real negative.
11. Web images, likely watermarks and duplicates [INFERRED]. 13. Failed tests: licence, origin, row proof weak.

### D28.5 — `jonathan-roberts1/Airbus-Wind-Turbines-Patches`. Verdict **SKIP**
CC BY-NC-SA 4.0 (via Kaggle) [CARD]. 147.7 MB as a single parquet. Rows: `{"image":{"w":128,"h":128},"label":0}` at offsets 0, 40000 and 71000 (label 1 at 71000) [ROW]. 40,513 no / 30,991 yes [ROW-stats]. **128×128 px** (tiny trap) and turbine presence only, with no damage label.

### D28.6 — `Manishsahu53/Solar-Panel-Thermal-Drone-UAV-Images`. Verdict **SKIP**
Apache-2.0 [CARD]. Three zips of 2.25–8.56 GB (single-archive trap). `/first-rows` shows image-only rows [ROW], so there are no labels.

### D29.1 — Corrosion (Roboflow-100 `LibreYOLO/corrosion-bi3q3`). Verdict **MAYBE** (label origin)
1. https://huggingface.co/datasets/LibreYOLO/corrosion-bi3q3. Origin: https://universe.roboflow.com/roboflow-100/corrosion-bi3q3 [CARD]
2. "This dataset is released under the **CC-BY-4.0** license"; `data.yaml roboflow.license: CC BY 4.0` [CARD]
3. open. 4. 67.4 MB; one label TXT under 1 KB [CARD api]
5. Raw label files [ROW]: `test/labels/Attaran7_JPG_jpg.rf.a9f0…txt` gives `2 0.415625 0.7984375 0.03828125 0.02421875`; `KwanLoneDSCN1716_JPG_jpg.rf.554f…txt` gives `1 0.3265625 0.221875 0.16875 0.25546875`; `KKR_DSCN1327_JPG_jpg.rf.0a59…txt` gives (empty file).
6. YOLO `class cx cy w h`; names [Slippage, corrosion, crack] [ROW data.yaml]
7. UNVERIFIED (RF100 sources are crowd Roboflow projects) [PAPER arXiv:2211.13523 not fetched].
8. Rule: yes if any line has class 1 (corrosion). Pick-one = the single distinct class.
9. Test split: 105 label files, of which 5 are empty [ROW computed], so negatives are few. Class counts UNVERIFIED.
11. Some image sizes are unknown. "rf." augmentation copies are possible. 13. Failed test: label origin. The number of negatives is small.

### D29.2 — Sewer defects: `ZhiyaYang/sewer-defect-crack-dataset` (MAYBE, no licence) and `SRuibo/Sewer-pipe-defects` (MAYBE, codes unexplained, positives only)
- ZhiyaYang: no licence [CARD]; 194.5 MB as 3 parquets, smallest `validation` 31.1 MB [CARD api]; `/first-rows` gives `{"label": 1}`, `{"label": 1}`, `{"label": 2}` with names [blockage, corrosion, crack] [ROW]; 409/88/88 rows. Origin UNVERIFIED. Rule: label name. Failed tests: licence, origin.
- SRuibo: `license: cc-by-4.0` [CARD]; 2,374 MB of PNG; `classes.txt` = `CK PL SG SL TL ZW` [ROW]. Label rows: `00320091_000.txt` gives `2 0.832451 0.633816 0.273714 0.649186` …; `PL_186_000.txt` gives `1 0.30625 0.277778 0.229953 0.526205` … [ROW]. Train has 1,000 label files listed with 0 empty, and test has 198 with 0 empty [ROW], so it is **positives only**. The code meanings are UNVERIFIED (likely Chinese pipe-defect abbreviations). Failed tests: class semantics, no negatives.

### D29.3 — `samhormozian/GasLeakPlumes`. Verdict **SKIP**
No licence [CARD]. `annotations.json` (3.0 MB, COCO) [ROW]: categories `Gas Leak Day`, `Gas Leak night`; image `{"id":1,"width":480,"height":296,"file_name":"image0001.png"}`; annotation `{"image_id":1,"category_id":1,"bbox":[241.1,79.37,129.82,171.37],"attributes":{"occluded":false,"track_id":0,"keyframe":true}}`. 5,487 of 5,515 images annotated [ROW computed], so it is effectively **positives only**. The 480×296 frames are small and come from tracked video, so they are near-duplicates.

### D30.1 / D30.2 — RDD2022 (`dronefreak/RDD2022`; official: sekilab/Figshare). Verdict **USE**
1. Landing: https://github.com/sekilab/RoadDamageDetector and Figshare https://figshare.com/articles/dataset/RDD2022_-_The_multi-national_Road_Damage_Dataset_released_through_CRDDC_2022/21431547. HF: https://huggingface.co/datasets/dronefreak/RDD2022 [CARD]
2. Licence: Figshare API gives `{'name': 'CC BY 4.0'}` [CARD api]. The HF card says "released by their creators under the Creative Commons Attribution-ShareAlike 4.0… (CC BY-SA 4.0)" [CARD]. **The sources conflict (BY vs BY-SA)**, but both are open and permit testing.
3. Access: open. The official S3 file list returned AccessDenied [ROW], so use Figshare or HF.
4. Size: official is a SINGLE ARCHIVE, `RDD2022_released_through_CRDDC2022.zip` at 13,264.2 MB [CARD api]. HF is 11,078.8 MB as per-image JPG and TXT, with per-shard `metadata.jsonl` of ~0.37 MB as the smallest annotation unit [CARD api]
5. Proof: fetched `https://huggingface.co/datasets/dronefreak/RDD2022/resolve/main/data/images/train/shard_000/metadata.jsonl` (3,000 rows) and `/first-rows` [ROW]:
   - `{"file_name": "China_Drone_000001.jpg", "objects": {"bbox": [[14, 70, 184, 29], [95, 114, 25, 158]], "categories": [1, 0]}}`
   - `{"file_name": "China_Drone_000003.jpg", "objects": {"bbox": [[9,467,195,22],[199,304,313,46],[199,1,78,296]], "categories": [1, 1, 0]}}`
   - `{"file_name": "China_Drone_000048.jpg", "objects": {"bbox": [], "categories": []}}` (negative)
6. Schema: `file_name` (country_source_id); `objects.categories` with 0 = longitudinal_crack (D00), 1 = transverse_crack (D10), 2 = alligator_crack (D20), 3 = pothole (D40); `objects.bbox` [ROW and CARD]
7. Label origin: **human**. The cvtechniques card (same source data) says "annotations… created by professional researchers in Tokyo" [CARD]. The data article is Arya et al., Geoscience Data Journal [CARD].
8. Answer rule: D30.1 is yes if 3 ∈ categories, no otherwise. D30.2 is the single distinct category when only one class is present.
9. Balance: 26,869 train / 5,758 val / 5,758 test [ROW `/size`]. Instance totals: D00 18,201, D10 8,386, D20 7,526, D40 7,554 [CARD]. Shard_000: 74/3,000 empty; images per class 0:1,664, 1:1,202, 2:520, 3:551 [ROW computed]. Card: "Roughly one third of images have no in-taxonomy damage" [CARD]. **Real negatives for "pothole?": yes** (images without class 3). **Caveat:** "empty" images may still contain dropped class-4 damage such as repairs or block cracks [CARD], so do not phrase the question as "any damage?".
10. Per-image fit: multi-label is common. For pick-one, filter to a single class.
11. Personal data: street scenes from six countries may show faces or plates [INFERRED]. Mixed resolutions (drone, motorbike, car). Public benchmark, so overlap is likely [INFERRED].
12. Templates: (a) "Is there a pothole?" yes/no. (b) "Which damage type is present?" (4). (c) "Is there an alligator (fatigue) crack?" yes/no.
13. Confidence: high (licence variant aside).

### D30.3 — `Arpitraj01/Pothole_classification`. Verdict **MAYBE** (label origin)
1. https://huggingface.co/datasets/Arpitraj01/Pothole_classification [CARD]. 2. `license: mit` [CARD]. 3. open. 4. 236.1 MB of JPEG (~0.6 MB each) [CARD api]
5. `/rows` offsets 0/100/200 give `{"image":{"w":3024,"h":4032},"label":0}`, `{…"label":1}`, `{…"label":2}` [ROW]
6. `label` ClassLabel [low, medium, none, severe] [ROW]. 7. UNVERIFIED. The card says only "collected over 50 km road from kerala" [CARD].
8. Rule: label name. 9. Train: low 100, medium 92, none 36, severe 52 [ROW-stats]. "none" gives real negatives for yes/no.
10. One label per image. 11. Phone photos, 3024×4032 [ROW]. People or vehicles may appear [INFERRED]. Severity is a judgement, and the labelling criteria are not documented.
12. "How severe: none/low/medium/severe?"; "Is there a pothole?"; "Is it severe?" yes/no.
13. Failed test: label origin. Severity criteria are undocumented.

### D30.4 / D30.6 — dacl10k (`Voxel51/dacl10k`). Verdict **MAYBE** (label origin not quoted on card)
1. HF: https://huggingface.co/datasets/Voxel51/dacl10k. Toolkit: https://github.com/phiyodr/dacl10k-toolkit. Paper: https://arxiv.org/abs/2309.00460 [CARD]
2. `license: cc-by-4.0` [CARD]. 3. open.
4. 5,211.3 MB; `samples.json` is 64.1 MB (over the 50 MB limit, so it was read with a 3 MB range request). Smallest unit: one JPG [CARD api]
5. Range request into `samples.json` [ROW]:
   - `{"filepath": "data/data_0/dacl10k_v2_train_1394.jpg", "width": 1200, "height": 800, "semseg_ground_truth_filled": {"polylines": [{"label": "Hollowareas", …}]}}`
   - `{"filepath": "data/data_0/dacl10k_v2_train_6451.jpg", "width": 1024, "height": 768, … [{"label": "Drainage"}, {"label": "Drainage"} …]}`
   - `{"filepath": "data/data_0/dacl10k_v2_train_4196.jpg", "width": 3024, "height": 4032, … [{"label": "Spalling"} …]}`
6. `semseg_ground_truth_filled.polylines[].label` (19 classes: 13 damages and 6 objects) [CARD and ROW]
7. Label origin: UNVERIFIED on the card (`annotations_creators: []`). Images come "from databases at authorities and engineering offices" [CARD].
8. Rule: D30.6 is yes if any label is `ExposedRebars`. D30.4 is the single damage label from {Spalling, Rust, Crack, Efflorescence, ExposedRebars, …}.
9. In the first 381 samples: Rust 192, Spalling 183, Weathering 143, Crack 107, Efflorescence 92, PEquipment 73, Cavity 63, Hollowareas 58, Wetspot 55, JTape 48, Drainage 47, ExposedRebars 47, Graffiti 43, Restformwork 41, Bearing 33, ACrack 25, WConccor 22, Rockpocket 18, EJoint 17. Only 2/381 have no label [ROW computed]. Image-level "any damage?" is therefore nearly positives-only, but per-class yes/no has many negatives (e.g. ExposedRebars 47 yes / 334 no).
10. Multi-label is common. Filter to images with exactly one damage class for pick-one.
11. Mixed resolutions up to 3024×4032 [ROW]. Graffiti may contain names [INFERRED].
12. "Is exposed rebar visible?"; "Which damage: spalling / rust / efflorescence / crack?"; "Is there graffiti?"
13. Failed test: label origin. Upgrade if the arXiv paper's annotation section confirms expert annotation (not fetched).

### D30.5 alt — CODEBRIM (Zenodo 2620293). Verdict **GATED** (licence-agreement terms; single archives)
Zenodo API gives licence `other-nc`, `access_right: open` [CARD]. `license.md`: "The researcher has requested permission to use the CODEBRIM database… The researcher shall use the database for non-commercial research and educational purposes only… shall not distribute the database" [CARD]. Files are single archives of 7.9–12.2 GB [CARD api], so it cannot be sampled. The HF mirror `h4tem/codebrim` is a 12.2 GB single zip with no licence [CARD api]; it may be the same data, so treat it as GATED as well. A person must accept the CODEBRIM terms.

### Other checked candidates, not carded (SKIP)
Each was checked [CARD api]:
- `tugberkkalay/autodamageiq-vehicle-damage-dataset`: CarDD (rejected) plus "HITL (GPT-4o labeled)", i.e. machine labels.
- `Naiscorp/car-damage-dataset`: card says "**Unlabeled**".
- `ybli/yolo-railway-track-defect-object-detection` and `ybli/yolo-car-brake-pad-flaw-detection`: README only, 0 files (a mirror with no images).
- `saluslab/Rail-VIVID`: CC BY 4.0, 109 GB of vibration CSVs and frames, no image-level defect labels.
- `KeenForgeAI/NEU-DET-corrected`: "Upstream license: none stated", and 200 px images.
- `tutitata/PCB_COMPONENTS_LABELLED`: no licence, 8.4 GB, partial upload per its card.
- `LouisChen15/ConstructionSite`: `gated=auto`, cc-by-nc-4.0, so GATED (login + accept) at https://huggingface.co/datasets/LouisChen15/ConstructionSite.
- `Synanthropic/reading-analog-gauge`: two zips of 1.2–1.4 GB, the licence file was not read, and the viewer labels are just folder names. Cannot verify.
- `cvtechniques/Road_Damage_Detection_USA`: 13.3 GB plus 444 MB zips (single archive), superseded by dronefreak.

---

## 3. CSV

```csv
domain,task_id,task,dataset,landing_url,repo_id,licence,licence_quote_url,access,total_mb,smallest_fetch_mb,single_archive,sample_proof_url,rows_pasted,label_origin,answer_rule,has_negatives,classes,one_answer_per_image,personal_data_risk,verdict,confidence,unverified_fields
21,D21.1,Steel sheet defect yes/no,Severstal steel defects (Voxel51),https://huggingface.co/datasets/Voxel51/severstal_steel_defects,Voxel51/severstal_steel_defects,UNVERIFIED (Kaggle competition rules),https://www.kaggle.com/competitions/severstal-steel-defect-detection,open,1758,0.2,no,https://huggingface.co/datasets/Voxel51/severstal_steel_defects/resolve/main/samples.json,yes,human (inferred),yes if has_defect,yes (~63%),defect classes 1-4,yes for yes/no; filter len(defect_classes)==1 for pick-one,none,MAYBE,med,licence;label_origin
21,D21.2,Steel defect class,Severstal steel defects (Voxel51),https://huggingface.co/datasets/Voxel51/severstal_steel_defects,Voxel51/severstal_steel_defects,UNVERIFIED,https://www.kaggle.com/competitions/severstal-steel-defect-detection,open,1758,0.2,no,https://huggingface.co/datasets/Voxel51/severstal_steel_defects/resolve/main/samples.json,yes,human (inferred),defect_classes[0] when single,n/a,1;2;3;4,filter single class,none,MAYBE,med,licence;label_origin;class counts
21,D21.3,Commutator crack yes/no,KolektorSDD (box release),https://www.vicos.si/resources/kolektorsdd/,Voxel51/Kolektor_Surface_Defect,CC BY-NC-SA 4.0,https://huggingface.co/datasets/Voxel51/Kolektor_Surface_Defect,open,106.6,0.27,no,https://huggingface.co/datasets/Voxel51/Kolektor_Surface_Defect/resolve/main/samples.json,yes,human,yes if has_defect,yes (347 neg / 52 pos),defect;no defect,yes,none,USE,high,
21,D21.4,Wood surface defect yes/no,Wood surface defects (Kodytek),https://huggingface.co/datasets/iluvvatar/wood_surface_defects,iluvvatar/wood_surface_defects,CC BY 4.0,https://huggingface.co/datasets/iluvvatar/wood_surface_defects,open,2202.9,439.65,no,https://datasets-server.huggingface.co/rows?dataset=iluvvatar/wood_surface_defects&config=default&split=train&offset=5000&length=40,yes,UNVERIFIED,yes if len(objects)>0,yes (~5-7% empty sampled),Live_Knot;Dead_Knot;... (full list UNVERIFIED),filter single label for type,none,MAYBE,med,label_origin;full class list
21,D21.6,Weld good/bad,Welding Defect Object Detection,https://huggingface.co/datasets/rikkarth/welding-defect-object-detection,rikkarth/welding-defect-object-detection,CC0 1.0,https://huggingface.co/datasets/rikkarth/welding-defect-object-detection,open,104.1,0.056,no,https://huggingface.co/datasets/rikkarth/welding-defect-object-detection/resolve/main/coco/test.json,yes,UNVERIFIED,good if categories=={Good Weld}; bad if Bad Weld or Defect and no Good Weld,yes (56/126 test good-only),Bad Weld;Good Weld;Defect,filter (24/126 mixed),none,MAYBE,med,label_origin
22,D22.1,Bare PCB defect yes/no,DeepPCB,https://github.com/tangsanli5201/DeepPCB,,MIT (README adds research-only),https://github.com/tangsanli5201/DeepPCB/blob/master/LICENSE,open,UNVERIFIED,0.023,no,https://raw.githubusercontent.com/tangsanli5201/DeepPCB/master/PCBData/group00041/00041_not/00041000.txt,yes,human (artificial defects),yes for *_test.jpg; no for *_temp.jpg,yes (1500 templates),open;short;mousebite;spur;copper;pin-hole,yes,none,USE,high,total_mb
22,D22.2,Bare PCB defect type,HRIPCB PCB_defect,https://huggingface.co/datasets/RobotHuman/PCB_defect,RobotHuman/PCB_defect,MIT (re-upload; upstream UNVERIFIED),https://huggingface.co/datasets/RobotHuman/PCB_defect,open,960.5,0.002,no,https://datasets-server.huggingface.co/rows?dataset=RobotHuman/PCB_defect&config=default&split=train&offset=300&length=1,yes,generator-like (Photoshop-inserted),distinct object name,no (positives only),missing_hole;mouse_bite;open_circuit;short;spur;spurious_copper,yes,none,MAYBE,med,upstream licence;per-class counts
22,D22.3,Assembled PCB defect type,pcb-defect-segmentation (Roboflow),https://huggingface.co/datasets/keremberke/pcb-defect-segmentation,keremberke/pcb-defect-segmentation,CC BY 4.0,https://huggingface.co/datasets/keremberke/pcb-defect-segmentation,open,9.7,0.155,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/pcb-defect-segmentation&config=full&split=train,yes,UNVERIFIED,single distinct category,no,dry_joint;incorrect_installation;pcb_damage;short_circuit,filter,none,MAYBE,low,label_origin;counts
23,D23.1,Tyre defective/good,Digital images of defective and good condition tyres,https://data.mendeley.com/datasets/bn7ch8tvyp,NMiriams/Good_Tires + NMiriams/Defective_Tires,CC BY 4.0,https://data.mendeley.com/datasets/bn7ch8tvyp,open,2917.7,1.5,no,https://datasets-server.huggingface.co/first-rows?dataset=NMiriams/Defective_Tires&config=default&split=train,yes (image-only; label=repo),human,label = source repo,yes (828 good),good;defective,yes,low,USE,med,annotator identity
23,D23.3,Vehicle make,Stanford Cars (tanganke),https://huggingface.co/datasets/tanganke/stanford_cars,tanganke/stanford_cars,UNVERIFIED,https://huggingface.co/datasets/tanganke/stanford_cars,open,6016.5,470,no,https://datasets-server.huggingface.co/first-rows?dataset=tanganke/stanford_cars&config=default&split=train,yes (weak),UNVERIFIED,make from label name,n/a,196 make-model-year,yes,plates possible,MAYBE,low,licence;label_origin
24,D24.1,Aircraft manufacturer/family,FGVC-Aircraft (Voxel51),https://huggingface.co/datasets/Voxel51/FGVC-Aircraft,Voxel51/FGVC-Aircraft,non-commercial research only (other),https://huggingface.co/datasets/Voxel51/FGVC-Aircraft,open,2775.5,0.08,no,https://huggingface.co/datasets/Voxel51/FGVC-Aircraft/resolve/main/samples.json,yes,UNVERIFIED,manufacturer field,n/a,41 manufacturers;70 families;102 variants,yes,low,MAYBE,med,label_origin
25,D25.1,Rail defect type,Dhika/defect_rail,https://huggingface.co/datasets/Dhika/defect_rail,Dhika/defect_rail,unknown,https://huggingface.co/datasets/Dhika/defect_rail,open,6.3,0.008,no,https://datasets-server.huggingface.co/rows?dataset=Dhika/defect_rail&config=default&split=train&offset=150&length=1,yes,UNVERIFIED,label name,no,corrugation;crack;putus;spalling;squat,yes,none,SKIP,high,licence;label_origin
26,D26.1,Construction machine type,excavator-detector (Roboflow),https://huggingface.co/datasets/keremberke/excavator-detector,keremberke/excavator-detector,CC BY 4.0,https://huggingface.co/datasets/keremberke/excavator-detector,open,193.4,0.161,no,https://datasets-server.huggingface.co/first-rows?dataset=keremberke/excavator-detector&config=full&split=train,yes,UNVERIFIED,single distinct category,n/a,excavators;dump truck;wheel loader,filter,low,MAYBE,med,label_origin;image counts
26,D26.2,Concrete crack yes/no,METU concrete crack images,https://huggingface.co/datasets/mohammadnajeeb/concrete_crack_images,mohammadnajeeb/concrete_crack_images,CC BY 4.0,https://huggingface.co/datasets/mohammadnajeeb/concrete_crack_images,open,244.9,49.06,no,https://datasets-server.huggingface.co/rows?dataset=mohammadnajeeb/concrete_crack_images&config=default&split=train&offset=12000&length=1,yes,UNVERIFIED,yes if Positive,yes (12000/12000),Negative;Positive,yes,none,SKIP,high,label_origin
26,D26.3,Rebar count,ROI-1555 rebar,https://huggingface.co/datasets/tsrobcvai/ROI-1555_Rebar_Detection_and_Instance_Segmentation_Dataset,tsrobcvai/ROI-1555_Rebar_Detection_and_Instance_Segmentation_Dataset,UNVERIFIED,https://huggingface.co/datasets/tsrobcvai/ROI-1555_Rebar_Detection_and_Instance_Segmentation_Dataset,open,586.5,0.06,no,https://datasets-server.huggingface.co/first-rows?dataset=tsrobcvai/ROI-1555_Rebar_Detection_and_Instance_Segmentation_Dataset&config=default&split=test,yes,UNVERIFIED,count shapes,n/a,straight-N (semantics UNVERIFIED),count,none,MAYBE,low,licence;label semantics
27,D27.1,Gauge reading,Meter_Reading (synthetic),https://huggingface.co/datasets/goodcoffee/Meter_Reading,goodcoffee/Meter_Reading,Apache-2.0,https://huggingface.co/datasets/goodcoffee/Meter_Reading,open,2449.3,0.022,no,https://datasets-server.huggingface.co/first-rows?dataset=goodcoffee/Meter_Reading&config=default&split=train,yes,generator,answer = synth_dial_value,n/a,continuous value,yes,none,USE,med,value diversity
27,D27.1,Gauge reading,synthetic-gauges-v6,https://huggingface.co/datasets/moondream/synthetic-gauges-v6,moondream/synthetic-gauges-v6,UNVERIFIED (none on card),https://huggingface.co/datasets/moondream/synthetic-gauges-v6,open,20578.5,458.4,no,https://datasets-server.huggingface.co/first-rows?dataset=moondream/synthetic-gauges-v6&config=default&split=train_0,yes,generator,answer = facts.units.outer.value,n/a,continuous,yes,none,MAYBE,med,licence
27,D27.2,Water meter reading,Watermeter,https://huggingface.co/datasets/rsnogueira/Watermeter,rsnogueira/Watermeter,UNVERIFIED (none on card),https://huggingface.co/datasets/rsnogueira/Watermeter,open,1104.6,0.289,no,https://huggingface.co/datasets/rsnogueira/Watermeter/resolve/main/data.csv,yes,UNVERIFIED,answer = value,n/a,continuous,yes,low,MAYBE,low,licence;label_origin
27,D27.2,Water meter reading,UniData water meters preview,https://huggingface.co/datasets/UniDataPro/water-meters,UniDataPro/water-meters,CC BY-NC-ND 4.0 (preview of paid set),https://huggingface.co/datasets/UniDataPro/water-meters,open,17.3,0.005,no,UNVERIFIED,no,UNVERIFIED,UNVERIFIED,n/a,UNVERIFIED,UNVERIFIED,low,MAYBE,low,rows;schema;origin
27,D27.3,Electricity meter reading,ElectricityMeterReadings1o4,https://huggingface.co/datasets/Praekelt/ElectricityMeterReadings1o4,Praekelt/ElectricityMeterReadings1o4,UNVERIFIED (none on card),https://huggingface.co/datasets/Praekelt/ElectricityMeterReadings1o4,open,44.2,44.2,no,https://datasets-server.huggingface.co/first-rows?dataset=Praekelt/ElectricityMeterReadings1o4&config=default&split=train,yes,UNVERIFIED,answer = reading,n/a,continuous,yes,low,MAYBE,low,licence;label_origin
27,D27.4,Meter type,utilitimetersai annotated dials,https://huggingface.co/datasets/utilitimetersai/Annotated-Mechanical-And-LCD-Utility-Meter-Dials-Dataset,utilitimetersai/Annotated-Mechanical-And-LCD-Utility-Meter-Dials-Dataset,CC BY-NC 4.0,https://huggingface.co/datasets/utilitimetersai/Annotated-Mechanical-And-LCD-Utility-Meter-Dials-Dataset,manual approval,3.2,0.002,no,none (401),no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,GATED,low,most fields
27,D27.1,Gauge reading,synthetic-analog-gauges,https://huggingface.co/datasets/Mileeena/synthetic-analog-gauges,Mileeena/synthetic-analog-gauges,CC BY 4.0,https://huggingface.co/datasets/Mileeena/synthetic-analog-gauges,login,2545.4,0.138,no,none (401),no,generator (inferred),UNVERIFIED,n/a,UNVERIFIED,UNVERIFIED,none,GATED,low,most fields
28,D28.1,PV cell EL defect yes/no,ELPV,https://github.com/zae-bayern/elpv-dataset,bardroh/elpv-el-defects,CC BY-NC-SA 4.0,https://github.com/zae-bayern/elpv-dataset,open,90.3,9.1,no,https://raw.githubusercontent.com/zae-bayern/elpv-dataset/master/src/elpv_dataset/data/labels.csv,yes,human (inferred),yes if prob==1.0; no if 0.0,yes (1508 neg),prob 0/0.33/0.67/1; mono/poly,yes,none,MAYBE,med,label_origin
28,D28.2,Broken insulator yes/no,Powerline components and faults,https://huggingface.co/datasets/docmhvr/powerline-components-and-faults,docmhvr/powerline-components-and-faults,MIT,https://huggingface.co/datasets/docmhvr/powerline-components-and-faults,open,122.2,2.29,no,https://datasets-server.huggingface.co/first-rows?dataset=docmhvr/powerline-components-and-faults&config=default&split=train,yes,human,yes if 'Broken Insulator' in labels; no if Insulators present without it,yes (830 neg / 663 pos),Broken Cable;Broken Insulator;Cable;Insulators;Tower;Vegetation,yes (presence),none,USE,high,augmentation duplicates
28,D28.3,Broken cable yes/no,Powerline components and faults,https://huggingface.co/datasets/docmhvr/powerline-components-and-faults,docmhvr/powerline-components-and-faults,MIT,https://huggingface.co/datasets/docmhvr/powerline-components-and-faults,open,122.2,2.29,no,https://datasets-server.huggingface.co/first-rows?dataset=docmhvr/powerline-components-and-faults&config=default&split=train,yes,human,yes if 'Broken Cable' in labels,yes (887 neg / 907 pos),same,yes (presence),none,USE,high,augmentation duplicates
28,D28.2,Broken insulator,broken-insulators-synthetic,https://huggingface.co/datasets/silera/broken-insulators-synthetic-detection,silera/broken-insulators-synthetic-detection,CC BY 4.0,https://huggingface.co/datasets/silera/broken-insulators-synthetic-detection,open,221.7,0.006,no,https://datasets-server.huggingface.co/first-rows?dataset=silera/broken-insulators-synthetic-detection&config=default&split=train,yes,generator (images),count boxes,no,UNVERIFIED names,yes,none,MAYBE,low,category names;negatives
28,D28.4,Solar panel condition,solar-panel-inspection,https://huggingface.co/datasets/metalmerge/solar-panel-inspection,metalmerge/solar-panel-inspection,UNVERIFIED (none),https://huggingface.co/datasets/metalmerge/solar-panel-inspection,open,247.8,0.3,no,https://huggingface.co/api/datasets/metalmerge/solar-panel-inspection,folder listing only,UNVERIFIED,answer = folder name,yes (Clean),Bird-drop;Clean;Dusty;Snow-Covered;Electrical-damage;Physical-Damage,yes,low,MAYBE,low,licence;origin
28,D28.5,Wind turbine present,Airbus Wind Turbine Patches,https://www.kaggle.com/datasets/airbusgeo/airbus-wind-turbines-patches,jonathan-roberts1/Airbus-Wind-Turbines-Patches,CC BY-NC-SA 4.0,https://huggingface.co/datasets/jonathan-roberts1/Airbus-Wind-Turbines-Patches,open,147.7,147.7,yes,https://datasets-server.huggingface.co/rows?dataset=jonathan-roberts1/Airbus-Wind-Turbines-Patches&config=default&split=train&offset=71000&length=1,yes,UNVERIFIED,label,yes,no wind turbine;wind turbine,yes,none,SKIP,high,label_origin
28,D28.6,Thermal hotspot,Solar-Panel-Thermal-Drone-UAV-Images,https://huggingface.co/datasets/Manishsahu53/Solar-Panel-Thermal-Drone-UAV-Images,Manishsahu53/Solar-Panel-Thermal-Drone-UAV-Images,Apache-2.0,https://huggingface.co/datasets/Manishsahu53/Solar-Panel-Thermal-Drone-UAV-Images,open,19093.5,2250.9,yes,https://datasets-server.huggingface.co/first-rows?dataset=Manishsahu53/Solar-Panel-Thermal-Drone-UAV-Images&config=default&split=train,no labels,none,cannot compute,UNVERIFIED,none,UNVERIFIED,none,SKIP,high,labels
29,D29.1,Corrosion present/type,RF100 corrosion,https://universe.roboflow.com/roboflow-100/corrosion-bi3q3,LibreYOLO/corrosion-bi3q3,CC BY 4.0,https://huggingface.co/datasets/LibreYOLO/corrosion-bi3q3,open,67.4,0.001,no,https://huggingface.co/datasets/LibreYOLO/corrosion-bi3q3/raw/main/test/labels/KwanLoneDSCN1716_JPG_jpg.rf.554fa608f97c8382b117b87f478ba00a.txt,yes,UNVERIFIED,yes if class 1 present,few (5/105 test empty),Slippage;corrosion;crack,filter,none,MAYBE,low,label_origin;counts
29,D29.2,Sewer defect type,sewer-defect-crack-dataset,https://huggingface.co/datasets/ZhiyaYang/sewer-defect-crack-dataset,ZhiyaYang/sewer-defect-crack-dataset,UNVERIFIED (none),https://huggingface.co/datasets/ZhiyaYang/sewer-defect-crack-dataset,open,194.5,31.1,no,https://datasets-server.huggingface.co/first-rows?dataset=ZhiyaYang/sewer-defect-crack-dataset&config=default&split=train,yes,UNVERIFIED,label name,no,blockage;corrosion;crack,yes,none,MAYBE,low,licence;origin
29,D29.2,Sewer defect type,Sewer-pipe-defects,https://huggingface.co/datasets/SRuibo/Sewer-pipe-defects,SRuibo/Sewer-pipe-defects,CC BY 4.0,https://huggingface.co/datasets/SRuibo/Sewer-pipe-defects,open,2374.1,0.001,no,https://huggingface.co/datasets/SRuibo/Sewer-pipe-defects/raw/main/Sewer%20pipe%20defects/labels/train/PL_186_000.txt,yes,UNVERIFIED,single distinct class code,no (0 empty label files),CK;PL;SG;SL;TL;ZW (meanings UNVERIFIED),filter,none,MAYBE,low,class semantics;origin
29,D29.3,Gas plume present,GasLeakPlumes,https://huggingface.co/datasets/samhormozian/GasLeakPlumes,samhormozian/GasLeakPlumes,UNVERIFIED (none),https://huggingface.co/datasets/samhormozian/GasLeakPlumes,open,706.5,2.996,no,https://huggingface.co/datasets/samhormozian/GasLeakPlumes/resolve/main/dataset%20copy/annotations.json,yes,UNVERIFIED,yes if annotated,no (5487/5515 positive),Gas Leak Day;Gas Leak night,yes,none,SKIP,high,licence
30,D30.1,Pothole yes/no,RDD2022,https://github.com/sekilab/RoadDamageDetector,dronefreak/RDD2022,CC BY 4.0 (Figshare) / CC BY-SA 4.0 (HF card),https://figshare.com/articles/dataset/RDD2022_-_The_multi-national_Road_Damage_Dataset_released_through_CRDDC_2022/21431547,open,11078.8,0.37,no (HF) / yes official 13264 MB,https://huggingface.co/datasets/dronefreak/RDD2022/resolve/main/data/images/train/shard_000/metadata.jsonl,yes,human,yes if category 3 present,yes,longitudinal;transverse;alligator;pothole,yes for presence,faces/plates possible,USE,high,licence variant
30,D30.2,Road damage type,RDD2022,https://github.com/sekilab/RoadDamageDetector,dronefreak/RDD2022,CC BY 4.0 / CC BY-SA 4.0,https://figshare.com/articles/dataset/RDD2022_-_The_multi-national_Road_Damage_Dataset_released_through_CRDDC_2022/21431547,open,11078.8,0.37,no,https://huggingface.co/datasets/dronefreak/RDD2022/resolve/main/data/images/train/shard_000/metadata.jsonl,yes,human,single distinct category,n/a,D00;D10;D20;D40,filter single class,faces/plates possible,USE,high,licence variant
30,D30.3,Pothole severity,Pothole_classification,https://huggingface.co/datasets/Arpitraj01/Pothole_classification,Arpitraj01/Pothole_classification,MIT,https://huggingface.co/datasets/Arpitraj01/Pothole_classification,open,236.1,0.6,no,https://datasets-server.huggingface.co/rows?dataset=Arpitraj01/Pothole_classification&config=default&split=train&offset=100&length=1,yes,UNVERIFIED,label name,yes (none=36),low;medium;none;severe,yes,low,MAYBE,med,label_origin;severity criteria
30,D30.4,Bridge damage type,dacl10k,https://github.com/phiyodr/dacl10k-toolkit,Voxel51/dacl10k,CC BY 4.0,https://huggingface.co/datasets/Voxel51/dacl10k,open,5211.3,0.14,no,https://huggingface.co/datasets/Voxel51/dacl10k/resolve/main/samples.json (range 0-3MB),yes,UNVERIFIED,single damage label / presence per class,per-class yes; image-level no (2/381 empty),19 classes (13 damage + 6 objects),filter,graffiti text,MAYBE,med,label_origin
30,D30.5,Concrete defect,CODEBRIM,https://zenodo.org/records/2620293,h4tem/codebrim (mirror),other-nc + terms agreement,https://zenodo.org/records/2620293/files/license.md,form or terms agreement,36361,7907.8,yes,none,no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,none,GATED,med,rows
26,D26.4,Construction site VQA,ConstructionSite,https://huggingface.co/datasets/LouisChen15/ConstructionSite,LouisChen15/ConstructionSite,CC BY-NC 4.0,https://huggingface.co/datasets/LouisChen15/ConstructionSite,login,4497.7,1375.1,no,none (401),no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,workers visible,GATED,low,most fields
```

---

## Part C. Question expansion recipes (USE candidates only)

**Common Tier C rules for all USE datasets.**
- Every model-written question is stored with `label_origin: model` and kept in a separate table. It is never scored together with Tier A or Tier B.
- A second model from a different vendor must answer each question independently and agree before the question is kept.
- The model under test never writes or validates questions for itself.
- The most useful Tier C outputs are:
  - rewordings of the Tier A question (plain operator language, e.g. "Would you scrap this part?");
  - harder distractors, e.g. visually similar defect names;
  - natural-language variety.
- Tier C never introduces new facts.

### KolektorSDD (D21.3)
- **Tier A:** "Does this surface show a crack?", answered from `has_defect`.
- **Tier B:**
  1. Board-level: "Do any of the 8 surfaces of board kosNN show a defect?" Answer = any(`has_defect`) grouped by `board_id`.
  2. "Which of these two images (same board) is defective?" The pair has one defective and one clean image.
  3. "How many of these k images are defective?" Count of `has_defect`.
  4. Defect size bucket "small / large" from the mask area of `ground_truth`. This requires decoding the mask but no person looking.
- **Tier C:** reword as an accept/reject decision, or ask a model to describe the crack location. That is not trusted.

### DeepPCB (D22.1)
- **Tier A:** test image means yes, template means no.
- **Tier B:**
  1. "Is there an open-circuit defect?" (type 1 ∈ lines).
  2. "Which defect type is most frequent here?" Use the argmax of the type counts, keeping only images with a unique max.
  3. "How many defects: 1–3 / 4–7 / 8+?" (line count).
  4. "Which defect type is NOT present: open / short / spur / pin-hole?" Use images where exactly one of the 4 types is absent.
  5. "Is there a defect in the top-left quadrant?" From the box coordinates.
- **Tier C:** distractor names such as "solder bridge" or "lifted pad" to test vocabulary robustness.

### Tyres (D23.1)
- **Tier A:** good vs defective.
- **Tier B:** the schema has only one label, so Tier B is limited to two forms. (1) A paired question: "Which of these two tyres is defective?" (one from each repo). (2) A set count: "How many of these 4 tyres are defective?"
- **Tier C:** ask a model to name the defect type (crack, bulge, tread wear) as an *untrusted* label. This needs dual-model agreement and is never scored as truth.

### Powerline components and faults (D28.2/D28.3)
- **Tier A:** broken insulator yes/no and broken cable yes/no.
- **Tier B:**
  1. "How many insulators (class 3 + class 1) are visible: 1–2 / 3–5 / 6+?"
  2. "Is vegetation present near the line?" (class 5).
  3. "Is a tower visible?" (class 4).
  4. "Which fault is present: broken insulator only / broken cable only / both / neither?" From label sets.
  5. "Are there more cables than insulators?" Compare the counts.
- **Tier C:** severity wording ("Should this span be scheduled for repair?") and distractor faults such as "flashover marks" or "bird nest". Untrusted.

### Synthetic meter reading (D27.1)
- **Tier A:** "What does the gauge read?" Answer = `synth_dial_value`, with 3 distractors at ±1–3 minor ticks.
- **Tier B:**
  1. "What is the maximum value on the scale?" (from `range_answer`/`minmax_answer`).
  2. "Is the reading above half of full scale?" (value vs (min+max)/2).
  3. "Is the reading below zero / below the minimum mark?" (value < min).
  4. "Which quarter of the scale is the needle in?" (4 bins).
  5. "Is the needle in the right half of the image?" (`needle_bbox` centre x > width/2).
- **Tier C:** unit wording (bar, psi), operator phrasing ("Is pressure within 0–8?") and rounding variants. Untrusted.

### RDD2022 (D30.1/D30.2)
- **Tier A:** pothole yes/no, and the damage type for single-class images.
- **Tier B:**
  1. "Is there any crack (D00, D10 or D20)?"
  2. "How many damage instances: 0 / 1–2 / 3+?"
  3. "Which damage type is NOT present (from 4)?" Use images with exactly 3 types absent and 1 present, or the reverse.
  4. "Is the damage mostly longitudinal or transverse?" Compare counts of class 0 vs class 1.
  5. "Which country/platform is this?" (from the `file_name` prefix, e.g. China_Drone). This is metadata, not damage, so use it as a control.
- **Tier C:** reword as maintenance priority ("Does this need urgent repair?"). Untrusted, because it is a judgement. Distractors can be "rutting" or "patch".

---

## 4. Gaps

| task | why no acceptable dataset | drawn/generator version realistic? how |
|---|---|---|
| D21.7 assembly completeness (missing screw/clip) | MVTec LOCO and AD 2 are rejected. No open, licensed, sampled alternative found in this session | **Yes**: render CAD assemblies (Blender/BlenderProc) with parts randomly removed. Store the removed part list as the answer |
| D22.4 component presence | `tutitata/PCB_COMPONENTS_LABELLED` has no licence and is a partial upload | **Partly**: procedurally generate board layouts with KiCad, then render with known component lists |
| D22.5 solder joint quality | none found | Hard to draw realistically. Needs human photos |
| D23.4 vehicle body damage | DrBimmer used, CarDD rejected, AutoDamageIQ uses GPT-4o labels and CarDD | No (photoreal damage is hard). Needs a new human-labelled source |
| D23.5 dashboard warning light | none found | **Yes**: composite ISO 2575 icons onto rendered cluster backgrounds. The icon set is the answer |
| D23.6 brake-pad wear | `ybli` repo is empty | Partly: render pad thickness from known mm values |
| D24.2–D24.5 aviation skin corrosion, borescope, FOD, aircraft tyre | none found on HF. FOD-A (GitHub) was not probed | Corrosion: no. FOD: **yes**, composite known objects onto runway photos and keep the object list as the answer. Borescope: no |
| D25.2–D25.4 rail obstruction, fasteners, catenary | RailSem19 needs a form [UNVERIFIED, not fetched]. `aurora0403/Railway_Foreign_Object_Dataset` was not probed | Fasteners: **yes**, render a sleeper with clips present or absent. Obstruction: composite objects onto track frames |
| D26.4 construction stage | ConstructionSite is GATED | No. Needs human photos |
| D27.4 meter type | only a GATED candidate | **Yes**: render mechanical-odometer vs LCD meter faces |
| D27.5 needle in red zone | derived from D27.1 generator (Tier B) | **Yes**: already covered by goodcoffee and moondream generators |
| D28.5 wind blade damage | only 128 px turbine-presence patches. `ybli` wind-blade repo not probed | No |
| D28.6 PV thermal hotspot | the Manishsahu53 set is unlabeled | Partly: synthetic thermal grids with hot cells at known positions (diagram-like) |
| D29.4 oil spill, D29.5 conveyor belt | not probed / none found | Belt: no. Oil spill (SAR): no |
| D21.1/2 Severstal licence | Kaggle rules not readable without login | n/a. A person should read the competition rules |

## 5. Cannot verify
- **Kaggle licences and rules.** The Severstal competition rules returned API 401. Only public dataset metadata (tyres) was readable.
- **Annotation method for these datasets.** The cards and the text I fetched do not say how the labels were made: wood surface defects (F1000 paper text did not yield a box-annotation statement), ELPV (README says only "annotated"), dacl10k (`annotations_creators: []`), FGVC-Aircraft, excavator-detector, welding, RF100 corrosion, Pothole_classification, the sewer sets and the meter sets.
- **DeepPCB total repo size.** The GitHub API call failed in this session.
- **RDD2022 official S3 file list.** Returned AccessDenied. The Figshare (CC BY 4.0) and HF card (CC BY-SA 4.0) licence statements conflict.
- **Missing rows.** UniDataPro water-meters `/first-rows` returned 500. RF100 corrosion `/first-rows` returned 500, so raw label files were used instead.
- **Not opened.** The full class list for the wood dataset; per-class image counts for HRIPCB, keremberke PCB and excavator; the CODEBRIM contents; FOD-A, RailSem19, the Railway_Foreign_Object_Dataset, and oil-spill sets.
- **Value-reason sources.** Most come from search-result snippets and are tagged [UNVERIFIED-snippet]. The pages were not opened, and many tasks have "No source fetched".
