from repository.client_service_repository import ClientServiceRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig


class ClientService:

    logger = LoggerConfig.getInstance()

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def voir_prestations(client_id):
        return ClientServiceRepository.get_prestations(client_id)


    @staticmethod
    def creer_prestation(type_service, description, date_debut, client_id, profil_id):

        ClientServiceRepository.create_prestation(
            type_service,
            description,
            date_debut,
            client_id,
            profil_id
        )

        HistoriqueService.enregistrer_action(
            client_id,
            "Création prestation"
        )


    @staticmethod
    def modifier_prestation(prestation_id, description):

        ClientServiceRepository.update_prestation(
            prestation_id,
            description
        )


    @staticmethod
    def supprimer_prestation(prestation_id):

        ClientServiceRepository.delete_prestation(
            prestation_id
        )

    # =========================
    # ANIMAUX
    # =========================

    @staticmethod
    def voir_animaux(client_id):
        return ClientServiceRepository.get_animaux(client_id)


    @staticmethod
    def ajouter_animal(nom, espece, race, age, client_id):

        ClientServiceRepository.add_animal(
            nom,
            espece,
            race,
            age,
            client_id
        )

    @staticmethod
    def modifier_animal(animal_id, nom, espece, race, age):

        ClientServiceRepository.update_animal(
            animal_id,
            nom,
            espece,
            race,
            age
        )

    @staticmethod
    def supprimer_animal(animal_id):

        ClientServiceRepository.delete_animal(animal_id)

    # =========================
    # PROFIL
    # =========================

    @staticmethod
    def voir_profil(client_id):
        return ClientServiceRepository.get_client_profile(client_id)


    @staticmethod
    def modifier_profil(client_id, nom, email, telephone, adresse):

        ClientServiceRepository.update_profile(
            client_id,
            nom,
            email,
            telephone,
            adresse
        )


    @staticmethod
    def modifier_mot_de_passe(client_id, mot_de_passe):

        ClientServiceRepository.update_password(
            client_id,
            mot_de_passe
        )