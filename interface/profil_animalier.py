from abc import ABC, abstractmethod


class ProfilAnimalier(ABC):

    @abstractmethod
    def afficher_profil(self):
        pass