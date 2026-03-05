from database.db import get_connection
from infra.logger_config import LoggerConfig


class NotificationService:

    def __init__(self):
        self.logger = LoggerConfig()

    def envoyer_notification(self, message, utilisateur_id):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO notifications (message, statut, utilisateur_id)
            VALUES (%s, 'NON_LUE', %s)
            """

            cursor.execute(query, (message, utilisateur_id))

            connection.commit()

            self.logger.log_info("Notification envoyée")

        except Exception as e:
            self.logger.log_error(f"Erreur notification : {e}")