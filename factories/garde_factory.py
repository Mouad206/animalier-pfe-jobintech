from models.Garde import Garde
from factories.profil_factory import ProfilFactory


class GardeFactory(ProfilFactory):

    @staticmethod
    def creer_profil(user, raison_sociale, certification,
                     experience, adresse, ville, disponibilite):

        return Garde(
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