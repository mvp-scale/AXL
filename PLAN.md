# AXL — Build Plan

> **AXL** — A machine-readable meta-language for describing, evaluating, and correcting digital experiences.

This file is the complete brief for an autonomous run (Claude Sonnet on Cloud Run, launched from the
Cloud command line). Read all of it, then execute Section 5 phase by phase. Do not ask questions.
Where this plan is silent, pick the simplest option, record the choice in `axl/DECISIONS.md`, and continue.

---

## 1. Problem

People steer AI agents on UI/UX with subjective verbs: *polish, bolder, quieter, delight, clarify,
elevate*. Every tool defines these differently, or not at all. Skills that rely on the model's
judgment are not a system; they are luck. Vendors also keep rebranding the same guidance.

AXL removes the luck. For every piece of UI/UX guidance it answers:

1. What exactly does it change, in measurable terms (a token, a property, a threshold)?
2. Can a tool check or apply it and return pass/fail? Is there a command we can run?
3. Who says so, and is that a real independent second source or a rebrand of the first?

Anything that cannot be answered stays in the catalog, honestly labelled **subjective**, and cannot
ship as a skill.

## 2. Inputs and hard rules

| Path | Role | Rule |
|---|---|---|
| `legacy/` | Old Design Language Lab (`index.html` holds a 41-group / ~470-prescription catalog and a Northstar demo app) | **Read-only. Never edit, move or delete.** |
| `best-practices/` | Research kit, playbooks, `SOURCES.md` | **Read-only.** Use as leads, not as proof. |
| `axl/` | Your output | Create it. All new work goes here. |

- Work on branch `axl-build`. If the session forces a different branch name, use that one and log it
  in `DECISIONS.md`. Commit **and push** at the end of every phase. Never touch `main`.
- **Open-source hygiene (this repo is public on GitHub, `mvp-scale/AXL`).** Do not commit full copies
  of third-party pages: `axl/receipts/sources/` is gitignored, and only URL, content hash, licence,
  and short attributed quotes (≤ 40 words each) are committed. Record each source's licence in
  `sources.json` (`license` field, `unknown` if not stated). Do not add a `LICENSE` file; the owner
  chooses it. Note in `SUMMARY.md` that it is still needed.
- **Never fabricate.** Every quote must be copied verbatim from a page you actually fetched in this
  run. If you cannot fetch a source, mark the claim `unverified`. Never mark it `verified`.
- No secrets in files. No deploy unless `DEPLOY=1` and `GCP_PROJECT` are set (Phase 9).
- Use Context7 (or the official docs) for any library or CLI syntax. Versions changed in 2025-26.
- **Gauntlet leakage:** the legacy groups `g0`–`g11` come from the owner's private "Gauntlet" system
  (terms like GauntletSkin, ClimbMountain, Worst Day HUD, `packages/gauntlet-ui`). They have no public
  source. Tag them `origin: private-kit` and exclude them from the public build. Keep their
  count and a short reason in `axl/reports/excluded.md`. A principle inside them may re-enter only if
  it independently verifies against a public source, and then it is cited to that source, not the kit.

## 3. Core concepts

### 3.1 Tiers (every claim gets exactly one)

| Tier | Meaning | Test |
|---|---|---|
| `enforced` | A tool or script checks or applies it and returns pass/fail | A runnable command exists, and you ran it |
| `measurable` | A concrete delta: property, before, after, unit or threshold | Can be written as `{selector, property, before, after}` or a numeric rule |
| `subjective` | A verb or advice with no measurable definition | Two agents could reasonably do opposite things |
| `process` | A workflow step (ask questions, review, iterate) | Not a UI property; kept but not scored as UI |

Decide the tier from the claim text alone. Do not upgrade a claim because the legacy page has a
live CSS example for it: the legacy `mapAction()` is a regex guess, so treat its mapping as a hint only.

### 3.2 Sources and independence

- A **source** has an id, URL, publisher, `retrieved_at`, and `kind`: `primary` (the author's own
  repo or docs) or `derivative` (a summary, roundup or rebrand of someone else).
- Every derivative lists `derives_from: [source_id]`. Build the lineage graph from this.
- **Independence rule:** a claim is `double-sourced` only if it is supported by at least two sources
  whose lineage roots differ. Two derivatives of the same root count as one.
- Claim status: `verified` (quote fetched and matches, and ≥ 2 independent roots), `single-source`
  (quote fetched, one root), `unverified` (could not fetch or match), `rejected` (source says
  otherwise, or the claim is wrong; keep it with the reason).

### 3.3 Verb dictionary

Every emotional or vague verb resolves to one of: a set of measurable deltas (with sources), a
tool-backed check, or `undefined`. The dictionary is the centerpiece; it is why the page exists.

## 4. AXL v0.1 language (keep it small)

Three operations, one JSON document per experience. Deliver as JSON Schema files in
`axl/spec/` plus a short `SPEC.md` with two worked examples (one web, one mobile).

- **describe**: surface (`web | mobile | platform | saas`), tokens (color, type, space, motion),
  components, states (`ready, loading, empty, error, success`), viewports.
- **evaluate**: a list of rules. Each rule is `{id, tier, check, pass_criteria, tool?, command?, claim_ids[]}`
  and produces a finding `{rule_id, pass|fail|na, evidence, location}`.
- **correct**: patch operations `{op: set|add|remove, target, property, value, reason, claim_id}`
  that a tool can apply mechanically. If a fix needs judgment, it is not a `correct`; it is a note.

Claim record (`axl/data/claims.json`, validated by `axl/spec/claim.schema.json`):

```json
{
  "id": "clm_0001",
  "verb": "polish",
  "text": "Fix optical as well as mathematical alignment.",
  "quote": "verbatim from the fetched page",
  "source_id": "src_impeccable",
  "source_url": "https://…",
  "retrieved_at": "2026-…",
  "quote_verified": true,
  "origin": "public | private-kit",
  "tier": "enforced | measurable | subjective | process",
  "surface": ["web", "mobile", "platform", "saas"],
  "delta": { "selector": "h1", "property": "font-size", "before": "24px", "after": "36px" },
  "enforcement": { "tool": "axe-core", "command": "…", "pass_criteria": "…" },
  "independent_roots": ["src_a", "src_b"],
  "status": "verified | single-source | unverified | rejected",
  "notes": ""
}
```

## 5. Execution loop

**Protocol.** Keep `axl/STATE.json` = `{phase, attempt, done:[…], blocked:[…]}`. On start, read it and
resume. For each phase: do the work, run that phase's gate (a script in `axl/scripts/gates/`), and on
failure fix and retry up to 3 times. After 3 failures write `axl/BLOCKED.md` (what, why, what you
tried) and move to the next phase that does not depend on it. Commit after every passing gate.
Print one status line per phase: `PHASE n <name>: PASS|FAIL|BLOCKED — <one-line evidence>`.

### Phase 0 — Setup
Create branch `axl-build` and the tree: `axl/{spec,data,scripts/gates,tools,receipts,site,skills,reports}`,
`DECISIONS.md`, `STATE.json`. **Gate:** tree exists; `legacy/` and `best-practices/` are unchanged
(`git diff --stat origin/main -- legacy best-practices` is empty).

### Phase 1 — Extract the legacy catalog
Write `scripts/extract_legacy.py` that reads `legacy/index.html`, evaluates the `const groups=[…]`
literal (parse the JS array as JSON; do not run the page) and writes `data/legacy_groups.json` with
one row per prescription. Also extract the Northstar demo template (`appTemplate`) and the `elements`
/ `effectOverrides` CSS to `data/legacy_effects.json`.
Note in `reports/legacy-findings.md`: total groups, total prescriptions, prescriptions truncated
mid-sentence, entries that are research caveats rather than prescriptions (e.g. group `g4`),
and prescriptions that map to no effect.
**Gate:** counts in the report match the file; re-running the script gives identical output.

### Phase 2 — Recon (find the real sources)
1. Build `data/sources.json` from every URL in `legacy/`, `best-practices/SOURCES.md` and
   `legacy/ATTRIBUTION.md`.
2. Fetch each. Record status, `retrieved_at`, a content hash and `kind`. Save the fetched text (or a
   trimmed excerpt) to `receipts/sources/<id>.txt` so quotes can be re-checked offline. That folder is not committed, so also write
   `scripts/refetch_sources.py` (fetch again by URL, compare the content hash, flag any page that
   changed) and run it first in any phase that reads the saved texts.
3. Determine lineage: for each derivative, find what it derives from (links, credited authors, repeated
   wording). Fill `derives_from`.
4. Search for more: skills and tools that claim to fix or judge UI/UX for agents (Impeccable,
   Anthropic `frontend-design`, shadcn skills, Hallmark, Taste-Skill, Google `design.md`, Unslop UI,
   OpenAI UI guidelines, Claw Design, the Playwright and axe ecosystems, and any others you find).
   Target ≥ 15 primary sources beyond the legacy set. Note the search queries used in `reports/recon.md`.
**Gate:** every source has a fetch result (ok or a stated failure); every derivative has a root;
`reports/recon.md` lists dead links.

### Phase 3 — Build the claim set
Turn `legacy_groups.json` plus new recon into `data/claims.json`. For each claim: find the verbatim
quote in the saved source text, set `quote_verified`, tag `origin`, choose the tier per 3.1, and
fill `delta` or `enforcement` where the tier requires it. Paraphrased legacy entries whose text you
cannot find in the source get `status: unverified`, not deleted.
**Gate:** `validate_claims.py` passes the schema; every `verified` claim has ≥ 2 distinct roots;
every `quote_verified: true` quote is found verbatim in `receipts/sources/`; no `measurable` claim
lacks a `delta`; no `enforced` claim lacks a command.

### Phase 4 — Verb dictionary
Write `data/verbs.json` covering at least: polish, distill, delight, bolder, quieter, animate,
colorize, clarify, harden, adapt, optimize, typeset, layout, onboard, critique, audit, extract, shape,
plus every verb that appears ≥ 3 times across sources. For each verb: the sources' definitions side
by side, the measurable deltas they share, where sources disagree, and a resolution
`{measurable | tool-backed | undefined}`.
**Gate:** every verb resolves to a class, and every delta points to a claim id.

### Phase 5 — Tools and receipts
Select tools that can turn claims into pass/fail. Start with: `@google/design.md lint` (if it
exists at run time), axe-core, Lighthouse, Playwright `toHaveScreenshot`, a WCAG/APCA contrast
check, `eslint-plugin-better-tailwindcss`, Stylelint. Verify each tool exists and record its version
before use; drop any you cannot install and say so.
Run each tool against the Northstar demo (before and after variants). For each run write
`receipts/runs/<id>.json`: `{tool, version, command, input_hash, exit_code, stdout_excerpt, findings, ran_at}`.
Rule: a receipt is valid only if re-running the command locally reproduces the same result.
Then set the final tier on claims from real runs: no run, no `enforced`.
**Gate:** `rerun_receipts.py` reproduces ≥ 90 % of receipts; the unreproducible ones are listed.

### Phase 6 — Metrics
Compute `reports/metrics.json` and `metrics.md`: counts by tier, by status, by origin; share of
claims that are double-sourced; share that are `enforced`; number of rebrand clusters (derivatives
sharing a root); number of `private-kit` exclusions. This headline belongs on the site: what
fraction of AI-UI guidance is a system, and what fraction is luck.
**Gate:** all numbers are computed from `claims.json`, not typed by hand.

### Phase 7 — The site
Static site in `axl/site/`, generated from `data/*.json` by `scripts/build_site.py`. No framework,
no runtime network calls, no external fonts or scripts. Split into `index.html`, `styles.css`,
`app.js`, `data/`, `demo/`.

Layout and behaviour:
- **Main stage: original vs receipt.** Two panes of the Northstar demo (states: ready, loading,
  empty, error, success; desktop and mobile). Selecting a claim applies its `delta` to the right
  pane. Each active claim shows its source, tier and status beside the pane. Tools with receipts show
  the command and result; the command is copyable.
- **Left rail:** catalog grouped by verb, filterable by tier, status, surface, source. Subjective
  claims are visibly marked "no measurable definition" and cannot be applied.
- **Side overlay: lineage map.** Nodes are sources, edges are `derives_from`, and colour shows the
  root. Selecting a claim highlights its supporting roots, so rebrands are visible as clusters.
- **Headline bar:** the Phase 6 metric (system vs luck).
- **Verb dictionary page:** the Phase 4 output as a comparison table.
- **Sources button, pinned at the bottom.** Opens a drawer for the current claim: the verbatim
  quote, source URL and date, the lineage chain, the independence count and how it was decided, and a
  "how to re-check" note. A full-table view lists all sources.
- **Export:** an AXL document containing the selected claims' `evaluate` and `correct` sections
  (the legacy export produced a loose markdown recipe; replace it).
- Professional and restrained; light and dark themes; keyboard operable; visible focus; contrast
  ≥ 4.5:1; respects `prefers-reduced-motion`; usable at 375px and 1440px. Do not use the anti-slop
  patterns from `best-practices/06-anti-slop.md` (default fonts, purple gradients, identical card grids).
**Gate:** `scripts/gates/site_check.py` builds, then runs Playwright at 375 and 1440 in both themes
with zero console errors, axe reports no serious or critical issues, every claim shown on the site
has a source, and the Sources drawer opens for every claim.

### Phase 8 — Skills hub
`axl/skills/<name>/SKILL.md` in the standard Agent Skills layout (frontmatter `name`,
`description`), each with a `scripts/` folder. **Admission rule:** a skill may include only
`enforced` or `measurable` claims. Its script does the deciding (lint, check, patch), and the
`SKILL.md` only tells the agent when to call it and how to read the result. Minimum set:
1. `axl-evaluate`: runs the enforced checks on a target and prints findings.
2. `axl-correct`: applies measurable patches from an AXL document.
3. `axl-verbs`: translates a vague request ("make it more polished") into concrete deltas via the
   verb dictionary, or replies that the verb is undefined.
4. `axl-tokens`: script that detects raw colours and off-scale spacing and aligns a stylesheet to a
   token file.
Add `skills/README.md` with the maintenance rules: each skill lists its claim ids; a nightly
re-fetch flags changed or dead sources; a skill with a claim whose status drops below `single-source`
is flagged for review; the version of every wrapped tool is pinned.
**Gate:** each skill's script runs on the demo and exits 0; `lint_skills.py` confirms no skill
references a `subjective` claim.

### Phase 9 — GCP
Write, don't run unless `DEPLOY=1` and `GCP_PROJECT` are set:
- `cloudbuild.yaml`: install tools, run Phases 5–7 gates, publish receipts and the site.
- Hosting: Firebase Hosting serving `axl/site/` (simplest static path on GCP). Record the alternative
  (Cloud Storage bucket + load balancer) in `DECISIONS.md`.
- `DEPLOY.md`: exact commands, required APIs and roles, and how the nightly source re-check is
  scheduled (Cloud Scheduler → Cloud Build).
- Live execution of tools in the browser (Cloud Run sandbox) is **out of scope for v1**. Receipts
  are the v1 answer to "can we run it": each one carries the exact command to rerun locally. Write
  the phase-2 design in `DEPLOY.md` as a short section.
**Gate:** `cloudbuild.yaml` and `firebase.json` parse; if deployed, `curl -I` on the URL returns 200.

## 6. Definition of done

- `git diff origin/main -- legacy best-practices` is empty.
- Every gate above passes, or has a `BLOCKED.md` entry with evidence.
- `reports/metrics.md` states the system-vs-luck numbers, computed.
- The site opens locally with `python -m http.server` from `axl/site/`, and every claim reaches a source.
- `axl/SUMMARY.md` (one page): what was built, headline numbers, what is blocked, what to review first.

## 7. Seed findings from the legacy page (verify, don't trust)

- ~41 groups / ~470 prescriptions; 12 groups (`g0`–`g11`) come from a private kit with a non-public source link.
- Several groups say their checklist is a paraphrase, not verified upstream (samber deslop,
  OneRedOak, Taste-Skill v1). Treat them as `unverified` until quotes are found.
- 18 Impeccable command groups (`g12`–`g29`) have per-command URLs and are the easiest to verify first.
- Effect mapping is regex over English text and can be wrong; some prescriptions are truncated
  mid-sentence; the catalog includes research caveats as prescriptions.
- Everything is in one 83-line file with the demo app as an inline string; the new build splits it.

## 8. Cloud-session notes

This plan runs in a Claude Code cloud session (`claude --cloud`). The prompt names which phases to run
on this pass; run only those, then stop and write `axl/SUMMARY.md`.

- **Budget is soft.** There is no enforced spend cap. Keep cost low: fetch each source once and save
  it; do not re-fetch or re-read large files; process claims in batches with scripts, not by reading
  every item into context; on the first pass cap recon at about 40 sources.
- **Tools:** if Playwright's Chromium is missing, try `npx playwright install chromium`; if that
  fails, mark the dependent gates BLOCKED. Do not fake receipts.
- **Nothing is deployed** from a cloud session. Phase 9 only writes files.
- The Cloud Run / API-key runner idea is dropped. Do not create one.
