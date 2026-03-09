from database.db import get_connection


class LogService:

    @staticmethod
    def log(niveau, utilisateur_id, message):

        connection = get_connection("aniservice_home")

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO logs_systeme (niveau, message, utilisateur_id)
            VALUES (%s,%s,%s)
        """, (niveau, message, utilisateur_id))

        connection.commit()

        cursor.close()
        connection.close()