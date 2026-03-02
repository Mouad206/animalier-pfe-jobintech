import mysql.connector
from mysql.connector import Error
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "aniservice_home"),
}


def get_connection(database=None):
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

        if connection.is_connected():
            print("Connexion réussie à MySQL")
            return connection

    except Error as e:
        print(f"Erreur de connexion : {e}")
        return None


def test_connection():
    """
    Test simple de requête SQL brute.
    """
    connection = get_connection()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Base connectée :", record)

        except Error as e:
            print(f"Erreur SQL : {e}")

        finally:
            cursor.close()
            connection.close()
            print("Connexion fermée.")


if __name__ == "__main__":
    test_connection()