#!/usr/bin/env python3
"""Verify data/previews.json: every tweak is covered once, visible previews really change the Northstar demo
(tools/runners/preview_check.js), and non-visible ones carry a kind + reason. Exit 1 on any failure."""
import json, os, subprocess, sys, tempfile, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
PV = json.load(open(f"{D}/previews.json")); TW = {t["id"] for t in json.load(open(f"{D}/tweaks.json"))["tweaks"]}
VIEWS = {"overview", "projects", "editor", "settings", "reports", "assistant", "site", "docs", "signin"}
KINDS = {"behaviour", "content", "process", "performance", "agent", "judgment"}
bad = [k for k in PV if k not in TW]
vis = []
for k, v in PV.items():
    if v.get("css") or v.get("patch"):
        if v.get("view") not in VIEWS: bad.append(f"{k}: view {v.get('view')}")
        if v.get("css") and (re.search(r"@import|url\(\s*['\"]?https?:", v["css"]) or len(v["css"]) > 900): bad.append(f"{k}: css")
        vis.append(dict(v, id=k))
    elif v.get("kind") not in KINDS or not v.get("why"): bad.append(f"{k}: kind/why")
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f: json.dump(vis, f)
out = json.loads(subprocess.run(["node", "runners/preview_check.js", f.name], cwd=f"{ROOT}/axl/tools", capture_output=True, text=True, check=True).stdout)
zero = [k for k in (x["id"] for x in vis) if out.get(k, {}).get("changed", 0) < 1]
print(f"previews: {len(PV)} · visible {len(vis)} · measured change {len(vis) - len(zero)} · not visible {len(PV) - len(vis)} · problems {len(bad) + len(zero)}")
for x in (bad + [f"{k}: no measured change" for k in zero])[:30]: print("  ", x)
sys.exit(1 if bad or zero else 0)
