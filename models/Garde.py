from models.profil import Profil


class Garde(Profil):

    def __init__(self, id, nom, prenom, email, telephone, mot_de_passe,
                 raison_sociale, certification, annee_experience,
                 adresse, disponibilite, statut_abonnement):

        super().__init__(id, nom, prenom, email, telephone, mot_de_passe,
                         raison_sociale, certification, annee_experience,
                         adresse, disponibilite, statut_abonnement)



    