#!/usr/bin/env python3
"""Merge sorted harvest into the catalogue.
In:  data/harvest/_rules.json, data/harvest/_taxonomy.json, sort outputs (scratch TSVs, copied to data/harvest/_sorted.tsv)
Out: data/tweaks.json (taxonomy + accepted NEW tweaks, css/check kept for existing ids), data/catalog.json (every rule with its tweaks)."""
import json, os, re, glob, collections, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = f"{ROOT}/axl"; H = f"{A}/data/harvest"
R = json.load(open(f"{H}/_rules.json"))["rules"]; TX = json.load(open(f"{H}/_taxonomy.json"))["tweaks"]
OLD = {t["id"]: t for t in json.load(open(f"{A}/data/tweaks.json"))["tweaks"]}
srt = {}
for line in open(f"{H}/_sorted.tsv", encoding="utf-8"):
    if "\t" not in line: continue
    i, v = line.rstrip("\n").split("\t", 1)
    if i.strip().isdigit(): srt[int(i)] = v.strip()
pre = json.load(open(f"{H}/_pre.json"))
ids = {t["id"] for t in TX}
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]
new = collections.defaultdict(lambda: {"n": 0, "cats": collections.Counter(), "names": collections.Counter()})
assign = {}
for i, r in enumerate(R):
    v = pre.get(str(i)) or srt.get(i)
    if isinstance(v, list): assign[i] = [x for x in v if x in ids]; continue
    if not v or v == "-": assign[i] = []; continue
    if v.startswith("NEW:"):
        name, _, cat = v[4:].partition("|"); k = slug(name)
        new[k]["n"] += 1; new[k]["cats"][cat.strip()] += 1; new[k]["names"][name.strip()] += 1; assign[i] = ["NEW:" + k]; continue
    assign[i] = [x for x in re.split(r"[,\s]+", v) if x in ids][:2]
CATS = {"Type", "Color", "Space & layout", "Surface", "Motion", "Interaction & states", "Access", "Content & process", "Components", "Performance", "Agent workflow"}
# a NEW tweak is accepted when at least 2 rules (any source) proposed the same name; singletons stay as unsorted rules
acc = {k: v for k, v in new.items() if v["n"] >= 2 and k not in ids}
tweaks = []
for t in TX:
    o = OLD.get(t["id"], {})
    tweaks.append({"id": t["id"], "name": o.get("name", t["name"]), "category": t["category"], "aka": t.get("also_known_as", []), "refs": t.get("standard_refs", []),
                   "effect": o.get("effect"), "check": o.get("check"), "kind": o.get("kind"), "source_quote": o.get("source_quote"), "source_url": o.get("source_url")})
for k, v in sorted(acc.items(), key=lambda kv: -kv[1]["n"]):
    cat = v["cats"].most_common(1)[0][0]; cat = cat if cat in CATS else "Content & process"
    tweaks.append({"id": k, "name": v["names"].most_common(1)[0][0][:48], "category": cat, "aka": [], "refs": [], "effect": None, "check": None, "kind": None})
ids2 = {t["id"] for t in tweaks}
rules = []
for i, r in enumerate(R):
    tw = [x[4:] if x.startswith("NEW:") else x for x in assign.get(i, [])]
    tw = [x for x in tw if x in ids2]
    rules.append({"src": r["src"], "text": r["text"], "url": r.get("url"), "command": r.get("command"), "tweaks": tw, "also": r.get("also", []), "check": r.get("check")})
json.dump({"categories": sorted(CATS, key=["Type", "Color", "Space & layout", "Surface", "Motion", "Interaction & states", "Components", "Access", "Content & process", "Performance", "Agent workflow"].index), "tweaks": tweaks},
          open(f"{A}/data/tweaks.json", "w"), indent=1)
json.dump({"rules": rules}, open(f"{A}/data/catalog.json", "w"), indent=0, ensure_ascii=False)
used = collections.Counter(x for r in rules for x in r["tweaks"])
print(f"tweaks {len(tweaks)} (new accepted {len(acc)}, singletons left {sum(1 for v in new.values() if v['n'] < 2)}); rules {len(rules)}; mapped {sum(1 for r in rules if r['tweaks'])}; not a UI rule {sum(1 for i in range(len(R)) if not assign.get(i))}; tweaks with >=1 rule {len(used)}")
