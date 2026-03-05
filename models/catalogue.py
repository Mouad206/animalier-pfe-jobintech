from abc import ABC
class Catalogue(ABC):

    def __init__(self, id, type_service, tarif, description):
        self.id = id
        self.type_service = type_service
        self.tarif = tarif
        self.description = description