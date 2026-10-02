import json, subprocess, hashlib, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
D = f"{ROOT}/axl/data"
h = lambda: [hashlib.sha256(open(f"{D}/{f}", "rb").read()).hexdigest() for f in ("legacy_groups.json", "legacy_effects.json")]
a = h()
subprocess.run(["python3", f"{ROOT}/axl/scripts/extract_legacy.py"], check=True, capture_output=True)
b = h()
assert a == b, "non-deterministic"
d = json.load(open(f"{D}/legacy_groups.json")); p = d["prescriptions"]
rep = open(f"{ROOT}/axl/reports/legacy-findings.md").read()
exp = {"groups": len(d["groups"]), "prescriptions": len(p), "truncated": sum(x["truncated"] for x in p),
       "caveats": sum(x["caveat"] for x in p), "no effect": sum(x["legacy_effect"] is None for x in p)}
for k, v in exp.items():
    assert re.search(rf"\*\*{k}:\*\* {v}\b", rep), f"report mismatch {k}={v}"
print(f"PHASE 1 Extract: PASS — {exp['groups']} groups, {exp['prescriptions']} prescriptions, deterministic re-run")
