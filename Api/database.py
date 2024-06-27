# database.py
# Configuration de la base de données et création de la session de base de données.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(dotenv_path='BDD/credentials.env')

DB_URL = os.getenv("DB_URL").replace("https://", "").replace("/", "")
PWD_DB = os.getenv("PWD_DB")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_URL}:{PWD_DB}@db.supabase.co/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
