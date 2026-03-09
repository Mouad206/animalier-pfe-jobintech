from repository.base_repository import BaseRepository


class AdminRepository(BaseRepository):

    # =========================
    # UTILISATEURS
    # =========================

    @staticmethod
    def get_all_users():
        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM utilisateurs")

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def create_user(nom, prenom, email, telephone, mot_de_passe, role):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO utilisateurs
        (nom, prenom, email, telephone, mot_de_passe, role)
        VALUES (%s,%s,%s,%s,%s,%s)
        """, (nom, prenom, email, telephone, mot_de_passe, role))

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def update_user(user_id, nom, prenom, email, telephone):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE utilisateurs
        SET nom=%s, prenom=%s, email=%s, telephone=%s
        WHERE id=%s
        """, (nom, prenom, email, telephone, user_id))

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def delete_user(user_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM utilisateurs WHERE id=%s",
            (user_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def change_role(user_id, role):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE utilisateurs SET role=%s WHERE id=%s",
            (role, user_id)
        )

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # PROFILS
    # =========================

    @staticmethod
    def get_all_profils():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM profils")

        profils = cursor.fetchall()

        cursor.close()
        connection.close()

        return profils


    @staticmethod
    def delete_profil(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM profils WHERE utilisateur_id=%s",
            (profil_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def get_all_prestations():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM prestations")

        prestations = cursor.fetchall()

        cursor.close()
        connection.close()

        return prestations


    @staticmethod
    def delete_prestation(prestation_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM prestations WHERE id=%s",
            (prestation_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # NOTIFICATIONS
    # =========================

    @staticmethod
    def get_all_notifications():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM notifications")

        notifications = cursor.fetchall()

        cursor.close()
        connection.close()

        return notifications


    @staticmethod
    def delete_notification(notification_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM notifications WHERE id=%s",
            (notification_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # HISTORIQUE
    # =========================

    @staticmethod
    def get_historique():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM historique_action")

        historique = cursor.fetchall()

        cursor.close()
        connection.close()

        return historique


    @staticmethod
    def delete_historique():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM historique_action")

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # LOGS
    # =========================

    @staticmethod
    def get_logs():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM logs_systeme")

        logs = cursor.fetchall()

        cursor.close()
        connection.close()

        return logs


    @staticmethod
    def delete_logs():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM logs_systeme")

        connection.commit()

        cursor.close()
        connection.close()
        
        
    # =========================
    # DASHBOARD STATISTIQUES
    # =========================

    @staticmethod
    def count_users():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM utilisateurs")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_clients():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM clients")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_profils():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM profils")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_profils_abonnes():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM abonnements
        WHERE statut = 'ACTIF';
        """)

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_profils_non_abonnes():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM abonnements
        WHERE statut='EXPIRE'
        """)

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_prestations():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM prestations")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_notifications():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM notifications")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_evaluations():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM evaluations")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_animaux():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM animaux")

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result
    
    @staticmethod
    def count_prestations_terminees():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM prestations
        WHERE statut='TERMINEE'
        """)

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result
    
    @staticmethod
    def moyenne_evaluations():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT AVG(note)
        FROM evaluations
        """)

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result
    
    @staticmethod
    def revenus_generes():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT SUM(c.tarif)
        FROM prestations p
        JOIN catalogue_services c
        ON p.catalogue_id = c.id
        WHERE p.statut='TERMINEE'
        """)

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result if result else 0