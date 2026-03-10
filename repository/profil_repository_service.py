from repository.base_repository import BaseRepository


class ProfilRepositoryService(BaseRepository):

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def get_prestations(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM prestations
        WHERE profil_id=%s
        """, (profil_id,))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def update_prestation_statut(prestation_id, statut):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE prestations
        SET statut=%s
        WHERE id=%s
        """, (statut, prestation_id))

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # NOTIFICATIONS
    # =========================

    @staticmethod
    def get_notifications(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM notifications
        WHERE utilisateur_id=%s
        """, (profil_id,))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    # =========================
    # PROFIL
    # =========================

    @staticmethod
    def get_profil(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT u.nom, u.prenom, u.email, u.telephone,
               p.role, p.raison_sociale, p.certification,
               p.annee_experience, p.adresse, p.ville,
               p.disponibilite, p.statut_abonnement
        FROM utilisateurs u
        JOIN profils p
        ON u.id = p.utilisateur_id
        WHERE u.id=%s
        """, (profil_id,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def update_profil(profil_id, nom, email, telephone, adresse, disponibilite):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE utilisateurs
        SET nom=%s, email=%s, telephone=%s
        WHERE id=%s
        """, (nom, email, telephone, profil_id))

        cursor.execute("""
        UPDATE profils
        SET adresse=%s, disponibilite=%s
        WHERE utilisateur_id=%s
        """, (adresse, disponibilite, profil_id))

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # ABONNEMENT
    # =========================

    @staticmethod
    def get_abonnement(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM abonnements
        WHERE profil_id=%s
        """, (profil_id,))

        abonnement = cursor.fetchall()

        cursor.close()
        connection.close()

        return abonnement

    # =========================
    # DASHBOARD
    # =========================

    @staticmethod
    def count_prestations_attente(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM prestations
        WHERE profil_id=%s AND statut='EN_ATTENTE'
        """, (profil_id,))

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def count_prestations_terminees(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM prestations
        WHERE profil_id=%s AND statut='TERMINEE'
        """, (profil_id,))

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def moyenne_note(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT AVG(e.note)
        FROM evaluations e
        JOIN prestations p
        ON e.prestation_id=p.id
        WHERE p.profil_id=%s
        """, (profil_id,))

        result = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return result