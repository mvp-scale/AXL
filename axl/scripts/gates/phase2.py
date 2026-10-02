import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
S = json.load(open(f"{ROOT}/axl/data/sources.json"))["sources"]; by = {s["id"]: s for s in S}
errs = []
for s in S:
    if not s["fetch_status"] or s["fetch_status"] == "pending": errs.append(("no fetch result", s["id"]))
    if s["fetch_status"] == "ok" and not os.path.exists(f"{ROOT}/axl/receipts/sources/{s['id']}.txt"): errs.append(("no saved text", s["id"]))
    if s["fetch_status"] == "ok" and not (s["content_hash"] and s["retrieved_at"]): errs.append(("no hash", s["id"]))
    if s["kind"] == "derivative" and not s["derives_from"] and "lineage unknown" not in s.get("lineage_note", ""): errs.append(("derivative w/o root", s["id"]))
    for p in s["derives_from"]:
        if p not in by: errs.append(("bad parent", s["id"]))
rec = open(f"{ROOT}/axl/reports/recon.md").read()
if "Dead links" not in rec: errs.append(("recon.md lacks dead links", ""))
new = [s for s in S if s["found_in"] == ["recon"] and s["fetch_status"] == "ok" and s["kind"] == "primary"]
if len(new) < 15: errs.append(("fewer than 15 new primaries", len(new)))
if errs: print("PHASE 2 Recon: FAIL", errs); sys.exit(1)
print(f"PHASE 2 Recon: PASS — {len(S)} sources, {sum(s['fetch_status']=='ok' for s in S)} fetched ok, {len(new)} new primaries, lineage complete")
