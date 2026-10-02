#!/usr/bin/env python3
"""Compute lineage roots from derives_from and write data/lineage.json (nodes, edges, root per source,
rebrand clusters = roots with >= 2 members)."""
import json, os, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def roots(by):
    def root(i, seen=()):
        if i in seen: raise SystemExit(f"cycle at {i}")
        s = by[i]
        if not s["derives_from"]: return i
        rs = sorted({root(p, seen + (i,)) for p in s["derives_from"]})
        return rs[0] if len(rs) == 1 else "+".join(rs)   # multi-root derivative: composite root, never counted independent of its parents
    return {i: root(i) for i in by}
def main():
    src = json.load(open(f"{ROOT}/axl/data/sources.json"))["sources"]
    by = {s["id"]: s for s in src}
    for s in src:
        for p in s["derives_from"]: assert p in by, (s["id"], p)
    r = roots(by)
    clusters = collections.defaultdict(list)
    for i, rt in r.items(): clusters[rt].append(i)
    out = {"nodes": [{"id": s["id"], "kind": s["kind"], "publisher": s["publisher"], "root": r[s["id"]]} for s in src],
           "edges": [{"from": s["id"], "to": p} for s in src for p in s["derives_from"]],
           "roots": r, "rebrand_clusters": {k: sorted(v) for k, v in clusters.items() if len(v) > 1}}
    json.dump(out, open(f"{ROOT}/axl/data/lineage.json", "w"), indent=1, sort_keys=True)
    return out
if __name__ == "__main__":
    o = main(); print(len(o["rebrand_clusters"]), "multi-member clusters")
