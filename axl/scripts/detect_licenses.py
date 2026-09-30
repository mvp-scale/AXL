#!/usr/bin/env python3
"""Best-effort licence detection for GitHub-hosted sources: fetch LICENSE from raw.githubusercontent.com
and match well-known phrases. Anything not detected stays 'unknown'. Non-GitHub pages stay 'unknown'."""
import json, re, os, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
P = f"{ROOT}/axl/data/sources.json"; d = json.load(open(P)); seen = {}
KEY = [("Apache-2.0", r"Apache License\s+Version 2\.0"), ("MIT", r"Permission is hereby granted, free of charge"),
       ("MPL-2.0", r"Mozilla Public License"), ("BSD", r"Redistribution and use in source and binary forms"),
       ("ISC", r"Permission to use, copy, modify, and/or distribute"), ("GPL", r"GNU GENERAL PUBLIC LICENSE"),
       ("CC-BY-4.0", r"Creative Commons Attribution 4\.0")]
def lic(repo):
    if repo in seen: return seen[repo]
    res = "unknown"
    for br in ("main", "master", "develop"):
        for f in ("LICENSE", "LICENSE.md", "LICENSE.txt", "license"):
            r = subprocess.run(["curl","-sL","-m","20","-w","%{http_code}",f"https://raw.githubusercontent.com/{repo}/{br}/{f}"],capture_output=True,text=True).stdout
            if r.endswith("200"):
                body = r[:-3]
                for name, pat in KEY:
                    if re.search(pat, body, re.I): res = name; break
                else: res = "other (LICENSE file present, not auto-identified)"
                seen[repo] = res; return res
    seen[repo] = res; return res
for s in d["sources"]:
    m = re.match(r"https://github\.com/([\w.-]+/[\w.-]+)", s["url"])
    if m and s["fetch"]: s["license"] = lic(m.group(1))
json.dump(d, open(P, "w"), indent=1, sort_keys=True)
print(seen)
