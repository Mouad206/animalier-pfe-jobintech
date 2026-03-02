from models.profil import Profil


class Garde(Profil):

    def afficher_profil(self):
        return f"Vétérinaire {self.nom} - {self.ville}"



    