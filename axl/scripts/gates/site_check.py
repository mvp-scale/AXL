#!/usr/bin/env python3
"""Phase 7 gate: build the single-file story page, then test it at 375 and 1440 px in both themes (+ reduced motion)."""
import os, sys, json, subprocess, socket, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
subprocess.run(["python3", f"{ROOT}/axl/scripts/build_story.py"], check=True, capture_output=True)
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
    if x["console_errors"]: errs.append((t, "console", x["console_errors"][:2]))
    if x["external"]: errs.append((t, "external requests", x["external"][:2]))
    if not x["split_by_1200ms"]: errs.append((t, "nothing moves in the first 1.2 s"))
    if x["first_screen_words"] > 14: errs.append((t, "too many words on the first screen", x["first_screen_words"]))
    if not x["control_in_first_screen"]: errs.append((t, "main control is below the fold"))
    if not x["meaning_quote"]: errs.append((t, "meaning does not open its source"))
    if x["counter"] != "0" or x["pins_on"] != 5: errs.append((t, "stage did not finish", x["counter"], x["pins_on"]))
    for l in x["lens"]:
        if not (l["cmd"] and l["src"] and l["imgs"] and l["big"]): errs.append((t, "lens incomplete", l))
    if not x["lens_closed"]: errs.append((t, "Escape did not close the lens"))
    if x["tiles"] != 34 or x["lit"] != "7" or x["tile_bad"]: errs.append((t, "wall", x["tiles"], x["lit"], x["tile_bad"]))
    if x["echo_dots"] < 20 or not x["echo_info"]: errs.append((t, "echo map"))
    if not x["command_shown"]: errs.append((t, "no command shown"))
    if x["overflow"] > 1: errs.append((t, "horizontal overflow", x["overflow"]))
    if x["axe"]: errs.append((t, "axe", x["axe"][:3]))
rd = out["reduced"]
if not (rd["split"] and rd["counter"] == "0" and rd["pins"] == 5): errs.append(("reduced motion end state", rd))
if errs: print("PHASE 7 Site: FAIL", json.dumps(errs)[:1200]); sys.exit(1)
w = out["runs"][-1]["first_screen_words"]
print(f"PHASE 7 Site: PASS — one file; {w} words on the first screen, word splits inside 1.2 s; stage ends at 0 problems with 5 pins, each opens a close-up, command and source; 34 tiles answer; no external requests; axe clean at 375/1440 in both themes")
