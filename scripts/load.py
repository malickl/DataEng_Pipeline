# scripts/load.py  – version psycopg 3

import os, pathlib, psycopg, dotenv, sys, shutil
dotenv.load_dotenv()

# 1) connexion
CONNINFO = (
    f"host={os.getenv('PGHOST', 'localhost')} "
    f"port={os.getenv('PGPORT', '5432')} "
    f"dbname={os.getenv('PGDATABASE', 'elt_proj')} "
    f"user={os.getenv('PGUSER', os.getenv('USER'))} "
    f"password={os.getenv('PGPASSWORD', '')}"
)

# 2) CSV le plus récent
RAW_DIR = pathlib.Path("data/raw")
try:
    csv_path = max(RAW_DIR.glob("services_bancaires.csv"),
                   key=lambda p: p.stat().st_mtime)
except ValueError:
    sys.exit(f"❌  Aucun fichier services_bancaires.csv trouvé dans {RAW_DIR}")

print("CSV détecté :", csv_path.name)

# 3) charge le fichier dans stg.services_bancaires
with psycopg.connect(CONNINFO) as conn, conn.cursor() as cur:
    cur.execute("TRUNCATE stg.services_bancaires")       # optionnel
    with open(csv_path, "rb") as f:
        # ouvre le canal COPY
        with cur.copy(
            "COPY stg.services_bancaires "
            "FROM STDIN WITH (FORMAT csv, HEADER TRUE, DELIMITER ',', QUOTE '\"')"
        ) as copy:
            shutil.copyfileobj(f, copy)                  # envoie le fichier

print("✅  Load terminé :", csv_path.name)

