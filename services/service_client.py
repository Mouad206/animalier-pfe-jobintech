from datetime import datetime

from repository.client_service_repository import ClientServiceRepository
from repository.prestation_repository import PrestationRepository
from services.historique_service import HistoriqueService
from services.catalogue_service import CatalogueService
from services.evaluation_service import EvaluationService
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
    def creer_prestation(client_id, profil_id, catalogue_id, description, type_service):

        date_debut = datetime.now()

        PrestationRepository.create(
            type_service,
            client_id,
            profil_id,
            description,
            date_debut,
            catalogue_id
        )

        print("✅ Prestation créée avec succès")

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
        
        
    # =========================
    # PROFIL
    # =========================
    @staticmethod
    def consulter_catalogue():

        return CatalogueService.voir_catalogue()
    
    @staticmethod
    def consulter_catalogue_par_type(type_service):

        return CatalogueService.consulter_catalogue_par_type(type_service)
    
    @staticmethod
    def consulter_catalogue_profil(profil_id):

        return CatalogueService.consulter_catalogue_profil(profil_id)
    
    # =========================
    # PROFIL
    # =========================
    
    @staticmethod
    def evaluer_prestation(prestation_id, client_id, note, commentaire):
        EvaluationService.evaluer(
            prestation_id,
            client_id,
            note,
            commentaire
        )