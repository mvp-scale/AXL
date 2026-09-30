#!/usr/bin/env python3
"""Filter + de-duplicate harvested rules. Deterministic: keeps an item only if it reads like a rule (directive/measurable wording, 5-45 words),
drops file/tool chatter, and collapses near-duplicates (token Jaccard >= .8) within and across sources. Writes data/harvest/_rules.json."""
import json, os, re, glob, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
H = f"{ROOT}/axl/data/harvest"
DIRECT = re.compile(r"\b(use|avoid|never|always|don't|do not|must|should|prefer|keep|make|ensure|limit|set|add|remove|reduce|increase|give|provide|pair|align|match|replace|default to|no more than|at least|at most|only|instead of|minimum|maximum|max|min|\d+(\.\d+)?\s?(px|rem|em|ms|%|:1|ch|pt))\b", re.I)
NOISE = re.compile(r"(\.md\b|\.json\b|\.ts\b|npm |npx |pnpm |git |curl |http|install|README|this file|this skill|this command|frontmatter|see also|copyright|license|```|^\||^#|^\s*[-*]?\s*$|argument|--[a-z])", re.I)
norm = lambda s: re.sub(r"[^a-z0-9 ]+", " ", s.lower())
tok = lambda s: set(w for w in norm(s).split() if len(w) > 2)
rules, stats = [], collections.Counter()
for f in sorted(glob.glob(f"{H}/*.json")):
    if os.path.basename(f).startswith("_"): continue
    d = json.load(open(f)); src = d["source"]
    for it in d["items"]:
        t = " ".join(it["text"].split()); stats[src, "raw"] += 1
        tool = d.get("kind") in ("tool", "standard")
        wc = len(t.split())
        if not tool and (wc < 5 or wc > 45 or NOISE.search(t) or not DIRECT.search(t)): continue
        rules.append({"src": src, "kind": d.get("kind"), "text": t, "category": it.get("category"), "command": it.get("command"), "file": it.get("file"),
                      "url": it.get("url") or (d.get("urls") or [None])[0], "check": it.get("check"), "id": it.get("id"), "measurable": it.get("measurable")})
        stats[src, "kept"] += 1
# near-duplicate collapse (keeps every source that states it)
out, idx = [], collections.defaultdict(list)
for r in rules:
    T = tok(r["text"]); hit = None
    for w in sorted(T)[:3]:
        for j in idx[w]:
            U = out[j]["_t"]; inter = len(T & U)
            if inter and inter / len(T | U) >= .8: hit = j; break
        if hit is not None: break
    if hit is None:
        r["_t"] = T; r["also"] = []; out.append(r)
        for w in T: idx[w].append(len(out) - 1)
    else:
        if r["src"] != out[hit]["src"] and r["src"] not in [a["src"] for a in out[hit]["also"]]: out[hit]["also"].append({"src": r["src"], "text": r["text"], "url": r["url"]})
        stats[r["src"], "dup"] += 1
for r in out: r.pop("_t")
json.dump({"rules": out}, open(f"{H}/_rules.json", "w"), indent=0, ensure_ascii=False)
srcs = sorted({s for s, _ in stats})
for s in srcs: print(f"{s:28} raw {stats[s,'raw']:5}  kept {stats[s,'kept']:5}  dup {stats[s,'dup']:4}")
print("unique rules:", len(out), "· stated by 2+ sources:", sum(1 for r in out if r["also"]))
