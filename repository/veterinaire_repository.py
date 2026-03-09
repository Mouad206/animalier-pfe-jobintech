from repository.base_repository import BaseRepository


class VeterinaireRepository(BaseRepository):

    @staticmethod
    def create(utilisateur_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO veterinaires (utilisateur_id) VALUES (%s)",
            (utilisateur_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()