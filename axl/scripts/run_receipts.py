#!/usr/bin/env python3
"""Phase 5: run every command in tools/receipts.json from the repo root and write receipts/runs/<id>.json:
{tool, version, command, input_hash, exit_code, stdout_excerpt, findings, ran_at}. Nothing is simulated."""
import json, os, subprocess, hashlib, datetime, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def versions():
    t = json.load(open(f"{ROOT}/axl/tools/package-lock.json"))["packages"]
    v = lambda n: t[f"node_modules/{n}"]["version"]
    return {"axe-core": "axe-core " + v("axe-core") + " via @axe-core/playwright " + v("@axe-core/playwright"), "lighthouse": "lighthouse " + v("lighthouse"),
            "stylelint": "stylelint " + v("stylelint"), "design.md lint": "@google/design.md " + v("@google/design.md"),
            "wcag-contrast": "axl contrast.js (WCAG 2.x relative luminance)", "playwright emulateMedia": "playwright " + v("playwright"),
            "playwright toHaveScreenshot": "@playwright/test " + v("@playwright/test"),
            "axl craft checks": "axl craft.js on playwright " + v("playwright"), "axl fix.js": "axl fix.js on playwright " + v("playwright") + " + axe-core " + v("axe-core")}
def input_hash(files):
    h = hashlib.sha256()
    for f in sorted(files): h.update(f.encode()); h.update(open(f"{ROOT}/{f}", "rb").read())
    return h.hexdigest() if files else None
def run(cmd):
    r = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, timeout=300)
    return r.returncode, r.stdout
def parse(out):
    for line in reversed(out.strip().splitlines()):
        try: return json.loads(line)
        except Exception: continue
    return None
if __name__ == "__main__":
    only = set(sys.argv[1:]); V = versions(); os.makedirs(f"{ROOT}/axl/receipts/runs", exist_ok=True)
    for s in json.load(open(f"{ROOT}/axl/tools/receipts.json"))["receipts"]:
        if only and s["id"] not in only: continue
        code, out = run(s["command"]); j = parse(out) or {}
        rec = {"id": s["id"], "tool": s["tool"], "version": V[s["tool"]], "command": s["command"], "input_hash": input_hash(s["inputs"]),
               "exit_code": code, "stdout_excerpt": out.strip()[:600], "findings": j.get("findings", []), "role": s["role"],
               "ran_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
        json.dump(rec, open(f"{ROOT}/axl/receipts/runs/{s['id']}.json", "w"), indent=1)
        print(s["id"].ljust(26), "exit", code, "findings", len(rec["findings"]))
