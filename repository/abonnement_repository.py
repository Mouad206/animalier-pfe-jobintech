from datetime import timedelta

from repository.base_repository import BaseRepository


class AbonnementRepository(BaseRepository):

    @staticmethod
    def create(profil_id, type_abonnement, montant, date_debut, date_fin):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()
        date_fin = date_debut + timedelta(days=30)  # abonnement d'un mois
        cursor.execute("""
        INSERT INTO abonnements
        (profil_id, type_abonnement, montant, date_debut, date_fin, statut)
        VALUES (%s,%s,%s,%s,%s,'ACTIF')
        """, (
            profil_id,
            type_abonnement,
            montant,
            date_debut,
            date_fin
        ))

        connection.commit()

        abonnement_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return abonnement_id


    @staticmethod
    def find_active_by_profil(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
        SELECT * FROM abonnements
        WHERE profil_id=%s AND statut='ACTIF'
        """, (profil_id,))

        abonnement = cursor.fetchone()

        cursor.close()
        connection.close()

        return abonnement