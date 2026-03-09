from models.Utilisateur import Utilisateur


class Profil(Utilisateur):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe,role,
                 raison_sociale, certification, annee_experience,
                 adresse, ville, disponibilite):

        super().__init__(id, nom, prenom, email, telephone, mot_de_passe, role)

        self.raison_sociale = raison_sociale
        self.certification = certification
        self.annee_experience = annee_experience
        self.adresse = adresse
        self.ville = ville
        self.disponibilite = disponibilite