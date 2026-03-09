from repository.evaluation_repository import EvaluationRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig


class EvaluationService:

    logger = LoggerConfig.getInstance()

    @staticmethod
    def evaluer(prestation_id, client_id, note, commentaire):

        if note < 1 or note > 5:
            print("❌ La note doit être entre 1 et 5")
            return

        evaluation_id = EvaluationRepository.create(
            prestation_id,
            client_id,
            note,
            commentaire
        )

        # historique utilisateur
        HistoriqueService.enregistrer_action(
            client_id,
            "Evaluation prestation",
            prestation_id
        )

        # log système
        EvaluationService.logger.log(
            "INFO",
            client_id,
            f"Evaluation créée ID {evaluation_id}"
        )

        print("✅ Evaluation enregistrée")

        return evaluation_id