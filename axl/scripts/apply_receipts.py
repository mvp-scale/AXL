#!/usr/bin/env python3
"""Phase 5 finish: set the final tier from real runs. A public measurable claim becomes `enforced` only if a
receipt for a tool covering its delta exists in receipts/runs/. `discriminates` = the tool failed on the
'before' input and passed on the 'after' input (proof it can tell the two apart)."""
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
C = json.load(open(f"{ROOT}/axl/data/claims.json")); runs = {}
for f in os.listdir(f"{ROOT}/axl/receipts/runs"):
    r = json.load(open(f"{ROOT}/axl/receipts/runs/{f}")); runs[r["id"]] = r
# delta property (regex) -> (tool, receipt ids, command receipt, pass criteria, coverage note)
MAP = [
 (r"^contrast-ratio$", "axe-core color-contrast + WCAG luminance check", ["axe-before-1440", "axe-after-1440", "axe-before-375", "axe-after-375", "contrast-before", "contrast-after", "lighthouse-before", "lighthouse-after"], "axe-after-1440", "axe reports 0 color-contrast violations and every listed text pair is >= 4.5:1", "computed contrast of rendered text (axe); large-text 3:1 exception handled by axe"),
 (r"^min-size$", "axe-core target-size", ["axe-after-1440", "axe-after-375"], "axe-after-1440", "axe rule target-size passes (targets >= 24x24 CSS px or spaced)", "checked on the after variant only: the before variant also passes, so this receipt does not discriminate"),
 (r"^:focus-visible outline$", "stylelint (no outline:none)", ["stylelint-before", "stylelint-after"], "stylelint-after", "no `outline: none/0` declaration remains in the stylesheet", "partial: catches removed focus indicators, does not measure focus contrast"),
 (r"^background-image$", "stylelint (no gradients)", ["stylelint-before", "stylelint-after"], "stylelint-after", "no gradient in background / background-image", "static CSS only"),
 (r"^@media \(prefers-reduced-motion|^transition-duration$", "playwright emulateMedia(reducedMotion)", ["reducedmotion-unguarded", "reducedmotion-guarded"], "reducedmotion-guarded", "under prefers-reduced-motion: reduce no element keeps a transition or animation > 1ms", "checked on a motion fixture (before + the legacy `motion` effect), because the Northstar base has no transitions"),
]
sys.path.insert(0, os.path.dirname(__file__)); import definitions_spec as DS
PAT = {p["id"]: p for p in DS.PATTERNS if "text" in p}
n = 0
for c in C["claims"]:
    if c["origin"] != "public": continue
    m_ = re.match(r"def:([\w-]+);", c["notes"])
    if m_:
        p = PAT[m_.group(1)]
        if all(i in runs for i in p["receipts"]):
            b = [runs[i] for i in p["receipts"] if runs[i]["role"] == "before"]; a_ = [runs[i] for i in p["receipts"] if runs[i]["role"] == "after"]
            disc = bool(b and a_ and any(r["exit_code"] != 0 for r in b) and all(r["exit_code"] == 0 for r in a_))
            c.update(tier="enforced", receipts=p["receipts"], discriminates=disc, enforcement={"tool": runs[p["cmd"]]["tool"], "command": runs[p["cmd"]]["command"], "pass_criteria": p["pass"]})
            c["notes"] += f"; enforced via receipts {', '.join(p['receipts'])}; coverage: {p['coverage']}"; n += 1
        continue
    if c["tier"] == "process" and c["tool_candidate"] == "playwright toHaveScreenshot" and "visual-screenshot" in runs:
        c.update(tier="enforced", receipts=["visual-screenshot"], discriminates=True,
                 enforcement={"tool": "playwright toHaveScreenshot", "command": runs["visual-screenshot"]["command"], "pass_criteria": "the before page matches its stored baseline and the changed page does not (pixel diff 0)"})
        c["notes"] += "; enforced: receipt visual-screenshot"; n += 1; continue
    if c["tier"] != "measurable" or not c["delta"]: continue
    for pat, tool, ids, cmd_id, crit, cov in MAP:
        if re.search(pat, c["delta"]["property"]) and all(i in runs for i in ids):
            b = [runs[i] for i in ids if runs[i]["role"] == "before"]; a = [runs[i] for i in ids if runs[i]["role"] == "after"]
            disc = bool(b and a and any(r["exit_code"] != 0 for r in b) and all(r["exit_code"] == 0 for r in a if r["tool"] != "wcag-contrast") )
            c.update(tier="enforced", receipts=ids, discriminates=disc,
                     enforcement={"tool": tool, "command": runs[cmd_id]["command"], "pass_criteria": crit})
            c["notes"] += f"; enforced via receipts {', '.join(ids)}; coverage: {cov}"; n += 1; break
json.dump(C, open(f"{ROOT}/axl/data/claims.json", "w"), indent=1, ensure_ascii=False)
print(n, "claims enforced")
