from database.db import get_connection
from mysql.connector import Error


class HistoriqueService:

    @staticmethod
    def ajouter_action(utilisateur_id, action):
        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO historique_action (utilisateur_id, action)
                VALUES (%s, %s)
            """, (utilisateur_id, action))

            connection.commit()

        except Error as e:
            print("Erreur historique:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()