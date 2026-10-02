#!/usr/bin/env python3
"""Gate: the kit checker works end to end.
1. `axl.py check demo/kit/polish.axl.md` fails the original Northstar page on the rules it breaks (exit 1, fixes named);
2. the same rules pass once exactly those fixes are applied (demo/kit/before-fixed.html);
3. the one-file checker (engine + axe-core + rules, pasted into a page with the network off) gives the same verdicts as the command line."""
import json, os, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
A = f"{ROOT}/axl"; KIT = f"{A}/demo/kit/polish.axl.md"
def cli(page):
    r = subprocess.run(["python3", f"{A}/axl.py", "check", KIT, page, "--json", "--quick"], capture_output=True, text=True, timeout=300)
    return r.returncode, {x["rule"]: x for x in json.loads(r.stdout)["results"]}
MUST_FAIL = ["text:body font-size >= 16px", "text:body line-height >= 1.5", "aria:heading line-height <= 1.2", "text:* wcag:1.4.3 pass", "state:focus-visible outline-style !contains none"]
errs = []
code, before = cli(f"{A}/demo/before.html")
if code != 1: errs.append(f"original page: exit {code}, expected 1")
for r in MUST_FAIL:
    if before.get(r, {}).get("status") != "FAIL" or not before[r].get("fix"): errs.append(f"original page: {r} should FAIL with a fix, got {before.get(r, {}).get('status')}")
_, after = cli(f"{A}/demo/kit/before-fixed.html")
for r in MUST_FAIL:
    if after.get(r, {}).get("status") != "PASS": errs.append(f"fixed page: {r} should PASS, got {after.get(r, {}).get('status')}")
# the one-file checker, offline, must agree with the command line on every rule a page can check about itself
js = f"""
const {{chromium}}=require('playwright');const fs=require('fs');
(async()=>{{const b=await chromium.launch({{executablePath:require('./runners/common').CHROME}});const ctx=await b.newContext({{viewport:{{width:1440,height:900}},offline:true}});const p=await ctx.newPage();
await p.goto('file://{A}/demo/before.html');
const V=JSON.parse(fs.readFileSync('../data/vocab.json','utf8'));const vocab=Object.fromEntries(V.elements.map(e=>[e.id,[e.name,e.css||'']]));
const rules=fs.readFileSync('{KIT}','utf8').match(/```axl\\n([\\s\\S]*?)```/)[1].split('\\n').filter(l=>l.trim().startsWith('- ')).map(l=>l.trim().slice(2));
const file=fs.readFileSync(require.resolve('axe-core/axe.min.js'),'utf8')+'\\n;window.AXL_VOCAB='+JSON.stringify(vocab)+';\\n'+fs.readFileSync('engine/axl-engine.js','utf8')+'\\nwindow.__r=AXL.check('+JSON.stringify(rules)+');';
await p.evaluate(file);console.log(JSON.stringify(await p.evaluate(()=>window.__r)));await b.close()}})();"""
r = subprocess.run(["node", "-e", js], cwd=f"{A}/tools", capture_output=True, text=True, timeout=300)
try: one = {x["rule"]: x for x in json.loads(r.stdout.strip().splitlines()[-1])}
except Exception: one = {}; errs.append("one-file checker did not run: " + (r.stderr or r.stdout)[-300:])
for rule, x in before.items():
    if "lighthouse:" in rule or "@media:" in rule: continue
    if one.get(rule, {}).get("status") != x["status"]: errs.append(f"one-file vs CLI differ on {rule}: {one.get(rule, {}).get('status')} vs {x['status']}")
if errs: print("KIT CHECK: FAIL"); [print("  -", e) for e in errs]; sys.exit(1)
print(f"KIT CHECK: PASS — original page fails {len(MUST_FAIL)} rules with fixes named; all {len(MUST_FAIL)} pass after the fixes; the offline one-file checker agrees with the command line on {sum(1 for k in before if 'lighthouse:' not in k and '@media:' not in k)} rules")
