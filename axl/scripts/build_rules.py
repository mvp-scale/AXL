#!/usr/bin/env python3
"""Build data/rules.json and data/commands.json from the per-area rule files in data/rules_src/ (one per former tweak area,
drafted by agents and validated against the saved standards), the statement catalogue (quote IDs) and data/entries.json.

A rule's ID is element/property[@context] (or element/ask:<hash> for a question). Tweaks that state different values for the same
element and property are the SAME rule with a disagreement: every stated value is kept with its quote IDs; the default test is
the one backed by the most statements."""
import json, os, re, sys, glob, hashlib, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
sys.path.insert(0, f"{ROOT}/axl/scripts")
from vocab import V, render
EL = {e["id"]: e for e in V["elements"]}
CLS = {c["id"]: c for c in V["classes"]}
ORIGIN = {"type": "type", "color": "color", "layout": "layout", "surface": "surface", "motion": "motion", "interaction": "interaction",
          "component": None, "access": "access", "content": "content", "perf": "perf", "agent": "process"}
LH_SEO = {"document-title", "meta-description", "http-status-code", "link-text", "crawlable-anchors", "is-crawlable", "robots-txt", "hreflang", "canonical", "structured-data", "image-alt"}
MEASURE_CLASS = json.load(open(f"{D}/measure_classes.json")) if os.path.exists(f"{D}/measure_classes.json") else {}

def css_class(p):
    """Class of a CSS property by the CSS module it belongs to."""
    if p in V["properties"]: return V["properties"][p]["class"]
    for rx, c in ((r"^(font|text|letter|word|line|hyphen|white-space|tab-size|quotes|hanging)", "type"), (r"^(color|background-color|accent-color|caret-color|fill|stroke|forced-color|color-scheme)", "color"),
                  (r"^(margin|padding|gap|row-gap|column-gap|width|height|min-|max-|inset|top|left|right|bottom|grid|flex|display|position|overflow|z-index|align|justify|place|order|columns|container|contain)", "layout"),
                  (r"^(border|outline|box-shadow|background|backdrop|mask|clip)", "surface"), (r"^(object-|aspect-ratio|filter|image-)", "imagery"),
                  (r"^(transition|animation|transform|translate|rotate|scale|scroll-behavior|view-transition|offset)", "motion"),
                  (r"^(cursor|pointer-events|user-select|touch-action|overscroll|scroll-snap|resize|caret)", "interaction"), (r"^(direction|writing-mode|unicode-bidi)", "locale")):
        if re.match(rx, p): return c
    return None

ALIAS = {"border-top-left-radius": "border-radius", "axl:border-radius": "border-radius"}   # agents had only longhands to choose from; the shorthand is the rule people mean

def parse(rule):
    m = re.match(r'(\S+)\s+ask\s+"(.+)"$', rule)
    if m: return {"element": m.group(1), "property": "ask", "question": m.group(2), "context": []}
    ctx = [c for c in re.findall(r"@(\S+)", rule)]; p = re.sub(r"\s*@\S+", "", rule).split()
    return {"element": p[0], "property": ALIAS.get(p[1], p[1]), "test": " ".join(p[2:]), "context": ctx}

def main():
    cat = {r["qid"]: r for r in json.load(open(f"{D}/catalog.json"))["rules"]}
    rules = collections.OrderedDict(); problems = []
    # cross-area question merges (data/rules_src/_questions.json): original question rule -> merged element, class and wording
    QM = {}
    if os.path.exists(f"{D}/rules_src/_questions.json"):
        for m in json.load(open(f"{D}/rules_src/_questions.json")):
            for f in m["from"]: QM[f] = m
    # rule links per tweak: the per-area files, then links for statements recovered from the harvest filter (add_recovered.py)
    items = []
    for f in sorted(glob.glob(f"{D}/rules_src/[a-z]*.json")):
        area = os.path.basename(f)[:-5]
        items += [(area, t, r) for t, rs in json.load(open(f))["tweaks"].items() for r in rs]
    if os.path.exists(f"{D}/rules_src/_recovered.json"):
        items += [(r["area"], t, dict(r, **{"class": r.get("class") or ORIGIN.get(r["area"]) or "content"}))
                  for t, rs in json.load(open(f"{D}/rules_src/_recovered.json"))["tweaks"].items() for r in rs]
    for area, t, r in items:
        x = parse(r["rule"])
        if x["property"] == "ask":
            cls = r.get("class"); m = QM.get(f'{x["element"]} ask "{x["question"]}"')
            if m: x["element"], x["question"], cls = m["element"], m["question"], m["class"]
            rid = f"{x['element']}/ask:{hashlib.sha1(x['question'].lower().encode()).hexdigest()[:6]}"
        else:
            rid = f"{x['element']}/{x['property']}" + "".join(f"@{c}" for c in x["context"])
            p = x["property"]
            cls = ("access" if p.startswith("wcag:") else ("seo" if p[11:] in LH_SEO else "perf") if p.startswith("lighthouse:")
                   else MEASURE_CLASS.get(p) or ORIGIN.get(area) if p.startswith("axl:") else css_class(p) or ORIGIN.get(area))
        if not cls: problems.append(f"no class for {rid} (from {area}/{t})"); cls = "interaction"
        R = rules.setdefault(rid, {"id": rid, "element": x["element"], "property": x["property"], "context": x["context"], "class": cls,
                                    "question": x.get("question"), "tests": collections.Counter(), "values": collections.defaultdict(set), "tweaks": set()})
        if x["property"] != "ask": R["tests"][x["test"]] += 1; R.setdefault("ttest", {})[t] = x["test"]
        R["tweaks"].add(t)
        for v in r.get("values", []):
            for q in v.get("qids", []):
                if q not in cat: problems.append(f"unknown qid {q} in {rid}")
                else: R["values"][v.get("value") if v.get("value") not in ("", None) else None].add(q)
    # tweaks from the earlier curated set have no harvested statements: their evidence is the public claims mapped to them (claim IDs)
    claims = {c["id"]: c for c in json.load(open(f"{D}/claims.json"))["claims"] if c["origin"] == "public"}
    tclaims = collections.defaultdict(set)
    for cid, ts in json.load(open(f"{D}/tweak_map.json")).items():
        if cid in claims:
            for t in ts: tclaims[t].add(cid)
    for R in rules.values():
        if not R["values"]:
            for t in R["tweaks"]:
                for cid in tclaims.get(t, ()): R["values"][None].add(f"claim:{cid}")
    out = []
    for R in rules.values():
        if R["property"] == "ask":
            code = f'{R["element"]} ask "{R["question"]}"'; kind = "ask"
        else:
            def support(te):   # statements whose stated value appears in this test
                return sum(len(q) for v, q in R["values"].items() if v is not None and str(v).split()[0] in te)
            best = max(R["tests"], key=lambda te: (support(te), R["tests"][te]))
            code = f'{R["element"]} {R["property"]} {best}' + "".join(f" @{c}" for c in R["context"]); kind = "auto"
            R["preview"] = sorted(t for t, te in R.get("ttest", {}).items() if te == best)   # the demo shows the default value only
        srcof = lambda i: ("claim:" + (claims[i[6:]].get("source_id") or "")) if i.startswith("claim:") else i.split(":")[0]
        vals = [{"value": v, "qids": sorted(q), "sources": sorted({srcof(i) for i in q})} for v, q in sorted(R["values"].items(), key=lambda a: -len(a[1]))]
        out.append({"id": R["id"], "class": R["class"], "element": R["element"], "property": R["property"], "context": R["context"], "kind": kind,
                    "code": code, "label": render(code), "values": vals, "sources": sorted({s for v in vals for s in v["sources"]}), "tweaks": sorted(R["tweaks"]), "preview": R.get("preview", sorted(R["tweaks"]))})
    # commands: each definition (command x source) -> rules, with the evidence behind each link
    E = json.load(open(f"{D}/entries.json"))["entries"]; by_tweak = collections.defaultdict(list)
    for r in out:
        for t in r["tweaks"]: by_tweak[t].append(r["id"])
    defs = []
    for e in E:
        links = collections.OrderedDict()
        for t in e["tweaks"]:
            for rid in by_tweak.get(t, []):
                L = links.setdefault(rid, {"rule": rid, "qids": set(), "via": set()})
                L["via"].add(t); L["qids"].update(e.get("ev", {}).get(t, []))
        defs.append({"command": e["word"], "source": e["src"], "url": e.get("url"), "quote": e.get("quote"), "derives_from": e.get("derives_from"),
                     "links": [{"rule": L["rule"], "qids": sorted(L["qids"]), "via": sorted(L["via"])} for L in links.values()]})
    json.dump({"version": "0.1", "rules": out}, open(f"{D}/rules.json", "w"), ensure_ascii=False, indent=0)
    json.dump({"version": "0.1", "definitions": defs}, open(f"{D}/commands.json", "w"), ensure_ascii=False, indent=0)
    n = collections.Counter(r["class"] for r in out); k = collections.Counter(r["kind"] for r in out)
    print(f"rules.json: {len(out)} rules ({k['auto']} measurable, {k['ask']} questions) on {len({r['element'] for r in out})} elements · commands.json: {len(defs)} definitions")
    print("  by class:", dict(n.most_common()))
    noev = [r["id"] for r in out if not r["values"]]
    if noev: print(f"  {len(noev)} rules with no evidence (tweak had no statement and no public claim): {noev[:8]}")
    unlinked = [t for t in json.load(open(f"{D}/tweaks.json"))["tweaks"] if t["id"] not in by_tweak]
    if unlinked: problems.append(f"{len(unlinked)} tweaks without rules")
    for p in problems[:20]: print("  !", p)
    return 1 if problems else 0

if __name__ == "__main__": sys.exit(main())
