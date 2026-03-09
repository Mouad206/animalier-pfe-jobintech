class Notification:

    def __init__(self, utilisateur_id, message, statut="NON_LUE", id=None):
        self.id = id
        self.utilisateur_id = utilisateur_id
        self.message = message
        self.statut = statut