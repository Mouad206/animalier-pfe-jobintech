from repository.base_repository import BaseRepository


class NotificationRepository(BaseRepository):

    @staticmethod
    def create(utilisateur_id, message):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO notifications
        (message, utilisateur_id)
        VALUES (%s,%s)
        """, (
            message,
            utilisateur_id
        ))

        connection.commit()

        notification_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return notification_id


    @staticmethod
    def find_by_user(utilisateur_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM notifications WHERE utilisateur_id=%s",
            (utilisateur_id,)
        )

        notifications = cursor.fetchall()

        cursor.close()
        connection.close()

        return notifications


    @staticmethod
    def mark_as_read(notification_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE notifications SET statut='LUE' WHERE id=%s",
            (notification_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()