from repository.evaluation_repository import EvaluationRepository
from services.historique_service import HistoriqueService
from services.notification_service import NotificationService
from infra.logger_config import LoggerConfig


class EvaluationService:

    logger = LoggerConfig.getInstance()

from repository.evaluation_repository import EvaluationRepository
from repository.prestation_repository import PrestationRepository
from services.notification_service import NotificationService
from services.historique_service import HistoriqueService


class EvaluationService:

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

        # récupérer le profil concerné par la prestation
        prestation = PrestationRepository.find_by_id(prestation_id)
        profil_id = prestation["profil_id"]

        # envoyer notification au profil
        NotificationService.envoyer(
            profil_id,
            f"Vous avez reçu une nouvelle évaluation (note {note}/5)"
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
    
    
    @staticmethod
    def prestations_a_evaluer(client_id):

        return EvaluationRepository.get_prestations_a_evaluer(client_id)