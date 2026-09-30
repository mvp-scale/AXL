#!/usr/bin/env python3
"""Refresh the axl-verbs reference snapshot from data/definitions.json + verbs.json (public data only)."""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
defs = {d["verb"]: d for d in json.load(open(f"{D}/definitions.json"))["definitions"]}
out = []
for v in json.load(open(f"{D}/verbs.json"))["verbs"]:
    d = defs.get(v["verb"])
    out.append({"verb": v["verb"], "resolution": v["resolution"], "plain": d["plain"] if d else None, "stays_subjective": d["stays_subjective"] if d else None,
                "patterns": [{"id": p["id"], "name": p["name"], "claim_id": p["claim_id"], "status": p["status"], "command": (p["check"] or {}).get("command"), "pass_criteria": (p["check"] or {}).get("pass_criteria")} for p in (d["patterns"] if d else [])]})
os.makedirs(f"{ROOT}/axl/skills/axl-verbs/references", exist_ok=True)
json.dump({"verbs": out}, open(f"{ROOT}/axl/skills/axl-verbs/references/verbs.json", "w"), indent=1)
print(len(out), "verbs in the axl-verbs snapshot")
