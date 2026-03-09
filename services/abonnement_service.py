from repository.abonnement_repository import AbonnementRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig
from datetime import date, timedelta


class AbonnementService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def payer_abonnement(profil_id, type_abonnement, montant):

        date_debut = date.today()
        date_fin = date_debut + timedelta(days=30)

        abonnement_id = AbonnementRepository.create(
            profil_id,
            type_abonnement,
            montant,
            date_debut,
            date_fin
        )

        HistoriqueService.enregistrer_action(
            profil_id,
            "Paiement abonnement",
            abonnement_id
        )

        AbonnementService.logger.log(
            "INFO",
            profil_id,
            f"Abonnement activé ID {abonnement_id}"
        )

        return abonnement_id


    @staticmethod
    def verifier_abonnement(profil_id):

        abonnement = AbonnementRepository.find_active_by_profil(profil_id)

        if not abonnement:
            return False

        return True