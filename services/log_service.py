import mysql.connector
from database.db import DB_CONFIG


class LogService:

    @staticmethod
    def log(utilisateur_id, niveau, message):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO logs_systeme (id, niveau, message) VALUES (%s, %s, %s)",
            (utilisateur_id, niveau, message)
        )

        connection.commit()
        cursor.close()
        connection.close()