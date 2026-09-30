#!/usr/bin/env python3
"""Validate AXL documents against spec/axl.schema.json, and check that every claim id they cite exists.
usage: validate_axl.py [file ...]   (default: spec/examples/*.json)"""
import json, sys, glob, os
from jsonschema import Draft202012Validator
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
V = Draft202012Validator(json.load(open(f"{ROOT}/axl/spec/axl.schema.json")))
ids = {c["id"] for c in json.load(open(f"{ROOT}/axl/data/claims.json"))["claims"]}
bad = 0
for f in sys.argv[1:] or sorted(glob.glob(f"{ROOT}/axl/spec/examples/*.json")):
    d = json.load(open(f)); errs = [e.message[:100] for e in V.iter_errors(d)]
    cited = [c for r in d.get("evaluate", {}).get("rules", []) for c in r["claim_ids"]] + [o["claim_id"] for o in d.get("correct", {}).get("ops", [])]
    errs += [f"unknown claim {c}" for c in cited if c not in ids]
    print(os.path.basename(f), "OK" if not errs else errs); bad += bool(errs)
sys.exit(1 if bad else 0)
