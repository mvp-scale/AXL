#!/usr/bin/env python3
"""axl-verbs: turn a vague request ("make it more polished") into concrete checks, or say the word is undefined.
usage: verbs.py "<request>" [--json]   |   verbs.py --list
Reads references/verbs.json (a snapshot of axl/data/definitions.json + verbs.json, refreshed by axl/scripts/build_skills.py)."""
import json, re, sys, pathlib
REF = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "references" / "verbs.json"))
V = {v["verb"]: v for v in REF["verbs"]}
STEM = lambda w: re.sub(r"(ing|ed|er|es|s|d|r|ful|ly|ness|ment)$", "", w) if len(w) > 4 else w
def find(text):
    words = re.findall(r"[a-z]+", text.lower()); known = {}
    for v in V: known[v] = v; known[STEM(v)] = v; known[v + "er"] = v; known[v + "ed"] = v; known[v + "ing"] = v
    known.update({"bold": "bolder", "quiet": "quieter", "colour": "colorize", "color": "colorize", "type": "typeset", "typography": "typeset", "responsive": "adapt", "mobile": "adapt", "accessible": "audit", "accessibility": "audit"})
    for w in words:
        if w in known and known[w] in V: return known[w]
        if STEM(w) in known and known[STEM(w)] in V: return known[STEM(w)]
    return None
def main():
    a = sys.argv[1:]
    if a == ["--list"]: print("\n".join(f"{v['verb']:14} {v['resolution']}" for v in REF["verbs"])); return 0
    if not a: print(__doc__); return 2
    v = find(a[0])
    if not v: res = {"request": a[0], "verb": None, "resolution": "unknown", "message": "No design word from the dictionary found. Ask for a concrete target (a property and a value) instead."}
    else:
        r = V[v]
        if r["resolution"] == "undefined": res = {"request": a[0], "verb": v, "resolution": "undefined", "message": f"'{v}' has no measurable definition in any source we checked. Do not guess. Ask the user which property should change and by how much, or offer one of: " + ", ".join(x["verb"] for x in REF["verbs"] if x["resolution"] != "undefined") + "."}
        else: res = {"request": a[0], "verb": v, "resolution": r["resolution"], "plain": r["plain"], "stays_subjective": r["stays_subjective"], "checks": r["patterns"]}
    if "--json" in a: print(json.dumps(res, indent=1))
    else:
        print(f"{res.get('verb') or '?'}: {res['resolution']}")
        if res["resolution"] in ("tool-backed", "measurable"):
            print(res["plain"]); print("Stays subjective:", res["stays_subjective"])
            print("(commands below show the demo page; replace the path with your file, or run axl-evaluate on it)")
            for p in res["checks"]: print(f"- {p['name']}  [{p['claim_id']}, {p['status']}]\n    run: {p['command'] or '(no command)'}\n    passes when: {p['pass_criteria'] or ''}")
        else: print(res["message"])
    return 0
sys.exit(main())
