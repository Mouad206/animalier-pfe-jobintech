class Prestation:

    def __init__(
        self,
        type_service,
        description,
        date_debut,
        client_id,
        profil_id,
        statut="EN_ATTENTE",
        date_fin=None,
        id=None
    ):

        self.id = id
        self.type_service = type_service
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.statut = statut
        self.client_id = client_id
        self.profil_id = profil_id