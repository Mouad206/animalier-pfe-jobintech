from factories.service_factory import Service_factory
from models.veterinaire import Veterinaire
from abc import ABC, abstractmethod

class VeterinaireFactory(Service_factory):

    def creer_service(self, **kwargs):
        return Veterinaire(
            nom=kwargs.get("nom"),
            email=kwargs.get("email"),
            profil=kwargs.get("profil"),
            certification=kwargs.get("certification"),
            annee_experience=kwargs.get("experience"),
            raison_sociale=kwargs.get("raison_sociale"),
            tarif_abonnement=kwargs.get("tarif_abonnement"),
            adresse=kwargs.get("adresse"),
            telephone=kwargs.get("telephone"),
            disponibilité=kwargs.get("disponibilité")
        )