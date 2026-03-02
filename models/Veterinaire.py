from models.profil import Profil


class Veterinaire(Profil):

    def afficher_profil(self):
        return f"Vétérinaire {self.nom} - {self.ville}"






