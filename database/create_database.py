import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    print("Base de données créée ✅")

except Error as e:
    print("Erreur :", e)

finally:
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()