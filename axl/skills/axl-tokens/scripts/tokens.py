#!/usr/bin/env python3
"""axl-tokens: find raw colours and off-scale spacing in a stylesheet and align it to a token file.
  tokens.py init  <css> <tokens.json> [--n 12]   derive a token set from the most-used colours (deterministic)
  tokens.py check <css> <tokens.json>            findings JSON on the last line; exit 1 if any (with --strict), else 0
  tokens.py fix   <css> <tokens.json> <out.css>  snap colours to the nearest token (RGB distance <= 60) and spacing to the 4px scale
The tokens file is {"colors": {"name": "#rrggbb"}, "spacing_unit": 4}. Only hex colours and padding/margin/gap declarations are handled."""
import json, re, sys, collections
HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
SP = re.compile(r"((?:padding|margin|gap|row-gap|column-gap)(?:-(?:top|right|bottom|left))?)\s*:\s*([^;}]+)")
def full(h):
    h = h.lower(); return "#" + "".join(c * 2 for c in h[1:]) if len(h) == 4 else h
def rgb(h): h = full(h); return [int(h[i:i + 2], 16) for i in (1, 3, 5)]
def dist(a, b): return sum((x - y) ** 2 for x, y in zip(rgb(a), rgb(b))) ** .5
def colours(css): return collections.Counter(full(c) for c in HEX.findall(css))
def off_scale(css, unit):
    out = []
    for m in SP.finditer(css):
        for v in re.findall(r"(-?\d+(?:\.\d+)?)px", m.group(2)):
            if float(v) != 0 and (float(v) / unit) != round(float(v) / unit): out.append((m.group(1), v + "px"))
    return out
def main():
    cmd, css_path, tok_path = sys.argv[1], sys.argv[2], sys.argv[3]; css = open(css_path).read()
    if cmd == "init":
        n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 12; keep = []
        for c, _ in sorted(colours(css).items(), key=lambda kv: (-kv[1], kv[0])):
            if all(dist(c, k) > 28 for k in keep): keep.append(c)
            if len(keep) == n: break
        json.dump({"colors": {f"c{i + 1:02d}": c for i, c in enumerate(sorted(keep))}, "spacing_unit": 4}, open(tok_path, "w"), indent=1); print(f"{len(keep)} tokens"); return 0
    tok = json.load(open(tok_path)); allowed = set(tok["colors"].values()); unit = tok.get("spacing_unit", 4)
    if cmd == "check":
        f = [{"rule_id": "raw-colour", "result": "fail", "evidence": f"{c} is not a token value ({n} use{'s' if n > 1 else ''})", "location": c} for c, n in sorted(colours(css).items()) if c not in allowed]
        f += [{"rule_id": "off-scale-spacing", "result": "fail", "evidence": f"{p}: {v} is not a multiple of {unit}px", "location": f"{p} {v}"} for p, v in sorted(set(off_scale(css, unit)))]
        print(json.dumps({"tool": "axl-tokens", "findings": f})); return 1 if f and "--strict" in sys.argv else 0
    if cmd == "fix":
        def snap_c(m):
            c = full(m.group(0))
            if c in allowed: return m.group(0)
            best = min(allowed, key=lambda t: (dist(c, t), t)); return best if dist(c, best) <= 60 else m.group(0)
        def snap_s(m):
            body = re.sub(r"(-?\d+(?:\.\d+)?)px", lambda v: f"{max(unit, round(float(v.group(1)) / unit) * unit):g}px" if float(v.group(1)) != 0 and float(v.group(1)) / unit != round(float(v.group(1)) / unit) else v.group(0), m.group(2))
            return f"{m.group(1)}:{body}"
        out = SP.sub(snap_s, HEX.sub(snap_c, css)); open(sys.argv[4], "w").write(out); print(f"wrote {sys.argv[4]}"); return 0
    print(__doc__); return 2
sys.exit(main())
