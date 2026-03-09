from repository.base_repository import BaseRepository


class EvaluationRepository(BaseRepository):

    @staticmethod
    def create(prestation_id, client_id, note, commentaire):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO evaluations
        (prestation_id, client_id, note, commentaire)
        VALUES (%s,%s,%s,%s)
        """, (
            prestation_id,
            client_id,
            note,
            commentaire
        ))

        connection.commit()

        evaluation_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return evaluation_id


    @staticmethod
    def find_by_prestation(prestation_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM evaluations WHERE prestation_id=%s",
            (prestation_id,)
        )

        evaluation = cursor.fetchone()

        cursor.close()
        connection.close()

        return evaluation


    @staticmethod
    def find_by_client(client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM evaluations WHERE client_id=%s",
            (client_id,)
        )

        evaluations = cursor.fetchall()

        cursor.close()
        connection.close()

        return evaluations