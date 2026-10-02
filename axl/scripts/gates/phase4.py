import os, sys, json, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
D = f"{ROOT}/axl/data"
V = json.load(open(f"{D}/verbs.json"))["verbs"]; C = {c["id"]: c for c in json.load(open(f"{D}/claims.json"))["claims"]}
REQ = "polish distill delight bolder quieter animate colorize clarify harden adapt optimize typeset layout onboard critique audit extract shape".split()
errs = [("missing required verb", v) for v in REQ if v not in {x["verb"] for x in V}]
for x in V:
    if x["resolution"] not in ("measurable", "tool-backed", "undefined"): errs.append(("bad resolution", x["verb"]))
    for d in x["shared_deltas"]:
        c = C.get(d["claim_id"])
        if not c or c["tier"] not in ("measurable", "enforced") or not c["delta"] or c["delta"]["property"] != d["property"]: errs.append(("delta not backed by claim", x["verb"], d["claim_id"]))
    if x["resolution"] == "measurable" and not x["shared_deltas"]: errs.append(("measurable w/o deltas", x["verb"]))
    if x["resolution"] == "tool-backed" and not x["enforced_claim_ids"]: errs.append(("tool-backed w/o tool", x["verb"]))
    for d in x["definitions"]:
        p = f"{ROOT}/axl/receipts/sources/{d['source_id']}.txt"
        if not os.path.exists(p) or d["quote"] not in open(p, encoding="utf-8").read(): errs.append(("definition not verbatim", x["verb"], d["source_id"]))
        if len(d["quote"].split()) > 40: errs.append(("definition > 40 words", x["verb"]))
    for cid in x["linked_claim_ids"]:
        if cid not in C: errs.append(("bad claim id", cid))
if errs: print("PHASE 4 Verbs: FAIL", errs[:10]); sys.exit(1)
import collections
r = collections.Counter(x["resolution"] for x in V)
print(f"PHASE 4 Verbs: PASS — {len(V)} verbs; {dict(r)}; all deltas cite measurable claims")
