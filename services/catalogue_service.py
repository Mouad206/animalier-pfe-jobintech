from repository.catalogue_repository import CatalogueRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig


class CatalogueService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def ajouter_service(profil_id, type_service, service_nom, description, tarif):

        catalogue_id = CatalogueRepository.create(
            profil_id,
            type_service,
            service_nom,
            description,
            tarif
        )

        HistoriqueService.enregistrer_action(
            profil_id,
            "Ajout service catalogue",
            catalogue_id
        )

        CatalogueService.logger.log(
            "INFO",
            profil_id,
            f"Nouveau service catalogue ID {catalogue_id}"
        )

        print("✅ Service ajouté au catalogue")

        return catalogue_id


    @staticmethod
    def voir_catalogue():

        return CatalogueRepository.find_all()


    @staticmethod
    def consulter_catalogue_profil(profil_id):

        return CatalogueRepository.find_by_profil(profil_id)
    
    
    @staticmethod
    def consulter_catalogue_par_type(type_service):

        return CatalogueRepository.find_by_type(type_service)


    @staticmethod
    def supprimer_service(catalogue_id):

        CatalogueRepository.delete(catalogue_id)

        print("Service supprimé")