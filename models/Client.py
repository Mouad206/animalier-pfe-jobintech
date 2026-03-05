from models.utilisateur import Utilisateur


class Client(Utilisateur):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe):
        super().__init__(id, nom, prenom, email, telephone, mot_de_passe)