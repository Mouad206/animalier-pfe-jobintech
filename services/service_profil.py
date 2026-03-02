from models.dresseur import Dresseur
from models.garde import Garde
from models.veterinaire import Veterinaire


class ServiceFournisseur:

    @staticmethod
    def payer_abonnement(fournisseur, session):
        fournisseur.statut_abonnement = "ACTIF"
        session.commit()

    @staticmethod
    def consulter_historique(fournisseur, session):
        return fournisseur.prestations

    @staticmethod
    def creer_service(fournisseur, type_service, data, session):
       pass