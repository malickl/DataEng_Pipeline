from pathlib import Path
import shutil
import datetime as dt

SRC = Path("/Users/mahassadiadoumalickjean/Desktop/csv_extract/services_bancaires.csv")

# Dossier du projet où le pipeline va chercher les CSV
DST = Path("data/raw") / SRC.name            # garde le même nom

DST.parent.mkdir(parents=True, exist_ok=True)  # crée data/raw si besoin
shutil.copy2(SRC, DST)
print("✅  Fichier copié →", DST)
