from repository.historique_repository import HistoriqueRepository
from infra.logger_config import LoggerConfig


class HistoriqueService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def enregistrer_action(utilisateur_id, action, prestation_id=None):

        try:

            historique_id = HistoriqueRepository.create(
                utilisateur_id,
                action,
                prestation_id
            )

            HistoriqueService.logger.log(
                "INFO",
                utilisateur_id,
                f"Historique enregistré ID {historique_id}"
            )

            return historique_id

        except Exception as e:

            HistoriqueService.logger.log(
                "ERROR",
                utilisateur_id,
                f"Erreur historique : {e}"
            )