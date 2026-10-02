#!/usr/bin/env python3
"""Give every harvested statement a permanent quote ID: <source-id>:<6 hex of sha1(text)>.
The ID depends only on the source and the exact verbatim text, so it never changes when the catalogue is rebuilt.
Writes data/sources_index.json (source id -> name, url, statement count) and adds `qid` to each rule in data/catalog.json."""
import json, os, hashlib, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
P = f"{ROOT}/axl/data/catalog.json"
SID = {"UI Craft": "ui-craft", "Hallmark": "hallmark", "Taste-Skill": "taste-skill", "Impeccable": "impeccable", "frontend-design-deslop": "deslop",
       "Vercel Web Interface Guidelines": "vercel", "Claw Design": "claw-design", "Lighthouse": "lighthouse", "make-interfaces-feel-better": "feel-better",
       "axe-core": "axe", "shadcn/ui skills": "shadcn", "Google DESIGN.md": "google-designmd", "W3C WCAG 2.2": "wcag22", "Unslop UI": "unslop",
       "Apple Human Interface Guidelines": "apple-hig", "OneRedOak design review": "oneredoak", "Anthropic frontend-design": "anthropic",
       "Nielsen Norman Group": "nngroup", "OpenAI UI guidelines (Apps SDK / Plugins)": "openai", "GOV.UK Design System": "govuk", "web.dev Learn Design + Forms": "webdev"}
def main():
    cat = json.load(open(P)); seen = {}; idx = collections.OrderedDict()
    for r in cat["rules"]:
        sid = SID[r["src"]]; n = 6
        while True:
            q = f"{sid}:{hashlib.sha1(r['text'].encode()).hexdigest()[:n]}"
            if q not in seen or seen[q] == r["text"]: break
            n += 1
        seen[q] = r["text"]; r["qid"] = q
        s = idx.setdefault(sid, {"id": sid, "name": r["src"], "urls": set(), "statements": 0}); s["statements"] += 1; s["urls"].add(r["url"])
    json.dump(cat, open(P, "w"), ensure_ascii=False, indent=0)
    out = [dict(v, urls=sorted(v["urls"])) for v in idx.values()]
    json.dump({"sources": out}, open(f"{ROOT}/axl/data/sources_index.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(seen)} quote IDs across {len(out)} sources")


if __name__ == "__main__": main()
