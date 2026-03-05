from database.db import get_connection
from infra.logger_config import LoggerConfig


class AbonnementService:

    def __init__(self):
        self.logger = LoggerConfig()


    def verifier_abonnement(self, profil_id):

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT statut_abonnement
            FROM profils
            WHERE utilisateur_id = %s
            """

            cursor.execute(query, (profil_id,))
            result = cursor.fetchone()

            if result and result[0] == "ACTIF":
                return True

            return False

        except Exception as e:

            self.logger.log_error(f"Erreur vérification abonnement : {e}")
            return False


    def revenus_abonnements(self):

        try:

            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT COUNT(*)
            FROM profils
            WHERE statut_abonnement = 'ACTIF'
            """

            cursor.execute(query)

            result = cursor.fetchone()

            return result[0]

        except Exception as e:

            self.logger.log_error(f"Erreur calcul revenus : {e}")
            return 0