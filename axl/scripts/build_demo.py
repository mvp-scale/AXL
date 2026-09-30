#!/usr/bin/env python3
"""Build demo variants from data/legacy_effects.json (Northstar template, read-only source).
before.html = template + <title>-less original; after.html = same + a fix layer (each rule cites a claim/tool)."""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
T = json.load(open(f"{ROOT}/axl/data/legacy_effects.json"))["appTemplate"]
FIX = """/* contrast >= 4.5:1 (WCAG 1.4.3) */
.topbar,.topbar span,#breadcrumb,.eyebrow{color:#4b596c}.activity small,li>small{color:#566579}th{color:#4f5d72}footer,footer span{color:#566579}
/* visible focus (WCAG 2.4.7 / 2.4.13) */
button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid #087d70;outline-offset:2px}
/* target size >= 44px */
button,input,select{min-height:44px}
/* reduced motion */
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
/* no decorative gradient */
.hero{background:transparent}"""
BASE_EDITS = [("button:focus,input:focus,select:focus,textarea:focus{outline:none}", ""), ("background:linear-gradient(120deg,#f4f5f8,#f0f2f7);", "")]
T2 = T
for a, b in BASE_EDITS:
    assert a in T2, a
    T2 = T2.replace(a, b)
after = T2.replace('<style id="recipe-style"></style>', f'<style id="recipe-style">{FIX}</style>').replace("<head>", "<head><title>Northstar</title>", 1)
before = T.replace("<head>", "<head><title>Northstar</title>", 1) if False else T
os.makedirs(f"{ROOT}/axl/demo/css", exist_ok=True)
open(f"{ROOT}/axl/demo/before.html", "w").write(before); open(f"{ROOT}/axl/demo/after.html", "w").write(after)
for n, h in (("before", before), ("after", after)):
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", h, re.S)).replace("}", "}\n")
    open(f"{ROOT}/axl/demo/css/{n}.css", "w").write(css)
E = {e["id"]: e["css"] for e in json.load(open(f"{ROOT}/axl/data/legacy_effects.json"))["elements"]}
motion = E["motion"]; guard = "@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}"
for n, css in (("fixture-motion-unguarded", motion), ("fixture-motion-guarded", motion + guard)):
    open(f"{ROOT}/axl/demo/{n}.html", "w").write(before.replace('<style id="recipe-style"></style>', f'<style id="recipe-style">{css}</style>'))
open(f"{ROOT}/axl/demo/fix.css", "w").write(FIX + "\n")
print("demo built")
