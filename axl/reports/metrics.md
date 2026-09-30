# Metrics (computed from data/claims.json by scripts/build_metrics.py)

## Headline: system vs luck
Of **332** UI/UX guidance statements audited from public sources (process/workflow steps excluded), **2.1%** have a measurable definition and **1.8%** are enforced by a tool with a re-runnable receipt.
**97.9%** have no measurable definition. That is the share that depends on an agent's judgment.

| Tier (audited guidance) | Claims |
|---|---|
| enforced | 6 |
| measurable | 1 |
| subjective | 325 |

## All public claims (377, incl. AXL definitions and standards)
- By tier: {'enforced': 20, 'measurable': 1, 'process': 31, 'subjective': 325}
- By status: {'single-source': 250, 'unverified': 125, 'verified': 2}
- Double-sourced (verified, >= 2 independent roots): **2** (0.5%)
- Enforced: **20** (5.3%); 15 fail on the before page and pass on the after page

## Sources and lineage
- 90 sources registered, 52 fetched.
- Rebrand clusters (roots shared by two or more sources): **5**; the largest has 23 sources.
- Private-kit claims excluded from the public build: **107**.

## Verb dictionary
- 34 verbs: {'tool-backed': 6, 'undefined': 28}
- Receipts on disk: 25
