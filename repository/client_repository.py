from repository.base_repository import BaseRepository


class ClientRepository(BaseRepository):

    @staticmethod
    def find_by_email(email):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM utilisateurs WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user


    @staticmethod
    def create(utilisateur_id):

            connection = BaseRepository.get_connection()
            cursor = connection.cursor()

            cursor.execute("""
            INSERT INTO clients (utilisateur_id)
            VALUES (%s)
            """, (utilisateur_id,))

            connection.commit()

            cursor.close()
            connection.close()

