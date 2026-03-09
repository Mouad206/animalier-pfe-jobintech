class Abonnement:

    def __init__(self, profil_id, type_abonnement, montant,
                 date_debut, date_fin, statut="ACTIF", id=None):

        self.id = id
        self.profil_id = profil_id
        self.type_abonnement = type_abonnement
        self.montant = montant
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.statut = statut