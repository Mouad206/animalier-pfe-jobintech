from models.catalogue import Catalogue


class CatalogueVeterinaire(Catalogue):

    def __init__(self, id, type_service, tarif, description, veterinaire_id):
        super().__init__(id, type_service, tarif, description)
        self.veterinaire_id = veterinaire_id