#!/usr/bin/env python3
"""Add statements the harvest filter dropped but a reading pass kept as real rules (data/harvest/_recovered.json).

The filter in consolidate_harvest.py keeps only imperative wording ("use", "avoid", a number), so descriptive rules such as
anti-pattern entries ("Hero eyebrow / pill chip: a tiny uppercase letter-spaced label ...") were lost. A reading pass sorted
each dropped statement into "rule" or "chatter" and linked the rules to tweaks and standard rule lines.

This script checks every recovered statement is verbatim in the saved source file (receipts/sources/), gives it a permanent
quote ID (same scheme as assign_ids.py), and adds it to data/catalog.json (marked recovered). The rule links are written to
data/rules_src/_recovered.json, which build_rules.py reads. Idempotent: earlier recovered entries are replaced."""
import json, os, re, hashlib, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = f"{ROOT}/axl"; D = f"{A}/data"
sys.path.insert(0, f"{A}/scripts")
from assign_ids import SID
norm = lambda s: " ".join(s.split())
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]
CAT = {"type": "Type", "color": "Color", "layout": "Space & layout", "surface": "Surface", "motion": "Motion", "interaction": "Interaction & states",
       "component": "Components", "access": "Access", "content": "Content & process", "perf": "Performance", "agent": "Agent workflow"}

def main():
    rec = json.load(open(f"{D}/harvest/_recovered.json"))
    cat = json.load(open(f"{D}/catalog.json")); cat["rules"] = [r for r in cat["rules"] if not r.get("recovered")]
    TW = json.load(open(f"{D}/tweaks.json")); TW["tweaks"] = [t for t in TW["tweaks"] if not t.get("recovered")]; tids = {t["id"] for t in TW["tweaks"]}
    area_of = {}
    for f in os.listdir(f"{D}/rules_src"):
        if f[0].isalpha(): area_of.update({t: f[:-5] for t in json.load(open(f"{D}/rules_src/{f}"))["tweaks"]})
    seen = {r["qid"]: r["text"] for r in cat["rules"]}; out = collections.defaultdict(list); problems = []; added = newt = 0
    cache = {}
    for src in rec["sources"]:
        sid = SID[src["name"]]
        for s in src["statements"]:
            if s["kind"] != "rule": continue
            t = norm(s["text"]); fp = f"{A}/receipts/sources/{s['file']}"
            if fp not in cache: cache[fp] = norm(open(fp, encoding="utf-8").read()) if os.path.exists(fp) else ""
            if t not in cache[fp]: problems.append(f"not verbatim in {s['file']}: {t[:70]}"); continue
            n = 6
            while True:
                q = f"{sid}:{hashlib.sha1(t.encode()).hexdigest()[:n]}"
                if q not in seen or seen[q] == t: break
                n += 1
            seen[q] = t; tw = []
            for L in s["links"]:
                tid = L.get("tweak")
                if not tid:   # no existing tweak fits: a new one, named by the reading pass
                    tid = slug(L["name"]); area = L.get("area") or "content"
                    if tid not in tids:
                        TW["tweaks"].append({"id": tid, "name": L["name"], "category": CAT.get(area, "Content & process"), "aka": [], "refs": [], "effect": None, "check": None, "kind": None, "recovered": True})
                        tids.add(tid); area_of[tid] = area; newt += 1
                if tid not in tids: problems.append(f"unknown tweak {tid}"); continue
                tw.append(tid)
                out[tid].append({"rule": L["rule"], "area": area_of.get(tid, "content"), "values": [{"value": L.get("value"), "qids": [q]}]})
            cat["rules"].append({"src": src["name"], "text": t, "url": s.get("url") or src.get("url"), "command": s.get("command"), "tweaks": sorted(set(tw)),
                                 "also": [], "check": None, "qid": q, "recovered": True})
            added += 1
    json.dump(cat, open(f"{D}/catalog.json", "w"), ensure_ascii=False, indent=0)
    json.dump(TW, open(f"{D}/tweaks.json", "w"), indent=1)
    json.dump({"note": "rule links for statements recovered by add_recovered.py (see data/harvest/_recovered.json)", "tweaks": out},
              open(f"{D}/rules_src/_recovered.json", "w"), ensure_ascii=False, indent=0)
    print(f"recovered {added} statements ({newt} new tweaks, {sum(len(v) for v in out.values())} rule links)")
    for p in problems[:20]: print("  !", p)
    return 1 if problems else 0

if __name__ == "__main__": sys.exit(main())
