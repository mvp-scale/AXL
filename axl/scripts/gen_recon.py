#!/usr/bin/env python3
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
S = json.load(open(f"{ROOT}/axl/data/sources.json"))["sources"]; L = json.load(open(f"{ROOT}/axl/data/lineage.json"))
ok = [s for s in S if s["fetch_status"] == "ok"]
bad = [s for s in S if s["fetch"] and s["fetch_status"] != "ok"]
skip = [s for s in S if not s["fetch"]]
new = [s for s in ok if "recon" in s["found_in"] and s["found_in"] == ["recon"]]
o = ["# Recon report", "",
 f"Registry: {len(S)} sources ({len(ok)} fetched ok, {len(bad)} fetch failures, {len(skip)} registered but not fetched).",
 f"Fetched on the first pass, capped at about 40 by design; {len(ok)} fetched because 18 Impeccable command pages were required and {len(new)} new primaries were added.", "",
 "## Dead links / fetch failures", ""]
o += [f"- {s['url']} — {s['fetch_status']}" for s in bad] or ["- None among fetched sources (every fetch returned HTTP 200)."]
o += ["", "Not fetched, so liveness is unknown (not counted as dead):", ""] + [f"- {s['url']} — {s['fetch_status']}" for s in skip]
o += ["", "## New primaries found beyond the legacy set", ""] + [f"- {s['url']} ({s['publisher']}, licence: {s['license']})" for s in new]
o += ["", "## Search queries used (WebSearch, standard mode)", "",
 "- `agent skill design system linter AI coding agents UI quality github` → UI Craft (added); skill linters (out of scope, not UI)",
 "- `Claude Code frontend design skill anti AI slop UI checklist repository` → confirmed Impeccable, Taste-Skill, Hallmark (already registered); Open Design listed only by a directory page (not fetched)",
 "- `WCAG 2.2 target size focus visible reduced motion tooling axe-core rules reference` → Deque axe target-size rule (added)",
 "- Other tools (WCAG, axe-core, Lighthouse, Playwright, Stylelint, APCA, better-tailwindcss, MDN, NN/g) were added from prior knowledge of the ecosystem; each was fetched and returned 200.", "",
 "## Lineage (`derives_from`)", ""]
for s in S:
    if s["derives_from"]: o.append(f"- `{s['id']}` → {', '.join('`'+p+'`' for p in s['derives_from'])} — {s.get('lineage_note','')}")
o += ["", "Rebrand clusters (sources sharing a root):", ""]
for r, m in L["rebrand_clusters"].items(): o.append(f"- root `{r}`: {len(m)} sources")
o += ["", "Unfetched derivatives (lineage unknown, each treated as its own root; nothing is verified against them):", ""]
o += [f"- {s['url']}" for s in S if s["kind"] == "derivative" and not s["fetch"]]
o += ["", "## Notes", "",
 "- Impeccable's README says it *started from* Anthropic's frontend-design skill, so all Impeccable sources share a root with it. Anthropic's blog, cookbook and skill are treated as one root (same prompt; direction unverified). This is conservative: it makes double-sourcing harder, not easier.",
 "- Licences are auto-detected from LICENSE files on raw.githubusercontent.com; non-GitHub pages are `unknown`. `anthropics/skills` has no root LICENSE (skills may carry their own); left `unknown`.",
 "- The GitHub API was not reachable for these repositories in this session, so licences and stars were not read from it."]
open(f"{ROOT}/axl/reports/recon.md", "w").write("\n".join(o) + "\n")
