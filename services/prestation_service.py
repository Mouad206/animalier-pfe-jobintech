from database.db import get_connection
from infra.logger_config import LoggerConfig
from services.historique_service import HistoriqueService
from services.notification_service import NotificationService
from services.abonnement_service import AbonnementService
from datetime import datetime


class PrestationService:

    def __init__(self):

        self.logger = LoggerConfig()
        self.historique_service = HistoriqueService()
        self.notification_service = NotificationService()
        self.abonnement_service = AbonnementService()


    def creer_prestation_veterinaire(self, client_id, veterinaire_id, animal_id, date_debut):

        try:

            # Vérifier abonnement
            if not self.abonnement_service.verifier_abonnement(veterinaire_id):

                self.logger.log_warning("Prestataire sans abonnement actif")
                return "Abonnement inactif"

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO prestation_veterinaire
            (date_debut, statut, client_id, veterinaire_id, animal_id)
            VALUES (%s, 'EN_ATTENTE', %s, %s, %s)
            """

            cursor.execute(query, (
                date_debut,
                client_id,
                veterinaire_id,
                animal_id
            ))

            connection.commit()

            prestation_id = cursor.lastrowid

            # Historique
            self.historique_service.enregistrer_action(
                utilisateur_id=client_id,
                action="Création prestation vétérinaire",
                prestation_id=prestation_id
            )

            # Notification
            self.notification_service.envoyer_notification(
                "Nouvelle demande de prestation",
                veterinaire_id
            )

            self.logger.log_info("Prestation vétérinaire créée")

            return prestation_id

        except Exception as e:

            self.logger.log_error(f"Erreur création prestation : {e}")