from models.Dresseur import Dresseur
from factories.profil_factory import ProfilFactory


class DresseurFactory(ProfilFactory):

    @staticmethod
    def creer_profil(user, raison_sociale, certification,
                     experience, adresse, ville, disponibilite):

        return Dresseur(
            user["id"],
            user["nom"],
            user["prenom"],
            user["email"],
            user["telephone"],
            user["mot_de_passe"],
            user["role"],
            raison_sociale,
            certification,
            experience,
            adresse,
            ville,
            disponibilite
        )