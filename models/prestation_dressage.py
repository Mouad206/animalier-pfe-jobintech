from models.prestation import Prestation


class PrestationDressage(Prestation):

    def __init__(self, id, date_debut, date_fin, statut,
                 client_id, animal_id, dresseur_id):

        super().__init__(id, date_debut, date_fin, statut, client_id, animal_id)

        self.dresseur_id = dresseur_id