#!/usr/bin/env python3
"""Phase 2 step 1: build data/sources.json (registry). Fetch results are merged in by refetch_sources.py.
URLs come from legacy/index.html group urls, legacy/ATTRIBUTION.md and best-practices/SOURCES.md,
plus a curated list of additional primaries (EXTRA). `fetch:false` = registered but skipped by the recon cap."""
import json, re, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = f"{ROOT}/axl/data/sources.json"
URL = re.compile(r"https?://[^\s)\]\"'<>`]+")
def urls(path):
    return [u.rstrip(".,;") for u in URL.findall(open(f"{ROOT}/{path}", encoding="utf-8").read())]
found = {}
def add(u, origin):
    found.setdefault(u, set()).add(origin)
for u in json.load(open(f"{ROOT}/axl/data/legacy_groups.json"))["groups"]:
    if u["url"].startswith("http"): add(u["url"], "legacy/index.html")
for u in urls("legacy/ATTRIBUTION.md"): add(u, "legacy/ATTRIBUTION.md")
for u in urls("best-practices/SOURCES.md"): add(u, "best-practices/SOURCES.md")

# id -> (url, fetch_url or None, publisher, kind, derives_from)
def raw(repo, path, br="main"): return f"https://raw.githubusercontent.com/{repo}/{br}/{path}"
IMP = ["adapt","animate","audit","bolder","clarify","colorize","critique","delight","distill","extract","harden","layout","onboard","optimize","polish","quieter","shape","typeset"]
FETCH_LEGACY = {  # legacy-set urls that get fetched (primaries + derivatives needed for lineage)
 "https://github.com/pbakaus/impeccable": (raw("pbakaus/impeccable","README.md"), "pbakaus/impeccable", "primary", []),
 "https://github.com/anthropics/skills/tree/main/skills/frontend-design": (raw("anthropics/skills","skills/frontend-design/SKILL.md"), "Anthropic", "primary", []),
 "https://github.com/Leonxlnx/taste-skill": (raw("Leonxlnx/taste-skill","README.md"), "Leonxlnx", "primary", []),
 "https://github.com/google-labs-code/design.md": (raw("google-labs-code/design.md","README.md"), "Google Labs", "primary", []),
 "https://ui.shadcn.com/docs/skills": (None, "shadcn/ui", "primary", []),
 "https://github.com/nutlope/hallmark": (raw("nutlope/hallmark","README.md"), "Nutlope / Together AI", "primary", []),
 "https://www.claudecodehq.com/playbooks/unslop-ui": (None, "claudecodehq.com", "derivative", []),
 "https://motion.dev/docs/react-accessibility": (None, "Motion", "primary", []),
 "https://developers.openai.com/plugins/concepts/ui-guidelines": (None, "OpenAI", "primary", []),
 "https://github.com/yuchangxu1989-Openclaw/claw-design": (raw("yuchangxu1989-Openclaw/claw-design","README.md"), "yuchangxu1989-Openclaw", "primary", []),
 "https://aiagentskills.net/skill/samber-cc-skills-frontend-design-deslop": (None, "aiagentskills.net (samber skill listing)", "derivative", []),
 "https://dynamicworkflow.run/workflows/oneredoak-claude-code-workflows-design-review": (None, "dynamicworkflow.run (OneRedOak workflow listing)", "derivative", []),
 "https://www.chaseai.io/blog/impeccable-4-claude-code-design-skill": (None, "chaseai.io", "derivative", []),
 "https://claude.com/blog/improving-frontend-design-through-skills": (None, "Anthropic", "primary", []),
 "https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics": (None, "Anthropic", "primary", []),
 "https://www.theadpharm.com/insights/claude-design-without-the-ai-slop-look": (None, "Adpharm", "derivative", []),
 "https://novitckii.com/resources/claude-design-skills/": (None, "novitckii.com", "derivative", []),
 "https://www.buildmvpfast.com/blog/design-md-file-ai-coding-agents-brand-consistency-2026": (None, "buildmvpfast.com", "derivative", []),
 "https://github.com/schoero/eslint-plugin-better-tailwindcss/blob/main/docs/rules/no-restricted-classes.md": (raw("schoero/eslint-plugin-better-tailwindcss","docs/rules/no-restricted-classes.md"), "schoero", "primary", []),
 "https://evilmartians.com/chronicles/ai-makes-design-system-guardrails-mandatory-this-framework-delivers-them": (None, "Evil Martians", "primary", []),
 "https://tianpan.co/blog/2026/07/02/your-design-system-needs-to-be-a-compiler": (None, "tianpan.co", "primary", []),
 "https://news.ycombinator.com/item?id=49058547": (None, "Hacker News", "derivative", []),
 "https://tailwindcss.com/docs/theme": (None, "Tailwind Labs", "primary", []),
 "https://qaskills.sh/blog/claude-code-screenshot-frontend-verification-mcp": (None, "qaskills.sh", "derivative", []),
 "https://betterstack.com/community/guides/ai/design-md-ai/": (None, "Better Stack", "derivative", []),
}
for n in IMP:
    u = f"https://github.com/pbakaus/impeccable/blob/main/skill/reference/{n}.md"
    FETCH_LEGACY[u] = (raw("pbakaus/impeccable", f"skill/reference/{n}.md"), "pbakaus/impeccable", "primary", [])
EXTRA = {  # additional primaries found in recon (tools/standards/skills) — not in legacy set
 "https://www.w3.org/TR/WCAG22/": "W3C",
 "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html": "W3C",
 "https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html": "W3C",
 "https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html": "W3C",
 "https://github.com/dequelabs/axe-core": "Deque",
 "https://playwright.dev/docs/test-snapshots": "Microsoft Playwright",
 "https://playwright.dev/docs/accessibility-testing": "Microsoft Playwright",
 "https://github.com/GoogleChrome/lighthouse": "Google Chrome",
 "https://github.com/schoero/eslint-plugin-better-tailwindcss": "schoero",
 "https://stylelint.io/user-guide/get-started": "Stylelint",
 "https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion": "MDN",
 "https://www.nngroup.com/articles/ten-usability-heuristics/": "Nielsen Norman Group",
 "https://github.com/Myndex/SAPC-APCA": "Myndex",
 "https://github.com/OneRedOak/claude-code-workflows": "OneRedOak",
 "https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html": "W3C",
 "https://github.com/educlopez/ui-craft": "educlopez",
 "https://dequeuniversity.com/rules/axe/4.8/target-size": "Deque",
 "https://github.com/samber/cc-skills": "samber",
 "https://github.com/shadcn-ui/ui": "shadcn-ui",
 "https://developer.apple.com/design/human-interface-guidelines/accessibility": "Apple",
 "https://m3.material.io/foundations/designing/structure": "Google Material",
 "https://web.dev/articles/vitals": "Google web.dev",
}
FETCH_RAW_EXTRA = {
 "https://github.com/dequelabs/axe-core": raw("dequelabs/axe-core","README.md","develop"),
 "https://github.com/GoogleChrome/lighthouse": raw("GoogleChrome/lighthouse","readme.md"),
 "https://github.com/educlopez/ui-craft": "https://cdn.jsdelivr.net/gh/educlopez/ui-craft@main/README.md",
 "https://github.com/schoero/eslint-plugin-better-tailwindcss": raw("schoero/eslint-plugin-better-tailwindcss","README.md"),
 "https://github.com/Myndex/SAPC-APCA": raw("Myndex/SAPC-APCA","README.md","master"),
 "https://github.com/OneRedOak/claude-code-workflows": raw("OneRedOak/claude-code-workflows","README.md"),
 "https://github.com/samber/cc-skills": raw("samber/cc-skills","README.md"),
 "https://github.com/shadcn-ui/ui": raw("shadcn-ui/ui","README.md"),
}
SKIP = {"https://developer.apple.com/design/human-interface-guidelines/accessibility","https://m3.material.io/foundations/designing/structure","https://web.dev/articles/vitals","https://news.ycombinator.com/item?id=49058547","https://qaskills.sh/blog/claude-code-screenshot-frontend-verification-mcp","https://betterstack.com/community/guides/ai/design-md-ai/","https://tailwindcss.com/docs/theme","https://evilmartians.com/chronicles/ai-makes-design-system-guardrails-mandatory-this-framework-delivers-them","https://tianpan.co/blog/2026/07/02/your-design-system-needs-to-be-a-compiler","https://www.buildmvpfast.com/blog/design-md-file-ai-coding-agents-brand-consistency-2026","https://github.com/shadcn-ui/ui","https://github.com/samber/cc-skills"}
for u in SKIP: FETCH_LEGACY.pop(u, None); EXTRA.pop(u, None)
for u in EXTRA: add(u, "recon")

def sid(u):
    s = re.sub(r"^https?://(www\.)?", "", u).lower()
    s = re.sub(r"github\.com/pbakaus/impeccable/blob/main/skill/reference/(\w+)\.md", r"impeccable-\1", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return "src_" + s[:60].strip("-")
prev = {}
if os.path.exists(OUT): prev = {s["url"]: s for s in json.load(open(OUT))["sources"]}
out = []
for u in sorted(found):
    fetch_url, pub, kind, dfrom = None, None, "unknown", []
    do_fetch = False
    if u in FETCH_LEGACY: fetch_url, pub, kind, dfrom = FETCH_LEGACY[u]; do_fetch = True
    elif u in EXTRA: pub, kind, do_fetch = EXTRA[u], "primary", True; fetch_url = FETCH_RAW_EXTRA.get(u)
    else: pub = re.sub(r"^https?://(www\.)?([^/]+).*", r"\2", u); kind = "derivative"
    row = {"id": sid(u), "url": u, "fetch_url": fetch_url, "publisher": pub, "kind": kind,
           "derives_from": dfrom, "license": "unknown", "found_in": sorted(found[u]), "fetch": do_fetch,
           "fetch_status": "skipped: recon cap (~40 fetches per first pass)" if not do_fetch else "pending",
           "retrieved_at": None, "content_hash": None, "bytes": None}
    if u in prev:  # keep results & manual lineage
        for k in ("fetch_status","retrieved_at","content_hash","bytes","derives_from","kind","license","lineage_note"):
            if k in prev[u]: row[k] = prev[u][k]
        if not do_fetch: row["fetch_status"] = "skipped: recon cap (~40 fetches per first pass)"
    out.append(row)
COOK = sid("https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics")
ANT = sid("https://github.com/anthropics/skills/tree/main/skills/frontend-design")
IMPR = sid("https://github.com/pbakaus/impeccable")
TASTE = sid("https://github.com/Leonxlnx/taste-skill")
SAMBER, JCJ = "src_samber-frontend-design-deslop", "src_jcarterjohnson-vibecoded-design-tells"
LIN = {  # id -> (derives_from, note). Evidence = text of the fetched page (see reports/recon.md)
 ANT: ([COOK], "Same Anthropic prompt (frontend_aesthetics) as the cookbook; direction of derivation unverified, treated as one root"),
 sid("https://claude.com/blog/improving-frontend-design-through-skills"): ([COOK], "Anthropic blog describing the same guidance; treated as one root with the cookbook"),
 IMPR: ([ANT], "Impeccable README: Anthropic's frontend-design 'was the first widely-used design skill for Claude. Impeccable started from there.'"),
 sid("https://github.com/OneRedOak/claude-code-workflows"): ([], ""),
 sid("https://aiagentskills.net/skill/samber-cc-skills-frontend-design-deslop"): ([SAMBER], "Directory listing mirroring samber's skill; the skill repo itself was not fetched"),
 sid("https://dynamicworkflow.run/workflows/oneredoak-claude-code-workflows-design-review"): ([sid("https://github.com/OneRedOak/claude-code-workflows")], "Listing page links to github.com/oneredoak/claude-code-workflows"),
 sid("https://novitckii.com/resources/claude-design-skills/"): ([ANT, IMPR, TASTE], "Roundup listing frontend-design, Impeccable, Taste-Skill (names + install commands)"),
 sid("https://www.chaseai.io/blog/impeccable-4-claude-code-design-skill"): ([IMPR], "Blog about Impeccable 4.0 (45 mentions of Impeccable)"),
 sid("https://www.claudecodehq.com/playbooks/unslop-ui"): ([JCJ], "Playbook cites github.com/JCarterJohnson/vibecoded-design-tells as the source repo for its automated check; partial lineage, repo not fetched"),
 sid("https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"): ([sid("https://www.w3.org/TR/WCAG22/")], "Understanding document companion to the WCAG 2.2 Recommendation; same lineage"),
 sid("https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html"): ([sid("https://www.w3.org/TR/WCAG22/")], "Understanding document companion to the WCAG 2.2 Recommendation; same lineage"),
 sid("https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html"): ([sid("https://www.w3.org/TR/WCAG22/")], "Understanding document companion to the WCAG 2.2 Recommendation; same lineage"),
 sid("https://dequeuniversity.com/rules/axe/4.8/target-size"): ([sid("https://www.w3.org/TR/WCAG22/")], "Deque rule page implements WCAG 2.2 SC 2.5.8 (page lists Guidelines: WCAG 2.2 (AA)); treated as derived from the W3C text"),
 sid("https://www.theadpharm.com/insights/claude-design-without-the-ai-slop-look"): ([COOK, sid("https://github.com/google-labs-code/design.md")], "Article discusses Anthropic's cookbook system prompt and DESIGN.md"),
}
for r in out:
    if r["id"] in LIN: r["derives_from"], r["lineage_note"] = LIN[r["id"]]
    if r["id"].startswith("src_impeccable-"): r["derives_from"], r["lineage_note"] = [IMPR], "Command reference inside the Impeccable repo"
    if r["kind"] == "derivative" and not r["derives_from"]: r["lineage_note"] = r.get("lineage_note") or "lineage unknown: page not fetched"
out += [
 {"id": SAMBER, "url": "https://github.com/samber/cc-skills", "fetch_url": None, "publisher": "samber", "kind": "primary", "derives_from": [],
  "license": "unknown", "found_in": ["recon"], "fetch": False, "fetch_status": "skipped: not fetched (referenced by aiagentskills.net listing)", "retrieved_at": None, "content_hash": None, "bytes": None, "lineage_note": "Placeholder root for the samber skill; never fetched, so no claim may be verified against it"},
 {"id": JCJ, "url": "https://github.com/JCarterJohnson/vibecoded-design-tells", "fetch_url": None, "publisher": "JCarterJohnson", "kind": "primary", "derives_from": [],
  "license": "unknown", "found_in": ["recon"], "fetch": False, "fetch_status": "skipped: not fetched (cited by the Unslop UI playbook)", "retrieved_at": None, "content_hash": None, "bytes": None, "lineage_note": "Placeholder root; never fetched"}]
json.dump({"sources": out}, open(OUT, "w"), indent=1, sort_keys=True)
print(len(out), "sources;", sum(s["fetch"] for s in out), "to fetch")
