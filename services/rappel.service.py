from database.db import get_connection
from infra.logger_config import LoggerConfig


class RappelService:

    def __init__(self):
        self.logger = LoggerConfig()

    def demander_rappel(self, message, client_id, profil_id):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO demande_rappel (message, statut, client_id, profil_id)
            VALUES (%s, 'EN_ATTENTE', %s, %s)
            """

            cursor.execute(query, (message, client_id, profil_id))

            connection.commit()

            self.logger.log_info("Demande de rappel créée")

        except Exception as e:
            self.logger.log_error(f"Erreur demande rappel : {e}")


    def accepter_rappel(self, rappel_id):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            UPDATE demande_rappel
            SET statut = 'ACCEPTEE'
            WHERE id = %s
            """

            cursor.execute(query, (rappel_id,))

            connection.commit()

            self.logger.log_info("Demande de rappel acceptée")

        except Exception as e:
            self.logger.log_error(f"Erreur acceptation rappel : {e}")