Services Bancaires -- Mini-pipeline ELT
======================================

> **Objectif :** importer régulièrement un CSV (« services_bancaires ») dans PostgreSQL, le nettoyer / dédoublonner et le rendre prêt pour l'analyse.

* * * * *

1 Structure du dépôt
--------------------


`services-bancaires-elt/
│
├─ data/
│   └─ raw/                 # CSV copiés par extract.py
│
├─ scripts/
│   ├─ extract.py           # déplace/télécharge le CSV → data/raw/
│   ├─ load.py              # COPY vers stg.services_bancaires
│   ├─ transform.py         # INSERT ... SELECT vers core.services_bancaires
│   └─ run_pipeline.py      # orchestre E → L → T
│
├─ sql/
│   ├─ 01_create_tables.sql # schémas + tables
│   └─ 02_transform.sql     # requête de nettoyage/dédoublonnage
│
├─ .env                     # variables PGHOST/PGPORT/...
├─ requirements.txt         # psycopg, python-dotenv (et pandas si besoin)
└─ README.md                # (ce fichier)`

* * * * *

2 Prérequis
-----------

-   PostgreSQL ≥ 14 installé en local (port 5432)

-   Python 3.9 +

-   Un environnement virtuel :


`python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt`

-   Fichier **.env** à la racine :


`PGHOST=localhost
PGPORT=5432
PGDATABASE=elt_proj
PGUSER=$USER           # ou un autre rôle
PGPASSWORD=...       # si besoin`

* * * * *

3 Initialisation des tables (une seule fois)
--------------------------------------------


`psql -d elt_proj -f sql/01_create_tables.sql`

* * * * *

4 Lancer la pipeline manuellement
---------------------------------


`source .venv/bin/activate
python scripts/run_pipeline.py      # extract → load → transform`


### Vérification rapide


`SELECT COUNT(*) FROM stg.services_bancaires;
SELECT COUNT(*) FROM core.services_bancaires;`

* * * * *

5 Licence
----------

*MIT* --- utilisation libre.
