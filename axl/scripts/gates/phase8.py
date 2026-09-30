import os, sys, subprocess, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
run = lambda *a: subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True, timeout=600)
CLI = "axl/axl.py"; FX = "axl/tools/fixtures/"; demo = "axl/demo/"
common = ["--tweaks", FX + "tweaks.sample.json"]; errs = []
r = run("python3", CLI, "check", FX + "verb.pass3.axl.json", demo + "before.html", *common)
if r.returncode != 1 or "FAIL" not in r.stdout: errs.append(("check before", r.returncode, (r.stdout + r.stderr)[-200:]))
r = run("python3", CLI, "check", FX + "verb.pass3.axl.json", demo + "polished.html", *common)
if r.returncode != 0: errs.append(("check polished", r.returncode, (r.stdout + r.stderr)[-300:]))
out = os.path.join(tempfile.gettempdir(), "axl_fixed.html")
if os.path.exists(out): os.remove(out)
r = run("python3", CLI, "fix", demo + "before.html", "--out", out)
if not os.path.exists(out): errs.append(("fix", r.returncode, (r.stdout + r.stderr)[-200:]))
r = run("python3", CLI, "tweaks", *common)
if r.returncode or not r.stdout.strip(): errs.append(("tweaks", r.stdout[-100:]))
if errs: print("PHASE 8 Tool: FAIL", errs); sys.exit(1)
print("PHASE 8 Tool: PASS — check fails on before, passes on polished, fix writes a page, tweaks lists")
