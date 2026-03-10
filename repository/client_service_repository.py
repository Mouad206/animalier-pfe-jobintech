from models import profil
from repository.base_repository import BaseRepository


class ClientServiceRepository(BaseRepository):

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def get_prestations(client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM prestations
        WHERE client_id=%s
        """, (client_id,))

        prestations = cursor.fetchall()

        cursor.close()
        connection.close()

        return prestations


    @staticmethod
    def create_prestation(type_prestation, client_id, profil_id,
               description, date_debut, catalogue_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO prestations
        (type_prestation, client_id, profil_id,
         description, date_debut, statut, catalogue_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
            type_prestation,
            client_id,
            profil_id,
            description,
            date_debut,
            "EN_ATTENTE",
            catalogue_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def update_prestation(prestation_id, description):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE prestations
        SET description=%s
        WHERE id=%s
        """, (
            description,
            prestation_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


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
    # ANIMAUX
    # =========================

    @staticmethod
    def get_animaux(client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM animaux
        WHERE client_id=%s
        """, (client_id,))

        animaux = cursor.fetchall()

        cursor.close()
        connection.close()

        return animaux


    @staticmethod
    def add_animal(nom, espece, race, age, client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO animaux
        (nom, espece, race, age, client_id)
        VALUES (%s,%s,%s,%s,%s)
        """, (
            nom,
            espece,
            race,
            age,
            client_id
        ))

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def delete_animal(animal_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM animaux WHERE id=%s",
            (animal_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()

    @staticmethod
    def update_animal(animal_id, nom, espece, race, age):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE animaux
        SET nom=%s, espece=%s, race=%s, age=%s
        WHERE id=%s
        """, (
            nom,
            espece,
            race,
            age,
            animal_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

    # =========================
    # PROFIL CLIENT
    # =========================

    @staticmethod
    def get_client_profile(client_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT u.nom, u.prenom, u.email, u.telephone, c.adresse
        FROM utilisateurs u
        JOIN clients c
        ON u.id = c.utilisateur_id
        WHERE u.id=%s
        """, (client_id,))

        profil = cursor.fetchone()

        cursor.close()
        connection.close()

        return profil


    @staticmethod
    def update_profile(client_id, nom, email, telephone, adresse):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE utilisateurs
        SET nom=%s, email=%s, telephone=%s
        WHERE id=%s
        """, (
            nom,
            email,
            telephone,
            client_id
        ))

        cursor.execute("""
        UPDATE clients
        SET adresse=%s
        WHERE utilisateur_id=%s
        """, (
            adresse,
            client_id
        ))

        connection.commit()

        cursor.close()
        connection.close()