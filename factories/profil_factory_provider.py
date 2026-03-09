from factories.veterinairie_factory import VeterinaireFactory
from factories.dresseur_factory import DresseurFactory
from factories.garde_factory import GardeFactory


class ProfilFactoryProvider:

    @staticmethod
    def get_factory(role):

        if role == "VETERINAIRE":
            return VeterinaireFactory()

        elif role == "DRESSEUR":
            return DresseurFactory()

        elif role == "GARDE":
            return GardeFactory()

        else:
            raise ValueError("Role non supporté")