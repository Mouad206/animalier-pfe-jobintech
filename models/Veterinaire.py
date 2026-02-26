import models.Utilisateur as Utilisateur

class Veterinaire(Utilisateur):
    def __init__(self, id_utilisateur: int, nom: str, prenom: str, email: str, mot_de_passe: str, role: str, telephone: str):
        super().__init__(id_utilisateur, nom, prenom, email, mot_de_passe, role, telephone)