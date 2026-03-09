from repository.base_repository import BaseRepository


class ProfilRepository(BaseRepository):

    @staticmethod
    def create(profil):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO profils
        (utilisateur_id, raison_sociale, certification,
        annee_experience, adresse, ville, disponibilite)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            profil.id,
            profil.raison_sociale,
            profil.certification,
            profil.annee_experience,
            profil.adresse,
            profil.ville,
            profil.disponibilite
        ))

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def find_all():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM profils")

        profils = cursor.fetchall()

        cursor.close()
        connection.close()

        return profils


    @staticmethod
    def find_by_id(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM profils WHERE utilisateur_id=%s",
            (profil_id,)
        )

        profil = cursor.fetchone()

        cursor.close()
        connection.close()

        return profil