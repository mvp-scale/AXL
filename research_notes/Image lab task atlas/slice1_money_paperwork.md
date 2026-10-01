# Slice 1: Money and paperwork (domains 1–10)

Research date: 2026-10-01. Every licence, size, class list and row below was fetched in this session from the Hugging Face Hub API (`/api/datasets/<id>?blobs=true`), datasets-server (`/splits`, `/info`, `/first-rows`, `/rows`, `/statistics`), raw dataset cards (`/raw/main/README.md`), small annotation files (each under 50 MB), the Kaggle public API landing JSON, and owner or regulator pages. Image bytes were never downloaded, apart from small annotation files.

Evidence tags: `[ROW]` = seen in a fetched row or annotation file; `[CARD]` = read on the owner's page, card or file listing; `[PAPER]` = paper or owner's readme shipped with the data; `[INFERRED]` = my reasoning; `[UNVERIFIED]` = not confirmed.

**Domain swaps:** none. Domains 5 (health billing), 6 (legal), 9 (customs half) and 10 (HR) are thin on open, licensed, labelled image data. I kept them and recorded the holes in Gaps, with generator plans, because the domains that would have replaced them belong to other slices.

**USE rule applied:** a candidate is rated USE only if it has a stated licence, open access, rows I pasted myself, labels made by a human or a generator, an answer rule that needs no one to look at the image, and real negatives for yes/no tasks. Non-commercial licences (CC-BY-NC-SA) are flagged but do not by themselves block USE for a research test bench.

---

## 1. Task atlas

### D1 Banking and payments documents
| id | task | typed question | options | image type | value reason (one source) |
|---|---|---|---|---|---|
| D1.1 | Cheque issuing bank | "Which bank's cheque is this?" | Axis / Canara / ICICI / Syndicate | scan | Check fraud is a leading fraud type: check-fraud Suspicious Activity Reports (SARs) nearly doubled to over 680,000 in 2022 ([FinCEN alert FIN-2023-Alert003, via ABA Banking Journal](https://bankingjournal.aba.com/2023/02/fincen-issues-alert-for-check-fraud-via-usps/)). Routing the cheque to the right bank template comes first. |
| D1.2 | Courtesy and legal amount agree | "Does the amount in words match the amount in figures?" | yes / no | scan | Same FinCEN source: altered cheques lead the list of check-fraud methods ([ACAMS](https://www.acams.org/en/news/fincen-lists-check-fraud-methods-alteration-tops-the-list)). |
| D1.3 | Cheque signed | "Is the drawer's signature present?" | yes / no | scan | Same FinCEN source. An unsigned item is returned (no separate source fetched). |
| D1.4 | Cheque stale-dated | "Is the cheque date more than 6 months before <reference date>?" | yes / no | scan | No source fetched. |
| D1.5 | Statement type | "Is this a bank-account statement or a credit-card statement?" | bank statement / credit card | scan, PDF render | No source fetched. Statement intake for lending and KYC is a common vendor use case, with no primary source found. |
| D1.6 | Transaction table on page | "Does this statement page contain a transaction table?" | yes / no | PDF render | No source fetched. |

### D2 Accounting and accounts payable
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D2.1 | Receipt total | "Which amount is the receipt's final total?" | 4 amounts printed on the receipt | scan | APQC cross-industry median cost to process accounts payable is $6.00 per invoice. The bottom quartile pays $10 or more ([APQC via CFO.com](https://www.cfo.com/news/metric-of-the-month-accounts-payable-cost/659393/)). |
| D2.2 | Payment method | "How was this receipt paid?" | cash / card / contactless / mobile wallet | photo (simulated) | Same APQC source (expense audit). |
| D2.3 | Receipt country | "Which country is this receipt from?" | US / UK / DE / IT / FR | photo (simulated) | Same APQC source. Country decides the VAT reclaim rules [INFERRED]. |
| D2.4 | PO reference present | "Does this invoice show a purchase-order number?" | yes / no | rendered scan | Same APQC source. Three-way match needs a PO [INFERRED]. |
| D2.5 | Hijri-dated invoice | "Is the invoice date written in the Hijri calendar?" | yes / no | rendered scan | Same APQC source. |
| D2.6 | Line-item count | "How many line items does this invoice list?" | 1 / 2 / 3 / 4 / 5+ | rendered scan | Same APQC source. |

### D3 Insurance, motor
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D3.1 | Vehicle damaged | "Is this car visibly damaged?" | yes / no | photo | The Coalition Against Insurance Fraud estimates insurance fraud at $308.6 B a year across all lines ([Reinsurance News](https://www.reinsurancene.ws/insurance-fraud-costs-308-6bn-annually-coalition-reports/); critics question the method, per [Rutgers CRR](https://crr.rutgers.edu/wp-content/uploads/sites/22/Misinformation-About-Insurance-Fraud-11-2024.pdf)). Photo triage of first notice of loss (FNOL) is the first gate. |
| D3.2 | Which end is shown | "Is this the front or the rear of the car?" | front / rear | photo | Same source. Point of impact must match the claim [INFERRED]. |
| D3.3 | Damage kind | "What damage is visible?" | none / breakage / crushed | photo | Same source. |
| D3.4 | Damage type | "Which damage type is shown?" | crack / dent / glass shatter / lamp broken / scratch / flat tyre | photo | Same source. |
| D3.5 | Body style | "What body style is this vehicle?" | sedan / SUV / coupe / convertible / hatchback / wagon | photo | No source fetched. Underwriting checks vehicle type. |
| D3.6 | Odometer reading | "Which reading does the odometer show?" | 4 numeric options | photo | No source fetched. |

### D4 Insurance, property and catastrophe
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D4.1 | Damage severity | "How severe is the damage to buildings or infrastructure?" | little or none / mild / severe | photo (ground level, social media) | Global insured nat-cat losses were USD 137 B in 2024 ([Swiss Re sigma 1/2025](https://www.swissre.com/institute/research/sigma-research/sigma-2025-01-natural-catastrophes-trend.html)). |
| D4.2 | Disaster type | "What kind of disaster is shown?" | earthquake / flood / hurricane / fire / landslide / none | photo | Same Swiss Re source. Peril assignment drives the claim route [INFERRED]. |
| D4.3 | Infrastructure damage | "Does the image show damage to buildings, roads or utilities?" | yes / no | photo | Same Swiss Re source. |
| D4.4 | Flooding | "Is flooding visible?" | yes / no | photo | Same Swiss Re source. |
| D4.5 | Roof damage (ground level) | "Is the roof damaged?" | yes / no | photo | Same source. No dataset (see Gaps). |

### D5 Insurance, health and medical billing documents (no diagnosis)
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D5.1 | Claim form type | "Which claim form is this?" | CMS-1500 / UB-04 / 1040 / I-9 / other | scan | The FY2024 Medicare FFS improper payment rate is 7.66%, or $31.70 B ([CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/fiscal-year-2024-improper-payments-fact-sheet)). |
| D5.2 | Medication count on prescription | "How many medications are listed?" | 1 / 2 / 3 / 4+ | scan or render | Same CMS source. |
| D5.3 | Claim form signed | "Is the patient or physician signature box filled?" | yes / no | scan | Same CMS source. Missing documentation is a main improper-payment cause [UNVERIFIED]. |
| D5.4 | Itemised bill | "Is this bill itemised by service line?" | yes / no | scan | Same CMS source. |
| D5.5 | Insurance card plan type | "Which plan type is printed on the member card?" | HMO / PPO / EPO / POS / other | photo | Same source. No dataset. |

### D6 Legal and contracts
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D6.1 | Signed | "Is the document page signed?" | yes / no | scan | Poor contract management costs the average business almost 9% of annual revenue ([WorldCC, via CFO.com](https://www.cfo.com/press-release/20250819-the-multi-million-dollar-leak-in-your-contracts-and-how-to-stop-it/)). |
| D6.2 | Page category | "What kind of document is this page from?" | laws & regulations / financial report / government tender / manual / patent / scientific article | scan or render | Same WorldCC source (routing for legal review). |
| D6.3 | Table present | "Does this page contain a table?" | yes / no | render | Same source. Schedules of fees and obligations sit in tables [INFERRED]. |
| D6.4 | Stamp or seal present | "Does the page carry a stamp or seal?" | yes / no | scan | Same source. No usable dataset. |
| D6.5 | Redaction present | "Is any text redacted (black-boxed)?" | yes / no | scan | Same source. No dataset. |

### D7 Government forms and permits
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D7.1 | Checkbox state | "Is the box for <question> ticked Yes or No?" | yes / no | scan of government form | The APQC public-sector median is $9.43 per invoice, the costliest industry ([APQC via CFO.com](https://www.cfo.com/news/metric-of-the-month-accounts-payable-cost/659393/)). This is a proxy for public paperwork cost. A form-specific source was not found. |
| D7.2 | Government tender page | "Is this page from a government tender?" | yes / no | render | Same proxy source. |
| D7.3 | Unanswered field | "Does this form contain a question with no answer filled in?" | yes / no | scan | No source fetched. |
| D7.4 | Is it a form | "Is this document a form, a letter, a memo, an invoice or a report?" | form / letter / memo / invoice / report | scan | No source fetched. |
| D7.5 | Permit validity | "Is the permit's expiry date before <reference date>?" | yes / no | scan | No dataset. |

### D8 Identity and KYC (specimen or synthetic documents only)
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D8.1 | Printed sex field | "What sex is printed on this (synthetic) ID card?" | M / F (LAKI-LAKI / PEREMPUAN) | render | FATF requires verifying identity with "reliable, independent" documents, data or information ([FATF Digital ID guidance](https://www.fatf-gafi.org/media/fatf/documents/recommendations/pdfs/Guidance-on-Digital-Identity-report.pdf)). |
| D8.2 | Date consistency | "Is the expiry date later than the issue date?" | yes / no | photo or scan (synthetic) | Same FATF source. Inconsistent dates flag a forgery [INFERRED]. |
| D8.3 | Nationality or issuing country | "Which nationality is printed?" | 4–6 countries | photo (synthetic) | Same FATF source. |
| D8.4 | Tampered document | "Has this ID document been tampered with?" | yes / no | scan (synthetic) | Same FATF source. |
| D8.5 | Document type | "Is this a passport or an ID card?" | passport / ID card | photo (specimen) | Same FATF source. |
| D8.6 | ID present in photo | "Is there an Indonesian KTP card in this photo?" | yes / no | photo | Same FATF source. |

### D9 Tax and customs documents
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D9.1 | Tax form page | "Which tax form page is this?" | e.g. 1040 p1 / 1040 p2 / Sch A / Sch B / Sch E p1 / Sch D p2 | scan | The IRS projected gross tax gap for TY2022 is $696 B, with underreporting at 77% ([IRS IR-2024-262](https://irs.gov/newsroom/irs-releases-2022-tax-gap-projections-voluntary-compliance-rate-among-taxpayers-remains-steady)). |
| D9.2 | W-2 state | "Which state is in box 15 (first line)?" | 4 state codes | render | Same IRS source. |
| D9.3 | W-2 box 13 | "Is the 'statutory employee' box in box 13 ticked?" | yes / no | render | Same IRS source. |
| D9.4 | IRS form family | "Which IRS form is this?" | 1040 / W-2 / W-4 / W-9 / 1099-NEC / 941 | render | Same IRS source. |
| D9.5 | Customs declaration goods category | "Which category is ticked on the CN22/CN23?" | gift / documents / commercial sample / returned goods / other | scan | WCO Time Release Study measures release time and is endorsed by WTO TFA Art. 7.6 ([WCO TRS excerpt](https://www.carecprogram.org/uploads/Day2-WCO-Time-Release-Study.pdf)). No dataset. |

### D10 HR and recruiting
| id | task | typed question | options | image type | value reason |
|---|---|---|---|---|---|
| D10.1 | I-9 form completeness | "Is Section 2 of the I-9 signed?" | yes / no | scan | I-9 paperwork violations draw per-form fines ([Experian Employer Services summary](https://www.experian.com/blogs/employer-services/how-to-avoid-form-i-9-fines-and-violations/); amounts there are secondary and change yearly) [UNVERIFIED primary]. |
| D10.2 | Business card has email | "Does this business card show an email address?" | yes / no | photo (simulated) | No source fetched. |
| D10.3 | Business card has mobile number | "Does this card list a mobile number?" | yes / no | photo (simulated) | No source fetched. |
| D10.4 | Timesheet total hours | "What total hours does the timesheet show?" | 4 numeric options | scan | No dataset. |
| D10.5 | Badge expired | "Is the badge expiry date before <reference date>?" | yes / no | photo | No dataset. |

---

## 2. Dataset cards

### D1.1 — candidate 1: jaganadhg/cheque-synthetic-images (IDRBT synthetic cheques) — **USE**
1. **Landing:** https://huggingface.co/datasets/jaganadhg/cheque-synthetic-images. File listing: https://huggingface.co/datasets/jaganadhg/cheque-synthetic-images/tree/main/data. Repo id `jaganadhg/cheque-synthetic-images` [CARD].
2. **Licence:** card YAML `license: apache-2.0` [CARD] (https://huggingface.co/datasets/jaganadhg/cheque-synthetic-images/raw/main/README.md). The card does not forbid research or testing. It notes the source "IDRBT Cheque Image Dataset… original TIFF images are **not** distributed" [CARD]. The IDRBT source terms were not checked [UNVERIFIED].
3. **Access:** open (API `gated: False`) [CARD].
4. **Size:** 466.1 MB total. Smallest unit: `data/validation-00000-of-00001.parquet` 76.11 MB, and test 95.25 MB [CARD]. Both exceed 50 MB, so sample through `/rows`.
5. **Sample-first proof:** `https://datasets-server.huggingface.co/first-rows?dataset=jaganadhg/cheque-synthetic-images&config=default&split=train` [ROW]
   - `{"image_id":"axis_syn_0086","bank":"axis","image_width":2365,"image_height":1065,"date":{"xmin":1694,"ymin":89,"xmax":2346,"ymax":229},"amount":{"xmin":1672,"ymin":425,"xmax":2308,"ymax":548},"sign":{"xmin":1803,"ymin":617,"xmax":2294,"ymax":927},...}`
   - `{"image_id":"axis_syn_0035","bank":"axis","image_width":2365,"image_height":1065,"amount":{"xmin":1677,"ymin":375,"xmax":2315,"ymax":525},"sign":{"xmin":2001,"ymin":660,"xmax":2303,"ymax":882},...}`
   - `{"image_id":"syndicate_syn_0004","bank":"syndicate","image_width":2365,"image_height":1100,"ifsc":{"xmin":781,"ymin":134,"xmax":1100,"ymax":215},...}`
6. **Schema:** `image_id` str, `filename` str, `bank` str (template bank), `image_width/height` int, `image`, and six boxes `date`, `amount`, `ifsc`, `acno`, `sign`, `name`, each `{xmin,ymin,xmax,ymax}` in absolute px [CARD][ROW]. Field text values are absent.
7. **Label origin:** generator for `bank`; carried-over human boxes for fields. Card: "For each of the four bank types… one blank canvas template… cropped patches are pasted onto the canvas template… The bounding-box annotations are carried over unchanged from the original"; YAML `annotations_creators: derived` [CARD].
8. **Answer rule:** answer = `bank` (axis→Axis, canara→Canara, icici→ICICI, syndicate→Syndicate).
9. **Classes and balance:** test split: axis 8, canara 8, icici 6, syndicate 8 (`/statistics`) [ROW]. Card totals: synthetic Axis 79, Canara 91, ICICI 63, Syndicate 62 (295 in all) [CARD].
10. **Per-image fit:** exactly one bank per image [CARD].
11. **Risks:** field patches come from real cheques, so real names, account numbers and signatures may appear [CARD][INFERRED]. Images are large (2365×~1065, good) [ROW]. Only 4 templates, so the bank may be readable from the printed logo alone (easy) [INFERRED]. Overlap with model training data is low (2025-era repo) [INFERRED].
12. **Question templates:** (a) "Which bank's cheque is this? Axis / Canara / ICICI / Syndicate". (b) "Is the amount box in the right half of the cheque? yes/no" (from `amount.xmin > width/2`). (c) "Which field is nearest the bottom-right corner? signature / amount / date / account number".
13. Tags are inline above.

### D1.2 — candidate 1: shivalikasingh/cheques_sample_data — **MAYBE** (fails: no licence; tiny 512×256 images)
1. Landing: https://huggingface.co/datasets/shivalikasingh/cheques_sample_data. Listing: https://huggingface.co/datasets/shivalikasingh/cheques_sample_data/tree/main/data [CARD].
2. Licence: none in the card or tags (`license(card): None`) [CARD] → UNVERIFIED.
3. Access: open [CARD].
4. Size: 58.9 MB total. Smallest unit: test parquet 5.87 MB [CARD].
5. Proof: `https://datasets-server.huggingface.co/first-rows?dataset=shivalikasingh/cheques_sample_data&config=default&split=train` [ROW]
   - `{"gt_parse":{"cheque_details":[{"amt_in_words":"Three Thousand Seven Hundred and Fifty Five"},{"amt_in_figures":"3755"},{"payee_name":"Edmee Pelletier"},{"bank_name":"AXIS BANK"},{"cheque_date":"06/05/22"}]}}`
   - `{... "amt_in_words":"Nine Thousand Six Hundred and Thirty Five"},{"amt_in_figures":"9635"},{"payee_name":"Katie Connor"} ...}`
   - `{... "amt_in_words":"Four Hundred and Sixty Four"},{"amt_in_figures":"464"},{"payee_name":"Naomi Grant"} ...}`
6. Schema: `image`, `ground_truth` (a JSON string holding `amt_in_words`, `amt_in_figures`, `payee_name`, `bank_name`, `cheque_date`) [ROW].
7. Label origin: generator likely, since the names look Faker-style. The card says nothing [UNVERIFIED].
8. Answer rule: yes if `words_to_number(amt_in_words) == int(amt_in_figures)`.
9. Classes: negatives exist. A related mirror shows a mismatch (see candidate 2) [ROW]. All 3 rows fetched here match. Balance is UNVERIFIED.
10. One answer per image [INFERRED].
11. Risks: 512×256 images (tiny-image trap at 1536 px) [ROW]. Every fetched date is "06/05/22", so the date field has little variety [ROW].
12. Templates: words/figures match yes/no; "Which bank? AXIS / Canara / ICICI / HSBC"; "Which is the payee? 4 names".

### D1.2 — candidate 2: aniketVerma07/handwritten_cheque_vqa_dataset — **MAYBE** (fails: tiny images; mixed non-cheque VQA rows)
1. Landing: https://huggingface.co/datasets/aniketVerma07/handwritten_cheque_vqa_dataset [CARD].
2. Licence: `apache-2.0` (tag) [CARD].
3. Access: open.
4. Size: 481.6 MB. Smallest unit: test parquet 50.19 MB [CARD].
5. Proof: first-rows, train [ROW]:
   - `{"query":"What is the fullform of SCIL?","answers":"['Safer Chemicals Ingredients List']"}` (not a cheque)
   - `{"query":"What is the content of the text in the image?","answers":"as from Nov. 1 . The hand-over , due in"}` (handwriting line)
   - `{"query":"Retrieve the amount in words, amount in figures, ...","answers":"[{'amt_in_words': 'Six Hundred and Eleven'}, {'amt_in_figures': '1070'}, {'payee_name': 'Naomi Grant'}, {'bank_name': 'Canara Bank'}, {'cheque_date': '06/05/22'}]"}`. This is a **real negative**: 611 ≠ 1070.
6. Schema: `image`, `query` str, `answers` str [ROW].
7. Label origin: mixed and unknown [UNVERIFIED].
8. Answer rule: filter rows whose `query` starts with "Retrieve the amount in words"; then apply the same rule as candidate 1.
9. Balance: UNVERIFIED.
10. One answer per cheque image [INFERRED].
11. Risks: cheque images are 512×256 [ROW]. Mixed sources include DocVQA-like rows (DocVQA was rejected) [ROW][INFERRED].
12. Templates: as for candidate 1.

### D1.5 — candidate 1: Bankstatemently/bank-statement-parsing-benchmark — **MAYBE** (fails: only 5 documents; PDFs need rendering)
1. Landing: https://huggingface.co/datasets/Bankstatemently/bank-statement-parsing-benchmark. GitHub: https://github.com/bankstatemently/bank-statement-parsing-benchmark [CARD].
2. Licence: `license: mit` and a "LICENSE # MIT" file [CARD].
3. Access: open.
4. Size: 0.4 MB total. PDFs 15–80 KB each [CARD].
5. Proof: first-rows [ROW]:
   - `{"id":"bsb-001","difficulty":"basic","documentType":"bank-statement","country":"SG","currency":"SGD","language":"en","pages":3,"transactionCount":12}`
   - `{"id":"bsb-002","difficulty":"basic","documentType":"credit-card","country":"US","currency":"USD","pages":4,"transactionCount":15}`
   - `{"id":"bsb-003","difficulty":"basic","documentType":"bank-statement","country":"NL","currency":"EUR","language":"nl","pages":3,"transactionCount":22}`
7. Label origin: generator ("15 synthetic statements"; "benchmark-generator") [CARD].
8. Answer rule: answer = `documentType`. A currency question uses `currency`.
9. Classes: 5 rows, at least 2 types [ROW]. "Ground truth is never in this dataset", so only metadata labels exist [CARD].
10. One `documentType` per PDF. Questions must be posed about page 1 [INFERRED].
11. Risks: far too small for scoring. Multi-page PDFs [CARD].
12. Templates: documentType (bank / credit card); currency (SGD/USD/EUR/...); "Is it in English? yes/no" (`language`).

### D1.6 — candidate 1: Panhapich/bank-statement-detection — **MAYBE** (fails: real negatives unverified; 400–500 MB shards)
1. Landing: https://huggingface.co/datasets/Panhapich/bank-statement-detection [CARD].
2. Licence: "**License** | MIT" [CARD].
3. Access: open.
4. Size: 3,534.8 MB, 8 shards of about 406–508 MB each [CARD].
5. Proof: first-rows [ROW]: `{"objects":{"bbox":[[0.5,0.4977,0.9055,0.9289]],"category":[0]}}`; `{"objects":{"bbox":[[0.5,0.4300,0.9055,0.7935]],"category":[0]}}`; `{"objects":{"bbox":[[0.5,0.6313,0.9055,0.6212]],"category":[0]}}`. Images are 1191×1684.
6. Schema: `objects.bbox` (normalised xywh), `objects.category` (0 = Table) [CARD].
7. Label origin: generator ("every annotation is produced during rendering"; "Python + ReportLab") [CARD].
8. Answer rule: yes if `len(objects.category) > 0`.
9. Negatives: the card says "Multi-page statements are stored as separate rows". Whether any page has no table is UNVERIFIED. All 3 fetched rows are positive.
10. One table per page in the fetched rows [ROW].
11. Risks: synthetic and clean. Shards are too large to sample offline.
12. Templates: table present yes/no; "Does the table span more than half the page height? yes/no" (bbox h > 0.5); "Is the page landscape? yes/no".

### D2.1 — candidate 1: jsdnrs/ICDAR2019-SROIE — **USE**
1. **Landing:** https://huggingface.co/datasets/jsdnrs/ICDAR2019-SROIE. Owner: https://rrc.cvc.uab.es/?ch=13. GitHub: https://github.com/jsdnrs/ICDAR2019-SROIE. Listing: /tree/main/data [CARD].
2. **Licence:** "The original dataset is licensed under the CC-BY-4.0 as noted on the ICDAR's Robust Reading Competition website… redistributed annotations and metadata remain under the CC-BY-4.0" [CARD] (https://huggingface.co/datasets/jsdnrs/ICDAR2019-SROIE/raw/main/README.md). No research restriction is stated.
3. **Access:** open [CARD].
4. **Size:** 509.8 MB. Smallest unit: `data/test-00000-of-00001.parquet` 191.05 MB, and train 318.62 MB [CARD]. Sample through `/rows`.
5. **Proof:** `https://datasets-server.huggingface.co/first-rows?dataset=jsdnrs/ICDAR2019-SROIE&config=default&split=train` [ROW]
   - `{"key":"X00016469612","image_size":{"width":463,"height":1013},"entities":{"company":"BOOK TA .K (TAMAN DAYA) SDN BHD","date":"25/12/2018","address":"NO.53 55,57 & 59, JALAN SAGU 18, ...","total":"9.00"},"words":["TAN WOON YANN","BOOK TA .K(TAMAN DAYA) SDN BND",...]}`
   - `{"key":"X00016469619","image_size":{"width":439,"height":1004},"entities":{"company":"INDAH GIFT & HOME DECO","date":"19/10/2018","total":"60.30"},...}`
   - `{"key":"X00016469620","image_size":{"width":459,"height":949},"entities":{"company":"MR D.I.Y. (JOHOR) SDN BHD","date":"12-01-19","total":"33.90"},"words":[...,"-INVOICE-",...]}`
6. **Schema:** `key` str; `image_size {width,height}`; `entities {company,date,address,total}` str (key fields); `words` list[str] (line transcripts); `bboxes` list[[x0,y0,x1,y1]] [ROW][CARD].
7. **Label origin:** human, from the ICDAR 2019 challenge. The card admits "The original publication… does not provide details about the annotation workflow" [CARD]. The `words` transcripts are human ICDAR ground truth, not OCR output [CARD]. Confidence is medium.
8. **Answer rule:** correct option = `entities.total`. Distractors = other money-format strings in `words` (regex `^\d+\.\d{2}$`) that differ from the total.
9. **Classes:** not a class task. 987 rows (`/size`) [ROW].
10. **Per-image fit:** one total per receipt [CARD].
11. **Risks:** the card says some fields "are blurred" for privacy, but it "still includes many" personal items (cashier names, e.g. "TAN WOON YANN") [CARD][ROW]. Width is about 440–460 px (low, a near-tiny trap at 1536) [ROW]. SROIE is very widely used, so training overlap is high [INFERRED].
12. **Templates:** (a) "Which amount is the final total? 4 amounts". (b) "Which date is printed? 4 dates" (`entities.date` plus shifted dates). (c) "Which company issued this receipt? 4 company names" (distractors drawn from other rows).

### D2.2 / D2.3 — candidate 1: albertobarnabo/synthetic-receipts-ocr — **USE**
1. **Landing:** https://huggingface.co/datasets/albertobarnabo/synthetic-receipts-ocr. Listing: /tree/main/data (17 train shards plus eval). The generator ships in `generator/` [CARD].
2. **Licence:** `license: apache-2.0` [CARD] (raw README). No research restriction.
3. **Access:** open.
4. **Size:** 4,084.7 MB. Shards about 227–229 MB each [CARD]. Sample through `/rows`.
5. **Proof:** `https://datasets-server.huggingface.co/rows?dataset=albertobarnabo/synthetic-receipts-ocr&config=default&split=eval&offset=0&length=100` [ROW]
   - `{"id":"eval-000000","locale":"UK","degradations":"perspective,lighting,jpeg65","n_items":6} fields: {"currency":"GBP","total":184.89,"payment":"MASTERCARD","tax_included":true,"loyalty":"LOYALTY PTS +85"}`
   - `{"id":"eval-000001","locale":"FR","degradations":"perspective,lighting,shadow,noise,blur,jpeg84","n_items":6} fields: {"currency":"EUR","total":62.41,"payment":"SANS CONTACT","tax_included":true}`
   - `{"id":"eval-000002","locale":"IT","degradations":"perspective,lighting,thermal_fade,noise,jpeg60","n_items":4} fields: {"currency":"EUR","total":26.75,"payment":"MASTERCARD","tax_included":true,"loyalty":null}`
6. **Schema:** `image_clean`, `image_photo` (degraded twin); `full_text`; `words` (exact boxes); `fields` (JSON string: merchant, address, phone, tax_id, date, time, receipt_no, lines[name,qty,unit_price,total,tax_rate], subtotal, taxes, total, payment, tendered, change, loyalty, currency, tax_included); `locale`; `font`; `degradations`; `n_items` [CARD][ROW].
7. **Label origin:** generator. "words… exact by construction (captured during rendering, never re-OCR'd)"; "a field is non-null if and only if its value is printed on the image"; "Every receipt is a pure function of (seed, index)" [CARD].
8. **Answer rules:** D2.2 maps `fields.payment`: {CASH, BAR, ESPECES, CONTANTI} → cash; {CONTACTLESS, SANS CONTACT, KONTAKTLOS, CARTA CONTACTLESS} → contactless; {APPLE PAY} → mobile wallet; all other card brands → card. D2.3: answer = `locale`.
9. **Classes (eval sample of 100 rows):** locale US 38, UK 19, FR 15, IT 15, DE 13. Payment: MASTERCARD 16, CASH 10, CONTACTLESS 8, VISA 7, AMEX 7, VISA DEBIT 7, CARTA CONTACTLESS 6, APPLE PAY 6, … BAR 3, ESPECES 2, CONTANTI 2. n_items ranges 1–13 [ROW]. Full counts are UNVERIFIED (`/statistics` returned 500).
10. **Per-image fit:** one payment and one locale per receipt [CARD].
11. **Risks:** synthetic data, so no personal data. Images are about 600–900 px wide [ROW] (borderline for 1536). Card limitation: "monospace thermal-style receipts only… degradations are parametric, not photographs" [CARD]. Training overlap is low [INFERRED].
12. **Templates:** payment method (4 options); country (5); "Is tax included in the prices? yes/no" (`tax_included`).

### D2.4 / D2.5 — candidate 1: HV09/synthetic-bilingual-invoices-200 — **USE**
1. **Landing:** https://huggingface.co/datasets/HV09/synthetic-bilingual-invoices-200. Listing: /tree/main/data. Raw annotation file: `data/metadata.jsonl` (0.1 MB) [CARD].
2. **Licence:** `license: cc-by-4.0` [CARD].
3. **Access:** open.
4. **Size:** 7.4 MB total. Smallest unit: metadata.jsonl 0.1 MB; each PNG about 0.03–0.05 MB [CARD].
5. **Proof:** downloaded `https://huggingface.co/datasets/HV09/synthetic-bilingual-invoices-200/resolve/main/data/metadata.jsonl` [ROW]
   - `{"file_name":"INV-1080.png","invoice_number":"INV-1080","supplier_trn":"100647382910003","invoice_date":"2026-06-10","invoice_date_raw":"١٠ يونيو ٢٠٢٦","date_calendar":"gregorian","po_reference":"PO-7919","qty":308,"unit_price":137.75,"subtotal":42427,"vat_amount":2121.35,"total":44548.35,"currency":"AED","language":"ar"}`
   - `{"file_name":"SUP-1158.png","date_calendar":"gregorian","po_reference":"PO-9399","qty":140,"total":6945.75,"currency":"AED","language":"ar"}`
   - `{"file_name":"FF-1323.png","date_calendar":"gregorian","po_reference":null,"qty":199,"total":4701.38,"currency":"AED","language":"ar"}`
6. **Schema:** 17 fields (invoice_number, supplier, supplier_ar, supplier_trn, invoice_date, invoice_date_raw, date_calendar, po_reference, description, qty, unit_price, subtotal, vat_amount, total, total_raw, currency, language) [CARD].
7. **Label origin:** generator. "A seeded generator renders HTML to PNG… No LLM is involved in generation, so the ground truth is the input to rendering" [CARD].
8. **Answer rules:** D2.4 is yes if `po_reference` is not null. D2.5 is yes if `date_calendar == "hijri"`.
9. **Classes (all 200 rows):** po_reference null 70 / present 130; date_calendar gregorian 185 / hijri 15; language ar 50, bilingual 50, en 50, en-au 50; currency AED 150, AUD 50 [ROW]. Real negatives exist for both yes/no tasks.
10. **Per-image fit:** one value per invoice [CARD].
11. **Risks:** images are 820×600, small for a full invoice [ROW]. Hijri positives are few (15). The data is fictional [CARD].
12. **Templates:** PO present yes/no; Hijri yes/no; "Which currency? AED / AUD / SAR / USD"; "Which language style? Arabic / bilingual / English" (from `language`).

### D2.6 — candidate 1: katanaml-org/invoices-donut-data-v1 (Sparrow) — **USE** (medium)
1. **Landing:** https://huggingface.co/datasets/katanaml-org/invoices-donut-data-v1. Original: https://data.mendeley.com/datasets/tnj49gpmtz [CARD].
2. **Licence:** `license: mit` [CARD]. The original Mendeley licence was not fetched [UNVERIFIED].
3. **Access:** open.
4. **Size:** 197.5 MB. Smallest unit: test parquet 10.44 MB [CARD].
5. **Proof:** first-rows, train and `/rows` test [ROW]
   - `{"gt_parse":{"header":{"invoice_no":"40378170","invoice_date":"10/15/2012","seller":"Patel, Thompson and Montgomery 356 Kyle Vista New James, MA 46228",...,"seller_tax_id":"958-74-3511",...`
   - `{"gt_parse":{"header":{"invoice_no":"61356291","invoice_date":"09/06/2012","seller":"Chapman, Kim and Green ...","client_tax_id":"939-98-8477",...`
   - test row 0: `{"header":{"invoice_no":"97159829","invoice_date":"09/18/2015",...},"items":[{"item_desc":"12\" Marble Lapis Inlay Chess Table Top ...","item_qty":"2,00","item_net_price":"444,60","item_net_worth":"889,20","item_vat":"10%","item_gross_worth":"978,12"}],"summary":{"total_net_worth":"$ 889,20","total_vat":"$ 88,92","total_gross_worth":"$ 978,12"}}`
6. **Schema:** `image`, `ground_truth` (a JSON string with header{invoice_no, invoice_date, seller, client, seller_tax_id, client_tax_id, iban}, items[...], summary{...}) [ROW].
7. **Label origin:** human: "Annotation and data preparation task was done by Katana ML team" [CARD]. The source invoices look like synthetic electronic invoices (Faker-style names) [INFERRED].
8. **Answer rule:** count = `len(items)`; bucket into 1/2/3/4/5+. Also VAT rate = `items[*].item_vat`.
9. **Classes:** distribution UNVERIFIED (string column). 501 rows [CARD].
10. One count per invoice.
11. **Risks:** fake tax IDs that look like SSNs (###-##-####) [ROW]. Images are 2481×3508 (good) [ROW].
12. **Templates:** line-item count; "What VAT rate is applied? 0% / 5% / 10% / 20%"; "Which is the gross total? 4 amounts".

### D3.1 / D3.2 / D3.3 — candidate 1: DrBimmer/comprehensive-car-damage — **USE** (medium)
1. **Landing:** https://huggingface.co/datasets/DrBimmer/comprehensive-car-damage. Listing: /tree/main (one folder per class, e.g. `F_Normal/FN_53.jpg`) [CARD]. This is not the "DrBimmer car parts and damage" set that is already used. It is a separate repo.
2. **Licence:** `license: mit` [CARD].
3. **Access:** open.
4. **Size:** 668.8 MB, 2,303 files. Smallest unit: one image, about 0.01–5 MB [CARD]. Single images can be fetched.
5. **Proof:** `/first-rows?dataset=DrBimmer/comprehensive-car-damage&config=default&split=train` gives `{"label":0}` ×3 (F_Breakage) on 800×600 images [ROW]. `/statistics` gives class counts (below) [ROW]. The file listing shows `F_Normal/FN_53.jpg`, `F_Normal/FN_273.png`, `R_Breakage/RB_302.png` [CARD].
6. **Schema:** `image`, `label` ClassLabel [F_Breakage, F_Crushed, F_Normal, R_Breakage, R_Crushed, R_Normal] [ROW].
7. **Label origin:** human: `annotations_creators: - manual` [CARD]. Image provenance is not stated (likely scraped web photos) [UNVERIFIED].
8. **Answer rules:** D3.1 yes if label ∉ {F_Normal, R_Normal}. D3.2 front if label starts "F_". D3.3 none / breakage / crushed from the suffix.
9. **Classes:** F_Breakage 500, F_Crushed 400, F_Normal 500, R_Breakage 300, R_Crushed 300, R_Normal 300 (2,300 rows) [ROW]. **Real negatives: 800 undamaged images** [ROW].
10. **Per-image fit:** one label per image by folder [CARD]. An image could show both breakage and crush; the folder picks one [INFERRED].
11. **Risks:** licence plates and bystanders are possible [INFERRED]. Mixed resolutions, some PNGs at 5 MB [CARD]. Folder classifications like this circulate on Kaggle, so overlap is likely [INFERRED]. There is also a `.DS_Store`, which is harmless.
12. **Templates:** damaged yes/no; front/rear; none/breakage/crushed.

### D3.1 — candidate 2: Kaggle anujms/car-damage-detection — **MAYBE** (fails: licence "Unknown"; no rows pasted)
1. Landing: https://www.kaggle.com/datasets/anujms/car-damage-detection. API JSON: https://www.kaggle.com/api/v1/datasets/view/anujms/car-damage-detection [CARD].
2. Licence: `"licenseName": "Unknown"` [CARD].
3. Access: download needs a Kaggle login [UNVERIFIED], so effectively login.
4. Size: totalBytes 130,044,688 (130 MB). The file list was empty in the anonymous API → SINGLE ARCHIVE [UNVERIFIED].
5. Proof: none. The subtitle reads "Damaged and Whole cars image dataset" [CARD].
6–12: UNVERIFIED. If used, the answer rule would be folder = damaged/whole.

### D3.4 — candidate 1: gigwegbe/damaged-car-dataset-annotated — **MAYBE** (fails: no licence; positives only; several boxes per image)
1. Landing: https://huggingface.co/datasets/gigwegbe/damaged-car-dataset-annotated [CARD].
2. Licence: none [CARD] → UNVERIFIED.
3. Access: open.
4. Size: 1,288.9 MB, 3 shards of 404–444 MB [CARD].
5. Proof: first-rows [ROW]: `{"bbox":[454.28,227.22,67.98,30.59],"category_id":"crack"}`; `{"bbox":[401.49,39.17,258.11,108.64],"category_id":"glass shatter"}`; `{"bbox":[316.94,268.45,234.73,217.1],"category_id":"tire flat"}`. Images are 1000×685.
6. Schema: one row per box: `image`, `bbox` [x,y,w,h], `category_id` str, `annotated_image` [ROW].
7. Label origin: UNVERIFIED. The class names match CarDD's 6 classes, so it may be derived from CarDD, which was rejected for needing a consent form [INFERRED]. **Flag possible CarDD mirror.**
8. Answer rule: group rows by image hash; the answer = the single category when an image has only one.
9. Negatives: none seen [ROW].
10. Several categories per image are possible.
11. Risks: possible consent-gated source.
12. Templates: damage type (6); box count; largest-box type.

### D3.4 — candidate 2: tugberkkalay/autodamageiq-vehicle-damage-dataset — **SKIP** (fails: machine labels; includes CarDD)
- Licence `cc-by-4.0` [CARD]. Size 557.7 MB, YOLO txt per image [CARD]. The card lists sources "**CarDD + VehiDE + HITL (GPT-4o labeled)**" and "HITL — Human-in-the-loop, GPT-4o Vision ile otomatik etiketlenmiş görseller" [CARD]. These are machine labels mixed with CarDD (consent required). datasets-server `/splits` returned HTTP 500, so no rows were pasted.

### D3.5 — candidate 1: tanganke/stanford_cars — **MAYBE** (fails: no licence on card; tiny images present)
1. Landing: https://huggingface.co/datasets/tanganke/stanford_cars [CARD].
2. Licence: none on the card [CARD] → UNVERIFIED.
3. Access: open.
4. Size: 6,016.5 MB, including corruption splits. Smallest unit: `data/pixelate-00000-of-00001.parquet` 3.74 MB (corrupted variant). Train/test shards are about 513 MB [CARD].
5. Proof: first-rows: `{"label":0}` (AM General Hummer SUV 2000) at 700×525, then `{"label":0}` at **85×64**, then `{"label":0}` at **94×71** [ROW].
6. Schema: `image`, `label` ClassLabel (196 "Make Model Body Year" names) [ROW].
7. Label origin: human (Stanford Cars) [UNVERIFIED in this session].
8. Answer rule: body style = the token before the year in the class name (Sedan, SUV, Coupe, Convertible, Hatchback, Wagon, Cab, Van, Minivan).
9. Classes: 196 [ROW].
10. One car per image [INFERRED].
11. Risks: **tiny images** (85×64) [ROW]. Very high training overlap [INFERRED]. Plates may be visible.
12. Templates: body style; make (4 options); "Is it a convertible? yes/no".

### D4.1 — candidate 1: QCRI/CrisisMMD (config `damage`) — **USE** (licence NC)
1. **Landing:** https://huggingface.co/datasets/QCRI/CrisisMMD. Owner: https://crisisnlp.qcri.org/crisismmd. Listing: /tree/main (images under `data_image/<event>/<date>/<tweetid>_<n>.jpg`). Original splits: https://crisisnlp.qcri.org/data/crisismmd/crisismmd_datasplit_all.zip [CARD].
2. **Licence:** `license: cc-by-nc-sa-4.0` [CARD]. Non-commercial and share-alike. No consent form. Research testing is allowed.
3. **Access:** open (API `gated: False`) [CARD].
4. **Size:** 1,941 MB in the repo (18,101 files). Smallest units: one image (KB to 3 MB); annotation zip `crisismmd_datasplit_all.zip` 3.07 MB (Content-Length 3072270); `task_damage_text_img_test.tsv` 0.13 MB [ROW].
5. **Proof:** (a) `https://datasets-server.huggingface.co/first-rows?dataset=QCRI/CrisisMMD&config=damage&split=train` [ROW]:
   - `{"event_name":"hurricane_harvey","image_id":"905960092822003712_0","image_path":"data_image/hurricane_harvey/8_9_2017/905960092822003712_0.jpg","label":2}` (severe_damage)
   - `{"event_name":"california_wildfires","image_id":"918008272363368448_0","image_path":"data_image/california_wildfires/11_10_2017/918008272363368448_0.jpg","label":2}`
   - `{"event_name":"hurricane_irma","image_id":"909396901254090752_0","image_path":"data_image/hurricane_irma/17_9_2017/909396901254090752_0.jpg","label":2}`

   (b) Original TSV `task_damage_text_img_test.tsv` [ROW]: `hurricane_maria 912065374929264640_1 … little_or_no_damage`; `hurricane_harvey 905930890735439873_1 … mild_damage`; `hurricane_irma 910225185176997895_0 … severe_damage`.
6. **Schema:** `event_name`, `tweet_id`, `image_id`, `tweet_text`, `image_path`, `image` (null in viewer; image is the repo file), `label` ClassLabel [little_or_no_damage, mild_damage, severe_damage] [ROW].
7. **Label origin:** human. Card: "several thousand manually annotated tweets and images" [CARD]. Datasplit Readme: "for damage task we only have a label for the image" [PAPER/readme in zip]. So the damage label is an **image** label.
8. **Answer rule:** answer = `label` (0 little_or_none, 1 mild, 2 severe).
9. **Classes:** train little 333 / mild 587 / severe 1,548; test 71 / 126 / 332 [ROW]. Little-or-none is a real but minority class.
10. **Per-image fit:** one label per image [readme].
11. **Risks:** Twitter images may show faces, people and text [INFERRED]. Some images are small or low quality (social media) [INFERRED]. The tweet text carries a usernames-in-text risk, so do not show the text. Published in 2018, so moderate training overlap [INFERRED].
12. **Templates:** severity (3); "Is there severe damage? yes/no"; "Which event type? hurricane / wildfire / earthquake / flood" (from `event_name` mapped to its type).

### D4.3 — candidate 1: CrisisMMD humanitarian task (original TSV `label_image` only) — **USE**; the HF `humanitarian` config alone is a **trap**
- Same landing, licence and access as D4.1.
- **Trap:** the datasplit Readme says "label: for informativeness and humanitarian tasks **randomly selected labels from text and image labels**" [readme]. The HF `humanitarian` config exposes only `label` (features list) [ROW], so its label may describe the tweet text, not the image. **Use `label_image` from `task_humanitarian_text_img_*.tsv`** in the 3.07 MB zip instead (the Readme documents the column `label_image`) [readme].
- HF test `label` counts: affected_individuals 86, infrastructure_and_utility_damage 319, injured_or_dead_people 41, missing_or_found_people 5, not_humanitarian 849, other_relevant_information 578, rescue_volunteering_or_donation_effort 340, vehicle_damage 19 [ROW].
- **Answer rule:** yes if `label_image == "infrastructure_and_utility_damage"`; no if `label_image == "not_humanitarian"` (clean negatives); drop other classes.
- Rows: three HF humanitarian test rows fetched (hurricane_harvey 905952332923338752_0; mexico_earthquake 912022130396672000_0; mexico_earthquake 910700764808564736_0) [ROW]. The `label_image` value of the TSV rows was not printed in this session, so the column's presence rests on the Readme [readme]. Confidence is medium.
- Templates: infrastructure damage yes/no; "Is anyone injured or dead shown? yes/no" (sensitive; avoid); vehicle damage yes/no (19 test rows, too few).

### D4.1 / D4.2 / D4.4 — candidate 2: QCRI/MEDIC — **MAYBE** (fails: label origin not stated in the card or abstract I fetched)
1. Landing: https://huggingface.co/datasets/QCRI/MEDIC. Paper: https://arxiv.org/abs/2108.12828 [CARD].
2. Licence: "The MEDIC dataset is published under CC BY-NC-SA 4.0 license, which means everyone can use this dataset for non-commercial research purpose" [CARD]. There is also a `terms-of-use.txt` [CARD] that I did not read [UNVERIFIED].
3. Access: open.
4. Size: 10,940 MB. Smallest unit: `data/test-00007-of-00010…parquet` 163.45 MB [CARD]. Use `/rows`.
5. Proof: first-rows, train [ROW]:
   - `{"image_id":"ASONAM2017","event_name":"ecuador_eq_severe_im_645.jpg","image_path":"data/ASONAM17_Damage_Image_Dataset/ecuador_eq/ecuador_eq_severe_im_645.jpg","damage_severity":2,"informative":0,"humanitarian":1,"disaster_types":0}` (600×383)
   - `{"event_name":"ecuador_eq_severe_im_1378.jpg","damage_severity":2,"informative":0,"humanitarian":1,"disaster_types":0}` (1000×562)
   - `{"event_name":"ecuador_eq_unlabelled_im_100.jpg","damage_severity":0,"informative":1,"humanitarian":2,"disaster_types":0}` (600×286)
6. Schema: `damage_severity` [little_or_none, mild, severe]; `informative` [informative, not_informative]; `humanitarian` [affected_injured_or_dead_people, infrastructure_and_utility_damage, not_humanitarian, rescue_volunteering_or_donation_effort]; `disaster_types` [earthquake, flood, hurricane, fire, landslide, not_disaster, other_disaster] [ROW].
7. Label origin: UNVERIFIED for the whole set. It merges CrisisMMD (human), AIDR, DMD and ASONAM17 [CARD]. The third row's file name contains "unlabelled", yet it carries labels [ROW], which suggests labels may have been propagated. **Check the paper before rating USE.**
8. Answer rules: D4.2 = `disaster_types`; D4.4 yes if `disaster_types == flood`, no if `not_disaster`; D4.1 = `damage_severity`.
9. Classes (test, 15,688 rows): damage little_or_none 10,252 / mild 1,527 / severe 3,909; disaster earthquake 1,795, flood 1,315, hurricane 1,518, fire 690, landslide 331, not_disaster 8,885, other_disaster 1,154 [ROW]. Real negatives are plentiful.
10. One label per task per image.
11. Risks: overlaps CrisisMMD, so do not double-count. Social-media faces. Some images are 286 px tall (small) [ROW].
12. Templates: disaster type (6); flood yes/no; severity (3).

### D5.1 — candidate 1: Symage/coherent-forms-1040-cms1500-i9 — **GATED**
- Landing: https://huggingface.co/datasets/Symage/coherent-forms-1040-cms1500-i9. API `gated: "auto"`; tag `license:other` [CARD]. The README and `/splits` return 401 "Access… is restricted… Please log in" [CARD].
- Size per the listing: `data/train.parquet` 1,576.94 MB, `data/test.parquet` 394.46 MB (1,971.4 MB total) [CARD].
- No rows are possible. A human must log in on the landing page and accept the terms. The name suggests it covers CMS-1500, 1040 and I-9 forms, which would serve D5.1, D9 and D10.1 [INFERRED].

### D5.2 — candidate 1: chinmays18/medical-prescription-dataset — **MAYBE** (fails: no licence; empty card; origin unknown)
1. Landing: https://huggingface.co/datasets/chinmays18/medical-prescription-dataset. Listing: `train/images/*.png`, `train/annotations/*.json` [CARD].
2. Licence: none; the README is 15 bytes [CARD].
3. Access: open.
4. Size: 983.8 MB. Smallest unit: one image (~1.75 MB) or one annotation JSON (<0.01 MB) [CARD].
5. Proof: first-rows [ROW]:
   - `"<s_ocr> doctor_name: Dr. F. Gomez clinic_name: Meadowview Health ... patient_name: Michael Brown patient_age: 51 date: 2024-12-16 medications: - Ibuprofen 5 mg - Take twice daily - Ciprofloxacin 25 mg - At bedtime - Metformin 100 mg - Every 12 hours signature: Dr. F. Gomez </..."`
   - `"... doctor_name: Dr. M. Lee ... patient_name: Carlos Chavez patient_age: 36 ... medications: - Gabapentin 500 mg ... - Prednisone 50 mg ... - Acetaminophen 100 mg ..."`
   - `"... patient_name: Aisha Khan patient_age: 65 ... medications: - Prednisone 500 mg ... - Ciprofloxacin 5 mg ... - Simvastatin 10 mg ... - Omeprazole 20 mg ..."`
6. Schema: `ground_truth` str (key: value Donut text); images are a separate folder [ROW][CARD].
7. Label origin: likely a generator (template doses such as "Prednisone 500 mg" are unrealistic) [INFERRED]. UNVERIFIED.
8. Answer rule: count the "- <drug> <n> mg" entries under `medications:`.
9. Classes: 3 / 3 / 4 in the rows fetched. Balance UNVERIFIED.
10. One count per image.
11. Risks: fictional patient names. Doses are unrealistic, so this is unsuitable for anything clinical [INFERRED].
12. Templates: medication count; "Which clinic? 4 names"; "Is a signature line present? yes/no" (all yes → no negatives).

### D5.4 — sansverse/medical-bill-samples — **SKIP** (fails: no labels)
- 17 PDFs (31.0 MB) with only a `pdf` column [ROW]. No licence [CARD]. There is nothing to compute an answer from.

### D6.1 — candidate 1: tech4humans/signature-detection — **GATED**
- Landing: https://huggingface.co/datasets/tech4humans/signature-detection. API `gated: "auto"`; tag `license:apache-2.0` [CARD]. The README and `/splits` return 401 [CARD]. Listing: `full/train-00000-of-00001.parquet` 112.21 MB, `full/test…` 17.34 MB, `full/validation…` 17.21 MB (147.4 MB total) [CARD].
- A human must accept the terms on the landing page. If it holds document pages with and without signature boxes, it is the best open option for D6.1 [INFERRED].

### D6.2 / D6.3 / D7.2 — candidate 1: DocLayNet (docling-project/DocLayNet-v1.2 and pierreguillou/DocLayNet-small) — **USE**
1. **Landing:** https://huggingface.co/datasets/docling-project/DocLayNet-v1.1 (licence text) and https://huggingface.co/datasets/docling-project/DocLayNet-v1.2 (data). Small mirror: https://huggingface.co/datasets/pierreguillou/DocLayNet-small [CARD].
2. **Licence:** "License: [CDLA-Permissive-1.0](https://cdla.io/permissive-1-0/)" (DocLayNet-v1.1 card, Licensing Information) [CARD]. The pierreguillou mirror also says "DocLayNet… published under license CDLA-Permissive-1.0" [CARD]. The v1.2 card has no licence tag [CARD].
3. **Access:** open.
4. **Size:** v1.2 is 39,770.6 MB over 87 files; smallest `data/test-00004-of-00006.parquet` 266.5 MB [CARD]. pierreguillou small: `data/dataset_small.zip` 380.92 MB, SINGLE ARCHIVE (but served by the viewer) [CARD]. Sample through `/rows`.
5. **Proof:** v1.2 first-rows [ROW]: row 0 `category_id:[6,10,10,10,10,10,10,10,10,10,10,5,...]`; row 1 `category_id:[10,10,10,7,8,10,10,5,7]`, metadata `{"collection":"ann_reports_00_04_fancy","doc_category":"financi...`; row 2 `category_id:[10,10,...,9,...]`. DocLayNet-small first-rows [ROW]: `{"original_filename":"Pascal - Manual & Report.pdf","page_no":150,"collection":"manuals","doc_category":"manuals"}`; `{"original_filename":"EN-Declaration on Honour.pdf","page_no":4,"num_pages":6,"collection":"eu_tenders","doc_category":"government_tenders"}`; row 0 `categories:[5,5,5,7,7,...]` (Aegon N.V. financial statements).
6. **Schema:** v1.2: `bboxes`, `category_id` list[int] (COCO ids), `metadata` JSON (doc_category, collection, sizes), `pdf_cells`, `modalities`. Small mirror: `categories` over ["Caption","Footnote","Formula","List-item","Page-footer","Page-header","Picture","Section-header","Table","Text","Title"] and `doc_category` str [ROW].
7. **Label origin:** human layout boxes. Paper title: "DocLayNet: A Large Human-Annotated Dataset for Document-Layout Analysis" (arXiv 2206.01062) [CARD]. The v1.1 YAML says `crowdsourced` [CARD]. `doc_category` comes from the source collection, so it is known by construction [INFERRED].
8. **Answer rules:** D6.2 = `doc_category` (6 options). D7.2 yes if `doc_category == government_tenders`. D6.3 yes if the Table class id is in `category_id` (id 8 in the small mirror's ClassLabel; check the v1.2 mapping, since it uses COCO 1-based ids [UNVERIFIED]).
9. **Classes:** small test (49 pages): financial_reports 20, scientific_articles 10, laws_and_regulations 8, manuals 7, government_tenders 2, patents 2 [ROW]. Table yes/no balance UNVERIFIED but surely mixed [INFERRED].
10. **Per-image fit:** one doc_category per page. Table presence is a clean yes/no.
11. **Risks:** images are 1025×1025 (square-padded) [ROW]. Public reports and filings only. DocLayNet is widely used for training layout models (overlap) [INFERRED].
12. **Templates:** page category (6); table present yes/no; "Does the page contain a picture? yes/no" (Picture id).

### D6.2 / D9.4 / D7.4 — candidate 2: nutrientdocs/document-classification-benchmark — **MAYBE** (fails: dataset-level licence is only "other"; per-row tags are given)
1. Landing: https://huggingface.co/datasets/nutrientdocs/document-classification-benchmark [CARD].
2. Licence: tag `license:other`. Card: "All sources are redistributable… DocLayNet CDLA-Permissive-1.0 | synthetic IRS forms (public-domain templates + faked fields) public-domain | mixed permissive HF sources… per upstream source" [CARD]. The per-row `license_tag` counts are permissive 160, public-domain 360, CDLA-Permissive-1.0 754 [ROW].
3. Access: open.
4. Size: 453.7 MB SINGLE parquet (`data/test-00000-of-00001.parquet` 453.67 MB) [CARD]. Use `/rows`.
5. Proof: `/rows` offsets 0, 377, 754, 1114 [ROW]:
   - `{"label":"financial reports","candidate_labels":["financial reports","scientific articles","laws and regulations","government tenders","manuals","patents"],"source":"DocLayNet (ds4sd/DocLayNet)","license_tag":"CDLA-Permissive-1.0","doc_id":"financial-reports_0000","track":"doclaynet"}`
   - `{"label":"1040","candidate_labels":["1040","1065","1099-DIV","1099-INT","1099-MISC","1099-NEC","1099-R","1120","940","941","Schedule A (1040)",...,"W-2","W-4","W-9"],"source":"synthetic IRS forms (public-domain templates)","license_tag":"public-domain","doc_id":"1040_000","track":"forms"}`
   - `{"label":"invoice","candidate_labels":["invoice","handwritten note","chart","table","letter","memo","form","report","scientific article","receipt","advertisement","resume"],"source":"mixed permissive HF sources","license_tag":"permissive","doc_id":"invoice_017","track":"ood"}`
6. Schema: `label`, `candidate_labels`, `source`, `license_tag`, `doc_id`, `track` (doclaynet / forms / ood / oov) [CARD].
7. Label origin: generator for the forms track ("public-domain templates + faked fields"); human/source for DocLayNet; "per upstream source" for ood [CARD].
8. Answer rule: answer = `label`. For pick-one with 2–6 options, sample 3–5 distractors from `candidate_labels`.
9. Classes: 34 labels; forms track 20 per IRS form (1040, W-2, W-4, W-9, 1099-x, 941, 1065, 1120, schedules); chart/invoice/handwritten note 40 each [ROW]. Total 1,274 rows.
10. One label per image.
11. Risks: images are 768×768 [ROW] (downscaled; small for forms). The OOV track reuses DocLayNet images, so de-duplicate against card D6.2.
12. Templates: IRS form (6 options); doc category (6); "Is this a form? yes/no" (ood track).

### D7.1 — candidate 1: mturski/CheckboxQA — **MAYBE** (fails: mirror with no images; PDFs are off-site and multi-page)
1. Landing: https://huggingface.co/datasets/mturski/CheckboxQA. GitHub: https://github.com/Snowflake-Labs/CheckboxQA. Paper: arXiv 2504.10419 [CARD].
2. Licence: "intended for non-commercial research purposes and is provided under the CC BY-NC license. Please refer to DocumentCloud's terms of service… for… the underlying document" [CARD]. "The dataset is intended solely for evaluation purposes" [CARD].
3. Access: annotations open. Documents must be fetched from DocumentCloud with `download_documents.py` and `data/document_url_map.json` [CARD (GitHub README)].
4. Size: `data/test-00000-of-00001.parquet` 0.04 MB [CARD]. PDF sizes UNVERIFIED.
5. Proof: downloaded the 0.04 MB parquet [ROW]:
   - `{"name":"e5076219","annotations":[{"key":"Is the applicant seeking to utilize the filing date from a previously submitted Application for Alien Employment Certidication (ETA 750)?","values":[{"value":"No"}]},{"key":"What is the prevailing wage source?","values":[{"value":"OES"}]},{"key":"Is training required in the job opportunity?","values":[{"value":"No"}]},...`
   - `{"name":"918b4710", ... "Is experience in the job offered required for the job?" → "Yes" ...}`
   - `{"name":"1be7b805", ... same ETA-9089 question set ...}`
6. Schema: `name`, `extension` (pdf), `annotations[{id,key,values[{value,value_variants}]}]`, `language`, `split`, and `pdf{bytes,path}`, where bytes are **null in all 88 rows** [ROW].
7. Label origin: human (paper title; annotation details not read) [UNVERIFIED].
8. Answer rule: for questions whose `values == ["Yes"]` or `["No"]`, answer = that value. **The page number is not given**, so someone must find the page with the checkbox, which fails "computable without looking" for the single-image format [ROW][INFERRED].
9. Balance: 579 questions: Yes 87, No 163, other (lists or values) 329 [ROW]. Real negatives exist.
10. A document carries several questions. Choose single-page docs only [INFERRED].
11. Risks: real US government filings (ETA-9089 labour certification) that may contain names [INFERRED]. Off-site hosting may disappear.
12. Templates: checkbox yes/no; "What is the prevailing wage source? OES / CBA / DBA / SCA / Other"; "Is training required? yes/no".

### D7.3 — candidate 1: konfuzio/funsd_plus — **GATED** (consent text in the card, even though the API reports not gated)
- Landing: https://huggingface.co/datasets/konfuzio/funsd_plus. API `gated: False`, but the card YAML has `extra_gated_prompt: "You agree to not attempt to determine the identity of individuals… You agree to the terms and conditions of the FUNSD+ license"` with form fields Name/Company/Country/Email [CARD]. Licence: "[FUNSD+ license](https://huggingface.co/datasets/konfuzio/funsd_plus/blob/main/LICENSE)" (not read) [CARD]. datasets-server serves rows anyway: `{"words":["JUL-24-98","12:11","FROM:","TOBACCO","INSTITUTE",...]}`, `{"words":["DES_18_'97.","11:52AM","PHILIP","MORRIS","LEGAL",...]}`, `{"words":["Lec:","Peggy","Goforth","CONTRACT","INFORMATION",...]}` [ROW]. Size 195.2 MB; test parquet 19.78 MB [CARD]. Card stats: "questions with no answers 2691 (18.3%)" [CARD], which gives real yes/no material for D7.3 via `linked_groups`. **A human must read the LICENSE and decide.**

### D7.3 — candidate 2: nielsr/funsd — **MAYBE** (fails: licence unverified; no question–answer links in this mirror)
- Landing: https://huggingface.co/datasets/nielsr/funsd. Owner: https://guillaumejaume.github.io/FUNSD/ (has a "License" menu item, but the licence text did not render in the fetched HTML) [CARD]. Size 16.6 MB; test parquet 4.38 MB [CARD].
- Rows [ROW]: id 0 `words:["R&D",":","Suggestion:","Date:","Licensee","Yes","No",...], ner_tags:[0,3,3,3,5,3,3,0,1,2,2,2,...]`; id 1 `words:["Brand:","Style:","PHOENIX","Company:",...]`; id 2 `words:["DATE:","INITIATED","BY:","COMPLETION",...]`. Images 762×1000.
- Labels: human (FUNSD paper; not fetched) [UNVERIFIED]. Tags: O, B/I-HEADER, B/I-QUESTION, B/I-ANSWER [ROW]. Without links, an "unanswered question" cannot be computed from this mirror; only "count of question fields" can. These are tobacco-industry forms, not government forms [ROW].

### D8.1 — candidate 1: cloverx-id/indonesian-id-card-dummy (config `flat`) — **USE**
1. **Landing:** https://huggingface.co/datasets/cloverx-id/indonesian-id-card-dummy. Listing: `data/flat/` (12 shards of about 1,038 MB) and `data/augmented/` (55 shards of about 65–86 MB) [CARD].
2. **Licence:** `license: cc-by-4.0`. Card: "100% safe for commercial-use licensing (CC-BY 4.0)" [CARD].
3. **Access:** open.
4. **Size:** 34,990 MB. Smallest unit: `data/augmented/train-00051-of-00055.parquet` 65.36 MB. Flat shards are about 1 GB [CARD]. Sample through `/rows`.
5. **Proof:** `https://datasets-server.huggingface.co/first-rows?dataset=cloverx-id/indonesian-id-card-dummy&config=flat&split=train` [ROW]
   - `{"image_name":"card_flat_00000.png","image_width":725,"image_height":451,"nik":"3212175503723347","nama":"NABILA PURWANTI","jenis_kelamin":"PEREMPUAN","golongan_darah":"O","agama":"BUDHA","status_perkawinan":"CERAI MATI","pekerjaan":"PETANI/PEKEBUN","provinsi":"PROVINSI JAWA BARAT",...}`
   - `{"image_name":"card_flat_00001.png","nama":"NABILA AYU PURWANTI","jenis_kelamin":"PEREMPUAN","golongan_darah":"AB","status_perkawinan":"CERAI HIDUP","provinsi":"PROVINSI JAWA TIMUR",...}`
   - `{"image_name":"card_flat_00002.png","nama":"OLIVIA TARI HASTUTI","jenis_kelamin":"PEREMPUAN","golongan_darah":"A","status_perkawinan":"KAWIN","provinsi":"PROVINSI SUMATERA UTARA",...}`
6. **Schema:** 20 printed-field columns (nik, nama, tempat_tanggal_lahir, jenis_kelamin = sex, golongan_darah = blood type, alamat, rt_rw, kel_desa, kecamatan, agama, status_perkawinan = marital status, pekerjaan, kewarganegaraan, berlaku_hingga, provinsi, kota, penerbitan_*), `card_bounding_box`, `annotations_json` (per-field text and box) [ROW].
7. **Label origin:** generator (synthetic "dummy" KTP; the fields are the render inputs) [CARD]. Faces are "real human faces from public directories (UTKFace)… dynamically morphed using… GLAM" [CARD]. That is a **risk**: the faces derive from real people.
8. **Answer rules:** D8.1 sex = `jenis_kelamin` (LAKI-LAKI → M, PEREMPUAN → F). Blood type = `golongan_darah`. Marital status = `status_perkawinan`.
9. **Classes (first 100 flat rows):** jenis_kelamin LAKI-LAKI 55 / PEREMPUAN 45; golongan_darah A 29, O 26, AB 25, B 20; status_perkawinan BELUM KAWIN 31, CERAI MATI 26, CERAI HIDUP 22, KAWIN 21; agama 5 values; kewarganegaraan WNI 100 (constant) [ROW]. Full counts UNVERIFIED (`/statistics` 500).
10. **Per-image fit:** one value per field per card.
11. **Risks:** morphed real faces from UTKFace [CARD]. Flat images are 725×451 (small) [ROW]. Questions about religion should be avoided, since that is a sensitive attribute [INFERRED].
12. **Templates:** sex (M/F); blood type (A/B/AB/O); "Which province issued it? 4 provinces" (`provinsi`).

### D8.6 — candidate 2: same repo, config `augmented` (hard negatives) — **MAYBE** (fails: negatives are third-party real photos that may hold personal data; licence chain unclear)
- The card describes "12,804 high-quality hard negative samples (with empty annotations)" from Roboflow sets including "Vietnamese IDs", "Passports", "Driving Licenses" [CARD]. Also: "there remains a slight possibility" a KTP appears in a negative, and "we do not own, verify, or endorse" the third-party negatives [CARD]. Answer rule: yes if `nik` is not null/empty [INFERRED; negative rows not fetched]. The negatives could contain real IDs, which breaks the specimen-only rule. Do not use without filtering.

### D8.2 / D8.3 — candidate 1: Voxel51/synthetic_us_passports_easy — **USE**
1. **Landing:** https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy. Original: https://huggingface.co/datasets/arnaudstiegler/synthetic_us_passports_easy. Generator repo: https://github.com/arnaudstiegler/synth-doc-AI [CARD].
2. **Licence:** "**License:** Apache-2.0" [CARD].
3. **Access:** open.
4. **Size:** 17,472 MB (9,756 files). Smallest unit: one PNG (up to 12.4 MB). Annotation file `samples.json` 23.38 MB per the listing; the fetched file was 10.05 MB [CARD][ROW].
5. **Proof:** downloaded `https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy/resolve/main/samples.json` (9,750 samples) [ROW]
   - `{"filepath":"data/data_0/passport_000000.png","nationality":{"label":"Samoa"},"place_of_birth":{"label":"Netherlands Antilles"},"authority":{"label":"Azerbaijan"},"sex":{"label":"F"},"type":"W","code":"s","passport_number":"503056413","surname":"Clayton","given_names":"Ronald Farmer","dob":"13 Jan 1988","date_of_issue":"27 Nov 2006","date_of_expiration":"23 Mar 1983"}`
   - `{"filepath":"data/data_0/passport_000001.png","nationality":{"label":"Italy"},"place_of_birth":{"label":"Timor-Leste"},...}`
   - The third row was not printed in full. Only 2 full rows were pasted; a third requires re-running the same command [UNVERIFIED third row].
6. **Schema:** `filepath`; FiftyOne Classifications `nationality`, `place_of_birth`, `authority`, `sex`; strings `type`, `code`, `passport_number`, `surname`, `given_names`, `dob`, `date_of_issue`, `date_of_expiration` [ROW].
7. **Label origin:** generator ("synthetic dataset of US passport images" built with synth-doc-AI) [CARD].
8. **Answer rules:** D8.2 yes if `parse(date_of_expiration) > parse(date_of_issue)`. Row 0 is a real negative: expiry 1983 is before issue 2006 [ROW]. D8.3 = `nationality.label` plus 3 distractor countries.
9. **Balance:** dates look independently random, so roughly mixed [INFERRED]. A full count is computable from samples.json but was not done [UNVERIFIED].
10. One value per image.
11. **Risks:** "tilted documents and high-resolution images where the passport occupies [a small part]" [CARD], so the passport may be small within a large frame. Images are up to 12 MB [CARD]. Random names. Nationality and authority values are random and inconsistent with a US passport, a realism problem [ROW].
12. **Templates:** expiry after issue yes/no; nationality (4); sex (M/F).

### D8.3 / D8.5 — candidate 2: zimka/midv-DoB-mini (MIDV-500 templates) — **MAYBE** (fails: no licence stated)
1. Landing: https://huggingface.co/datasets/zimka/midv-DoB-mini. MIDV-500 paper: https://arxiv.org/abs/1807.05786 [CARD].
2. Licence: none on the card [CARD]. The paper's search snippet says source images "are either in public domain or distributed under public copyright licenses" [PAPER via search snippet]. The dataset licence itself is UNVERIFIED.
3. Access: open.
4. Size: 267.3 MB. Smallest unit: `data/template-00000-of-00001.parquet` 35.68 MB [CARD].
5. Proof: first-rows `template` [ROW]:
   - `{"template_id":16,"view":"template","date_of_birth":"12.08.1964","meta":{"template_name":"deu","original_image_path":"templates/images/16_deu_passport_new.tif",...}}` (577×407)
   - `{"template_id":4,"date_of_birth":"09.09.1971","meta":{"template_name":"aut","original_image_path":"templates/images/04_aut_id.tif"}}` (504×318)
   - `{"template_id":33,"date_of_birth":"03-12-1960","meta":{"template_name":"mac","original_image_path":"templates/images/33_mac_id.tif"}}` (1280×804)
6. Schema: `markup.template_id`, `view`, `date_of_birth`, `meta.template_name` (country code), `meta.original_image_path` (holds passport/id/drvlic) [ROW].
7. Label origin: MIDV-500 human ground truth over specimen templates [UNVERIFIED].
8. Answer rule: D8.5 = "passport" if "passport" is in `original_image_path`, else ID card. D8.3 = `template_name`.
9. Splits: template 46, distortion 184, lightning 92 [CARD].
10. One per image.
11. Risks: specimen images. Small templates (504 px) [ROW]. The paper is from 2018, so overlap is possible.
12. Templates: passport or ID; issuing country (4); "Which date of birth is printed? 4 dates".

### D8.4 — candidate 1: cactuslab/IDNet-2025 — **MAYBE** (fails: SINGLE ARCHIVE per country ≥1.35 GB; no rows)
- Landing: https://huggingface.co/datasets/cactuslab/IDNet-2025. Licence `cc-by-4.0` [CARD]. "entirely synthetically generated and does not contain any private information" [CARD]. Files: `EST.tar.gz` 1,354.22 MB (smallest data archive), `ALB.tar.gz` 14,743.95 MB, … 124,933.5 MB total [CARD]. Structure: "positive" folder (genuine) plus `fraud5_inpaint_and_rewrite` and `fraud6_crop_and_replace` with meta JSONs [CARD], so real negatives exist by design and labels come from a generator. `/splits` is empty, so no sample is possible without fetching more than 1.3 GB. A human could approve one country archive.

### D8.4 — candidate 2: zodumair/sifta-document-forgery-dataset — **MAYBE** (fails: no licence; document type unknown)
- Landing: https://huggingface.co/datasets/zodumair/sifta-document-forgery-dataset. The card is YAML only, with no licence [CARD]. Size 196.5 MB; test parquet 26.14 MB [CARD]. Rows: `{"label":0,"label_name":"real"}` ×3 (1132×1600, 1162×1600, 827×1169) [ROW]. Test balance: real 16 / forged 13 [ROW]. Label origin UNVERIFIED. It is unclear whether the documents are identity documents or real people's papers.

### D9.1 — candidate 1: hyturing/US_tax_forms_donut (NIST Special Database 2) — **USE**
1. **Landing:** https://huggingface.co/datasets/hyturing/US_tax_forms_donut. Owner: https://www.nist.gov/srd/nist-special-database-2 [CARD].
2. **Licence:** `license: mit` (card) [CARD]. NIST page: "Price: No charge" [CARD]. The NIST SRD terms were not read [UNVERIFIED].
3. **Access:** open (HF). NIST zip download is free [CARD].
4. **Size:** 947.0 MB. Smallest unit: `data/test-00000-of-00001.parquet` 95.3 MB [CARD]. Use `/rows`.
5. **Proof:** first-rows and `/rows` [ROW]: `{"label":"1040_1","ground_truth":"{\"gt_parse\": {\"class\" : \"1040_1\"}}"}` (2560×3300); `{"label":"4562_1",...}`; `{"label":"sch_a",...}`; test row 0 `{"label":"sch_e_2"}`.
6. **Schema:** `image`, `label` str (form face), `ground_truth` (Donut JSON holding only the class in the rows seen; the card's "Full text ground truth" was not seen) [ROW].
7. **Label origin:** generator. NIST: "5,590 pages of binary, black-and-white images of synthesized documents… The document images… appear to be real forms prepared by individuals, but the images have been automatically derived and synthesized using a computer" [CARD].
8. **Answer rule:** answer = `label`. Build 4–6 options from a related family (e.g. {1040_1, 1040_2, sch_a, sch_b, sch_e_1, sch_e_2}).
9. **Classes (test, 559):** 1040_2 105, 1040_1 88, sch_a 54, sch_b 51, sch_e_2 34, sch_e_1 33, sch_d_2 28, sch_d_1 23, 4562_2 21, 4562_1 22, sch_c_1 20, sch_se_2 15, 2106_1 10, sch_c_2 10, sch_se_1 9, 6251 9, sch_f_1 7, sch_f_2 7, 2106_2 7, 2441 6 [ROW].
10. One form face per image.
11. **Risks:** binary B/W 1988 forms. Images are 2560×3300 (good) [ROW]. Synthetic people. NIST SD2 is old and widely distributed (moderate overlap) [INFERRED].
12. **Templates:** form face (6); "Is this page 1 or page 2 of the form? 1/2" (suffix); "Is this a Schedule (A–F, SE) rather than a numbered form? yes/no".

### D9.2 / D9.3 — candidate 1: singhsays/fake-w2-us-tax-form-dataset — **USE** (medium; the licence comes from the upstream Kaggle page, not the HF card)
1. **Landing:** https://huggingface.co/datasets/singhsays/fake-w2-us-tax-form-dataset. Upstream: https://www.kaggle.com/datasets/mcvishnu1/fake-w2-us-tax-form-dataset [CARD].
2. **Licence:** the HF card has none. The Kaggle API for the upstream gives `"licenseName": "CC0: Public Domain"` [CARD] (https://www.kaggle.com/api/v1/datasets/view/mcvishnu1/fake-w2-us-tax-form-dataset).
3. **Access:** open on HF.
4. **Size:** 309.6 MB. Smallest unit: `data/test-…parquet` 15.47 MB [CARD].
5. **Proof:** first-rows and `/rows` test [ROW]
   - `{"box_b_employer_identification_number":"47-5592725","box_c_employer_name":"Bennett, Allen and Yang Inc","box_a_employee_ssn":"412-88-2525",...}`
   - `{"box_b_employer_identification_number":"87-6351907","box_c_employer_name":"White-Rivera Group",...}`
   - test row 0: `{"box_1_wages":126589.34,"box_2_federal_tax_withheld":43873.99,...,"box_12a_code":"E","box_12b_code":"None","box_12c_code":"D","box_13_statutary_employee":"x","box_13_retirement_plan":"None","box_13_third_part_sick_pay":"x","box_15_1_state":"HI","box_15_2_state":"WI",...}`
6. **Schema:** a `ground_truth` JSON with every W-2 box (box_a … box_20_2) [ROW].
7. **Label origin:** generator: "synthetically generated US Tax Return W2 Forms, with generated fake data such as names, ids, dates and addresses. Only real city, state and zipcodes have been used" [CARD].
8. **Answer rules:** D9.3 yes if `box_13_statutary_employee == "x"`. D9.2 = `box_15_1_state` plus 3 distractor states.
9. **Balance:** "x" and "None" values both occur [ROW]. Counts UNVERIFIED.
10. One value per box.
11. **Risks:** fake SSNs [ROW]. Images are 612×792 (small: a PDF page at 72 dpi) [ROW]. Values are random and internally inconsistent (e.g. SS wages larger than wages) [ROW].
12. **Templates:** box 13 statutory ticked yes/no; state in box 15 (4); "Which code is in box 12a? D / E / C / DD".

### D10.2 / D10.3 — candidate 1: ilovelevi/business_card_dataset — **MAYBE** (fails: no licence; origin unknown; `is_business_card` is all true)
1. Landing: https://huggingface.co/datasets/ilovelevi/business_card_dataset. Annotation file: `labels/labels.json` 0.39 MB [CARD].
2. Licence: none; the README is 15 bytes [CARD].
3. Access: open.
4. Size: 40.1 MB; images 0.02–0.33 MB each [CARD].
5. Proof: downloaded labels.json (500 entries) [ROW]
   - `{"images":["card_00000.jpg"],"assistant":{"is_business_card":true,"name":"박서연","company":"유한회사 에스와이코퍼레이션","job_title":"대리","email":"help@daum.net","company_phone":" 82-634039322","mobile_phone":""},"augmentation":{"blur":2.0,"noise":3,"shadow":false,...}}`
   - `{"images":["card_00001.jpg"],"assistant":{"is_business_card":true,"name":"조지수","company":"㈜ 나노하이텍 Co.Ltd.","job_title":"부장","email":"info@company.co.kr","company_phone":"  82-32 912 6140","mobile_phone":""},"augmentation":{"blur":1.5,"noise":20,"shadow":true,...}}`
   - Only two rows were pasted in full. Count: `is_business_card` True 500 / False 0 [ROW].
6. Schema: chat-format messages; the assistant content has `is_business_card`, name, company, job_title, department, email, company_phone, mobile_phone; plus `augmentation` [ROW].
7. Label origin: the `augmentation` block suggests generated images with known values (generator) [INFERRED]. UNVERIFIED.
8. Answer rules: D10.2 yes if `email != ""`; D10.3 yes if `mobile_phone.strip() != ""`.
9. Negatives: the "is this a business card" task has none. Email and mobile presence are mixed (mobile is empty in 2/2 fetched) [ROW]. Full balance not computed.
10. One value per card.
11. Risks: Korean names that may resemble real people. 856×540 [ROW].
12. Templates: email present; mobile present; "Which job title is printed? 대리 / 부장 / 과장 / 사원".

### D10 — d4rk3r/resumes-raw-pdf — **SKIP** (fails: the label is a folder name ("all-domains" / "it-domain"), not a checkable visual fact; PDFs only)
- Licence `mit` [CARD]. Rows: `{"label":0}` ×3 with PDF thumbnails 612×792 / 595×842 / 596×842 [ROW]. 832.4 MB [CARD].

### Other probes rejected (recorded for completeness)
- **Naiscorp/car-damage-dataset:** labels are opaque folder ids "001"…"N" (`{"label":0}`) [ROW]; licence `other` [CARD] → SKIP.
- **ikuldeep1/vehicle-damage-fraud-image-balanced:** labels "0"/"1" with no card [ROW][CARD] → SKIP.
- **Reverb/CarDamage:** despite the name, the classes are `frontJOimages`, `backQAimages1`, `frontUAEimages`… with files `card_175.png` [ROW][CARD]. These look like front/back **identity cards from Jordan, Qatar and UAE**, possibly real; the README is 24 bytes → SKIP (personal-data risk).
- **erickcrus/BID_Dataset:** 20 rows of Brazilian ID ground truth (`{"name":"GALIZIA EVELY ANOUCH","rg":"911290060",...}`) [ROW]; no licence [CARD] → SKIP (too small; licence).
- **GIGAParviz/stamp_detection2:** label txt files only, no images in the viewer (`{"text":"stamp"}`, polygon rows) [ROW]; no licence → SKIP.
- **FrenchCastle/xray-baggages-customs:** licence `other`; zips of 6.4–7.2 GB each; viewer 501 [CARD] → SKIP (single huge archives; security screening, not customs paperwork).
- **unc061/cz-stk-odometer:** a tabular VIN → km index from Czech inspections, not images [CARD] → not applicable to D3.6.
- **Ronysalem/medical-forms-dataset:** 8 rows of clinical forms (chief complaints) [ROW] → SKIP (clinical content; too small).

---

## Part C. Question-expansion recipes (USE-rated candidates)

General rule for every dataset: Tier A and B rows carry `label_origin: human|generator` and `tier: A|B`. Tier C rows always carry `label_origin: model`, `tier: C`, and the writer model's id. They are stored in a separate file and never pooled into Tier A/B scores. A Tier C question is kept only if a second, different model answers it identically, blind to the first model's answer. The model under test never writes questions. The most useful Tier C outputs are (1) rewordings of Tier A questions (for robustness), (2) harder distractors that are still verifiably wrong under the Tier A rule, and (3) natural-language variety in locale or phrasing.

**jaganadhg/cheque-synthetic-images (D1.1)**
- A: bank (4).
- B: (1) "Is the signature box in the lower-right quadrant?" (`sign.xmin > W/2 and sign.ymin > H/2`); (2) "Which field is topmost? date / IFSC / name" (min ymin); (3) "Is the amount box wider than the account-number box?" (width compare); (4) "Which field is NOT where it usually is?" Skip this one: there is no variation.
- C: rewordings ("Which bank printed this cheque leaf?"); distractor bank names from other Indian banks (must not be the 4 truths). Avoid asking for printed account numbers (personal data).

**jsdnrs/ICDAR2019-SROIE (D2.1)**
- A: total (4 options); date (4); company (4).
- B: (1) "Is the total above RM 50?" (`float(total) > 50`); (2) "Is the receipt dated in 2018?" (parse date); (3) "Which of these strings does NOT appear on the receipt?" (3 from `words` plus 1 from another receipt); (4) "Does the word 'INVOICE' or 'TAX INVOICE' appear?" (substring in `words`; note that `words` is human transcript, not OCR); (5) "How many text lines does the receipt have? <30 / 30–50 / >50" (`len(words)`).
- C: rephrase questions in Malay or English; distractor totals that also appear on the receipt (subtotal, cash tendered), validated against `entities.total`.

**albertobarnabo/synthetic-receipts-ocr (D2.2, D2.3)**
- A: payment class; locale; tax_included.
- B: (1) item count bucket (`n_items`); (2) "Is a loyalty line printed?" (`loyalty != null`); (3) "Was change given?" (`change != null`); (4) "Which item is the most expensive? 4 names" (`argmax lines.total`); (5) "Is the VAT rate 22%? yes/no" (from `taxes.rate`). Also pair `image_clean` with `image_photo` to test degradation robustness.
- C: locale-specific rephrasings; distractors from same-locale payment words.

**HV09/synthetic-bilingual-invoices-200 (D2.4, D2.5)**
- A: PO present; Hijri date; currency; language style.
- B: (1) "Is VAT about 5% of subtotal?" (`abs(vat/subtotal - 0.05) < 0.001`); (2) "Is quantity above 200?" (`qty`); (3) "Which total is correct? 4 numbers" (`total` plus perturbed values); (4) "Which invoice number is printed? 4" (`invoice_number`).
- C: Arabic rewordings; Eastern-Arabic numeral distractors. The second model must agree.

**katanaml-org/invoices-donut-data-v1 (D2.6)**
- A: line-item count; invoice number.
- B: (1) VAT rate class (`item_vat`); (2) "Is gross total above $1,000?" (parse summary); (3) "Which invoice date year? 4 years"; (4) "Does an IBAN appear?" (`header.iban` non-empty).
- C: rewordings; item-description distractors.

**DrBimmer/comprehensive-car-damage (D3.1–D3.3)**
- A: damaged yes/no; front/rear; none/breakage/crushed.
- B: (1) "Is this an undamaged rear view?" (label == R_Normal); (2) "Which of these is NOT shown: front breakage / rear crush / front normal?" (one true, two false); (3) a pair task, "Do these two images show the same end of the car?" (only if two-image prompts are allowed; otherwise skip).
- C: claims-adjuster phrasing ("Would you file this as a front-end collision?"), kept separate. Distractors such as "flood damage" are unverifiable, so they are disallowed in A/B.

**QCRI/CrisisMMD (D4.1, D4.3)**
- A: damage severity (3); infrastructure damage yes/no (from `label_image`).
- B: (1) "Is there any damage (mild or severe)?" (label ≠ little_or_no); (2) disaster type from `event_name` (hurricane_harvey/irma/maria → hurricane; california_wildfires → wildfire; mexico/iraq_iran earthquake → earthquake; srilanka_floods → flood); (3) "Which event is this from? 4 events" (`event_name`). Note: the event label is metadata, not a visual property, so it is weaker.
- C: rewordings; never use the tweet text as a question source (personal data).

**DocLayNet (D6.2, D6.3, D7.2)**
- A: doc_category (6); government tender yes/no.
- B: (1) table present; (2) picture present; (3) "How many tables? 0 / 1 / 2 / 3+" (count of the class id); (4) "Is there a formula?" (Formula id); (5) "Which element is largest by area? text / table / picture" (`area` argmax per class).
- C: legal-review phrasing ("Is this a statute page?"); distractor categories that are near synonyms (borrow nutrientdocs OOV synonyms).

**cloverx-id/indonesian-id-card-dummy flat (D8.1)**
- A: sex; blood type; marital status.
- B: (1) "Is the card valid for life (SEUMUR HIDUP)?" (`berlaku_hingga`); (2) "Which province? 4" (`provinsi`); (3) "Is the holder born before 1980?" (parse `tempat_tanggal_lahir`); (4) "Which occupation is printed? 4" (`pekerjaan`). Avoid `agama` (religion).
- C: English rewordings of Indonesian field names.

**Voxel51/synthetic_us_passports_easy (D8.2, D8.3)**
- A: expiry after issue; nationality; sex.
- B: (1) "Is the holder over 18 on the issue date?" (dob vs date_of_issue); (2) "Is the passport expired as of 2026-10-01?" (date_of_expiration < ref); (3) "Which passport number is printed? 4" (distractors with one digit changed); (4) "Does place of birth equal nationality?" (compare labels).
- C: KYC-analyst phrasing; distractor countries close in name.

**hyturing/US_tax_forms_donut (D9.1)**
- A: form face (6 within a family).
- B: (1) page 1 vs 2; (2) Schedule vs numbered form; (3) "Which form family? 1040 / 4562 / 2106 / 6251" (prefix).
- C: rewordings ("Which IRS attachment is this?").

**singhsays/fake-w2 (D9.2, D9.3)**
- A: box 13 statutory; state in box 15.
- B: (1) "Is federal withholding above 30% of wages?" (box2/box1); (2) "How many box-12 codes are filled? 0–4" (count of non-"None" codes); (3) "Is there a second state line?" (`box_15_2_state` not None); (4) "Which box-12a code? 4".
- C: payroll-clerk phrasing.

---

## 3. CSV

```csv
domain,task_id,task,dataset,landing_url,repo_id,licence,licence_quote_url,access,total_mb,smallest_fetch_mb,single_archive,sample_proof_url,rows_pasted,label_origin,answer_rule,has_negatives,classes,one_answer_per_image,personal_data_risk,verdict,confidence,unverified_fields
1,D1.1,Cheque issuing bank,IDRBT synthetic cheques,https://huggingface.co/datasets/jaganadhg/cheque-synthetic-images,jaganadhg/cheque-synthetic-images,apache-2.0,https://huggingface.co/datasets/jaganadhg/cheque-synthetic-images/raw/main/README.md,open,466.1,76.11,no,https://datasets-server.huggingface.co/first-rows?dataset=jaganadhg/cheque-synthetic-images&config=default&split=train,yes,generator,answer=bank,n/a,axis|canara|icici|syndicate,yes,medium (real field patches),USE,high,IDRBT upstream terms
1,D1.2,Amount words vs figures,cheques_sample_data,https://huggingface.co/datasets/shivalikasingh/cheques_sample_data,shivalikasingh/cheques_sample_data,none,UNVERIFIED,open,58.9,5.87,no,https://datasets-server.huggingface.co/first-rows?dataset=shivalikasingh/cheques_sample_data&config=default&split=train,yes,UNVERIFIED,yes if words2num(amt_in_words)==amt_in_figures,UNVERIFIED,match|mismatch,yes,low (fake names),MAYBE,low,licence;label_origin;balance;tiny 512x256
1,D1.2,Amount words vs figures,handwritten_cheque_vqa_dataset,https://huggingface.co/datasets/aniketVerma07/handwritten_cheque_vqa_dataset,aniketVerma07/handwritten_cheque_vqa_dataset,apache-2.0,https://huggingface.co/datasets/aniketVerma07/handwritten_cheque_vqa_dataset,open,481.6,50.19,no,https://datasets-server.huggingface.co/first-rows?dataset=aniketVerma07/handwritten_cheque_vqa_dataset&config=default&split=train,yes,UNVERIFIED,filter cheque queries then words2num compare,yes (611 vs 1070 seen),match|mismatch,yes,low,MAYBE,low,label_origin;balance;tiny images
1,D1.5,Statement type,Bankstatemently benchmark,https://huggingface.co/datasets/Bankstatemently/bank-statement-parsing-benchmark,Bankstatemently/bank-statement-parsing-benchmark,MIT,https://huggingface.co/datasets/Bankstatemently/bank-statement-parsing-benchmark,open,0.4,0.02,no,https://datasets-server.huggingface.co/first-rows?dataset=Bankstatemently/bank-statement-parsing-benchmark&config=default&split=train,yes,generator,answer=documentType,n/a,bank-statement|credit-card,yes,none,MAYBE,med,only 5 docs
1,D1.6,Transaction table on page,bank-statement-detection,https://huggingface.co/datasets/Panhapich/bank-statement-detection,Panhapich/bank-statement-detection,MIT,https://huggingface.co/datasets/Panhapich/bank-statement-detection,open,3534.8,406.22,no,https://datasets-server.huggingface.co/first-rows?dataset=Panhapich/bank-statement-detection&config=default&split=train,yes,generator,yes if len(objects.category)>0,UNVERIFIED,table,yes,none,MAYBE,med,negatives
2,D2.1,Receipt total,ICDAR2019 SROIE,https://huggingface.co/datasets/jsdnrs/ICDAR2019-SROIE,jsdnrs/ICDAR2019-SROIE,CC-BY-4.0,https://huggingface.co/datasets/jsdnrs/ICDAR2019-SROIE/raw/main/README.md,open,509.8,191.05,no,https://datasets-server.huggingface.co/first-rows?dataset=jsdnrs/ICDAR2019-SROIE&config=default&split=train,yes,human,correct=entities.total; distractors=other money strings in words,n/a,n/a,yes,medium (cashier names),USE,high,annotation workflow
2,D2.2;D2.3,Payment method; receipt country,synthetic-receipts-ocr,https://huggingface.co/datasets/albertobarnabo/synthetic-receipts-ocr,albertobarnabo/synthetic-receipts-ocr,apache-2.0,https://huggingface.co/datasets/albertobarnabo/synthetic-receipts-ocr/raw/main/README.md,open,4084.7,227.56,no,https://datasets-server.huggingface.co/rows?dataset=albertobarnabo/synthetic-receipts-ocr&config=default&split=eval&offset=0&length=100,yes,generator,map fields.payment to cash|card|contactless|wallet; locale,n/a,US|UK|DE|IT|FR; payment strings,yes,none,USE,high,full class counts
2,D2.4;D2.5,PO present; Hijri date,synthetic-bilingual-invoices-200,https://huggingface.co/datasets/HV09/synthetic-bilingual-invoices-200,HV09/synthetic-bilingual-invoices-200,CC-BY-4.0,https://huggingface.co/datasets/HV09/synthetic-bilingual-invoices-200/raw/main/README.md,open,7.4,0.1,no,https://huggingface.co/datasets/HV09/synthetic-bilingual-invoices-200/resolve/main/data/metadata.jsonl,yes,generator,yes if po_reference not null; yes if date_calendar==hijri,yes (70 no-PO; 185 gregorian),po 130/70; hijri 15/185,yes,none,USE,high,none
2,D2.6,Line-item count,Sparrow invoices,https://huggingface.co/datasets/katanaml-org/invoices-donut-data-v1,katanaml-org/invoices-donut-data-v1,MIT,https://huggingface.co/datasets/katanaml-org/invoices-donut-data-v1/raw/main/README.md,open,197.5,10.44,no,https://datasets-server.huggingface.co/first-rows?dataset=katanaml-org/invoices-donut-data-v1&config=default&split=train,yes,human,len(items) bucketed,n/a,UNVERIFIED,yes,low (fake tax ids),USE,med,count distribution; Mendeley licence
3,D3.1;D3.2;D3.3,Car damaged; front/rear; damage kind,comprehensive-car-damage,https://huggingface.co/datasets/DrBimmer/comprehensive-car-damage,DrBimmer/comprehensive-car-damage,MIT,https://huggingface.co/datasets/DrBimmer/comprehensive-car-damage/raw/main/README.md,open,668.8,0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=DrBimmer/comprehensive-car-damage&config=default&split=train,yes,human,damaged if label not *_Normal; F_/R_ prefix; suffix,yes (800 normal),F_Breakage 500|F_Crushed 400|F_Normal 500|R_Breakage 300|R_Crushed 300|R_Normal 300,yes,medium (plates),USE,med,image provenance
3,D3.1,Car damaged,Kaggle car-damage-detection,https://www.kaggle.com/datasets/anujms/car-damage-detection,,Unknown,https://www.kaggle.com/api/v1/datasets/view/anujms/car-damage-detection,login,130.0,130.0,yes,none,no,UNVERIFIED,folder damaged|whole,UNVERIFIED,damaged|whole,yes,UNVERIFIED,MAYBE,low,licence;rows;access
3,D3.4,Damage type,damaged-car-dataset-annotated,https://huggingface.co/datasets/gigwegbe/damaged-car-dataset-annotated,gigwegbe/damaged-car-dataset-annotated,none,UNVERIFIED,open,1288.9,404.47,no,https://datasets-server.huggingface.co/first-rows?dataset=gigwegbe/damaged-car-dataset-annotated&config=default&split=train,yes,UNVERIFIED,single category per image,no,crack|dent|glass shatter|lamp broken|scratch|tire flat,no,medium,MAYBE,low,licence;origin (possible CarDD)
3,D3.4,Damage type,AutoDamageIQ,https://huggingface.co/datasets/tugberkkalay/autodamageiq-vehicle-damage-dataset,tugberkkalay/autodamageiq-vehicle-damage-dataset,CC-BY-4.0,https://huggingface.co/datasets/tugberkkalay/autodamageiq-vehicle-damage-dataset/raw/main/README.md,open,557.7,0.01,no,none (viewer 500),no,machine (GPT-4o) + CarDD,n/a,no,6 classes,no,medium,SKIP,high,n/a
3,D3.5,Body style,Stanford Cars,https://huggingface.co/datasets/tanganke/stanford_cars,tanganke/stanford_cars,none,UNVERIFIED,open,6016.5,3.74,no,https://datasets-server.huggingface.co/first-rows?dataset=tanganke/stanford_cars&config=default&split=train,yes,UNVERIFIED,body token in class name,n/a,196,yes,medium (plates),MAYBE,low,licence;tiny images
4,D4.1,Damage severity,CrisisMMD v2 damage,https://huggingface.co/datasets/QCRI/CrisisMMD,QCRI/CrisisMMD,CC-BY-NC-SA-4.0,https://huggingface.co/datasets/QCRI/CrisisMMD/raw/main/README.md,open,1941.0,3.07,no,https://datasets-server.huggingface.co/first-rows?dataset=QCRI/CrisisMMD&config=damage&split=train,yes,human,answer=label (image label),yes (little_or_no 333 train),little 333|mild 587|severe 1548 (train),yes,medium (faces; tweets),USE,high,none
4,D4.3,Infrastructure damage,CrisisMMD v2 humanitarian (label_image),https://crisisnlp.qcri.org/data/crisismmd/crisismmd_datasplit_all.zip,QCRI/CrisisMMD,CC-BY-NC-SA-4.0,https://huggingface.co/datasets/QCRI/CrisisMMD/raw/main/README.md,open,1941.0,3.07,no,https://datasets-server.huggingface.co/first-rows?dataset=QCRI/CrisisMMD&config=humanitarian&split=test,yes,human,yes if label_image==infrastructure_and_utility_damage; no if not_humanitarian,yes (849 not_humanitarian test),8 humanitarian classes,yes,medium,USE,med,label_image values not printed
4,D4.1;D4.2;D4.4,Severity; disaster type; flood,MEDIC,https://huggingface.co/datasets/QCRI/MEDIC,QCRI/MEDIC,CC-BY-NC-SA-4.0,https://huggingface.co/datasets/QCRI/MEDIC/raw/main/README.md,open,10940.1,163.45,no,https://datasets-server.huggingface.co/first-rows?dataset=QCRI/MEDIC&config=default&split=train,yes,UNVERIFIED (mixed sources),disaster_types; damage_severity,yes (not_disaster 8885 test),7 disaster types; 3 severities,yes,medium,MAYBE,med,label origin; terms-of-use.txt
5,D5.1,Claim form type,coherent-forms-1040-cms1500-i9,https://huggingface.co/datasets/Symage/coherent-forms-1040-cms1500-i9,Symage/coherent-forms-1040-cms1500-i9,other,https://huggingface.co/datasets/Symage/coherent-forms-1040-cms1500-i9,manual approval,1971.4,394.46,no,none (401),no,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,UNVERIFIED,GATED,low,all
5,D5.2,Medication count,medical-prescription-dataset,https://huggingface.co/datasets/chinmays18/medical-prescription-dataset,chinmays18/medical-prescription-dataset,none,UNVERIFIED,open,983.8,0.01,no,https://datasets-server.huggingface.co/first-rows?dataset=chinmays18/medical-prescription-dataset&config=default&split=train,yes,UNVERIFIED,count '- <drug>' entries,n/a,3|4 seen,yes,low (fictional),MAYBE,low,licence;origin
5,D5.4,Itemised bill,medical-bill-samples,https://huggingface.co/datasets/sansverse/medical-bill-samples,sansverse/medical-bill-samples,none,UNVERIFIED,open,31.0,0.23,no,https://datasets-server.huggingface.co/first-rows?dataset=sansverse/medical-bill-samples&config=default&split=train,yes,none,cannot compute,no,none,n/a,UNVERIFIED,SKIP,high,n/a
6,D6.1,Document signed,signature-detection,https://huggingface.co/datasets/tech4humans/signature-detection,tech4humans/signature-detection,apache-2.0 (tag),https://huggingface.co/datasets/tech4humans/signature-detection,manual approval,147.4,17.21,no,none (401),no,UNVERIFIED,UNVERIFIED,UNVERIFIED,signature,UNVERIFIED,medium (signatures),GATED,low,all
6,D6.2;D6.3;D7.2,Page category; table present; tender page,DocLayNet,https://huggingface.co/datasets/docling-project/DocLayNet-v1.2,docling-project/DocLayNet-v1.2,CDLA-Permissive-1.0,https://huggingface.co/datasets/docling-project/DocLayNet-v1.1/raw/main/README.md,open,39770.6,266.5,no,https://datasets-server.huggingface.co/first-rows?dataset=pierreguillou/DocLayNet-small&config=DocLayNet_2022.08_processed_on_2023.01&split=train,yes,human,doc_category; Table id in category_id,yes,6 doc categories; 11 layout classes,yes,low,USE,high,v1.2 class-id mapping
6,D6.2;D9.4;D7.4,Doc type incl IRS forms,document-classification-benchmark,https://huggingface.co/datasets/nutrientdocs/document-classification-benchmark,nutrientdocs/document-classification-benchmark,other (per-row tags),https://huggingface.co/datasets/nutrientdocs/document-classification-benchmark/raw/main/README.md,open,453.7,453.67,yes,https://datasets-server.huggingface.co/rows?dataset=nutrientdocs/document-classification-benchmark&config=default&split=test&offset=377&length=2,yes,mixed (generator forms; human DocLayNet),answer=label,n/a,34 labels,yes,low,MAYBE,med,dataset-level licence
7,D7.1,Checkbox state,CheckboxQA,https://huggingface.co/datasets/mturski/CheckboxQA,mturski/CheckboxQA,CC-BY-NC-4.0,https://huggingface.co/datasets/mturski/CheckboxQA/raw/main/README.md,open (docs off-site),0.3,0.04,no,https://huggingface.co/datasets/mturski/CheckboxQA/resolve/main/data/test-00000-of-00001.parquet,yes,UNVERIFIED (human per paper),values==[Yes]/[No] but page unknown,yes (163 No / 87 Yes),yes|no|other,no (multi-question multi-page),medium (real filings),MAYBE,med,page index; PDFs
7,D7.3,Unanswered field,FUNSD+,https://huggingface.co/datasets/konfuzio/funsd_plus,konfuzio/funsd_plus,FUNSD+ license (unread),https://huggingface.co/datasets/konfuzio/funsd_plus/blob/main/LICENSE,form or email request,195.2,19.78,no,https://datasets-server.huggingface.co/first-rows?dataset=konfuzio/funsd_plus&config=default&split=train,yes,UNVERIFIED,question group with no linked answer,yes (18.3% per card),header|question|answer,no,medium (names),GATED,med,licence text
7,D7.3,Form fields,FUNSD (nielsr),https://huggingface.co/datasets/nielsr/funsd,nielsr/funsd,UNVERIFIED,https://guillaumejaume.github.io/FUNSD/,open,16.6,4.38,no,https://datasets-server.huggingface.co/first-rows?dataset=nielsr/funsd&config=default&split=train,yes,UNVERIFIED,count B-QUESTION tags,n/a,O|HEADER|QUESTION|ANSWER,yes,medium (names),MAYBE,low,licence;origin;links
8,D8.1,Printed sex / blood type on synthetic KTP,indonesian-id-card-dummy (flat),https://huggingface.co/datasets/cloverx-id/indonesian-id-card-dummy,cloverx-id/indonesian-id-card-dummy,CC-BY-4.0,https://huggingface.co/datasets/cloverx-id/indonesian-id-card-dummy/raw/main/README.md,open,34990.2,65.36,no,https://datasets-server.huggingface.co/first-rows?dataset=cloverx-id/indonesian-id-card-dummy&config=flat&split=train,yes,generator,jenis_kelamin; golongan_darah,n/a,M 55/F 45; A29 O26 AB25 B20 (sample),yes,medium (morphed real faces),USE,med,full counts
8,D8.6,KTP present in photo,indonesian-id-card-dummy (augmented),https://huggingface.co/datasets/cloverx-id/indonesian-id-card-dummy,cloverx-id/indonesian-id-card-dummy,CC-BY-4.0 (third-party negatives),https://huggingface.co/datasets/cloverx-id/indonesian-id-card-dummy/raw/main/README.md,open,34990.2,65.36,no,https://datasets-server.huggingface.co/info?dataset=cloverx-id/indonesian-id-card-dummy&config=augmented,no,generator + third-party,yes if nik non-empty,yes (12804 negatives per card),ktp|none,yes,high (real IDs in negatives),MAYBE,low,negative rows; licences of negatives
8,D8.2;D8.3,Expiry after issue; nationality,synthetic_us_passports_easy,https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy,Voxel51/synthetic_us_passports_easy,Apache-2.0,https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy/raw/main/README.md,open,17472.3,10.05,no,https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy/resolve/main/samples.json,yes,generator,date_of_expiration>date_of_issue; nationality.label,yes (row 0 expiry<issue),nationality many; sex F|M,yes,low,USE,med,third row; balance
8,D8.3;D8.5,Issuing country; passport vs ID,midv-DoB-mini,https://huggingface.co/datasets/zimka/midv-DoB-mini,zimka/midv-DoB-mini,none,UNVERIFIED,open,267.3,35.68,no,https://datasets-server.huggingface.co/first-rows?dataset=zimka/midv-DoB-mini&config=default&split=template,yes,UNVERIFIED,'passport' in original_image_path; template_name,n/a,~50 templates,yes,low (specimens),MAYBE,low,licence
8,D8.4,Tampered ID,IDNet-2025,https://huggingface.co/datasets/cactuslab/IDNet-2025,cactuslab/IDNet-2025,CC-BY-4.0,https://huggingface.co/datasets/cactuslab/IDNet-2025/raw/main/README.md,open,124933.5,1354.22,yes,none (no splits),no,generator,positive vs fraud5/fraud6 folders,yes (by design),genuine|inpaint_rewrite|crop_replace,yes,none (synthetic),MAYBE,med,rows; meta JSON fields
8,D8.4,Forged document,sifta-document-forgery,https://huggingface.co/datasets/zodumair/sifta-document-forgery-dataset,zodumair/sifta-document-forgery-dataset,none,UNVERIFIED,open,196.5,26.14,no,https://datasets-server.huggingface.co/first-rows?dataset=zodumair/sifta-document-forgery-dataset&config=default&split=train,yes,UNVERIFIED,answer=label_name,yes (real 16/forged 13 test),real|forged,yes,UNVERIFIED,MAYBE,low,licence;origin;doc type
9,D9.1,Tax form page,NIST SD2 (US tax forms donut),https://huggingface.co/datasets/hyturing/US_tax_forms_donut,hyturing/US_tax_forms_donut,MIT (HF card); NIST no charge,https://huggingface.co/datasets/hyturing/US_tax_forms_donut/raw/main/README.md,open,947.0,95.3,no,https://datasets-server.huggingface.co/first-rows?dataset=hyturing/US_tax_forms_donut&config=default&split=train,yes,generator,answer=label,n/a,20 form faces (counts in card),yes,none (synthesized),USE,high,NIST SRD terms
9,D9.2;D9.3,W-2 state; box 13,fake W-2,https://huggingface.co/datasets/singhsays/fake-w2-us-tax-form-dataset,singhsays/fake-w2-us-tax-form-dataset,CC0 (upstream Kaggle),https://www.kaggle.com/api/v1/datasets/view/mcvishnu1/fake-w2-us-tax-form-dataset,open,309.6,15.47,no,https://datasets-server.huggingface.co/rows?dataset=singhsays/fake-w2-us-tax-form-dataset&config=default&split=test&offset=0&length=1,yes,generator,box_13_statutary_employee=='x'; box_15_1_state,yes (x and None both seen),state codes; x|None,yes,low (fake SSNs),USE,med,balance; HF card licence absent
10,D10.2;D10.3,Card shows email / mobile,business_card_dataset,https://huggingface.co/datasets/ilovelevi/business_card_dataset,ilovelevi/business_card_dataset,none,UNVERIFIED,open,40.1,0.39,no,https://huggingface.co/datasets/ilovelevi/business_card_dataset/resolve/main/labels/labels.json,yes,UNVERIFIED (likely generator),email!=''; mobile_phone!='',UNVERIFIED,is_business_card all true,yes,medium (names),MAYBE,low,licence;origin;balance
10,D10,Resume domain,resumes-raw-pdf,https://huggingface.co/datasets/d4rk3r/resumes-raw-pdf,d4rk3r/resumes-raw-pdf,MIT,https://huggingface.co/datasets/d4rk3r/resumes-raw-pdf,open,832.4,0.02,no,https://datasets-server.huggingface.co/first-rows?dataset=d4rk3r/resumes-raw-pdf&config=default&split=train,yes,folder,not a visual fact,n/a,all-domains|it-domain,yes,high (resumes),SKIP,high,n/a
```

---

## 4. Gaps (tasks with no acceptable dataset) and whether a generator is realistic

| task | why no dataset | generator realistic? how |
|---|---|---|
| D1.3 Cheque signed | jaganadhg always has a `sign` box, so there are no negatives [ROW]. | **Yes.** Reuse the jaganadhg blank bank templates (or draw cheque leaves) and paste or omit a signature patch. Signatures can be synthetic handwriting fonts. Answer = whether the patch was pasted. |
| D1.4 Stale-dated cheque | shivalikasingh dates are constant "06/05/22" [ROW]. | **Yes.** Render random dates on cheque templates. Answer = date vs reference. |
| D3.6 Odometer reading | Only tabular odometer data was found (cz-stk) [CARD]. | **Partly.** Render digital odometer LCD crops with known values. Realism of dashboard photos is limited. Real photos are needed for production fidelity. |
| D4.5 Roof damage (ground level) | Only aerial sets, and xBD was rejected. | **No** for a realistic look; human photos are needed. CrisisMMD/MEDIC severity is the nearest proxy. |
| D5.1/D5.3 CMS-1500 / UB-04 form type, signed | Symage is GATED. | **Yes.** CMS-1500 is a public form. Fill a blank PDF with Faker values, optionally sign box 12/13/31, and render it. Answers come from the generator. Very realistic. |
| D5.4 Itemised bill | No labelled data. | **Yes.** Render hospital bills with or without line items. |
| D5.5 Insurance card plan type | None found. | **Yes.** Draw member cards with HMO/PPO text. Use fake payers only, never real brands (brand impersonation risk). |
| D6.1 Signed page | tech4humans is GATED. | **Yes.** Render contract pages from public-domain templates and add or omit a signature image in the signature block. |
| D6.4 Stamp / seal | No licensed, image-bearing set (GIGAParviz has no images or licence). | **Yes.** Draw generic round or rectangular stamps (fake org names) onto DocLayNet-style pages. |
| D6.5 Redaction | None. | **Yes.** Black-box random text spans on rendered pages. Answer = whether boxes were drawn. Trivial and realistic. |
| D7.5 Permit validity | None. | **Yes.** Render generic permit templates with issue and expiry dates. |
| D9.5 Customs declaration (CN22/CN23) | None found on HF. | **Yes.** CN22/CN23 layouts are public (UPU); fill category ticks, contents and values with a generator. |
| D10.1 I-9 Section 2 signed | Symage is GATED. | **Yes.** The I-9 is a public USCIS form; fill and sign or leave blank. |
| D10.4 Timesheet total hours | None. | **Yes.** Render weekly timesheets (printed or handwritten font) with known hours. Answer = the sum. |
| D10.5 Badge expired | None. A real badge would show a face, so identifying a person is a risk. | **Yes, faceless.** Draw badges with a silhouette avatar and expiry date. |
| D8.6 ID present in photo (clean) | cloverx negatives are third-party real photos. | **Yes.** Composite synthetic KTP/passport renders onto desk backgrounds with and without cards. |

---

## 5. Cannot verify

- **Kaggle anujms/car-damage-detection:** the file list is empty in the anonymous API and the download needs login [CARD]. No rows.
- **tech4humans/signature-detection** and **Symage/coherent-forms-1040-cms1500-i9:** README and viewer return 401 (gated "auto"). Content, classes and real licence text are unknown.
- **konfuzio/funsd_plus LICENSE** was not opened. The card asks users to agree to it with personal details, so I treated it as GATED.
- **FUNSD licence:** the owner page has a "License" nav item but no licence text rendered in fetched HTML.
- **MIDV-500 / zimka mirror licence:** no licence found. The paper snippet only covers the source images.
- **MEDIC label origin** and the `terms-of-use.txt` content were not read. The arXiv abstract does not describe the annotation process.
- **CrisisMMD `label_image` values:** the column's presence comes from the Readme; I did not print humanitarian TSV rows.
- **IDNet-2025 meta JSON fields:** inside tar.gz archives of 1.35 GB or more, so not sampled.
- **datasets-server `/statistics` returned HTTP 500** for cloverx-id, HV09 and albertobarnabo. I used sampled or file-based counts instead (marked).
- **tugberkkalay/autodamageiq:** `/splits` returned 500, so no rows (SKIP stands on card evidence).
- **NIST SRD licence terms** for SD2 were not read (the page shows "Price: No charge").
- **Value-reason sources:** the FinCEN, APQC, Coalition, Swiss Re, CMS, IRS, WorldCC and FATF figures come from web-search result summaries citing those pages, not from full-page reads. The I-9 penalty source is secondary (Experian) and conflicting amounts appeared in search snippets, so treat it as [UNVERIFIED primary].
- **Voxel51 passports:** the listing says `samples.json` is 23.38 MB but the fetched file was 10.05 MB (possibly compressed transfer or a different revision). Only 2 full rows were pasted.
- **Training-data overlap** statements are [INFERRED] throughout. No contamination check was run.
