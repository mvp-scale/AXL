#!/usr/bin/env python3
"""axl.py - deterministic checker for a user's verb definition.
  axl.py check <kit.axl.md> <page.html|https://url> [--json] [--quick]     run a kit's rules (element property test) on any page
  axl.py check <verb.json> <page.html> [--width 1440] [--json] [--tweaks P] [--tokens F]   (older verb files)
  axl.py bundle <kit.axl.md> --out <file.check.js>   one file to paste into any page's console (offline)
  axl.py fix <page.html> --out <out.html> [--width 1440]
  axl.py tweaks [--category X] [--tweaks P]
Exit: check 0 all pass, 1 any fail, 2 usage."""
import json, re, subprocess, sys, os, tempfile, argparse, collections
AXL = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(AXL); RUN = os.path.join(AXL, "tools", "runners")
_cache = {}
def run_json(cmd):
    k = tuple(cmd)
    if k not in _cache:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=300)
        try: _cache[k] = json.loads(r.stdout.strip().splitlines()[-1]).get("findings", [])
        except Exception: _cache[k] = [{"rule_id": "runner-error", "result": "fail", "evidence": (r.stderr or r.stdout)[-200:] or "no output", "location": ""}]
    return _cache[k]
HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
SP = re.compile(r"((?:padding|margin|gap|row-gap|column-gap)(?:-(?:top|right|bottom|left))?)\s*:\s*([^;}]+)")
def full(h):
    h = h.lower(); return "#" + "".join(c * 2 for c in h[1:]) if len(h) == 4 else h
def tokens_check(css, tok):
    allowed = set(tok["colors"].values()); unit = tok.get("spacing_unit", 4)
    cols = collections.Counter(full(c) for c in HEX.findall(css)); f = []
    for c, n in sorted(cols.items()):
        if c not in allowed: f.append({"rule_id": "raw-colour", "result": "fail", "evidence": f"{c} is not a token value ({n} uses)", "location": c})
    seen = set()
    for m in SP.finditer(css):
        for v in re.findall(r"(-?\d+(?:\.\d+)?)px", m.group(2)):
            if float(v) != 0 and float(v) / unit != round(float(v) / unit): seen.add((m.group(1), v + "px"))
    f += [{"rule_id": "off-scale-spacing", "result": "fail", "evidence": f"{p}: {v} is not a multiple of {unit}px", "location": f"{p} {v}"} for p, v in sorted(seen)]
    return f
def styles(page):
    return "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", open(page, encoding="utf-8").read(), re.S | re.I))
def evaluate(check, page, width, tokens):
    n = lambda *a: ["node", os.path.join(RUN, a[0])] + list(a[1:])
    if check == "contrast": return [f for f in run_json(n("axe.js", page, width)) if f["rule_id"] == "color-contrast"]
    if check == "axe": return run_json(n("axe.js", page, width))
    if check in ("spacing-4", "target-44", "measure-80", "body-16", "leading-1.5", "duration-500"): return run_json(n("craft.js", page, width, check))
    if check == "reflow-320": return run_json(n("craft.js", page, "320", check))
    if check == "reduced-motion": return run_json(n("reducedmotion.js", page))
    if check in ("focus-visible", "no-gradient", "banned-fonts"):
        with tempfile.NamedTemporaryFile("w", suffix=".css", delete=False) as t: t.write(styles(page))
        try: fs = run_json(n("stylelint.js", t.name))
        finally: os.unlink(t.name)
        key = {"focus-visible": "outline", "no-gradient": "gradient", "banned-fonts": "font-family"}[check]
        return [f for f in fs if key in str(f.get("evidence", ""))]
    if check == "tokens":
        if not tokens: return None
        return tokens_check(styles(page), json.load(open(tokens)))
    raise SystemExit(f"unknown check {check}")
def load_tweaks(p): return json.load(open(p or os.path.join(AXL, "data", "tweaks.json")))["tweaks"]
def cmd_check(a):
    try: verb = json.load(open(a.verb)); defs = {t["id"]: t for t in load_tweaks(a.tweaks)}
    except Exception as e: print(f"error: {e}", file=sys.stderr); return 2
    page = os.path.abspath(a.page); out = []; bad = 0
    for tid in verb.get("tweaks", []):
        t = defs.get(tid)
        if not t: out.append({"tweak": tid, "status": "UNKNOWN", "evidence": ["not in tweaks file"]}); bad += 1; continue
        if not t.get("check"): out.append({"tweak": tid, "status": "JUDGMENT", "evidence": ["judgment — not machine-checked"]}); continue
        fs = evaluate(t["check"], page, str(a.width), a.tokens)
        if fs is None: out.append({"tweak": tid, "check": t["check"], "status": "SKIP", "evidence": ["needs a token file (--tokens)"]}); continue
        fails = [f for f in fs if f.get("result") == "fail"]
        if fails: bad += 1
        out.append({"tweak": tid, "check": t["check"], "status": "FAIL" if fails else "PASS", "evidence": [f"{f.get('location','')}: {f.get('evidence','')}" for f in fails]})
    if a.json: print(json.dumps({"verb": verb.get("name"), "results": out, "failed": bad}))
    else:
        print(f"verb: {verb.get('name')}  page: {a.page}")
        for r in out:
            print(f"{r['status']:8} {r['tweak']} {r.get('check','')}")
            for e in r["evidence"][:5]: print(f"           {e}")
    return 1 if bad else 0
def cmd_fix(a):
    tmp = a.out + ".patch.css"
    r = subprocess.run(["node", os.path.join(RUN, "fix.js"), os.path.abspath(a.page), str(a.width), os.path.abspath(tmp), "spacing-4,target-44,contrast"], cwd=ROOT, capture_output=True, text=True, timeout=300)
    try: res = json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: print("fix runner failed: " + (r.stderr or r.stdout)[-300:], file=sys.stderr); return 2
    css = "\n".join(l for l in open(tmp).read().splitlines() if not l.startswith("/*")); os.remove(tmp)
    h = open(a.page, encoding="utf-8").read(); block = f'<style id="axl-patch">\n{css}\n</style>'
    open(a.out, "w", encoding="utf-8").write(h.replace("</head>", block + "</head>", 1) if "</head>" in h else block + h)
    print(f"findings before: {res['before']}, after: {res['after']}, patch rules: {res['rules']} -> {a.out}")
    return 0 if res["after"] == 0 else 1
def cmd_tokens(a):
    fs = tokens_check(open(a.css).read(), json.load(open(a.tokens)))
    print(json.dumps({"tool": "axl tokens", "findings": fs})); return 1 if fs else 0
def cmd_tweaks(a):
    for t in load_tweaks(a.tweaks):
        if a.category and t.get("category") != a.category: continue
        print(f"{t['id']}\t{t.get('category','')}\t{'yes' if t.get('check') else 'no'}")
    return 0
def kit_rules(path):
    """The rules of a kit: the lines of its ```axl block ("  - <rule>"), or a plain list of rule lines."""
    t = open(path, encoding="utf-8").read(); m = re.search(r"```axl\n(.*?)```", t, re.S); body = m.group(1) if m else t
    name = (re.search(r"^word:\s*(.+)$", body, re.M) or re.search(r"^#\s*(.+)$", t, re.M))
    return (name.group(1).strip() if name else os.path.basename(path)), [l.strip()[2:].strip() for l in body.splitlines() if l.strip().startswith("- ")]

def cmd_kit(a):
    try: return _cmd_kit(a)
    except BrokenPipeError: return 0

def _cmd_kit(a):
    name, rules = kit_rules(a.verb)
    if not rules: print("no rules found (expected an ```axl block with '  - <rule>' lines)"); return 2
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f: json.dump([{"rule": r} for r in rules], f)
    r = subprocess.run(["node", os.path.join(RUN, "rulecheck.js"), f.name, a.page] + (["--quick"] if a.quick else []) + (["--insecure"] if a.insecure else []), cwd=ROOT, capture_output=True, text=True, timeout=600)
    try: res = json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: print("checker error:", (r.stderr or r.stdout)[-400:]); return 2
    n = collections.Counter(x["status"] for x in res)
    if a.json: print(json.dumps({"word": name, "page": a.page, "summary": dict(n), "results": res}, indent=1))
    else:
        print(f"{name} on {a.page}: {n['PASS']} pass · {n['FAIL']} fail · {n['ASK']} to review · {n['UNSUPPORTED']} not checkable yet" + (f" · {n['INVALID']} invalid" if n['INVALID'] else ""))
        for x in sorted(res, key=lambda x: ["FAIL", "INVALID", "PASS", "UNSUPPORTED", "ASK"].index(x["status"])):
            print(f"  {x['status']:11} {x['rule']}\n              {x.get('detail', '')}")
            if x.get("fix"): print(f"              fix: {x['fix']}")
    return 1 if n["FAIL"] or n["INVALID"] else 0

def cmd_bundle(a):
    """One self-contained file (axe-core + the AXL engine + the kit's rules) to paste into any page's console. Works offline."""
    name, rules = kit_rules(a.kit)
    V = json.load(open(os.path.join(AXL, "data", "vocab.json"))); vocab = {e["id"]: [e["name"], e.get("css", "")] for e in V["elements"]}
    axe = open(os.path.join(AXL, "tools", "node_modules", "axe-core", "axe.min.js"), encoding="utf-8").read()
    eng = open(os.path.join(AXL, "tools", "engine", "axl-engine.js"), encoding="utf-8").read()
    head = f"/* AXL check: {name} ({len(rules)} rules). One file, nothing to install, works offline.\n   Use: open any web page, press F12 to open DevTools, go to Console, paste this whole file, press Enter.\n   Includes axe-core (MPL-2.0, https://github.com/dequelabs/axe-core). */\n"
    out = head + axe + f"\n;window.AXL_VOCAB={json.dumps(vocab)};\n" + eng + f"\nAXL.run({json.dumps(name)}, {json.dumps(rules)});\n"
    open(a.out, "w", encoding="utf-8").write(out); print(f"{a.out}: {len(rules)} rules, {len(out)//1024} KB"); return 0

def main():
    p = argparse.ArgumentParser(prog="axl.py"); s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("check"); c.add_argument("verb"); c.add_argument("page"); c.add_argument("--width", default="1440"); c.add_argument("--json", action="store_true"); c.add_argument("--quick", action="store_true", help="skip Lighthouse audits"); c.add_argument("--insecure", action="store_true", help="accept untrusted TLS certificates (proxied networks)"); c.add_argument("--tweaks"); c.add_argument("--tokens")
    f = s.add_parser("fix"); f.add_argument("page"); f.add_argument("--out", required=True); f.add_argument("--width", default="1440")
    bu = s.add_parser("bundle", help="make the one-file console checker for a kit"); bu.add_argument("kit"); bu.add_argument("--out", required=True)
    k = s.add_parser("tokens"); k.add_argument("css"); k.add_argument("tokens")
    t = s.add_parser("tweaks"); t.add_argument("--category"); t.add_argument("--tweaks")
    try: a = p.parse_args()
    except SystemExit as e: return 2 if e.code else 0
    if a.cmd == "check" and a.verb.endswith(".md"): return cmd_kit(a)
    return {"check": cmd_check, "fix": cmd_fix, "tokens": cmd_tokens, "tweaks": cmd_tweaks, "bundle": cmd_bundle}[a.cmd](a)
if __name__ == "__main__": sys.exit(main())
