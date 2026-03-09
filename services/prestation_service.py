from repository.prestation_repository import PrestationRepository
from services.historique_service import HistoriqueService
from services.notification_service import NotificationService
from infra.logger_config import LoggerConfig


class PrestationService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def creer_prestation(prestation):

        prestation_id = PrestationRepository.create(prestation)

        # historique
        HistoriqueService.enregistrer_action(
            prestation.client_id,
            "Création prestation",
            prestation_id
        )

        # notification au professionnel
        NotificationService.envoyer_notification(
            prestation.profil_id,
            "Nouvelle demande de prestation"
        )

        # log
        PrestationService.logger.log(
            "INFO",
            prestation.client_id,
            f"Prestation créée ID {prestation_id}"
        )

        return prestation_id


    @staticmethod
    def voir_prestations_client(client_id):

        return PrestationRepository.find_by_client(client_id)


    @staticmethod
    def voir_prestations_profil(profil_id):

        return PrestationRepository.find_by_profil(profil_id)


    @staticmethod
    def confirmer_prestation(prestation_id):

        PrestationRepository.update_statut(prestation_id, "CONFIRMEE")