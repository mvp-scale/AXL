import os, sys, json, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
r = subprocess.run(["python3", f"{ROOT}/axl/scripts/rerun_receipts.py"], capture_output=True, text=True)
sys.path.insert(0, f"{ROOT}/axl/scripts"); import validate_claims
claims, errs = validate_claims.check()
enf = [c for c in claims if c["tier"] == "enforced"]
if r.returncode or errs or not enf: print("PHASE 5 Tools: FAIL", r.stdout, errs[:5]); sys.exit(1)
print(f"PHASE 5 Tools: PASS — {r.stdout.strip().splitlines()[-1]}; {len(enf)} claims enforced ({sum(1 for c in enf if c.get('discriminates'))} discriminate before/after)")
