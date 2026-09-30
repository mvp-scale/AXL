#!/usr/bin/env python3
"""Validate data/verb_sources.json against data/tweaks.json and receipts/sources/."""
import json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = {"word", "source", "publisher", "url", "file", "retrieved_at", "kind", "derives_from", "quote", "tweaks"}
norm = lambda s: re.sub(r"\s+", " ", s).strip()

def main():
    errs = []
    d = json.loads((ROOT / "data/verb_sources.json").read_text())
    tw = json.loads((ROOT / "data/tweaks.json").read_text())
    tw = tw.get("tweaks", tw) if isinstance(tw, dict) else tw
    ids = {t["id"] for t in tw}
    for k in ("retrieved", "queries", "entries"):
        if k not in d:
            errs.append(f"missing top-level {k}")
    seen, counts, vague = set(), Counter(), 0
    for n, e in enumerate(d.get("entries", [])):
        tag = f"#{n} {e.get('word')}/{e.get('file')}"
        if set(e) != KEYS:
            errs.append(f"{tag}: keys {sorted(set(e) ^ KEYS)}"); continue
        if e["kind"] not in ("primary", "derivative"):
            errs.append(f"{tag}: bad kind")
        if e["kind"] == "primary" and e["derives_from"] is not None:
            errs.append(f"{tag}: primary with derives_from")
        if not isinstance(e["tweaks"], list) or len(e["tweaks"]) > 6:
            errs.append(f"{tag}: tweaks must be list <=6")
        for t in e["tweaks"]:
            if t not in ids:
                errs.append(f"{tag}: unknown tweak {t}")
        if len(e["quote"].split()) > 40:
            errs.append(f"{tag}: quote >40 words")
        key = (e["word"], e["url"])
        if key in seen:
            errs.append(f"{tag}: duplicate (word,url)")
        seen.add(key)
        p = ROOT / "receipts/sources" / e["file"]
        if not p.exists():
            errs.append(f"{tag}: missing file")
        elif norm(e["quote"]) not in norm(p.read_text(errors="replace")):
            errs.append(f"{tag}: quote not verbatim in file")
        counts[e["word"]] += 1
        vague += not e["tweaks"]
    summary = ", ".join(f"{w}={c}" for w, c in counts.most_common())
    if errs:
        print("FAIL", len(errs), "errors;", summary)
        for x in errs: print("  ", x)
        sys.exit(1)
    print(f"PASS entries={sum(counts.values())} vague={vague} | {summary}")

main()
