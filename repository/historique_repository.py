from database.db import get_connection
from infra.logger_config import LoggerConfig
from datetime import datetime


class HistoriqueRepository:

    @staticmethod
    def enregistrer_action(utilisateur_id, action, prestation_id=None):

        logger = LoggerConfig.getInstance()

        try:

            connection = get_connection("aniservice_home")
            cursor = connection.cursor()

            query = """
            INSERT INTO historique_action
            (date_action, action, utilisateur_id, prestation_id)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(query, (
                datetime.now(),
                action,
                utilisateur_id,
                prestation_id
            ))

            connection.commit()

            logger.log(
                "INFO",
                utilisateur_id,
                f"Historique enregistré : {action}"
            )

        except Exception as e:

            logger.log(
                "ERROR",
                utilisateur_id,
                f"Erreur historique : {e}"
            )

        finally:

            if connection.is_connected():
                cursor.close()
                connection.close()