from database.db import get_connection
from mysql.connector import Error
from services.auth_service import AuthService
from services.log_service import LogService
from services.historique_service import HistoriqueService


class PrestationVeterinaireService:

    @staticmethod
    def creer_prestation(client_id, veterinaire_id, type_service, date_debut):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO prestation_veterinaire
                (type_service, date_debut, client_id, veterinaire_id)
                VALUES (%s, %s, %s, %s)
            """, (type_service, date_debut, client_id, veterinaire_id))

            connection.commit()

            prestation_id = cursor.lastrowid

            # Historique client
            HistoriqueService.ajouter_action(
                client_id,
                "Création prestation vétérinaire"
            )

            # Log système
            user = AuthService.get_current_user()

            LogService.log(
                "INFO",
                user["id"],
                f"Nouvelle prestation vétérinaire créée ID {prestation_id}"
            )

            return prestation_id

        except Error as e:

            user = AuthService.get_current_user()

            LogService.log(
                "ERROR",
                user["id"] if user else None,
                f"Erreur création prestation vétérinaire: {str(e)}"
            )

            print("Erreur:", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()