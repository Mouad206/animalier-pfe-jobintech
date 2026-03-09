from abc import ABC, abstractmethod

class ProfilFactory(ABC):

    @staticmethod
    @abstractmethod
    def creer_profil(user, raison_sociale, certification,
                     experience, adresse, ville, disponibilite):
        pass