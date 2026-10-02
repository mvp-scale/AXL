#!/usr/bin/env python3
"""Re-run each receipt's command and compare exit code + findings (canonical JSON) with the stored receipt.
Prints reproduced share and lists unreproducible receipts. Exit 1 if < 90% reproduce."""
import json, glob, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from run_receipts import run, parse, input_hash, ROOT
canon = lambda f: json.dumps(f, sort_keys=True)
ok, bad = 0, []
recs = sorted(glob.glob(f"{ROOT}/axl/receipts/runs/*.json"))
for p in recs:
    r = json.load(open(p)); code, out = run(r["command"]); j = parse(out) or {}
    same = code == r["exit_code"] and canon(j.get("findings", [])) == canon(r["findings"])
    spec = next(s for s in json.load(open(f"{ROOT}/axl/tools/receipts.json"))["receipts"] if s["id"] == r["id"])
    if input_hash(spec["inputs"]) != r["input_hash"]: same = False
    if same: ok += 1
    else: bad.append(r["id"])
share = ok / len(recs) if recs else 0
open(f"{ROOT}/axl/reports/receipts-rerun.md", "w").write(f"# Receipt re-run\n\n- receipts: {len(recs)}\n- reproduced: {ok} ({share:.0%})\n- unreproducible: {', '.join(bad) or 'none'}\n")
print(f"reproduced {ok}/{len(recs)} ({share:.0%}); unreproducible: {bad or 'none'}"); sys.exit(0 if share >= 0.9 else 1)
