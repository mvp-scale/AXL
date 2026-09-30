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
    if not x["cycles_without_input"]: errs.append((t, "nothing changes in the first 2 s"))
    if not x["preview_visible"]: errs.append((t, "the page preview is not on the first screen"))
    if x["words_above_preview"] > 16: errs.append((t, "too many words before the preview", x["words_above_preview"]))
    a1 = x["after_one_tap"]
    if not (a1["mine"] == 1 and a1["mode"] == "true" and a1["facts"]): errs.append((t, "one tap does not build your word", a1))
    if not x["saved"] or not x["sheet_closed"]: errs.append((t, "save sheet"))
    if x["words"] < 20 or x["chips"] < 45 or not x["switch_ok"]: errs.append((t, "landscape too small", x["words"], x["chips"]))
    if x["overflow"] > 1: errs.append((t, "horizontal overflow", x["overflow"]))
if errs: print("PHASE 7 Site: FAIL", json.dumps(errs)[:1200]); sys.exit(1)
print(f"PHASE 7 Site: PASS — one file; the page changes on its own within 2 s ({out['runs'][-1]['words_above_preview']} words above the preview); one tap starts your word; save gives a checkable definition; {out['runs'][-1]['chips']} tweaks, {out['runs'][-1]['words']} words; no network, no overflow, axe clean at 390/1440 light and dark")
