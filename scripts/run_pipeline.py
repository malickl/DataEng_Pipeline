# scripts/run_pipeline.py
import subprocess, sys, pathlib   # ← ajoute pathlib ici

BASE = pathlib.Path(__file__).parent           # dossier scripts/
STEPS = ["extract.py", "load.py", "transform.py"]

for step in STEPS:
    script = BASE / step
    print(f"\n=== {step} ===")
    result = subprocess.run([sys.executable, str(script)])
    if result.returncode != 0:
        raise SystemExit(f"❌  Step {step} failed")

print("\n🎉  Pipeline ELT terminé sans erreur")

