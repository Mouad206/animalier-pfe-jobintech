import mysql.connector
from database.db import DB_CONFIG
from services.log_service import LogService


class PrestationGardeService:

    @staticmethod
    def creer_prestation(garde_id, client_id, description, date_debut, date_fin):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        query = """
        INSERT INTO prestations (
            client_id,
            type_prestation,
            description,
            date_prestation
        )
        VALUES (%s, %s, %s, NOW())
        """

        cursor.execute(
            query,
            (client_id, "garde", description)
        )

        connection.commit()

        # récupérer l'id généré
        prestation_id = cursor.lastrowid

        cursor.close()
        connection.close()

        # log système
        LogService.log(client_id, "INFO", "Prestation garde créée")

        return prestation_id