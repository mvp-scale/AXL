# Deploying the AXL site (GCP, Firebase Hosting)

Nothing here runs from a build session. Files are written; you run them.

## What gets published
`axl/site/index.html`: one self-contained file (styles, script, data, demo pages and close-up images inline; no runtime network calls). Receipts stay in the repository.

## One-time setup
```bash
export GCP_PROJECT=<your-project-id>
gcloud config set project $GCP_PROJECT
gcloud services enable cloudbuild.googleapis.com firebasehosting.googleapis.com cloudscheduler.googleapis.com
firebase projects:addfirebase $GCP_PROJECT          # or add Firebase in the console
```
Roles for the Cloud Build service account (`<project-number>@cloudbuild.gserviceaccount.com`): `roles/firebasehosting.admin` (deploy), `roles/logging.logWriter`.

## Deploy
```bash
gcloud builds submit --config axl/cloudbuild.yaml --substitutions=_DEPLOY=1 .
curl -I https://$GCP_PROJECT.web.app/        # expect HTTP/2 200
```
Without `_DEPLOY=1` the build runs every gate and stops before publishing.
Local check of the same files: `cd axl/site && python3 -m http.server 8000`.

## Nightly source re-check
`axl/cloudbuild.nightly.yaml` re-fetches every source, flags a changed hash or a dead link, and lints the skills. Schedule it:
```bash
gcloud builds triggers create manual --name=axl-nightly --build-config=axl/cloudbuild.nightly.yaml \
  --repo=<owner>/AXL --repo-type=GITHUB --branch=<branch>
gcloud scheduler jobs create http axl-nightly --schedule="0 3 * * *" --uri="https://cloudbuild.googleapis.com/v1/projects/$GCP_PROJECT/triggers/axl-nightly:run" \
  --http-method=POST --oauth-service-account-email=<scheduler-sa>@$GCP_PROJECT.iam.gserviceaccount.com --message-body='{"branchName":"<branch>"}'
```
The scheduler service account needs `roles/cloudbuild.builds.editor`. A red nightly build is the alert: a `FLAG` line names the changed or dead source. `refetch_sources.py --update` accepts a new hash after a human has read the change.

## Alternative hosting (not used)
Cloud Storage bucket behind an external HTTPS load balancer with Cloud CDN. More moving parts (bucket, backend bucket, URL map, certificate, forwarding rule), so Firebase Hosting was chosen. Recorded in `DECISIONS.md`.

## Phase 2 design: running tools live in the browser (out of scope for v1)
v1 answers "can we run it?" with receipts: each carries the exact command to re-run locally, and `rerun_receipts.py` proves they reproduce.
Phase 2 would add a "Run it" button that sends the page URL or an uploaded HTML file to a Cloud Run service. That service runs the same Playwright image used in `cloudbuild.yaml` in a sandbox (no network except the target, CPU and time limits, one request per container, non-root), executes the pinned runners in `axl/tools/runners/`, and returns the same `{rule_id, result, evidence, location}` findings. Results would be shown next to the stored receipt and cached by input hash. Needs: request authentication, an allow-list for target hosts, abuse limits, and a review of the sandbox before any public URL is accepted.
