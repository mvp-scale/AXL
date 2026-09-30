#!/usr/bin/env python3
"""axl-evaluate: run the enforced AXL checks on a local HTML file and print findings.
usage: evaluate.py <file.html> [--width 1440] [--json] [--axl out.json] [--strict]
Exit 0 when the checks ran (findings are reported, not an error); --strict exits 1 when any check fails.
Needs: node, and `npm ci` in axl/tools (Playwright, axe-core). Chromium via CHROME_PATH."""
import json, subprocess, sys, os, pathlib
AXL = pathlib.Path(__file__).resolve().parents[3]; ROOT = AXL.parent; RUN = AXL / "tools" / "runners"
DEFS = {p["id"]: p for d in json.load(open(AXL / "data" / "definitions.json"))["definitions"] for p in d["patterns"]}
def claim(pid): return [DEFS[pid]["claim_id"]]
def node(script, *args):
    r = subprocess.run(["node", str(RUN / script), *args], cwd=ROOT, capture_output=True, text=True, timeout=300)
    try: return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: return {"error": (r.stderr or r.stdout)[-300:], "findings": []}
def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"): print(__doc__); return 2
    f = os.path.abspath(a[0]); width = a[a.index("--width") + 1] if "--width" in a else "1440"
    plan = [("axe.js", [f, width], "rules-engine-clean", None), ("axe.js", [f, width], "readable-contrast", ["color-contrast"]),
            ("craft.js", [f, width, "spacing-4"], "on-grid-spacing", None), ("craft.js", [f, width, "target-44"], "reachable-targets", None),
            ("craft.js", [f, width, "measure-80"], "line-length", None), ("craft.js", [f, width, "body-16"], "text-size-floor", None),
            ("craft.js", [f, width, "leading-1.5"], "running-text-leading", None), ("craft.js", [f, "320", "reflow-320"], "reflow", None),
            ("reducedmotion.js", [f], "reduced-motion", None)]
    cache, out, rules = {}, [], []
    for script, args, pid, only in plan:
        key = (script, tuple(args)); cache.setdefault(key, node(script, *args)); res = cache[key]
        fs = [x for x in res.get("findings", []) if x.get("result") == "fail" and (not only or x["rule_id"] in only)]
        p = DEFS[pid]; rules.append({"id": pid, "tier": p["tier"], "check": p["name"], "pass_criteria": (p["check"] or {}).get("pass_criteria", ""), "tool": (p["check"] or {}).get("tool", ""), "command": f"node axl/tools/runners/{script} " + " ".join(os.path.relpath(x, ROOT) if x == f else x for x in args), "claim_ids": claim(pid)})
        if "error" in res: out.append({"rule_id": pid, "result": "na", "evidence": "tool error: " + res["error"][:120], "location": "", "claim_ids": claim(pid)}); continue
        if not fs: out.append({"rule_id": pid, "result": "pass", "evidence": "no findings", "location": "", "claim_ids": claim(pid)})
        for x in fs[:25]: out.append({"rule_id": pid, "result": "fail", "evidence": x.get("evidence", ""), "location": x.get("location", ""), "claim_ids": claim(pid)})
    bad = [x for x in out if x["result"] == "fail"]
    if "--json" in a: print(json.dumps({"file": os.path.relpath(f, ROOT), "width": width, "findings": out}, indent=1))
    else:
        for pid in dict.fromkeys(x["rule_id"] for x in out):
            rows = [x for x in out if x["rule_id"] == pid]; st = "FAIL" if any(x["result"] == "fail" for x in rows) else rows[0]["result"].upper()
            print(f"{st:5} {pid:22} {DEFS[pid]['name']}  [{', '.join(claim(pid))}]")
            for x in rows[:3]:
                if x["result"] == "fail": print(f"        - {x['location']}: {x['evidence']}")
        print(f"{len(bad)} failing findings across {len({x['rule_id'] for x in bad})} rules")
    if "--axl" in a:
        doc = {"axl": "0.1", "describe": {"name": os.path.basename(f), "surface": "web", "states": ["ready"], "viewports": [f"{width}x900"]},
               "evaluate": {"rules": rules, "findings": [{k: x[k] for k in ("rule_id", "result", "evidence", "location")} for x in out]}}
        json.dump(doc, open(a[a.index("--axl") + 1], "w"), indent=1)
    return 1 if bad and "--strict" in a else 0
sys.exit(main())
