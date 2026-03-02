import mysql.connector
from database.db import DB_CONFIG
from services.log_service import LogService


class PrestationVeterinaireService:

    @staticmethod
    def creer_prestation(client_id, description):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        query = """
        INSERT INTO prestations (client_id, type_prestation, description)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (client_id, "veterinaire", description)
        )

        connection.commit()
        prestation_id = cursor.lastrowid

        cursor.close()
        connection.close()

        # log système
        LogService.log(client_id, "INFO", "Prestation vétérinaire créée")

        return prestation_id


    @staticmethod
    def terminer_prestation(prestation_id, client_id):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE prestations SET statut='TERMINEE' WHERE id=%s",
            (prestation_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

        LogService.log(client_id, "INFO", "Prestation vétérinaire terminée")


    @staticmethod
    def annuler_prestation(prestation_id, client_id):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE prestations SET statut='ANNULEE' WHERE id=%s",
            (prestation_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

        LogService.log(client_id, "WARNING", "Prestation vétérinaire annulée")