import os, sys, json, subprocess, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, f"{ROOT}/axl/scripts")
subprocess.run(["python3", f"{ROOT}/axl/scripts/refetch_sources.py"], check=True, capture_output=True)
import validate_claims
claims, errs = validate_claims.check()
priv = [c for c in claims if c["origin"] == "private-kit"]
ex = open(f"{ROOT}/axl/reports/excluded.md").read()
if f"**claims:** {len(priv)}" not in ex: errs.append(("excluded.md count mismatch", len(priv)))
if errs: print("PHASE 3 Claims: FAIL", errs[:10]); sys.exit(1)
st = collections.Counter(c["status"] for c in claims); tr = collections.Counter(c["tier"] for c in claims)
print(f"PHASE 3 Claims: PASS — {len(claims)} claims; status {dict(st)}; tier {dict(tr)}; {sum(1 for c in claims if c['quote_verified'])} quotes verified verbatim")
