from models.prestation import Prestation


class PrestationGarde(Prestation):

    def __init__(self, id, date_debut, date_fin, statut,
                 client_id, animal_id, garde_id):

        super().__init__(id, date_debut, date_fin, statut, client_id, animal_id)

        self.garde_id = garde_id