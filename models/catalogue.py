class Catalogue:

    def __init__(self, profil_id, type_service, service_nom, description, tarif, id=None):

        self.id = id
        self.profil_id = profil_id
        self.type_service = type_service
        self.service_nom = service_nom
        self.description = description
        self.tarif = tarif