from models.Veterinaire import Veterinaire
from factories.profil_factory import ProfilFactory


class VeterinaireFactory(ProfilFactory):

    @staticmethod
    def creer_profil(user, raison_sociale, certification,
                     experience, adresse, ville, disponibilite):

        return Veterinaire(
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