from abc import ABC, abstractmethod


class Utilisateur(ABC):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe, role):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.mot_de_passe = mot_de_passe
        self.role = role

    @abstractmethod
    def afficher_infos(self):
        pass