#!/usr/bin/env python3
"""Validate data/claims.json: schema, quotes verbatim in receipts/sources, >=2 roots for verified,
delta for measurable, command for enforced, independence recomputed from lineage."""
import json, os, sys
from jsonschema import Draft202012Validator
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"; TXT = f"{ROOT}/axl/receipts/sources"
def check():
    claims = json.load(open(f"{D}/claims.json"))["claims"]
    v = Draft202012Validator(json.load(open(f"{ROOT}/axl/spec/claim.schema.json")))
    S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}
    LIN = json.load(open(f"{D}/lineage.json"))["roots"]
    errs, seen = [], set()
    def txt(i):
        p = f"{TXT}/{i}.txt"
        return open(p, encoding="utf-8").read() if os.path.exists(p) else None
    for c in claims:
        for e in v.iter_errors(c): errs.append((c["id"], "schema", e.message[:120]))
        if c["id"] in seen: errs.append((c["id"], "duplicate id"))
        seen.add(c["id"])
        if c["origin"] == "public" and c["source_id"] not in S: errs.append((c["id"], "unknown source", c["source_id"]))
        if c["quote_verified"]:
            t = txt(c["source_id"])
            if t is None or not c["quote"] or c["quote"] not in t: errs.append((c["id"], "quote not verbatim in saved source"))
            if c["quote"] and len(c["quote"].split()) > 40: errs.append((c["id"], "quote > 40 words"))
        elif c["status"] in ("verified", "single-source"): errs.append((c["id"], "status without verified quote"))
        for s in c.get("supports", []):
            t = txt(s["source_id"])
            if t is None or s["quote"] not in t: errs.append((c["id"], "support quote not verbatim", s["source_id"]))
        if c["status"] == "verified":
            if len(set(c["independent_roots"])) < 2: errs.append((c["id"], "verified with < 2 roots"))
        if c["quote_verified"]:
            roots = set(LIN[c["source_id"]].split("+")) if "+" in LIN[c["source_id"]] else {LIN[c["source_id"]]}
            for s in c.get("supports", []):
                if "+" not in LIN[s["source_id"]]: roots.add(LIN[s["source_id"]])
            if sorted(roots) != sorted(c["independent_roots"]): errs.append((c["id"], "independent_roots stale"))
        if c["tier"] == "measurable" and not c["delta"]: errs.append((c["id"], "measurable without delta"))
        if c["tier"] == "enforced" and not (c["enforcement"] and c["enforcement"].get("command")): errs.append((c["id"], "enforced without command"))
        if c["tier"] == "subjective" and c["delta"]: errs.append((c["id"], "subjective with delta"))
    return claims, errs
if __name__ == "__main__":
    claims, errs = check()
    for e in errs[:30]: print(e)
    print(f"{len(claims)} claims, {len(errs)} errors"); sys.exit(1 if errs else 0)
