import os, sys, json, yaml
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
errs = []
for f in ("cloudbuild.yaml", "cloudbuild.nightly.yaml"):
    d = yaml.safe_load(open(f"{ROOT}/axl/{f}"))
    ids = [s["id"] for s in d["steps"]]
    if len(ids) != len(set(ids)): errs.append((f, "duplicate step id"))
    for s in d["steps"]:
        for w in s.get("waitFor", []):
            if w not in ids: errs.append((f, s["id"], "waitFor unknown", w))
fb = json.load(open(f"{ROOT}/axl/firebase.json"))
if fb["hosting"]["public"] != "axl/site" or not os.path.isdir(f"{ROOT}/{fb['hosting']['public']}"): errs.append(("firebase public dir",))
dep = open(f"{ROOT}/axl/DEPLOY.md").read()
for k in ("Phase 2 design", "cloudbuild.googleapis.com", "Cloud Scheduler", "curl -I"):
    if k not in dep and k.lower() not in dep.lower(): errs.append(("DEPLOY.md lacks", k))
deployed = os.environ.get("DEPLOY") == "1" and os.environ.get("GCP_PROJECT")
if errs: print("PHASE 9 GCP: FAIL", errs); sys.exit(1)
print("PHASE 9 GCP: PASS — cloudbuild.yaml, cloudbuild.nightly.yaml and firebase.json parse; " + ("deploy requested" if deployed else "not deployed (DEPLOY=1 and GCP_PROJECT not set)"))
