#!/usr/bin/env python3
"""Phase 3: build data/claims.json from legacy_groups.json + saved source texts (+ seed standards claims).
Quotes are raw slices of receipts/sources/<id>.txt found by word-run matching; nothing is generated.
Tier follows 3.1 from the claim text alone (the legacy effect mapping is ignored)."""
import json, os, re, sys, bisect, difflib, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"; TXT = f"{ROOT}/axl/receipts/sources"
S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}
LIN = json.load(open(f"{D}/lineage.json"))["roots"]
def sid(u): 
    for s in S.values():
        if s["url"] == u: return s["id"]
IMP = lambda n: sid(f"https://github.com/pbakaus/impeccable/blob/main/skill/reference/{n}.md")
GROUP_SRC = {f"g{12+i}": [IMP(n)] for i, n in enumerate("polish distill delight bolder quieter animate colorize clarify harden adapt optimize typeset layout onboard critique audit extract shape".split())}
GROUP_SRC.update({
 "g30": [sid("https://www.claudecodehq.com/playbooks/unslop-ui")],
 "g31": [sid("https://github.com/anthropics/skills/tree/main/skills/frontend-design"), sid("https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics"), sid("https://claude.com/blog/improving-frontend-design-through-skills")],
 "g32": [sid("https://ui.shadcn.com/docs/skills")], "g33": [sid("https://github.com/nutlope/hallmark")],
 "g34": [sid("https://motion.dev/docs/react-accessibility")], "claw": [sid("https://github.com/yuchangxu1989-Openclaw/claw-design")],
 "google": [sid("https://github.com/google-labs-code/design.md")], "extra37": [sid("https://github.com/Leonxlnx/taste-skill")],
 "extra38": [sid("https://developers.openai.com/plugins/concepts/ui-guidelines")],
 "extra39": [sid("https://aiagentskills.net/skill/samber-cc-skills-frontend-design-deslop")],
 "extra40": [sid("https://dynamicworkflow.run/workflows/oneredoak-claude-code-workflows-design-review"), sid("https://github.com/OneRedOak/claude-code-workflows")]})
PRIVATE = {f"g{i}" for i in range(12)}

# ---------- text normalisation with index map ----------
TR = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-", " ": " "})
def norm(raw):
    out, idx, prev_space = [], [], True
    for i, ch in enumerate(raw.translate(TR)):
        if ch in "*`": continue
        ch = ch.lower()
        if ch.isspace():
            if prev_space: continue
            ch, prev_space = " ", True
        else: prev_space = False
        out.append(ch); idx.append(i)
    return "".join(out), idx
class Doc:
    def __init__(s, sid_):
        s.id = sid_; s.raw = open(f"{TXT}/{sid_}.txt", encoding="utf-8").read()
        s.n, s.idx = norm(s.raw)
        s.words = [(m.group(), m.start(), m.end()) for m in re.finditer(r"[^\s]+", s.n)]
        s.wtxt = [re.sub(r"^\W+|\W+$", "", w[0]) for w in s.words]
        s.grams = {tuple(s.wtxt[i:i+4]) for i in range(len(s.wtxt) - 3)}
    def slice(s, a, b):  # normalised [a,b) -> raw slice
        return s.raw[s.idx[a]: s.idx[b - 1] + 1]
    def match(s, text):
        """returns (coverage, quote) — quote is a verbatim raw slice, capped at 40 words"""
        cn, _ = norm(text)
        cw = [re.sub(r"^\W+|\W+$", "", w) for w in cn.split()]
        if not cw: return 0, None
        if len(cw) < 4:
            k = s.n.find(cn.rstrip(".;:, "))
            return (1.0, s.slice(k, k + len(cn.rstrip(".;:, ")))) if k >= 0 and len(cn) > 12 else (0, None)
        sm = difflib.SequenceMatcher(None, s.wtxt, cw, autojunk=False)
        m = sm.find_longest_match(0, len(s.wtxt), 0, len(cw))
        if m.size < 4: return 0, None
        cov = m.size / len(cw)
        a, b = m.a, m.a + min(m.size, 40)
        return cov, s.slice(s.words[a][1], s.words[b - 1][2])
DOCS = {}
def doc(i):
    if i not in DOCS: DOCS[i] = Doc(i)
    return DOCS[i]
def fetched(i): return i and S[i]["fetch_status"] == "ok" and os.path.exists(f"{TXT}/{i}.txt")
def grams_of(text):
    cn, _ = norm(text); w = [re.sub(r"^\W+|\W+$", "", x) for x in cn.split()]
    return {tuple(w[i:i+4]) for i in range(len(w) - 3)}

# ---------- tier / delta rules (text only) ----------
PROC = re.compile(r"^(review|audit|check|verify|ask|run|read|document|iterate|test|inspect|gather|determine|report|generate|compile|explore|confirm|classify|screenshot|capture|use the feature|start with|begin|write a|create a|log|record|interview)\b|\bask (the )?(user|questions?)\b", re.I)
FONTS = r"(Inter|Roboto|Arial|Open Sans|Lato|Space Grotesk|system-ui|Fraunces|Instrument Serif)"
def rules(t):
    """-> (tier, delta|None, tool_candidate|None)"""
    tl = t.lower()
    m = re.search(r"(\d+(?:\.\d+)?)\s*:\s*1", t)
    if m and re.search(r"contrast", tl): return "measurable", ("text", "contrast-ratio", None, f">= {m.group(1)}:1"), "axe-core color-contrast"
    m = re.search(r"(\d+)\s*(?:x|×|by)?\s*(?:\d+)?\s*(px|pt|dp)\b", tl)
    if m and re.search(r"touch|tap|target|hit area|click area", tl): return "measurable", ("interactive controls", "min-size", None, f">= {m.group(1)}{m.group(2)}"), "axe-core target-size"
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:-|to|–)?\s*(?:\d+(?:\.\d+)?)?\s*ms\b", tl)
    if m and re.search(r"motion|duration|transition|animat|ease|timing|hover|press|feedback|reveal|latency|delay", tl): return "measurable", ("animated elements", "transition-duration", None, re.search(r"\d+(?:\.\d+)?(?:\s*(?:-|to)\s*\d+(?:\.\d+)?)?\s*ms", tl).group(0)), "stylelint"
    m = re.search(r"(\d+)\s*(?:-\s*\d+\s*)?(ch|characters|chars)\b", tl)
    if m and re.search(r"line|measure|width|length|column", tl): return "measurable", ("body text", "max-width", None, m.group(0)), "stylelint"
    m = re.search(r"line-height[^.\d]{0,20}(\d(?:\.\d+)?)|(\d(?:\.\d+)?)\s*(?:line[- ]height|leading)", tl)
    if m: return "measurable", ("body text", "line-height", None, m.group(1) or m.group(2)), "stylelint"
    if re.search(r"prefers-reduced-motion|reduced motion|reduce motion", tl) and not re.search(r"follow the .{0,40}section", tl): return "measurable", ("*", "@media (prefers-reduced-motion: reduce)", None, "animation/transition reduced or disabled"), "playwright emulateMedia + screenshot"
    m = re.search(r"\b(\d+)\s*(?:px|pt)\b", tl)
    if m and re.search(r"grid|scale|spacing|multiples? of|rhythm", tl): return "measurable", ("layout", "spacing-unit", None, f"multiples of {m.group(1)}px"), "stylelint"
    m = re.search(r"\b(\d+)\s*(?:px|rem|em)\b", tl)
    if m and re.search(r"font|type|text size|body", tl): return "measurable", ("text", "font-size", None, m.group(0)), "stylelint"
    m = re.search(r"\b(\d+)\s*(?:px|rem)\b", tl)
    if m and re.search(r"radius|corner", tl): return "measurable", ("cards,buttons", "border-radius", None, m.group(0)), "stylelint"
    m = re.search(r"(?:no more than|max(?:imum)?(?: of)?|at most|limit(?:ed)? to|only|exactly|one to|two)\s+(\d+|one|two|three|four)\s+(font famil|typeface|font|color|accent|weight)", tl)
    if m: return "measurable", ("page", f"count({m.group(2).strip()})", None, f"<= {m.group(1)}"), None
    fn = re.findall(FONTS, t)
    if fn and re.search(r"avoid|ban|never|as the|display face|fallback|overused|default", tl): return "measurable", ("h1,h2,h3", "font-family", None, "excludes: " + ", ".join(sorted(set(fn)))), "stylelint"
    if re.search(r"#000\b|#fff\b|pure (black|white)", tl) and re.search(r"avoid|pure|never|not", tl): return "measurable", ("page,cards", "color", None, "not pure #000 / #fff"), "stylelint"
    if re.search(r"gradient", tl) and re.search(r"avoid|no |never|purple|decorat|remove", tl): return "measurable", ("*", "background-image", None, "no decorative gradient"), "stylelint"
    if re.search(r"focus (ring|indicator|state|style|visible)|focus-visible", tl): return "measurable", ("interactive controls", ":focus-visible outline", None, "visible focus indicator present"), "axe-core / playwright"
    if PROC.search(t.strip()): return "process", None, None
    return "subjective", None, None
def surface(t):
    tl = t.lower(); s = ["web"]
    if re.search(r"mobile|touch|ios|android|native|swiftui|compose|thumb", tl): s.append("mobile")
    if re.search(r"dashboard|admin|saas|enterprise|table|workspace", tl): s.append("saas")
    return s

# ---------- build ----------
G = json.load(open(f"{D}/legacy_groups.json"))["prescriptions"]
claims, n = [], 0
def new_id():
    global n; n += 1; return f"clm_{n:04d}"
def independent(primary, supports):
    roots = {r for r in LIN[primary].split("+")} if "+" not in LIN[primary] else set()
    if "+" in LIN[primary]: roots = set(LIN[primary].split("+"))
    for s in supports:
        if "+" not in LIN[s["source_id"]]: roots.add(LIN[s["source_id"]])
    return sorted(roots)
def corroborate(text, primary_id):
    g = grams_of(text); out = []
    if len(g) < 3: return out
    for i in sorted(S):
        if i == primary_id or not fetched(i): continue
        d = doc(i)
        if len(g & d.grams) / len(g) < 0.5: continue
        cov, q = d.match(text)
        if cov >= 0.6 and q: out.append({"source_id": i, "quote": q, "coverage": round(cov, 2)})
    return out
for r in G:
    gid = r["group_id"]; t = r["text"]
    tier, delta, tool = rules(t)
    if r["caveat"]: tier, delta, tool = "process", None, None
    c = {"id": new_id(), "verb": r["group_name"].lower(), "text": t, "quote": None, "source_id": "", "source_url": r["url"], "retrieved_at": None,
         "quote_verified": False, "origin": "private-kit" if gid in PRIVATE else "public", "tier": tier, "surface": surface(t),
         "delta": dict(zip(("selector", "property", "before", "after"), delta)) if delta else None, "enforcement": None, "tool_candidate": tool,
         "supports": [], "independent_roots": [], "status": "unverified", "notes": "", "legacy_id": r["id"]}
    notes = [f"legacy:{r['id']}"]
    if r["truncated"]: notes.append("legacy text looks truncated mid-sentence")
    if r["caveat"]: notes.append("research caveat / open question, not a prescription")
    if gid in PRIVATE:
        c["source_id"] = "private-kit"; c["source_url"] = "legacy/ATTRIBUTION.md#research-kit"
        notes.append("origin private-kit: no public source; excluded from the public build")
    else:
        best = (0, None, None)
        for sid_ in GROUP_SRC.get(gid, []):
            if not fetched(sid_): continue
            cov, q = doc(sid_).match(t)
            if cov > best[0]: best = (cov, q, sid_)
        if not GROUP_SRC.get(gid): notes.append("no source mapped to this group")
        cov, q, sid_ = best
        if sid_ and q and cov >= 0.6:
            c.update(quote=q, source_id=sid_, source_url=S[sid_]["url"], retrieved_at=S[sid_]["retrieved_at"], quote_verified=True)
            if cov < 0.999: notes.append(f"partial match: {round(cov*100)}% of the legacy words found as one run in the source; legacy text is a paraphrase")
            c["supports"] = corroborate(t, sid_)
            c["independent_roots"] = independent(sid_, c["supports"])
            c["status"] = "verified" if len(c["independent_roots"]) >= 2 else "single-source"
        else:
            first = GROUP_SRC.get(gid, [None])[0]
            c["source_id"] = first or "none"; c["source_url"] = S[first]["url"] if first else r["url"]
            if first: c["retrieved_at"] = S[first]["retrieved_at"]
            notes.append("text not found in the saved source (best coverage %d%%); legacy entry is a paraphrase or the source was not fetched" % round(cov * 100))
    c["notes"] = "; ".join(notes)
    claims.append(c)

# ---------- seed standards / tool claims (regex against the saved text; quote is the matched slice) ----------
SEEDS = [
 ("accessibility", "Text has a contrast ratio of at least 4.5:1 (large text 3:1).", sid("https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"), r"has a contrast ratio of at least 4\.5:1", ("text", "contrast-ratio", None, ">= 4.5:1 (>= 3:1 large text)"), "axe-core color-contrast"),
 ("accessibility", "Pointer targets are at least 24 by 24 CSS pixels unless spacing or another exception applies.", sid("https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html"), r"The size of the target for pointer inputs is at least 24 by 24 CSS pixels", ("interactive controls", "min-size", None, ">= 24x24 CSS px"), "axe-core target-size"),
 ("accessibility", "Focus indicators have a contrast ratio of at least 3:1 between focused and unfocused states.", sid("https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html"), r"has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states", ("interactive controls", ":focus-visible outline", None, "contrast >= 3:1 vs unfocused"), None),
 ("accessibility", "axe-core target-size rule: touch targets must be 24px large or leave sufficient space.", sid("https://dequeuniversity.com/rules/axe/4.8/target-size"), r"All touch targets must be 24px large, or leave sufficient space", ("interactive controls", "min-size", None, ">= 24px or spacing"), "axe-core target-size"),
 ("verify", "Visually compare screenshots against a stored reference with toHaveScreenshot().", sid("https://playwright.dev/docs/test-snapshots"), r"visually compare screenshots using await expect\(page\)\.toHaveScreenshot\(\)", None, "playwright toHaveScreenshot"),
]
for verb, text, sid_, pat, delta, tool in SEEDS:
    if not fetched(sid_): continue
    d = doc(sid_); m = re.search(pat, d.raw, re.I)
    c = {"id": new_id(), "verb": verb, "text": text, "quote": None, "source_id": sid_, "source_url": S[sid_]["url"], "retrieved_at": S[sid_]["retrieved_at"],
         "quote_verified": bool(m), "origin": "public", "tier": "measurable" if delta else "process", "surface": ["web"],
         "delta": dict(zip(("selector", "property", "before", "after"), delta)) if delta else None, "enforcement": None, "tool_candidate": tool,
         "supports": [], "independent_roots": [], "status": "unverified", "notes": "seed claim from recon (standards/tool docs); tier set from claim text; no tool run yet", "legacy_id": None}
    if m:
        c["quote"] = d.raw[m.start(): m.end()]
        c["independent_roots"] = independent(sid_, []); c["status"] = "single-source"
    claims.append(c)
# 4.5:1 and 24px are also stated by axe-core's rule page: record as a *derived* support only (same lineage), not independent
json.dump({"claims": claims}, open(f"{D}/claims.json", "w"), indent=1, ensure_ascii=False)
cnt = collections.Counter((c["tier"], c["status"]) for c in claims)
print(len(claims), dict(collections.Counter(c["status"] for c in claims)), dict(collections.Counter(c["tier"] for c in claims)))
