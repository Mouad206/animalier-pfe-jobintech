from datetime import datetime


class Historique:

    def __init__(self, action, utilisateur_id):
        self.action = action
        self.utilisateur_id = utilisateur_id
        self.date_action = datetime.now()