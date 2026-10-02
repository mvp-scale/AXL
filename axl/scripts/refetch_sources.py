#!/usr/bin/env python3
"""Fetch every source with fetch:true, save extracted text to receipts/sources/<id>.txt (gitignored),
record status / retrieved_at / sha256 of the text in data/sources.json.
Modes: default = refetch and FLAG pages whose hash changed vs. the recorded one (does not overwrite the
recorded hash); --init = record results for sources with no hash yet; --update = accept new hashes.
Missing local texts are re-created. Run first in any phase that reads the saved texts."""
import json, os, sys, re, hashlib, subprocess, datetime, html
from html.parser import HTMLParser
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC = f"{ROOT}/axl/data/sources.json"; TXT = f"{ROOT}/axl/receipts/sources"
os.makedirs(TXT, exist_ok=True)
class T(HTMLParser):
    def __init__(s): super().__init__(); s.o=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in("script","style","noscript","svg","template"): s.skip+=1
        if t in("p","br","li","h1","h2","h3","h4","h5","h6","div","tr","pre","section"): s.o.append("\n")
    def handle_endtag(s,t):
        if t in("script","style","noscript","svg","template") and s.skip: s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.o.append(d)
def to_text(body, ctype, url):
    if "html" in ctype and not url.endswith((".md", ".txt")) and "raw.githubusercontent" not in url:
        p = T(); p.feed(body); t = html.unescape("".join(p.o))
    else: t = body
    t = re.sub(r"[ \t\r\f\v]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()
def fetch(url):
    r = subprocess.run(["curl","-sSL","-m","45","--max-filesize","6000000","-A","axl-recon/0.1 (+https://github.com/mvp-scale/AXL)",
        "-w","\n__CODE__%{http_code}__CT__%{content_type}","--compressed",url],capture_output=True)
    out = r.stdout.decode("utf-8","replace")
    m = re.search(r"\n__CODE__(\d+)__CT__(.*)$", out, re.S)
    if not m: return None, "", f"curl error {r.returncode}: {r.stderr.decode()[:120].strip()}"
    return int(m.group(1)), m.group(2), out[:m.start()]
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    d = json.load(open(SRC)); changed = []
    for s in d["sources"]:
        if not s["fetch"]: continue
        have_txt = os.path.exists(f"{TXT}/{s['id']}.txt")
        if mode == "--init" and s["content_hash"] and have_txt: continue
        code, ct, body = fetch(s["fetch_url"] or s["url"])
        if code != 200:
            if not s["content_hash"]: s["fetch_status"] = f"failed: {code if code else body}"
            else: changed.append((s["id"], f"now failing: {code}"))
            continue
        text = to_text(body, ct, s["fetch_url"] or s["url"])
        h = hashlib.sha256(text.encode()).hexdigest()
        if s["content_hash"] and s["content_hash"] != h and mode != "--update":
            changed.append((s["id"], "content changed")); 
            if have_txt: continue
        open(f"{TXT}/{s['id']}.txt","w",encoding="utf-8").write(text)
        s.update(content_hash=h, bytes=len(text.encode()), fetch_status="ok",
                 retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"))
    json.dump(d, open(SRC,"w"), indent=1, sort_keys=True)
    for c in changed: print("FLAG", *c)
    print(sum(s["fetch_status"]=="ok" for s in d["sources"]), "ok;", sum(str(s["fetch_status"]).startswith("failed") for s in d["sources"]), "failed;", len(changed), "flagged")
main()
