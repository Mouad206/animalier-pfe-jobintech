from database.db import get_connection
from infra.logger_config import LoggerConfig


class ReclamationService:

    def __init__(self):
        self.logger = LoggerConfig()

    def creer_reclamation(self, motif, description, client_id, profil_id):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO reclamations (motif, description, statut, client_id, profil_id)
            VALUES (%s, %s, 'EN_ATTENTE', %s, %s)
            """

            cursor.execute(query, (motif, description, client_id, profil_id))

            connection.commit()

            self.logger.log_info("Nouvelle réclamation créée")

        except Exception as e:
            self.logger.log_error(f"Erreur création réclamation : {e}")