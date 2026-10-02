#!/usr/bin/env python3
"""Phase 4: build data/verbs.json. Definitions are verbatim raw slices of saved source texts. Resolution is rule-based:
measurable  = >=1 linked public claim of tier measurable/enforced with a delta (and none enforced) (delta cites the claim id)
tool-backed = >=1 linked public claim is enforced (a receipt exists for its command)
undefined   = neither. Term list: the 18 required verbs + candidate vague terms mentioned >=3 times across saved sources."""
import json, os, re, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"; TXT = f"{ROOT}/axl/receipts/sources"
S = {s["id"]: s for s in json.load(open(f"{D}/sources.json"))["sources"]}
LIN = json.load(open(f"{D}/lineage.json"))["roots"]
C = [c for c in json.load(open(f"{D}/claims.json"))["claims"] if c["origin"] == "public"]
DEF = {d["verb"]: d for d in json.load(open(f"{D}/definitions.json"))["definitions"]}
REQ = "polish distill delight bolder quieter animate colorize clarify harden adapt optimize typeset layout onboard critique audit extract shape".split()
CAND = "simplify elevate refine tighten soften declutter modernize sharpen premium clean minimal bold subtle playful professional elegant crisp calm energetic vibrant intuitive cohesive consistent balanced hierarchy rhythm airy dense compact warm".split()
raw = {i: open(f"{TXT}/{i}.txt", encoding="utf-8").read() for i in S if os.path.exists(f"{TXT}/{i}.txt")}
pat = lambda v: re.compile(r"\b" + v + r"(?:e?s|ed|ing)?\b", re.I)
counts = {v: sum(len(pat(v).findall(t)) for t in raw.values()) for v in REQ + CAND}
verbs = REQ + [v for v in CAND if counts[v] >= 3]
def slice40(t, start):
    m = list(re.finditer(r"\S+", t[start:start + 600]))[:40]
    return t[start: start + m[-1].end()].strip()
def definition_of(v, i):
    t = raw[i]
    if i == f"src_impeccable-{v}":
        body = re.sub(r"^\s*---.*?---", "", t, flags=re.S)
        for m in re.finditer(r"^(?![>#\-|`\d])[^\n]{60,}$", t, re.M):
            return slice40(t, m.start())
    m = pat(v).search(t)
    if not m: return None
    st = max(t.rfind(". ", 0, m.start()), t.rfind("\n", 0, m.start())) + 1
    return slice40(t, st) if m.end() - st < 400 else slice40(t, m.start())
out = []
for v in verbs:
    defids = {p["claim_id"] for p in DEF.get(v, {}).get("patterns", [])}
    linked = [c for c in C if c["id"] in defids or c["verb"] == v or (v in REQ and c["verb"] == v) or (c["legacy_id"] is None and pat(v).search(c["text"]))]
    meas = [c for c in linked if c["tier"] in ("measurable", "enforced") and c["delta"]]
    enf = [c for c in linked if c["tier"] == "enforced"]
    tool = [c for c in linked if c["tool_candidate"]]
    defs, roots_seen = [], set()
    own = f"src_impeccable-{v}"
    order = ([own] if own in raw else []) + [i for i in sorted(raw) if i != own and not i.startswith("src_impeccable-")]
    for i in order:
        q = definition_of(v, i)
        if not q or q not in raw[i]: continue
        r = LIN[i]
        if r in roots_seen and len(defs) >= 1 and i != own: continue   # one definition per root keeps rebrands from padding the table
        roots_seen.add(r); defs.append({"source_id": i, "kind": S[i]["kind"], "root": r, "url": S[i]["url"], "quote": q})
        if len(defs) >= 4: break
    res = "tool-backed" if enf else "measurable" if meas else "undefined"
    grams = [set(zip(*[re.findall(r"\w+", d["quote"].lower())[k:] for k in range(4)])) for d in defs]
    disagree = ("single source of definition; agreement cannot be assessed" if len(defs) < 2 else
                "auto-flag: definitions share no 4-word phrase; possible divergence, needs human review" if not set.intersection(*grams) else "definitions overlap textually")
    out.append({"verb": v, "mentions_across_sources": counts[v], "required": v in REQ, "definitions": defs,
        "shared_deltas": [{"claim_id": c["id"], "selector": c["delta"]["selector"], "property": c["delta"]["property"], "before": c["delta"]["before"], "after": c["delta"]["after"], "status": c["status"]} for c in meas],
        "tool_candidates": sorted({c["tool_candidate"] for c in tool}), "enforced_claim_ids": [c["id"] for c in enf], "linked_claim_ids": [c["id"] for c in linked],
        "axl_patterns": [p["id"] for p in DEF.get(v, {}).get("patterns", [])], "linked_tiers": dict(collections.Counter(c["tier"] for c in linked)),
        "disagreement": disagree, "resolution": res,
        "note": {"measurable": "at least one linked claim has a concrete delta; the rest of the verb stays subjective",
                 "tool-backed": "at least one linked claim is enforced: a command was run and has a receipt; the rest of the verb stays subjective",
                 "undefined": "no measurable definition in any fetched source; the skill must say so instead of guessing"}[res]})
json.dump({"verbs": out}, open(f"{D}/verbs.json", "w"), indent=1, ensure_ascii=False)
print(len(out), dict(collections.Counter(x["resolution"] for x in out)))
