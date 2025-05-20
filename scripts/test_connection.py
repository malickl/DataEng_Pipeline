import psycopg, os, dotenv

dotenv.load_dotenv()                      # charge le fichier .env
conninfo = (
    f"host={os.getenv('PGHOST')} "
    f"port={os.getenv('PGPORT')} "
    f"dbname={os.getenv('PGDATABASE')} "
    f"user={os.getenv('PGUSER')}"
)

with psycopg.connect(conninfo) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM stg.services_bancaires;")
        print("Lignes en staging :", cur.fetchone()[0])
