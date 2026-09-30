#!/usr/bin/env python3
"""Validate data/tweaks.json and data/tweak_map.json."""
import json, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
CHECKS = {"contrast","spacing-4","target-44","measure-80","reflow-320","body-16","leading-1.5",
          "duration-500","reduced-motion","focus-visible","no-gradient","banned-fonts","tokens","axe"}
def main():
    errs = []
    try:
        tw = json.load(open(os.path.join(D, "tweaks.json")))
        mp = json.load(open(os.path.join(D, "tweak_map.json")))
        cl = json.load(open(os.path.join(D, "claims.json")))
        eff = json.load(open(os.path.join(D, "effects.json"))) if os.path.exists(os.path.join(D, "effects.json")) else None
    except Exception as e:
        print("FAIL invalid JSON: %s" % e); return 1
    cats, T = tw.get("categories", []), tw.get("tweaks", [])
    if len(cats) != 8: errs.append("categories=%d" % len(cats))
    if not 45 <= len(T) <= 75: errs.append("tweaks=%d" % len(T))
    ids = [t["id"] for t in T]
    if len(set(ids)) != len(ids): errs.append("duplicate ids")
    for t in T:
        if t.get("category") not in cats: errs.append("bad category " + t["id"])
        if t.get("check") is not None and t["check"] not in CHECKS: errs.append("bad check " + t["id"])
        if t.get("kind") not in ("visual", "behavior", "process"): errs.append("bad kind " + t["id"])
    used = [t["effect"] for t in T if t.get("effect")]
    if len(set(used)) != len(used): errs.append("effect reused")
    if len(used) != 42: errs.append("effects used=%d" % len(used))
    if eff is not None:
        want = {e["id"] for e in (eff if isinstance(eff, list) else eff.get("effects", []))}
        if want and want != set(used): errs.append("effect id mismatch")
    claims = [c["id"] for c in cl["claims"] if c.get("origin") == "public" and c.get("legacy_id")]
    miss = [c for c in claims if c not in mp]
    if miss: errs.append("%d claims missing from map" % len(miss))
    idset = set(ids)
    for k, v in mp.items():
        if len(v) > 3: errs.append("%s >3 tweaks" % k)
        for x in v:
            if x not in idset: errs.append("unknown tweak %s in %s" % (x, k))
    mapped = sum(1 for c in claims if mp.get(c)); none = len(claims) - mapped
    print("%s tweaks=%d mapped=%d unmapped=%d%s" % ("FAIL" if errs else "PASS", len(T), mapped, none,
          (" :: " + "; ".join(errs[:8])) if errs else ""))
    return 1 if errs else 0
sys.exit(main())
