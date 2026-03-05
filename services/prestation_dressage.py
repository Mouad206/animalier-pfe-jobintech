from database.db import get_connection
from mysql.connector import Error
from services.auth_service import AuthService
from services.log_service import LogService
from services.historique_service import HistoriqueService


class PrestationDresseurService:

    @staticmethod
    def creer_prestation(client_id, dresseur_id, type_service, date_debut):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO prestation_dresseur
                (type_service, date_debut, client_id, dresseur_id)
                VALUES (%s, %s, %s, %s)
            """, (type_service, date_debut, client_id, dresseur_id))

            connection.commit()

            prestation_id = cursor.lastrowid

            # historique client
            HistoriqueService.ajouter_action(
                client_id,
                "Création prestation dressage"
            )

            # log système
            user = AuthService.get_current_user()

            LogService.log(
                "INFO",
                user["id"],
                f"Prestation dressage créée ID {prestation_id}"
            )

            return prestation_id

        except Error as e:

            user = AuthService.get_current_user()

            LogService.log(
                "ERROR",
                user["id"] if user else None,
                f"Erreur création prestation dressage: {str(e)}"
            )

            print("Erreur:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def confirmer_prestation(prestation_id):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE prestation_dresseur
                SET statut='CONFIRMEE'
                WHERE id=%s
            """, (prestation_id,))

            connection.commit()

            user = AuthService.get_current_user()

            LogService.log(
                "INFO",
                user["id"],
                f"Prestation dressage {prestation_id} confirmée"
            )

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()