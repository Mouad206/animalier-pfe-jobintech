from repository.base_repository import BaseRepository


class CatalogueRepository(BaseRepository):

    @staticmethod
    def create(profil_id, type_service, service_nom, description, tarif):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO catalogue_services
        (profil_id, type_service, service_nom, description, tarif)
        VALUES (%s,%s,%s,%s,%s)
        """, (
            profil_id,
            type_service,
            service_nom,
            description,
            tarif
        ))

        connection.commit()

        catalogue_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return catalogue_id


    @staticmethod
    def find_by_profil(profil_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM catalogue_services WHERE profil_id=%s",
            (profil_id,)
        )

        services = cursor.fetchall()

        cursor.close()
        connection.close()

        return services


    @staticmethod
    def find_all():

        connection = BaseRepository.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM catalogue_services")

        services = cursor.fetchall()

        cursor.close()
        connection.close()

        return services


    @staticmethod
    def delete(catalogue_id):

        connection = BaseRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM catalogue_services WHERE id=%s",
            (catalogue_id,)
        )

        connection.commit()

        cursor.close()
        connection.close()