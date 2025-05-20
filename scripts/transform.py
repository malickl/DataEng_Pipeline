import psycopg, os, dotenv

dotenv.load_dotenv()          # charge .env à la racine du projet

conninfo = (
    f"host={os.getenv('PGHOST', 'localhost')} "
    f"port={os.getenv('PGPORT', '5432')} "
    f"dbname={os.getenv('PGDATABASE', 'elt_proj')} "
    f"user={os.getenv('PGUSER', os.getenv('USER'))} "
    f"password={os.getenv('PGPASSWORD', '')}"
)

INSERT_SQL = """
INSERT INTO core.services_bancaires (
    annee, pays, tranche_age, type_operation,
    nombre_utilisateurs, volume_transactions, valeur_transactions,
    taux_penetration_fintechs, service_fintech_populaire,
    bancarisation_traditionnelle, acces_internet_smartphone,
    revenu_moyen, frein_adoption
)
SELECT
    annee, pays, tranche_age, type_operation,
    nombre_utilisateurs, volume_transactions, valeur_transactions,
    taux_penetration_fintechs, service_fintech_populaire,
    bancarisation_traditionnelle, acces_internet_smartphone,
    revenu_moyen, frein_adoption
FROM stg.services_bancaires
ON CONFLICT (annee, pays, tranche_age, type_operation) DO NOTHING;
"""

with psycopg.connect(conninfo) as conn, conn.cursor() as cur:
    transform_sql = open('sql/02_transform.sql').read()
    cur.execute(transform_sql)
print("✅  Transform terminé")
