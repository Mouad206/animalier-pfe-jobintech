from models.dresseur import Dresseur
from models.garde import Garde
from models.veterinaire import Veterinaire


class InscriptionService:

    @staticmethod
    def creer_dresseur(data, session):
        dresseur = Dresseur(**data)
        session.add(dresseur)
        session.commit()
        return dresseur

    @staticmethod
    def creer_garde(data, session):
        garde = Garde(**data)
        session.add(garde)
        session.commit()
        return garde

    @staticmethod
    def creer_veterinaire(data, session):
        veterinaire = Veterinaire(**data)
        session.add(veterinaire)
        session.commit()
        return veterinaire