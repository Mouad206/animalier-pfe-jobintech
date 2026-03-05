from abc import ABC


class Evaluation(ABC):

    def __init__(self, id, note, commentaire, date):
        self.id = id
        self.note = note
        self.commentaire = commentaire
        self.date = date