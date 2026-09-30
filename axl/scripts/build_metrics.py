#!/usr/bin/env python3
"""Phase 6: compute reports/metrics.json and metrics.md from data/*.json. No number is typed by hand."""
import json, os, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = f"{ROOT}/axl/data"
C = json.load(open(f"{D}/claims.json"))["claims"]; V = json.load(open(f"{D}/verbs.json"))["verbs"]
L = json.load(open(f"{D}/lineage.json")); S = json.load(open(f"{D}/sources.json"))["sources"]
pub = [c for c in C if c["origin"] == "public"]; priv = [c for c in C if c["origin"] == "private-kit"]
cnt = lambda xs, k: dict(sorted(collections.Counter(x[k] for x in xs).items()))
legacy = [c for c in pub if c["legacy_id"] and c["tier"] != "process"]   # UI guidance being audited: excludes AXL's own definitions, seed standards and process steps (not UI properties)
def share(a, b): return round(a / b, 4) if b else 0.0
n = len(legacy)
system = sum(c["tier"] in ("enforced", "measurable") for c in legacy)
enforced = sum(c["tier"] == "enforced" for c in legacy)
M = {"claims_total": len(C), "public_claims": len(pub), "private_kit_excluded": len(priv),
     "by_tier_public": cnt(pub, "tier"), "by_status_public": cnt(pub, "status"), "by_origin": cnt(C, "origin"),
     "double_sourced_public": sum(c["status"] == "verified" for c in pub), "double_sourced_share_public": share(sum(c["status"] == "verified" for c in pub), len(pub)),
     "enforced_public": sum(c["tier"] == "enforced" for c in pub), "enforced_share_public": share(sum(c["tier"] == "enforced" for c in pub), len(pub)),
     "guidance_audited": {"claims": n, "system_share": share(system, n), "enforced_share": share(enforced, n), "luck_share": share(n - system, n),
                          "by_tier": cnt(legacy, "tier"), "definition": "system = tier enforced or measurable; luck = subjective (no measurable definition); process steps are not scored as UI"},
     "rebrand_clusters": len(L["rebrand_clusters"]), "sources_in_largest_cluster": max((len(v) for v in L["rebrand_clusters"].values()), default=0),
     "sources_total": len(S), "sources_fetched": sum(s["fetch_status"] == "ok" for s in S),
     "verbs_total": len(V), "verbs_by_resolution": cnt(V, "resolution"), "enforced_discriminating": sum(1 for c in pub if c["tier"] == "enforced" and c.get("discriminates")),
     "receipts": len(os.listdir(f"{ROOT}/axl/receipts/runs"))}
json.dump(M, open(f"{ROOT}/axl/reports/metrics.json", "w"), indent=1)
g = M["guidance_audited"]; pc = lambda x: f"{x*100:.1f}%"
open(f"{ROOT}/axl/reports/metrics.md", "w").write(f"""# Metrics (computed from data/claims.json by scripts/build_metrics.py)

## Headline: system vs luck
Of **{g['claims']}** UI/UX guidance statements audited from public sources (process/workflow steps excluded), **{pc(g['system_share'])}** have a measurable definition and **{pc(g['enforced_share'])}** are enforced by a tool with a re-runnable receipt.
**{pc(g['luck_share'])}** have no measurable definition. That is the share that depends on an agent's judgment.

| Tier (audited guidance) | Claims |
|---|---|
""" + "\n".join(f"| {k} | {v} |" for k, v in g["by_tier"].items()) + f"""

## All public claims ({M['public_claims']}, incl. AXL definitions and standards)
- By tier: {M['by_tier_public']}
- By status: {M['by_status_public']}
- Double-sourced (verified, >= 2 independent roots): **{M['double_sourced_public']}** ({pc(M['double_sourced_share_public'])})
- Enforced: **{M['enforced_public']}** ({pc(M['enforced_share_public'])}); {M['enforced_discriminating']} fail on the before page and pass on the after page

## Sources and lineage
- {M['sources_total']} sources registered, {M['sources_fetched']} fetched.
- Rebrand clusters (roots shared by two or more sources): **{M['rebrand_clusters']}**; the largest has {M['sources_in_largest_cluster']} sources.
- Private-kit claims excluded from the public build: **{M['private_kit_excluded']}**.

## Verb dictionary
- {M['verbs_total']} verbs: {M['verbs_by_resolution']}
- Receipts on disk: {M['receipts']}
""")
print(json.dumps({k: M[k] for k in ("guidance_audited",)}, indent=0)[:400])
