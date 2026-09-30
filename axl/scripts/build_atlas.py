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
EXTRA_CSS = {  # visible stand-ins on the Northstar demo for tweaks that have no legacy effect (AXL's rendering, not a source's CSS)
 "contrast-text": ".topbar,.topbar span,#breadcrumb,.eyebrow,.subcopy,.metric-label,.metric-note{color:#3d4a5c!important}.activity small,li>small,th{color:#4f5d72!important}",
 "body-16": "p,li,td,.subcopy,.project-detail{font-size:16px!important}",
 "banned-fonts": "h1,h2,.brand{font-family:Charter,'Bitstream Charter','Iowan Old Style',Georgia,serif!important;letter-spacing:-.01em}",
 "type-scale": "h1{font-size:30px!important;line-height:1.15}h2{font-size:19px!important}.metric-value{font-size:30px!important}.metric-label,.metric-note,th{font-size:12px!important}",
 "remove-clutter": ".eyebrow,.metric-note,.topbar .user span:not(.avatar),.nav-bottom{display:none!important}",
 "progressive-disclosure": ".activity li:nth-child(n+3),tbody tr:nth-child(n+4){display:none!important}",
 "mute-color": "button.primary,.progress span,.chart-line,.badge{filter:saturate(.45)}",
 "color-roles": ".badge.active{background:#e7f0fb!important;color:#1f4f8a!important}.badge.review{background:#fff4dc!important;color:#7a4b00!important}.badge.risk{background:#fdeaea!important;color:#9b1c1c!important}.badge.done{background:#e6f4ea!important;color:#1e6b34!important}",
 "design-tokens": "button.primary{background:#1f3a5c!important;border-color:#1f3a5c!important}.chart-line{stroke:#1f3a5c!important}.progress span{background:#1f3a5c!important}h1,h2,.metric-value{color:#1f3a5c!important}",
 "contrast-7": "body,.subcopy,.metric-label,.metric-note,.topbar,#breadcrumb,.eyebrow,small,th,td,footer{color:#1f2733!important}",
 "non-text-contrast": ".card,input,select,textarea,.data-panel,button:not(.primary){border-color:#7b8796!important}",
 "text-spacing": "p,li,td,.subcopy{line-height:1.5!important;letter-spacing:.12em;word-spacing:.16em}",
 "color-not-only": ".badge::before{content:'● ';}.badge.risk::before{content:'▲ '}.badge.done::before{content:'✓ '}",
 "states-designed": ".card:empty,.empty-state{outline:2px dashed #8a97a8}.data-panel tbody tr:first-child td{background:#f3f6fa}",
 "focal-motion": ".hero h1{text-shadow:0 0 0 transparent}",
}
EXTRA_CSS.pop("states-designed"); EXTRA_CSS.pop("focal-motion")   # not honestly visible as a static change
tweaks = {t["id"]: dict(t, css=EFF.get(t["effect"]) if t.get("effect") else EXTRA_CSS.get(t["id"]), asks=[]) for t in TW["tweaks"]}
# previews for every other tweak: a real CSS change shown on the view where it applies (measured by tools/runners/preview_check.js),
# or an honest reason it can't be seen on a static page. Written with model help, verified by script, reviewable in data/previews.json.
PV = json.load(open(f"{D}/previews.json")) if os.path.exists(f"{D}/previews.json") else {}
for t in tweaks.values():
    p = PV.get(t["id"], {})
    if t["css"]: t.update(view="overview", state=None, patch=None, kind=None, why=None)
    else: t.update(css=p.get("css"), patch=p.get("patch"), view=p.get("view"), state=p.get("state"), kind=p.get("kind"), why=p.get("why"))
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
VSF = f"{D}/verb_sources.json"
if os.path.exists(VSF):
    for e in json.load(open(VSF))["entries"]:
        words.setdefault(e["word"], []).append({"src": e["source"], "word": e["word"], "url": e["url"], "quote": e["quote"], "tweaks": e["tweaks"], "kind": e.get("kind"), "derives_from": e.get("derives_from"), "n": 1})
for vs in words.values():
    for v in vs: v["tweaks"] = [t for t in v["tweaks"] if t in tweaks]
    vs.sort(key=lambda v: (v.get("kind") == "derivative", -len(v["tweaks"])))
CANON = [("better-web-ui", "better-web-ui"), ("Agent Skills Finder", "Agent Skills Finder"), ("openclaw", "OpenClaw"), ("ui-final-polish", "ui-final-polish"),
         ("make-interfaces-feel-better", "Feel Better"), ("better-ui skill", "UI Skills"), ("alvarovillalbaa", "Villalba"), ("ce-polish", "Compound Eng."),
         ("UI Craft", "UI Craft"), ("ui-craft", "UI Craft"), ("Impeccable", "Impeccable"), ("IxDF", "IxDF"), ("awesome-design-skills", "Awesome Design"),
         ("taste-skill", "Taste-Skill"), ("mcouthon", "mcouthon"), ("design-overhaul", "design-overhaul"),
         ("Anthropic frontend-design", "Anthropic"), ("frontend-design-deslop", "samber deslop"), ("make-interfaces-feel-better", "Feel Better"), ("shadcn/ui skills", "shadcn/ui"),
         ("OneRedOak design review", "OneRedOak"), ("OpenAI UI guidelines", "OpenAI"), ("Vercel Web Interface", "Vercel"), ("Apple Human Interface", "Apple HIG"),
         ("Nielsen Norman", "NN/g"), ("GOV.UK", "GOV.UK"), ("web.dev", "web.dev"), ("Unslop", "Unslop UI"), ("Hallmark", "Hallmark"), ("Claw Design", "Claw Design"),
         ("Google DESIGN.md", "Google DESIGN.md"), ("W3C WCAG", "W3C WCAG 2.2"), ("axe-core", "axe-core"), ("Lighthouse", "Lighthouse")]
def canon(n):
    for k, v in CANON:
        if k.lower() in n.lower(): return v
    return n
isverb = lambda w: re.fullmatch(r"[a-z]+", w) is not None
entries = {}
for w0, vs in words.items():
    w = w0 if isverb(w0) else "checklist"   # a source's own named guideline set ("design review", "audit gates"...) = its general checklist
    for v in vs:
        key = (w, canon(v["src"]))
        e = entries.setdefault(key, {"word": w, "src": key[1], "tweaks": [], "quote": v.get("quote"), "url": v["url"], "kind": v.get("kind") or "primary", "derives_from": v.get("derives_from")})
        for t in v["tweaks"]:
            if t in tweaks and t not in e["tweaks"]: e["tweaks"].append(t)
        if not e["quote"] and v.get("quote"): e["quote"] = v["quote"]
# ---- the full harvest: every source's own rule set, grouped by its commands (or "checklist") ----
CATF = f"{D}/catalog.json"
catalog = json.load(open(CATF))["rules"] if os.path.exists(CATF) else []
DENY = {"taste", "document", "visualize", "overdrive", "android", "ios", "brandkit", "stitch", "new", "work", "ui", "craft", "frontend", "design", "live", "image", "code", "gpt", "manual", "finish", "reviewer", "asset", "producer", "applier", "setup", "init", "doctor", "hooks", "detector", "antipatterns"}
def cmd_word(c):
    if not c: return "checklist"
    c = re.sub(r"^(ui-craft-|impeccable-)", "", c.lower()); c = re.sub(r"-skill(-v\d+)?$", "", c); c = {"minimalist": "minimal", "brutalist": "brutalist"}.get(c, c)
    return c if re.fullmatch(r"[a-z]{4,14}", c) and c not in DENY else "checklist"
for r in catalog:
    key = (cmd_word(r["command"]), canon(r["src"]))
    e = entries.setdefault(key, {"word": key[0], "src": key[1], "tweaks": [], "quote": None, "url": r.get("url") or "", "kind": "primary", "derives_from": None})
    for t_ in r["tweaks"]:
        if t_ in tweaks and t_ not in e["tweaks"]: e["tweaks"].append(t_)
        if t_ in tweaks and r.get("qid"): e.setdefault("ev", {}).setdefault(t_, []).append(r["qid"])   # quote IDs behind this link
    if not e["quote"] and r["tweaks"]: e["quote"] = r["text"]
    for t_ in r["tweaks"]:
        if t_ in tweaks: tweaks[t_]["asks"].append({"src": key[1], "word": key[0], "text": r["text"], "verified": True, "url": r.get("url") or ""})
entries = list(entries.values())
# the command layer as data: every definition (command x source) with its linked tweaks and the quote IDs behind each link
json.dump({"entries": entries}, open(f"{D}/entries.json", "w"), ensure_ascii=False, indent=0)
srcs = sorted({e["src"] for e in entries}, key=lambda s: (-sum(e["src"] == s for e in entries), s))
wl = sorted({e["word"] for e in entries if isverb(e["word"])}, key=lambda w: (-sum(e["word"] == w for e in entries), w))
def prov(t):
    out, seen = [], set()
    for a in t["asks"]:
        k = (canon(a["src"]), a["text"][:60])
        if k in seen: continue
        seen.add(k); out.append({"src": canon(a["src"]), "quote": a["text"], "url": a["url"], "verified": a["verified"]})
    for e in entries:
        if t["id"] in e["tweaks"] and e.get("quote") and not any(o["src"] == e["src"] for o in out):
            out.append({"src": e["src"], "quote": e["quote"], "url": e["url"], "verified": True})
    if t.get("source_quote"): out.append({"src": "W3C WCAG 2.2" if "w3.org" in t["source_url"] else "Smashing Magazine", "quote": t["source_quote"], "url": t["source_url"], "verified": True})
    return out
# the rule layer (Class › Element › Rules) and every quote ID it cites, so a source chip can show the exact statements
RULES = json.load(open(f"{D}/rules.json"))["rules"] if os.path.exists(f"{D}/rules.json") else []
VOC = json.load(open(f"{D}/vocab.json"))
CATQ = {r["qid"]: r for r in catalog}; CLM = {c["id"]: c for c in json.load(open(f"{D}/claims.json"))["claims"]}
SIDX = {s_["id"]: s_["name"] for s_ in json.load(open(f"{D}/sources_index.json"))["sources"]}
quotes = {}
for r in RULES:
    for v in r["values"]:
        for q in v["qids"]:
            if q in CATQ: quotes[q] = [q.split(":")[0], " ".join(CATQ[q]["text"].split())[:260], CATQ[q].get("url") or ""]
            elif q.startswith("claim:") and q[6:] in CLM: c = CLM[q[6:]]; quotes[q] = [c.get("source_id") or "", " ".join((c["quote"] if c["quote_verified"] else c["text"]).split())[:260], c["source_url"]]
# only rules with at least one source statement or public claim are shown (the rest are listed in the build output, not guessed at)
RULES = [r for r in RULES if r["values"]]
rules_d = [{"id": r["id"], "class": r["class"], "element": r["element"], "kind": r["kind"], "code": r["code"], "label": r["label"], "sources": r["sources"],
            "values": [{"v": v["value"], "q": v["qids"]} for v in r["values"]], "tweaks": r["tweaks"], "pv": r["preview"]} for r in RULES]
data = {"frame": {"width": 980, "height": 760}, "before": open(f"{A}/demo/northstar.html", encoding="utf-8").read(),
  "categories": TW["categories"], "tweaks": [dict({k: t[k] for k in ("id", "name", "category", "check", "css", "patch", "view", "state", "kind", "why") if t.get(k) is not None}, asks=prov(t)) for t in tweaks.values()],
  "rules": rules_d, "elements": {e["id"]: {"name": e["name"], "family": e["family"]} for e in VOC["elements"]}, "classes": [c for c in VOC["classes"] if not c.get("staged")],
  "quotes": quotes, "srcnames": SIDX,
  "entries": entries, "words": wl, "sources": srcs, "vague": vague[:40],
  "stats": {"rules": len(catalog), "statements": len(claims) + len(catalog), "sources": len(srcs), "words": len(wl), "tweaks": len(tweaks), "vague": len(vague)}}
js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
html = open(f"{A}/scripts/atlas_template.html", encoding="utf-8").read().replace("/*DATA*/null", js)
open(f"{A}/site/index.html", "w", encoding="utf-8").write(html)
print(f"site/index.html {len(html)//1024} KB · words {len(wl)} · sources {len(srcs)} · entries {len(entries)} · polish sources {[e['src'] for e in entries if e['word']=='polish']}")
