from repository.base_repository import BaseRepository


class PrestationRepository(BaseRepository):

    @staticmethod
    def create(type_prestation, client_id, profil_id,
               description, date_debut, catalogue_id,animal_id=None):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO prestations
            (type_prestation, client_id, profil_id,
            description, date_debut, statut, catalogue_id, animal_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
            type_prestation,
            client_id,
            profil_id,
            description,
            date_debut,
            "EN_ATTENTE",
            catalogue_id,
            animal_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


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
        
        
    @staticmethod
    def find_by_id(prestation_id):

                connection = BaseRepository.get_connection()
                cursor = connection.cursor(dictionary=True)

                cursor.execute("""
                    SELECT *
                    FROM prestations
                    WHERE id = %s
                """, (prestation_id,))

                prestation = cursor.fetchone()

                cursor.close()
                connection.close()

                return prestation