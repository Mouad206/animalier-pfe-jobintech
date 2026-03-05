from models.prestation import Prestation


class PrestationVeterinaire(Prestation):

    def __init__(self, id, date_debut, date_fin, statut,
                 client_id, animal_id, veterinaire_id):

        super().__init__(id, date_debut, date_fin, statut, client_id, animal_id)

        self.veterinaire_id = veterinaire_id