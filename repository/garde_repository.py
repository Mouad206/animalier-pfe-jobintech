from repository.base_repository import BaseRepository


class GardeRepository(BaseRepository):

    @staticmethod
    def create(utilisateur_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO gardes (utilisateur_id) VALUES (%s)",
            (utilisateur_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()