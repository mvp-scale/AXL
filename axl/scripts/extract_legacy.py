#!/usr/bin/env python3
"""Phase 1: extract the legacy catalog. Groups are parsed as JSON (page is not run).
Pure-data JS snippets (elements, effectOverrides, appTemplate, mapAction) are evaluated
in an empty node vm sandbox with no DOM. Deterministic output."""
import json, re, subprocess, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
lines = open(f"{ROOT}/legacy/index.html", encoding="utf-8").read().split("\n")
OUT = f"{ROOT}/axl/data"
os.makedirs(OUT, exist_ok=True)

gl = next(l for l in lines if l.startswith("const groups="))
groups = json.loads(gl[len("const groups="):].rstrip().rstrip(";"))

def find(prefix):
    return next(i for i, l in enumerate(lines) if l.startswith(prefix))
i_el, i_map = find("const elements=["), find("function mapAction")
i_tpl = find("const appTemplate")
i_ov = find("const effectOverrides")
i_end = next(i for i, l in enumerate(lines) if l.startswith("for(const e of elements)")) + 1
js = "\n".join(lines[i_el:i_map + 1] + lines[i_tpl:i_end])
prog = js + "\n;JSON.stringify({elements,appTemplate,mapped:(globalThis.__groups||[]).map(a=>mapAction(a))})"
runner = """const vm=require('vm');const fs=require('fs');
const groups=JSON.parse(fs.readFileSync(0,'utf8'));
const ctx={__groups:groups};vm.createContext(ctx);
process.stdout.write(vm.runInContext(fs.readFileSync(process.argv[2],'utf8'),ctx,{timeout:5000}));"""
tmp = f"{OUT}/.tmp_prog.js"; tmp2 = f"{OUT}/.tmp_run.js"
open(tmp, "w").write(prog); open(tmp2, "w").write(runner)
texts = [a for g in groups for a in g["actions"]]
res = json.loads(subprocess.run(["node", tmp2, tmp], input=json.dumps(texts), capture_output=True, text=True, check=True).stdout)
os.remove(tmp); os.remove(tmp2)

rows, k = [], 0
for g in groups:
    for i, t in enumerate(g["actions"]):
        eff = res["mapped"][k]; k += 1
        t_ = t.rstrip()
        rows.append({
            "id": f"{g['id']}-{i}", "group_id": g["id"], "group_name": g["name"],
            "source": g["source"], "url": g["url"], "group_origin_note": g["origin"],
            "text": t,
            "legacy_effect": eff,
            "truncated": not re.search(r"[.!?)\]\"'”:;`%\w]$", t_) or t_.endswith(",") or bool(re.search(r"\b(and|or|the|a|to|of|with|for|in|by|that|but)$", t_, re.I)),
            "caveat": bool(re.match(r"(?i)^(caveat|note|warning|limitation|unverified|not verified|research)", t_)) or (g["id"] == "g4" and i >= 8),
        })
json.dump({"groups": [{k_: v for k_, v in g.items() if k_ != "actions"} | {"count": len(g["actions"])} for g in groups],
           "prescriptions": rows}, open(f"{OUT}/legacy_groups.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False, sort_keys=True)
json.dump({"appTemplate": res["appTemplate"], "elements": res["elements"]},
          open(f"{OUT}/legacy_effects.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False, sort_keys=True)
print(len(groups), len(rows))
