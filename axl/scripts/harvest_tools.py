#!/usr/bin/env python3
"""Deterministic harvest of machine-readable rule sets: axe-core rules, Lighthouse audits (installed packages), WCAG 2.2 success criteria (saved text)."""
import json, os, re, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = f"{ROOT}/axl"; H = f"{A}/data/harvest"; os.makedirs(H, exist_ok=True)
axe = json.loads(subprocess.run(["node", "-e", "const a=require('axe-core');console.log(JSON.stringify({v:a.version,r:a.getRules()}))"], cwd=f"{A}/tools", capture_output=True, text=True, check=True).stdout)
CAT = {"cat.color": "Color", "cat.forms": "Interaction & states", "cat.keyboard": "Access", "cat.text-alternatives": "Access", "cat.aria": "Access", "cat.name-role-value": "Access",
       "cat.structure": "Access", "cat.semantics": "Access", "cat.tables": "Access", "cat.language": "Content & process", "cat.parsing": "Access", "cat.time-and-media": "Motion", "cat.sensory-and-visual-cues": "Access"}
def wcag_refs(tags): return sorted({".".join(t[4:]) if len(t[4:]) == 3 else f"{t[4]}.{t[5]}.{t[6:]}" for t in tags if re.fullmatch(r"wcag\d{3,4}", t)})
items = [{"id": f"axe:{r['ruleId']}", "text": r["help"], "detail": r["description"], "url": r["helpUrl"].split("?")[0], "category": next((CAT[t] for t in r["tags"] if t in CAT), "Access"),
          "check": f"axe:{r['ruleId']}", "wcag": wcag_refs(r["tags"]), "best_practice": "best-practice" in r["tags"], "measurable": True} for r in axe["r"]]
json.dump({"source": "axe-core", "publisher": "Deque", "kind": "tool", "version": axe["v"], "items": items}, open(f"{H}/axe-core.json", "w"), indent=1)
# Lighthouse: titles live in each audit module's UIStrings
js = r"""
const fs=require('fs'),path=require('path');const base=path.dirname(require.resolve('lighthouse/package.json'))+'/core/audits';const out=[];
function walk(d){for(const f of fs.readdirSync(d)){const p=path.join(d,f);if(fs.statSync(p).isDirectory())walk(p);else if(f.endsWith('.js')){const s=fs.readFileSync(p,'utf8');const t=s.match(/title:\s*'((?:[^'\\]|\\.)*)'/);const id=s.match(/id:\s*'([a-z0-9-]+)'/);const g=path.relative(base,d)||'general';if(t&&id)out.push({id:id[1],title:t[1].replace(/\\'/g,"'"),group:g});}}}
walk(base);console.log(JSON.stringify(out));"""
lh = json.loads(subprocess.run(["node", "-e", js], cwd=f"{A}/tools", capture_output=True, text=True, check=True).stdout)
GRP = {"accessibility": "Access", "seo": "Content & process", "dobetterweb": "Performance", "byte-efficiency": "Performance", "metrics": "Performance", "general": "Performance", "manual": "Access", "agentic": "Agent workflow", "insights": "Performance"}
lhv = json.load(open(f"{A}/tools/node_modules/lighthouse/package.json"))["version"]
json.dump({"source": "Lighthouse", "publisher": "Google Chrome", "kind": "tool", "version": lhv, "items": [{"id": f"lh:{x['id']}", "text": x["title"], "group": x["group"], "category": GRP.get(x["group"].split("/")[0], "Performance"), "check": f"lighthouse:{x['id']}", "measurable": True} for x in lh]},
          open(f"{H}/lighthouse.json", "w"), indent=1)
# WCAG 2.2 success criteria from the saved recommendation text
t = open(f"{A}/receipts/sources/src_w3-org-tr-wcag22.txt", encoding="utf-8").read(); n = " ".join(t.split())
sc = {}
for m in re.finditer(r"Success Criterion (\d\.\d{1,2}\.\d{1,2}) (.{2,80}?) Understanding .{2,80}? \| How to Meet .{2,80}? \(Level (A{1,3})\) (.{10,1400}?)(?= Success Criterion \d| Guideline \d| Principle \d| Note 1| Note:|$)", n):
    num, name, lvl, body = m.groups()
    if num in sc: continue
    first = re.split(r"(?<=[.:])\s", body.strip())[0][:320]
    sc[num] = {"id": f"wcag:{num}", "text": f"{name}: {first}", "name": name.strip(), "level": lvl, "url": "https://www.w3.org/TR/WCAG22/#" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"), "measurable": True}
items = [dict(v, category="Access") for k, v in sorted(sc.items(), key=lambda kv: [int(x) for x in kv[0].split(".")])]
json.dump({"source": "W3C WCAG 2.2", "publisher": "W3C", "kind": "standard", "items": items}, open(f"{H}/wcag22.json", "w"), indent=1)
print(f"axe {len(axe['r'])} · lighthouse {len(lh)} · wcag SC {len(items)}")
