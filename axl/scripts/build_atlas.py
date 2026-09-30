#!/usr/bin/env python3
"""Build axl/site/index.html (one self-contained file) from data/tweaks.json, data/tweak_map.json, claims, sources, lineage,
legacy effect CSS and the demo page. Quotes are verbatim slices of fetched sources; tweak mappings are model-assisted and reviewable."""
import json, os, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = f"{ROOT}/axl"; D = f"{A}/data"
TW = json.load(open(f"{D}/tweaks.json")); TM = json.load(open(f"{D}/tweak_map.json"))
claims = [c for c in json.load(open(f"{D}/claims.json"))["claims"] if c["origin"] == "public" and c["legacy_id"]]
S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}; SU = {s["url"]: s for s in S.values()}
ROOTS = json.load(open(f"{D}/lineage.json"))["roots"]
EFF = {e["id"]: e["css"] for e in json.load(open(f"{D}/legacy_effects.json"))["elements"]}
SHORT = [("impeccable", "Impeccable"), ("unslop", "Unslop UI"), ("anthropics", "Anthropic"), ("claude.com", "Anthropic"), ("shadcn", "shadcn/ui"), ("hallmark", "Hallmark"),
         ("motion.dev", "Motion"), ("claw-design", "Claw Design"), ("design.md", "Google DESIGN.md"), ("taste-skill", "Taste-Skill"), ("openai", "OpenAI"),
         ("deslop", "samber deslop"), ("oneredoak", "OneRedOak")]
def short(url):
    u = url.lower()
    for k, v in SHORT:
        if k in u: return v
    return S[SU[url]["id"]]["publisher"] if url in SU else url
tweaks = {t["id"]: dict(t, css=EFF.get(t["effect"]) if t.get("effect") else None, asks=[]) for t in TW["tweaks"]}
by_eff = {t["effect"]: t["id"] for t in TW["tweaks"] if t.get("effect")}
groups = collections.OrderedDict(); vague = []
for c in claims:
    src = short(c["source_url"]); key = (src, c["verb"])
    g = groups.setdefault(key, {"src": src, "word": c["verb"], "url": c["source_url"], "tweaks": [], "n": 0}); g["n"] += 1
    ids = TM.get(c["id"], [])
    if not ids: vague.append({"src": src, "word": c["verb"], "text": " ".join(c["text"].split())[:140], "verified": c["quote_verified"]})
    for tid in ids:
        if tid not in g["tweaks"]: g["tweaks"].append(tid)
        a = {"src": src, "word": c["verb"], "text": " ".join((c["quote"] if c["quote_verified"] else c["text"]).split())[:180], "verified": c["quote_verified"], "url": c["source_url"]}
        if len(tweaks[tid]["asks"]) < 8 or src not in {x["src"] for x in tweaks[tid]["asks"]}: tweaks[tid]["asks"].append(a)
for t in tweaks.values(): t["srcs"] = sorted({a["src"] for a in t["asks"]})
# curated versions of "polish" from verbatim quotes (each quote is re-located in the fetched text; mapping quote -> tweaks is ours)
def q(url, rx):
    s = SU[url]; txt = open(f"{A}/receipts/sources/{s['id']}.txt", encoding="utf-8").read(); m = re.search(rx, txt); assert m, rx; return txt[m.start():m.end()]
polish = [dict(groups[("Impeccable", "polish")], quote=q("https://github.com/pbakaus/impeccable", r"Final pass, design system alignment, and shipping readiness")),
  {"src": "Taste-Skill", "word": "polish", "url": "https://github.com/Leonxlnx/taste-skill", "quote": q("https://github.com/Leonxlnx/taste-skill", r"Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion"),
   "tweaks": [by_eff[e] for e in ("quiet", "airy", "serif", "bouncy", "shadow") if e in by_eff]},
  {"src": "Anthropic", "word": "polish", "url": "https://claude.com/blog/improving-frontend-design-through-skills", "quote": q("https://claude.com/blog/improving-frontend-design-through-skills", r"prompting for motion \(animations and micro-interactions\) adds polish that static designs lack"),
   "tweaks": [by_eff[e] for e in ("motion", "bouncy", "weighty") if e in by_eff]}]
if ("OneRedOak", "design review") in groups:
    g = groups[("OneRedOak", "design review")]; polish.append(dict(g, word="polish", quote=q("https://dynamicworkflow.run/workflows/oneredoak-claude-code-workflows-design-review", r"visual polish; WCAG 2")))
words = collections.OrderedDict([("polish", polish)])
for (src, w), g in groups.items():
    if (src, w) == ("Impeccable", "polish"): continue
    words.setdefault(w, []).append(dict(g, quote=None))
for vs in words.values():
    for v in vs: v["tweaks"] = [t for t in v["tweaks"] if t in tweaks]
srcs = sorted({g["src"] for g in groups.values()})
data = {"frame": {"width": 980, "height": 760}, "before": open(f"{A}/demo/before.html", encoding="utf-8").read(),
  "categories": TW["categories"], "tweaks": list(tweaks.values()), "words": [{"word": w, "versions": vs} for w, vs in words.items()], "sources": srcs,
  "vague": vague[:40], "stats": {"statements": len(claims), "sources": len(srcs), "words": len(words), "tweaks": len(tweaks), "vague": len(vague),
  "checkable": sum(1 for t in tweaks.values() if t.get("check")), "shared3": sum(1 for t in tweaks.values() if len(t["srcs"]) >= 3)}}
js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
html = open(f"{A}/scripts/atlas_template.html", encoding="utf-8").read().replace("/*DATA*/null", js)
open(f"{A}/site/index.html", "w", encoding="utf-8").write(html)
print(f"site/index.html {len(html)//1024} KB · {data['stats']} · polish versions {[ (v['src'], len(v['tweaks'])) for v in polish]}")
