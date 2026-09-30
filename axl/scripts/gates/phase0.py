import subprocess, os, sys
root = subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip()
need = ["spec","data","scripts/gates","tools","receipts","site","skills","reports"]
miss = [d for d in need if not os.path.isdir(f"{root}/axl/{d}")]
miss += [f for f in ["DECISIONS.md","STATE.json"] if not os.path.isfile(f"{root}/axl/{f}")]
diff = subprocess.check_output(["git","diff","--stat","origin/main","--","legacy","best-practices"],text=True,cwd=root).strip()
if miss or diff:
    print("FAIL", miss, diff); sys.exit(1)
print("PHASE 0 Setup: PASS — tree exists; legacy/ and best-practices/ unchanged")
