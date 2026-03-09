from repository.base_repository import BaseRepository


class PrestationRepository(BaseRepository):

    @staticmethod
    def create(prestation):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO prestations
        (type_prestation, description, date_debut, date_fin, statut, client_id, profil_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            prestation.type_prestation,
            prestation.description,
            prestation.date_debut,
            prestation.date_fin,
            prestation.statut,
            prestation.client_id,
            prestation.profil_id
        ))

        connection.commit()

        prestation_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return prestation_id


    @staticmethod
    def find_by_client(client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM prestations WHERE client_id=%s",
            (client_id,)
        )

        prestations = cursor.fetchall()

        cursor.close()
        connection.close()

        return prestations


    @staticmethod
    def find_by_profil(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM prestations WHERE profil_id=%s",
            (profil_id,)
        )

        prestations = cursor.fetchall()

        cursor.close()
        connection.close()

        return prestations


    @staticmethod
    def update_statut(prestation_id, statut):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE prestations SET statut=%s WHERE id=%s",
            (statut, prestation_id)
        )

        connection.commit()

        cursor.close()
        connection.close()