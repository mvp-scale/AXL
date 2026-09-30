#!/usr/bin/env python3
"""Lint skills: layout, frontmatter, admission rule (only enforced/measurable claims), claim status, receipts exist."""
import json, os, re, glob, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
C = {c["id"]: c for c in json.load(open(f"{ROOT}/axl/data/claims.json"))["claims"]}
errs, flags = [], []
for d in sorted(glob.glob(f"{ROOT}/axl/skills/*/")):
    name = os.path.basename(d.rstrip("/")); f = f"{d}SKILL.md"
    if not os.path.exists(f): errs.append((name, "no SKILL.md")); continue
    t = open(f, encoding="utf-8").read()
    m = re.match(r"---\nname: ([\w-]+)\ndescription: (.+)\n---\n", t)
    if not m or m.group(1) != name: errs.append((name, "bad frontmatter or name mismatch"))
    if not os.path.isdir(f"{d}scripts") or not glob.glob(f"{d}scripts/*"): errs.append((name, "no scripts/"))
    ids = sorted(set(re.findall(r"clm_\d{4}", t)))
    if name != "axl-verbs" and not ids: errs.append((name, "lists no claim ids"))
    for i in ids:
        c = C.get(i)
        if not c: errs.append((name, f"unknown claim {i}")); continue
        if c["tier"] in ("subjective", "process"): errs.append((name, f"cites {c['tier']} claim {i}"))
        if c["origin"] != "public": errs.append((name, f"cites non-public claim {i}"))
        if c["status"] not in ("verified", "single-source"): flags.append((name, i, c["status"]))
        if c["tier"] == "enforced":
            for r in c.get("receipts", []):
                if not os.path.exists(f"{ROOT}/axl/receipts/runs/{r}.json"): errs.append((name, f"{i}: missing receipt {r}"))
    if name == "axl-verbs":
        ref = json.load(open(f"{d}references/verbs.json"))
        for v in ref["verbs"]:
            for p in v["patterns"]:
                if C[p["claim_id"]]["tier"] in ("subjective", "process"): errs.append((name, f"snapshot cites {p['claim_id']}"))
for e in errs: print("ERROR", *e)
for f_ in flags: print("REVIEW", *f_)
print(f"lint_skills: {len(errs)} errors, {len(flags)} review flags"); sys.exit(1 if errs else 0)
