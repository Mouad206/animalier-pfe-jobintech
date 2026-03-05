from models.catalogue import Catalogue


class CatalogueGarde(Catalogue):

    def __init__(self, id, type_service, tarif, description, garde_id):
        super().__init__(id, type_service, tarif, description)
        self.garde_id = garde_id