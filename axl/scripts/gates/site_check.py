#!/usr/bin/env python3
"""Phase 7 gate: build the single-file Verb Studio page, then test it at 390 and 1440 px in both themes."""
import os, sys, json, subprocess, socket, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
subprocess.run(["python3", f"{ROOT}/axl/scripts/build_atlas.py"], check=True, capture_output=True)
errs = []
if os.listdir(f"{ROOT}/axl/site") != ["index.html"]: errs.append(("site is not a single file", os.listdir(f"{ROOT}/axl/site")))
s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
srv = subprocess.Popen(["python3", "-m", "http.server", str(port), "--bind", "127.0.0.1"], cwd=f"{ROOT}/axl/site", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
try: r = subprocess.run(["node", f"{ROOT}/axl/tools/runners/site_check.js", f"http://127.0.0.1:{port}/index.html"], cwd=ROOT, capture_output=True, text=True, timeout=600)
finally: srv.terminate()
try: out = json.loads(r.stdout.strip().splitlines()[-1])
except Exception: print("PHASE 7 Site: FAIL — runner error", (r.stderr or r.stdout)[-500:]); sys.exit(1)
for x in out["runs"]:
    t = f"{x['width']}px/{x['scheme']}"
    for k, msg in (("console_errors", "console"), ("external", "external requests"), ("axe", "axe")):
        if x[k]: errs.append((t, msg, x[k][:3]))
    if not x["walks_without_input"]: errs.append((t, "nothing changes in the first 3 s"))
    if not x.get("why_shown") or not x.get("why_closes"): errs.append((t, "why-AXL modal missing or doesn't close with Esc"))
    if not x["preview_visible"]: errs.append((t, "the demo is not on the first screen"))
    if x["words_above_preview"] > 24: errs.append((t, "too many words above the demo", x["words_above_preview"]))
    if not (x["peek"] and x["unpeek"]): errs.append((t, "hold Shift does not show the original"))
    if x.get("pinned_views") not in (None, ["signin"]): errs.append((t, f"playing does not stay on the page the person picked: {x['pinned_views']}"))
    if x["word_tiles"] < 20 or x["source_tiles"] < 20: errs.append((t, "pickers too small", x["word_tiles"], x["source_tiles"]))
    if x["multi_words"] != "2 commands": errs.append((t, "multi-select words", x["multi_words"]))
    if not x["word_walk"].startswith("\u201c"): errs.append((t, "walking words", x["word_walk"]))
    a1 = x["after_one_tap"]
    if not (a1["mine"] == 1 and a1["state"].startswith("Your")): errs.append((t, "one tap does not build your word", a1))
    if not x["saved"] or not x["sheet_closed"] or x.get("script_parses") is not True: errs.append((t, "save outputs", x.get("script_parses")))
    if x["chips"] < 45: errs.append((t, "board too small", x["chips"]))
    if x["overflow"] > 1: errs.append((t, "horizontal overflow", x["overflow"]))
if errs: print("PHASE 7 Site: FAIL", json.dumps(errs)[:1200]); sys.exit(1)
r = out["runs"][-1]
print(f"PHASE 7 Site: PASS — one file; plays on its own inside 3 s ({r['lit_during_walk']} rule rows lit); commands and sources pickers ({r['word_tiles']} x {r['source_tiles']}) multi-select and walk; hold Shift shows the original; tap a rule to see its sources, add it to yours; save gives one kit with a definition block; no network, no overflow, axe clean at 390/1440 light and dark")
