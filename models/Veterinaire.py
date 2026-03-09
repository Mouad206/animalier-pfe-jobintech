from models.profil import Profil


class Veterinaire(Profil):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe,role,
                 raison_sociale, certification, annee_experience,
                 adresse, ville, disponibilite):

        super().__init__(
            id, nom, prenom, email, telephone, mot_de_passe,role,
            raison_sociale, certification, annee_experience,
            adresse, ville, disponibilite
        )
        
        
    def afficher_infos(self):
        print("\n===== PROFIL VÉTÉRINAIRE =====")
        print("Nom :", self.nom, self.prenom)
        print("Email :", self.email)
        print("Téléphone :", self.telephone)
        print("Raison sociale :", self.raison_sociale)
        print("Certification :", self.certification)
        print("Expérience :", self.annee_experience)
        print("Adresse :", self.adresse)
        print("Ville :", self.ville)
        print("Disponible :", self.disponibilite)