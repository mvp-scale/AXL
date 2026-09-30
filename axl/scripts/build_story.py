#!/usr/bin/env python3
"""Build axl/site/index.html: ONE self-contained file (inline CSS, JS, data, demo pages and close-up images). No network at runtime.
Every number on the page is read from data/*.json, receipts/runs/*.json and demo/crops/pins.json; quotes are verbatim slices of saved sources."""
import json, os, re, base64, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = f"{ROOT}/axl"; D = f"{A}/data"
claims = [c for c in json.load(open(f"{D}/claims.json"))["claims"] if c["origin"] == "public"]
C = {c["id"]: c for c in claims}
S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}
SU = {s["url"]: s for s in S.values()}
LIN = json.load(open(f"{D}/lineage.json"))
V = json.load(open(f"{D}/verbs.json"))["verbs"]; DEFS = json.load(open(f"{D}/definitions.json"))["definitions"]
runs = {f[:-5]: json.load(open(f"{A}/receipts/runs/{f}")) for f in os.listdir(f"{A}/receipts/runs")}
pj = json.load(open(f"{A}/demo/crops/pins.json"))
pat = {p["id"]: p for d in DEFS for p in d["patterns"]}
uri = lambda f: "data:image/png;base64," + base64.b64encode(open(f, "rb").read()).decode()
def fails(rid, rule=None, contains=None):
    n = 0
    for f in runs[rid]["findings"]:
        if f.get("result") != "fail": continue
        if rule and f.get("rule_id") != rule: continue
        if contains and contains not in f.get("evidence", ""): continue
        n += f.get("nodes", 1)
    return n
COUNT = {"contrast": (("axe-before-1440", "color-contrast", None), ("axe-after-1440", "color-contrast", None)),
         "targets": (("craft-layout-before", "target-44", None), ("craft-layout-after", "target-44", None)),
         "spacing": (("craft-layout-before", "spacing-4", None), ("craft-layout-after", "spacing-4", None)),
         "type": (("craft-type-before", "body-16", None), ("craft-type-after", "body-16", None)),
         "focus": (("stylelint-before", None, "outline"), ("stylelint-after", None, "outline"))}
def quote_of(url, rx):
    s = SU[url]; t = open(f"{A}/receipts/sources/{s['id']}.txt", encoding="utf-8").read(); m = re.search(rx, t); assert m, rx
    return t[m.start():m.end()], s
pins = []
for i, pn in enumerate(pj["pins"], 1):
    p = pat[pn["pattern"]]; c = C[p["claim_id"]]; b, a = COUNT[pn["id"]]
    sup = c.get("supports") or []
    pin = {"n": i, "id": pn["id"], "title": pn["title"], "unit": pn["unit"], "before": pn["before"], "after": pn["after"], "rect": pn["rect"], "rectM": pn["rectM"],
           "imgBefore": uri(f"{A}/demo/crops/pin-{pn['id']}-before.png"), "imgAfter": uri(f"{A}/demo/crops/pin-{pn['id']}-after.png"),
           "command": p["check"]["command"], "tool": p["check"]["tool"], "pass": p["check"]["pass_criteria"], "failsBefore": fails(*b), "failsAfter": fails(*a),
           "roots": len(c["independent_roots"]), "quote": c["quote"], "publisher": S[c["source_id"]]["publisher"], "retrieved": c["retrieved_at"], "url": c["source_url"], "claim": c["id"], "status": c["status"]}
    if sup: s2 = S[sup[0]["source_id"]]; pin.update(quote2=sup[0]["quote"], publisher2=s2["publisher"], url2=s2["url"])
    pins.append(pin)
totals = {"before": sum(p["failsBefore"] for p in pins), "after": sum(p["failsAfter"] for p in pins)}
QS = [("https://github.com/pbakaus/impeccable", r"Final pass, design system alignment, and shipping readiness"),
      ("https://claude.com/blog/improving-frontend-design-through-skills", r"prompting for motion \(animations and micro-interactions\) adds polish that static designs lack"),
      ("https://github.com/Leonxlnx/taste-skill", r"Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion")]
meanings = []
for url, rx in QS: q, s = quote_of(url, rx); meanings.append({"quote": q, "publisher": s["publisher"], "url": url})
NUM = {"on-grid-spacing": "4px scale", "readable-contrast": "4.5 : 1", "visible-focus": "focus ring", "reachable-targets": "44 px", "line-length": "80 chars", "reflow": "320 px",
       "running-text-leading": "1.5 line-height", "text-size-floor": "14 px", "motion-duration": "500 ms", "reduced-motion": "motion off", "rules-engine-clean": "0 violations", "colour-tokens": "12 colours"}
DV = {d["verb"]: d for d in DEFS}
tiles = []
for v in sorted(V, key=lambda x: x["verb"]):
    d = DV.get(v["verb"]); lit = v["resolution"] != "undefined" and d
    t = {"verb": v["verb"], "lit": bool(lit)}
    if lit:
        t["nums"] = [NUM[p["id"]] for p in d["patterns"] if p["id"] in NUM]; t["command"] = d["patterns"][0]["check"]["command"]
    else:
        defs = [x for x in v["definitions"] if x["source_id"] == f"src_impeccable-{v['verb']}"] or v["definitions"]
        if defs:
            q = " ".join(defs[0]["quote"].split()); q = q if len(q) <= 150 else q[:150].rsplit(" ", 1)[0] + "…"
            t.update(quote=q, publisher=S[defs[0]["source_id"]]["publisher"], url=defs[0]["url"])
    tiles.append(t)
cited = {c["source_id"] for c in claims} | {s["source_id"] for c in claims for s in c.get("supports", [])}
nodes = [s for s in S.values() if s["id"] in cited or s["derives_from"] or any(s["id"] in o["derives_from"] for o in S.values())]
byroot = {}
for s in nodes: byroot.setdefault(LIN["roots"][s["id"]], []).append(s)
clusters = []
for r, m in sorted(byroot.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    m = sorted(m, key=lambda s: (s["id"] != r, s["id"])); clusters.append({"name": (S[r]["publisher"] if r in S else r), "n": len(m), "members": [{"id": s["id"], "publisher": s["publisher"]} for s in m]})
edges = [[e["from"], e["to"]] for e in LIN["edges"] if LIN["roots"][e["from"]] == LIN["roots"][e["to"]]]
data = {"meanings": meanings, "frame": pj["frame"], "frameM": pj["frameM"], "totals": totals, "pins": pins, "tiles": tiles, "echo": {"clusters": clusters, "edges": edges},
        "before": open(f"{A}/demo/before.html", encoding="utf-8").read(), "after": open(f"{A}/demo/polished.html", encoding="utf-8").read(),
        "stats": {"double": sum(c["status"] == "verified" for c in claims), "claims": len(claims), "sources": len(S), "receipts": len(runs)}}
# stable public registry: what other tools consume (the reason to come back and build on it)
terms = {"axl_terms": "0.1", "note": "Each term resolves to measurable patterns with a check command, or to 'undefined'. Ids are stable; thresholds marked axl-default are proposals.",
         "terms": [{"id": f"axl:term/{v['verb']}@0.1", "term": v["verb"], "resolution": v["resolution"],
                    "patterns": [{"id": f"axl:pattern/{p['id']}@0.1", "name": p["name"], "claim": p["claim_id"], "status": p["status"], "tool": (p["check"] or {}).get("tool"), "command": (p["check"] or {}).get("command"),
                                  "pass": (p["check"] or {}).get("pass_criteria"), "parameter": p.get("parameter_origin")} for p in (DV[v["verb"]]["patterns"] if v["verb"] in DV else [])]} for v in sorted(V, key=lambda x: x["verb"])]}
json.dump(terms, open(f"{A}/terms.json", "w"), indent=1, ensure_ascii=False)
js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
html = open(f"{A}/scripts/story_template.html", encoding="utf-8").read().replace("/*DATA*/null", js)
os.makedirs(f"{A}/site", exist_ok=True); open(f"{A}/site/index.html", "w", encoding="utf-8").write(html)
print(f"site/index.html {len(html)//1024} KB; pins {[ (p['n'], p['failsBefore'], p['failsAfter']) for p in pins]}; totals {totals}; lit {sum(t['lit'] for t in tiles)}/{len(tiles)}; clusters {[c['n'] for c in clusters][:6]}")
