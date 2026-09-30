#!/usr/bin/env python3
"""Phase 7 gate: build the site, serve it with http.server, run Playwright at 375 and 1440 in both themes."""
import os, sys, json, subprocess, time, socket
from jsonschema import Draft202012Validator
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
subprocess.run(["python3", f"{ROOT}/axl/scripts/build_site.py"], check=True, capture_output=True)
s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
srv = subprocess.Popen(["python3", "-m", "http.server", str(port), "--bind", "127.0.0.1"], cwd=f"{ROOT}/axl/site", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    r = subprocess.run(["node", f"{ROOT}/axl/tools/runners/site_check.js", str(port)], cwd=ROOT, capture_output=True, text=True, timeout=600)
finally:
    srv.terminate()
try: out = json.loads(r.stdout.strip().splitlines()[-1])
except Exception: print("PHASE 7 Site: FAIL — runner error", r.stderr[-400:]); sys.exit(1)
errs = []
for x in out["results"]:
    tag = f"{x['width']}px/{x['scheme']}"
    if x["console_errors"]: errs.append((tag, "console errors", x["console_errors"][:2]))
    if x["external_requests"]: errs.append((tag, "external requests", x["external_requests"][:2]))
    if x["axe_serious_critical"]: errs.append((tag, "axe", x["axe_serious_critical"][:3]))
    if x["horizontal_overflow_px"] > 1: errs.append((tag, "horizontal overflow", x["horizontal_overflow_px"]))
    if "none" in x["focus"]["outline"]: errs.append((tag, "no focus ring", x["focus"]))
if out["claims_without_source"]: errs.append(("claims without a source", out["claims_without_source"]))
if out["drawer_ok"] != out["claims_checked"]: errs.append(("drawer failed", out["drawer_fail"]))
if not out["drawer_keyboard"]: errs.append(("drawer not keyboard operable",))
V = Draft202012Validator(json.load(open(f"{ROOT}/axl/spec/axl.schema.json")))
errs += [("export schema", e.message[:100]) for e in V.iter_errors(out["export_doc"])]
ids = {c["id"] for c in json.load(open(f"{ROOT}/axl/data/claims.json"))["claims"]}
errs += [("export cites unknown claim", c) for c in [o["claim_id"] for o in out["export_doc"]["correct"]["ops"]] if c not in ids]
if errs: print("PHASE 7 Site: FAIL", json.dumps(errs)[:900]); sys.exit(1)
print(f"PHASE 7 Site: PASS — 4 viewport/theme runs clean (0 console errors, 0 serious/critical axe, no external requests); {out['drawer_ok']}/{out['claims_checked']} claims open a Sources drawer; export validates against the AXL schema")
