from models.Utilisateur import Utilisateur


class Administrateur(Utilisateur):

    def afficher_infos(self):
        return f"Admin: {self.nom} ({self.email})"