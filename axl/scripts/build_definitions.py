#!/usr/bin/env python3
"""Write data/definitions.json: per verb, the curated patterns with their claim, verbatim basis quotes, check command and receipt evidence."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import definitions_spec as DS
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
C = json.load(open(f"{D}/claims.json"))["claims"]; S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}
runs = {f[:-5]: json.load(open(f"{ROOT}/axl/receipts/runs/{f}")) for f in os.listdir(f"{ROOT}/axl/receipts/runs")}
def claim_for(p):
    if "reuse" in p: return next(c for c in C if c["origin"] == "public" and c["text"].startswith(p["reuse"]))
    return next(c for c in C if c["notes"].startswith(f"def:{p['id']};"))
pats = {}
for p in DS.PATTERNS:
    c = claim_for(p)
    rc = [{"id": i, "role": runs[i]["role"], "exit_code": runs[i]["exit_code"], "findings": len(runs[i]["findings"]), "tool": runs[i]["tool"], "version": runs[i]["version"]} for i in p.get("receipts", c.get("receipts", [])) if i in runs]
    basis = [{"source_id": c["source_id"], "url": c["source_url"], "quote": c["quote"], "supports": None}] + [{"source_id": s["source_id"], "url": S[s["source_id"]]["url"], "quote": s["quote"], "supports": None} for s in c.get("supports", [])]
    whats = [w for _, _, w in p.get("basis", [])]
    for b, w in zip(basis, whats): b["supports"] = w
    pats[p["id"]] = {"id": p["id"], "name": p["name"], "plain": p["plain"], "claim_id": c["id"], "tier": c["tier"], "status": c["status"], "independent_roots": c["independent_roots"],
        "delta": c["delta"], "basis": basis, "check": c["enforcement"], "receipts": rc, "discriminates": c.get("discriminates"),
        "parameter_origin": p.get("param"), "coverage": p.get("coverage"), "disagreement": p.get("disagreement"), "example": p.get("example")}
out = []
for v, meta in DS.VERBS.items():
    out.append({"verb": v, "plain": meta["plain"], "stays_subjective": meta["stays_subjective"], "patterns": [pats[p["id"]] for p in DS.PATTERNS if v in p["verbs"]]})
json.dump({"definitions": out, "note": "AXL definitions: claim text and thresholds are written by AXL; each pattern cites verbatim source quotes and a re-runnable receipt."}, open(f"{D}/definitions.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "verbs,", sum(len(x["patterns"]) for x in out), "pattern links")
