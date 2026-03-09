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
    def create(nom, prenom, email, telephone, mot_de_passe, role):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO utilisateurs
        (nom, prenom, email, telephone, mot_de_passe, role)
        VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            nom,
            prenom,
            email,
            telephone,
            mot_de_passe,
            role
        ))

        connection.commit()

        user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return user_id