from database.db import get_connection
from infra.logger_config import LoggerConfig
from datetime import datetime


class HistoriqueService:

    def __init__(self):
        self.logger = LoggerConfig()

    def enregistrer_action(self, utilisateur_id, action, prestation_id=None):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO historique (date, action, utilisateur_id, prestation_id)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(query, (
                datetime.now(),
                action,
                utilisateur_id,
                prestation_id
            ))

            connection.commit()

            self.logger.log_info(f"Historique enregistré : {action}")

        except Exception as e:
            self.logger.log_error(f"Erreur historique : {e}")