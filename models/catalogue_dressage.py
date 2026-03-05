from models.catalogue import Catalogue
class CatalogueDresseur(Catalogue):

    def __init__(self, id, type_service, tarif, description, dresseur_id):
        super().__init__(id, type_service, tarif, description)
        self.dresseur_id = dresseur_id