import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(dotenv_path='BDD/credentials.env')

DB_URL = os.getenv("DB_URL").replace("https://", "").replace("/", "")
PWD_DB = os.getenv("PWD_DB")

print(f"DB_URL: {DB_URL}")
print(f"PWD_DB: {PWD_DB}")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_URL}:{PWD_DB}@db.supabase.co/postgres"

def test_connection():
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        # Exécuter une requête simple pour tester la connexion
        result = db.execute(text("SELECT 1"))
        print("Connexion à la base de données réussie!")
        db.close()
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")

if __name__ == "__main__":
    test_connection()
