import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from databse.base import Base

# Charger .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# URL sans base (pour créer la base)
SERVER_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

# URL avec base
DATABASE_URL = f"{SERVER_DATABASE_URL}/{DB_NAME}"

# Engine principal
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)


def init_db():
    # 1️⃣ Créer la base si elle n'existe pas
    server_engine = create_engine(SERVER_DATABASE_URL)

    with server_engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
        print(f"✅ Base '{DB_NAME}' vérifiée/créée.")

    # 2️⃣ Créer les tables depuis les modèles
    import models  # important pour charger les modèles
    Base.metadata.create_all(bind=engine)

    print("Base de donnée créées avec succès.")