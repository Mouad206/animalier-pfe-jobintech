import mysql.connector
from database.db import DB_CONFIG
from services.log_service import LogService


class DressageService:

    @staticmethod
    def creer_prestation(client_id, description):

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO prestations (client_id, type_prestation, description) VALUES (%s, %s, %s)",
            (client_id, "dressage", description)
        )

        connection.commit()
        prestation_id = cursor.lastrowid

        cursor.close()
        connection.close()

        LogService.log(client_id, "INFO", "Prestation dressage créée")

        return prestation_id

    @staticmethod
    def payer(prestation_id):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE prestations SET statut='PAYEE' WHERE id=%s",
            (prestation_id,)
        )

        connection.commit()
        cursor.close()
        connection.close()