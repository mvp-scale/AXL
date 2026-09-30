# Excluded from the public build: private-kit claims

- **Groups:** 12 (`g0`–`g11`), **claims:** 107 (tagged `origin: private-kit` in `data/claims.json`).
- **Reason:** they come from the owner's private "Gauntlet" research kit (`legacy/ATTRIBUTION.md#research-kit`); there is no public source URL, and some entries name private components (GauntletSkin, ClimbMountain, Worst Day HUD, `packages/gauntlet-ui`). No quote can be verified, so all are `unverified`.
- **Handling:** kept in `claims.json` only so counts are computable; the site build (Phase 7) and skills (Phase 8) must filter `origin == "public"`.
- **Re-entry:** a principle may re-enter only if it independently verifies against a public source and is then cited to that source. Not attempted in this pass.
- Counts are computed by `scripts/gates/phase3.py`.
