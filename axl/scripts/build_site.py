#!/usr/bin/env python3
"""Phase 7: generate axl/site/ from data/*.json. Writes site/data/data.js (window.AXL = {...}), copies demo/ pages.
index.html, styles.css and app.js are hand-written and live in site/. No network calls at runtime."""
import json, os, re, shutil, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"; SITE = f"{ROOT}/axl/site"
os.makedirs(f"{SITE}/data", exist_ok=True); os.makedirs(f"{SITE}/demo", exist_ok=True)
claims = [c for c in json.load(open(f"{D}/claims.json"))["claims"] if c["origin"] == "public"]     # private-kit excluded
S = json.load(open(f"{D}/sources.json"))["sources"]; LIN = json.load(open(f"{D}/lineage.json"))
V = json.load(open(f"{D}/verbs.json"))["verbs"]; DEFS = json.load(open(f"{D}/definitions.json"))["definitions"]
M = json.load(open(f"{ROOT}/axl/reports/metrics.json"))
runs = {f[:-5]: json.load(open(f"{ROOT}/axl/receipts/runs/{f}")) for f in os.listdir(f"{ROOT}/axl/receipts/runs")}
patch = open(f"{ROOT}/axl/demo/patch.css").read().splitlines()[1:]
fix = open(f"{ROOT}/axl/demo/fix.css").read()
line = lambda pat: "\n".join(l for l in patch if re.search(pat, l))
CSS = {   # CSS that the receipts validated (see receipts craft-*, axe-*, stylelint-*); nothing else is ever applied
 "on-grid-spacing": line(r"(padding|margin|gap)"),
 "readable-contrast": ".topbar,.topbar span,#breadcrumb,.eyebrow{color:#4b596c}.activity small,li>small{color:#566579}th{color:#4f5d72}footer,footer span{color:#566579}\n" + line(r"\{color:"),
 "visible-focus": "button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid #087d70;outline-offset:2px}",
 "reachable-targets": "button,input,select{min-height:44px}\n" + line(r"min-height"),
 "running-text-leading": ".subcopy,#page-copy{line-height:1.65;max-width:58ch}",
 "text-size-floor": "li,td,.activity li{font-size:14px}",
 "reduced-motion": "@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}",
}
CSS["rules-engine-clean"] = "\n".join([CSS["readable-contrast"], CSS["visible-focus"], CSS["reachable-targets"], ".hero{background:transparent}"])
CSS["polish-all"] = "\n".join(CSS[k] for k in ("on-grid-spacing", "readable-contrast", "visible-focus", "reachable-targets", "reduced-motion")) + "\n.hero{background:transparent}"
pat_by_claim = {p["claim_id"]: p["id"] for d in DEFS for p in d["patterns"]}
def claim_css(c):
    if c["id"] in pat_by_claim and pat_by_claim[c["id"]] in CSS: return CSS[pat_by_claim[c["id"]]]
    pr = (c.get("delta") or {}).get("property", "")
    if c["tier"] in ("enforced", "measurable") and pr == "contrast-ratio": return CSS["readable-contrast"]
    if c["tier"] in ("enforced", "measurable") and pr == ":focus-visible outline": return CSS["visible-focus"]
    if c["tier"] in ("enforced", "measurable") and pr.startswith("@media (prefers-reduced-motion"): return CSS["reduced-motion"]
    return None
cl = []
for c in claims:
    cl.append({k: c.get(k) for k in ("id", "verb", "text", "quote", "source_id", "source_url", "retrieved_at", "tier", "status", "surface", "delta", "enforcement", "receipts", "independent_roots", "discriminates", "notes")}
               | {"supports": c.get("supports", []), "css": claim_css(c)})
used = {c["source_id"] for c in cl} | {s["source_id"] for c in cl for s in c["supports"]}
def chain(i, by, out=None):
    out = out or []; out.append(i)
    for p in by[i]["derives_from"]: chain(p, by, out)
    return out
by = {s["id"]: s for s in S}
src = [{"id": s["id"], "url": s["url"], "publisher": s["publisher"], "kind": s["kind"], "derives_from": s["derives_from"], "license": s["license"], "retrieved_at": s["retrieved_at"],
        "content_hash": s["content_hash"], "fetch_status": s["fetch_status"], "root": LIN["roots"][s["id"]], "lineage_note": s.get("lineage_note", ""), "chain": chain(s["id"], by),
        "cited": s["id"] in used} for s in S]
rc = {k: {"id": k, "tool": r["tool"], "version": r["version"], "command": r["command"], "exit_code": r["exit_code"], "findings": len(r["findings"]), "fails": sum(1 for f in r["findings"] if f.get("result") == "fail"), "role": r["role"],
          "sample": [f.get("evidence", "")[:110] for f in r["findings"][:3]], "ran_at": r["ran_at"]} for k, r in runs.items()}
pj = json.load(open(f"{SITE}/img/pins.json"))
pat = {p["id"]: p for d in DEFS for p in d["patterns"]}
pins = []
for i, pn in enumerate(pj["pins"], 1):
    p = pat[pn["pattern"]]; c = next(x for x in cl if x["id"] == p["claim_id"])
    pins.append({"n": i, "id": pn["id"], "title": pn["title"], "unit": pn["unit"], "before": pn["before"], "after": pn["after"], "rect": pn["rect"], "claim_id": p["claim_id"], "status": p["status"], "tier": p["tier"],
                 "roots": len(p["independent_roots"]), "plain": p["plain"], "command": (p["check"] or {}).get("command"), "tool": (p["check"] or {}).get("tool"), "pass": (p["check"] or {}).get("pass_criteria"),
                 "receipts": [{"id": r["id"], "role": r["role"], "fails": rc[r["id"]]["fails"]} for r in p["receipts"] if r["id"] in rc]})
QS = [("https://github.com/pbakaus/impeccable", r"Final pass, design system alignment, and shipping readiness", "a final pass before shipping"),
      ("https://claude.com/blog/improving-frontend-design-through-skills", r"prompting for motion \(animations and micro-interactions\) adds polish that static designs lack", "added motion"),
      ("https://github.com/Leonxlnx/taste-skill", r"Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion", "an expensive look, with softer contrast")]
quotes = []
for url, rx, meaning in QS:
    src_ = next(x for x in S if x["url"] == url); txt = open(f"{ROOT}/axl/receipts/sources/{src_['id']}.txt", encoding="utf-8").read(); m = re.search(rx, txt)
    assert m, rx
    quotes.append({"publisher": src_["publisher"], "quote": txt[m.start():m.end()], "url": url, "meaning": meaning})
_pd = next(d for d in DEFS if d["verb"] == "polish"); rids = {r["id"] for p in _pd["patterns"] for r in p["receipts"]}
totals = {"before": sum(rc[i]["fails"] for i in rids if rc[i]["role"] == "before"), "after": sum(rc[i]["fails"] for i in rids if rc[i]["role"] == "after")}
data = {"pins": pins, "frame": pj["frame"], "polish_quotes": quotes, "polish_totals": totals, "claims": cl, "sources": src, "lineage": {"edges": LIN["edges"], "roots": LIN["roots"], "clusters": LIN["rebrand_clusters"]}, "verbs": V, "definitions": DEFS, "metrics": M, "receipts": rc, "css": CSS,
        "excluded": {"private_kit": M["private_kit_excluded"]}}
open(f"{SITE}/data/data.js", "w", encoding="utf-8").write("window.AXL=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
for f in ("before.html", "after.html", "polished.html", "fixture-motion-unguarded.html", "fixture-motion-guarded.html", "fixture-typeset.html"):
    shutil.copy(f"{ROOT}/axl/demo/{f}", f"{SITE}/demo/{f}")
print("site data:", len(cl), "claims,", len(src), "sources,", os.path.getsize(f"{SITE}/data/data.js") // 1024, "KB")
