from models.profil import Profil


class Garde(Profil):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe,role,
                 raison_sociale, certification, annee_experience,
                 adresse, ville, disponibilite):

        super().__init__(
            id, nom, prenom, email, telephone, mot_de_passe,role,
            raison_sociale, certification, annee_experience,
            adresse, ville, disponibilite
        )
        
        
        
    def afficher_infos(self):
        print("\n===== PROFIL GARDE =====")
        print("Nom :", self.nom, self.prenom)