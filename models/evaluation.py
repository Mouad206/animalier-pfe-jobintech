from abc import ABC, abstractmethod


class Evaluation(ABC):

    def __init__(self, note, commentaire, prestation_id, client_id):
        self.note = note
        self.commentaire = commentaire
        self.prestation_id = prestation_id
        self.client_id = client_id

    @abstractmethod
    def sauvegarder(self):
        pass