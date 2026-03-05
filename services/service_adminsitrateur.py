from database.db import get_connection
from mysql.connector import Error
from services.log_service import LogService


class ServiceAdministrateur:

    # ==========================
    # Voir tous les utilisateurs
    # ==========================
    @staticmethod
    def voir_clients_inscrits():

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute("""
                SELECT id, nom, prenom, email
                FROM utilisateurs
                WHERE role='CLIENT'
            """)

            return cursor.fetchall()

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    # ==========================
    # Supprimer profil
    # ==========================
    @staticmethod
    def supprimer_profil(user_id):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM utilisateurs WHERE id=%s",
                (user_id,)
            )

            connection.commit()

            LogService.log(
                "WARNING",
                f"Suppression utilisateur ID {user_id}"
            )

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    # ==========================
    # Dashboard admin
    # ==========================
    @staticmethod
    def voir_dashboard():

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            # total clients
            cursor.execute("""
                SELECT COUNT(*) FROM utilisateurs WHERE role='CLIENT'
            """)
            total_clients = cursor.fetchone()[0]

            # total prestations
            cursor.execute("""
                SELECT
                    (SELECT COUNT(*) FROM prestation_veterinaire) +
                    (SELECT COUNT(*) FROM prestation_dresseur) +
                    (SELECT COUNT(*) FROM prestation_garde)
            """)
            total_prestations = cursor.fetchone()[0]

            return {
                "total_clients": total_clients,
                "total_prestations": total_prestations
            }

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
                
@staticmethod
def voir_profils_notes():

    connection = get_connection("aniservice_home")

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT u.nom, u.role, p.moyenne_note
            FROM profils p
            JOIN utilisateurs u
                ON p.utilisateur_id = u.id
            WHERE u.role IN ('VETERINAIRE','DRESSEUR','GARDE')
            ORDER BY p.moyenne_note DESC
        """)

        return cursor.fetchall()

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()