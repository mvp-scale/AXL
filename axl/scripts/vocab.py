#!/usr/bin/env python3
"""The rule vocabulary (data/vocab.json): validate it against the fetched standards, and render rules as plain sentences.
  python3 axl/scripts/vocab.py                 validate + print sample sentences
  from vocab import render; render("text:body font-size >= 16px") -> "Body text size is at least 16px" """
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
V = json.load(open(f"{D}/vocab.json"))
EL = {e["id"]: e for e in V["elements"]}
WCAG = {"1.1.1": "text alternatives", "1.3.1": "structure is marked up", "1.4.1": "color isn't the only signal", "1.4.3": "text contrast (AA)", "1.4.4": "text resizes to 200%",
        "1.4.6": "text contrast (AAA)", "1.4.10": "reflow at 320px", "1.4.11": "non-text contrast", "1.4.12": "text spacing", "2.1.1": "keyboard access", "2.3.3": "motion from interaction",
        "2.4.1": "skip links", "2.4.6": "headings and labels", "2.4.7": "visible focus", "2.4.11": "focus not hidden", "2.5.8": "target size", "3.1.1": "page language", "3.3.1": "errors identified",
        "3.3.2": "labels or instructions", "3.3.3": "error suggestions", "4.1.2": "name, role, value"}

def validate():
    err = []
    aria = json.load(open(f"{D}/standards/aria_roles.json")); roles = set(aria["roles_1_2"]) | set(aria["added_in_1_3"])
    oui = set(json.load(open(f"{D}/standards/openui_components.json"))["components"])
    typ = set(json.load(open(f"{D}/standards/type_roles.json"))["roles"])
    for e in V["elements"]:
        ns, _, name = e["id"].partition(":")
        if ns == "aria" and name not in roles: err.append(f"{e['id']}: not an ARIA role")
        if ns == "aria" and name in aria["abstract_roles"]: err.append(f"{e['id']}: abstract ARIA role")
        if ns == "ui" and name not in oui and "not in research list" not in e["standard"]: err.append(f"{e['id']}: not an Open UI component")
        if ns == "text" and name not in typ and "extends" not in e["standard"] and name not in ("*", "code"): err.append(f"{e['id']}: not a type-scale role")
    names = [e["name"] for e in V["elements"]]
    if len(names) != len(set(names)): err.append("duplicate element names")
    return err

def _prop(p):
    if p in V["properties"]: return V["properties"][p]["words"]
    if p.startswith("wcag:"): return f"{WCAG.get(p[5:], 'WCAG ' + p[5:])} (WCAG {p[5:]})"
    if p.startswith("lighthouse:"): return p[11:].replace("-", " ") + " (Lighthouse)"
    if p.startswith("axl:"): return p[4:].replace("-", " ")
    return p.replace("-", " ")

def render(rule):
    """'<element> <property> <test...> [@media:x|@state:x]' or '<element> ask "question"' -> plain sentence."""
    m = re.match(r'(\S+)\s+ask\s+"(.*)"', rule)
    if m: return m.group(2)
    ctx = re.findall(r"@(\S+)", rule); rule = re.sub(r"\s*@\S+", "", rule).strip()
    el, prop, *test = rule.split()
    who = EL[el]["name"] if el in EL else el
    op, val = (test + ["", ""])[:2]; t = V["tests"].get(op, op); val = " ".join(test[1:])
    P = V.get("phrases", {})
    one = EL.get(el, {}).get("singular")
    agree = lambda x: re.sub(r"^\{el\} (use|come|have|meet|include|show|keep)\b", lambda m: "{el} " + ({"have": "has"}.get(m.group(1), m.group(1) + "s") if one else m.group(1)), x)
    if prop in P: s = agree(P[prop]).format(el=who, t=t, v=val)
    elif prop.startswith("wcag:"): s = agree(P["wcag:pass"]).format(el=who, sc=prop[5:], what=WCAG.get(prop[5:], ""))
    else: s = P["css"].format(el=who, p=_prop(prop), t=t, v=val)
    if ctx: s += " — " + ", ".join(EL[c]["name"].lower() if c in EL else c for c in ctx)
    return s[0].upper() + s[1:]

if __name__ == "__main__":
    e = validate(); print("\n".join(e) if e else f"vocab OK: {len(V['elements'])} elements, {len(V['classes'])} classes, {len(V['properties'])} properties")
    for r in ['text:* axl:distinct-font-sizes <= 6', 'text:body font-size >= 16px', 'aria:textbox font-size >= 16px @media:narrow', 'aria:heading line-height <= 1.2',
              'page axl:spacing-off-scale == 0', 'ui:icon axl:icon-sets <= 1', 'ui:icon axl:emoji-as-icons == 0', 'aria:img lighthouse:unsized-images pass',
              'aria:button wcag:2.5.8 pass', 'text:* wcag:1.4.3 pass', 'state:hover transition-duration <= 200ms', 'state:invalid ask "Does every error say what went wrong and how to fix it?"']:
        print(f"  {render(r):60} ← {r}")
    sys.exit(1 if e else 0)
