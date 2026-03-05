from database.db import get_connection
from services.auth_service import AuthService
from services.prestation_veterinaire import PrestationVeterinaireService
from services.prestation_dressage import PrestationDresseurService
from services.prestation_garde import PrestationGardeService


class ServiceClient:

    # ===============================
    # Voir ses prestations
    # ===============================
    @staticmethod
    def voir_prestations():

        user = AuthService.current_user

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor(dictionary=True)

            # vétérinaire
            cursor.execute("""
                SELECT id,type_service,date_debut,statut
                FROM prestation_veterinaire
                WHERE client_id=%s
            """, (user["id"],))

            vet = cursor.fetchall()

            # dressage
            cursor.execute("""
                SELECT id,type_service,date_debut,statut
                FROM prestation_dresseur
                WHERE client_id=%s
            """, (user["id"],))

            dress = cursor.fetchall()

            # garde
            cursor.execute("""
                SELECT id,date_debut,date_fin,statut
                FROM prestation_garde
                WHERE client_id=%s
            """, (user["id"],))

            garde = cursor.fetchall()

            return {
                "veterinaire": vet,
                "dressage": dress,
                "garde": garde
            }

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # ===============================
    # Créer prestation vétérinaire
    # ===============================
    @staticmethod
    def demander_veterinaire(veterinaire_id, type_service, date_debut):

        user = AuthService.current_user

        return PrestationVeterinaireService.creer_prestation(
            user["id"],
            veterinaire_id,
            type_service,
            date_debut
        )

    # ===============================
    # Créer prestation dressage
    # ===============================
    @staticmethod
    def demander_dressage(dresseur_id, type_service, date_debut):

        user = AuthService.current_user

        return PrestationDresseurService.creer_prestation(
            user["id"],
            dresseur_id,
            type_service,
            date_debut
        )

    # ===============================
    # Créer prestation garde
    # ===============================
    @staticmethod
    def demander_garde(garde_id, date_debut, date_fin):

        user = AuthService.current_user

        return PrestationGardeService.creer_prestation(
            user["id"],
            garde_id,
            date_debut,
            date_fin
        )

    # ===============================
    # Modifier profil client
    # ===============================
    @staticmethod
    def modifier_profil(nom, prenom, telephone):

        user = AuthService.current_user

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE utilisateurs
                SET nom=%s, prenom=%s, telephone=%s
                WHERE id=%s
            """, (nom, prenom, telephone, user["id"]))

            connection.commit()

            print("Profil modifié")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # ===============================
    # Ajouter animal
    # ===============================
    @staticmethod
    def ajouter_animal(nom, espece, race, age):

        user = AuthService.current_user

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO animaux
                (nom,espece,race,age,client_id)
                VALUES (%s,%s,%s,%s,%s)
            """, (
                nom,
                espece,
                race,
                age,
                user["id"]
            ))

            connection.commit()

            print("Animal ajouté")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # ===============================
    # Voir ses animaux
    # ===============================
    @staticmethod
    def voir_animaux():

        user = AuthService.current_user

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute("""
                SELECT id,nom,espece,race,age
                FROM animaux
                WHERE client_id=%s
            """, (user["id"],))

            animaux = cursor.fetchall()

            return animaux

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()