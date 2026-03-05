import mysql.connector
from database.db import DB_CONFIG


class LogService:

    @staticmethod
    def log(niveau, utilisateur_id, message):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO logs_systeme (niveau, message, utilisateur_id)
            VALUES (%s, %s, %s)
            """,
            (niveau, message, utilisateur_id)
        )

        connection.commit()

        cursor.close()
        connection.close()