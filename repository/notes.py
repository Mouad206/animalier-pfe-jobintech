class Note:
    def __init__(self, beneficiaire, commentaire: str, note: float):
        self.beneficiaire = beneficiaire
        self.commentaire = commentaire
        self.note = note  # 1 à 5 par exemple