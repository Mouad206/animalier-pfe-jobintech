from abc import ABC, abstractmethod

class Service_animalier(ABC):

    def __init__(self, nom, tarif):
        self.nom = nom
        self.tarif = tarif

    @abstractmethod
    def calculer_prix(self):
        pass