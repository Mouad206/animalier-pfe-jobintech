from abc import ABC, abstractmethod
from Enums.enums import statutRole




class Utilisateur(ABC):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe, role:statutRole):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.mot_de_passe = mot_de_passe
        self.role = role

    def afficher_resume(self):
        return f"{self.nom} {self.prenom} - {self.role.value}"

    @abstractmethod
    def afficher_infos(self):
        pass