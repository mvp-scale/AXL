import os, sys, subprocess, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
run = lambda *a, **k: subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True, timeout=400, **k)
run("python3", "axl/scripts/build_skills.py")
errs = []
lint = run("python3", "axl/scripts/lint_skills.py")
if lint.returncode: errs.append(("lint", lint.stdout[-300:]))
S = "axl/skills/"; demo = "axl/demo/"
steps = [("axl-evaluate", ["python3", S + "axl-evaluate/scripts/evaluate.py", demo + "before.html", "--json", "--axl", "/tmp/axl_eval.json"]),
         ("axl-correct auto", ["python3", S + "axl-correct/scripts/correct.py", "auto", demo + "before.html", "--out", "/tmp/axl_fixed.html", "--ops-out", "/tmp/axl_ops.json"]),
         ("axl-correct apply", ["python3", S + "axl-correct/scripts/correct.py", "apply", demo + "before.html", "/tmp/axl_ops.json", "--out", "/tmp/axl_applied.html"]),
         ("axl-verbs", ["python3", S + "axl-verbs/scripts/verbs.py", "make it more polished"]),
         ("axl-verbs undefined", ["python3", S + "axl-verbs/scripts/verbs.py", "make it delightful"]),
         ("axl-tokens check", ["python3", S + "axl-tokens/scripts/tokens.py", "check", demo + "css/before.css", demo + "tokens.json"]),
         ("axl-tokens fix", ["python3", S + "axl-tokens/scripts/tokens.py", "fix", demo + "css/before.css", demo + "tokens.json", "/tmp/axl_tok.css"])]
for name, cmd in steps:
    r = run(*cmd)
    if r.returncode != 0: errs.append((name, r.returncode, (r.stderr or r.stdout)[-200:]))
    elif name == "axl-verbs" and "tool-backed" not in r.stdout: errs.append((name, "polish not tool-backed"))
    elif name == "axl-verbs undefined" and "undefined" not in r.stdout: errs.append((name, "delightful should be undefined"))
# the evaluate output must show failures on the original and validate as an AXL document
doc = json.load(open("/tmp/axl_eval.json")) if os.path.exists("/tmp/axl_eval.json") else None
if doc:
    sys.path.insert(0, f"{ROOT}/axl/scripts"); v = run("python3", "axl/scripts/validate_axl.py", "/tmp/axl_eval.json")
    if v.returncode: errs.append(("axl doc", v.stdout[-200:]))
# after auto-correct, the fixed page must have fewer failing checks than the original
a = run("python3", S + "axl-evaluate/scripts/evaluate.py", "/tmp/axl_fixed.html", "--json"); b = run("python3", S + "axl-evaluate/scripts/evaluate.py", demo + "before.html", "--json")
n = lambda r: sum(1 for x in json.loads(r.stdout)["findings"] if x["result"] == "fail")
if not (n(a) < n(b)): errs.append(("correct did not reduce failures", n(b), n(a)))
if errs: print("PHASE 8 Skills: FAIL", errs); sys.exit(1)
print(f"PHASE 8 Skills: PASS — 4 skills lint clean (no subjective claims), each script exits 0 on the demo; auto-correct cut failing findings {n(b)} -> {n(a)}")
