from abc import ABC


class Prestation(ABC):

    def __init__(self, id, date_debut, date_fin, statut):
        self.id = id
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.statut = statut