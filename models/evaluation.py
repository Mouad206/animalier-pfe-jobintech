class Evaluation():

    def __init__(self, note, commentaire, prestation_id, client_id, id=None):

        self.id = id
        self.note = note
        self.commentaire = commentaire
        self.prestation_id = prestation_id
        self.client_id = client_id