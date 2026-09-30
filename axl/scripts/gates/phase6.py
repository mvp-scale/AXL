import os, sys, json, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
old = open(f"{ROOT}/axl/reports/metrics.json").read()
subprocess.run(["python3", f"{ROOT}/axl/scripts/build_metrics.py"], check=True, capture_output=True)
new = open(f"{ROOT}/axl/reports/metrics.json").read()
M = json.loads(new); C = json.load(open(f"{ROOT}/axl/data/claims.json"))["claims"]
ok = old == new and M["claims_total"] == len(C) and abs(M["guidance_audited"]["system_share"] + M["guidance_audited"]["luck_share"] - 1) < 1e-3
md = open(f"{ROOT}/axl/reports/metrics.md").read()
ok = ok and f"**{M['guidance_audited']['claims']}**" in md
if not ok: print("PHASE 6 Metrics: FAIL"); sys.exit(1)
g = M["guidance_audited"]
print(f"PHASE 6 Metrics: PASS — computed; {g['system_share']*100:.1f}% of {g['claims']} audited guidance has a measurable definition, {g['enforced_share']*100:.1f}% enforced; {M['double_sourced_public']} double-sourced")
