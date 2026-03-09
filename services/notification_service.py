from repository.notification_repository import NotificationRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig


class NotificationService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def envoyer_notification(utilisateur_id, message):

        notification_id = NotificationRepository.create(
            utilisateur_id,
            message
        )

        HistoriqueService.enregistrer_action(
            utilisateur_id,
            "Notification envoyée",
            notification_id
        )

        NotificationService.logger.log(
            "INFO",
            utilisateur_id,
            f"Notification envoyée ID {notification_id}"
        )

        return notification_id


    @staticmethod
    def voir_notifications(utilisateur_id):

        return NotificationRepository.find_by_user(utilisateur_id)