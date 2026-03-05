from models.evaluation import Evaluation


class EvaluationVeterinaire(Evaluation):

    def __init__(self, id, note, commentaire, date, prestation_id):
        super().__init__(id, note, commentaire, date)
        self.prestation_id = prestation_id