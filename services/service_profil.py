from repository.profil_repository_service import ProfilRepositoryService
from services.abonnement_service import AbonnementService


class ProfilService:

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def voir_prestations(profil_id):

        return ProfilRepositoryService.get_prestations(profil_id)


    @staticmethod
    def modifier_statut_prestation(prestation_id, statut):

        ProfilRepositoryService.update_prestation_statut(
            prestation_id,
            statut
        )

    # =========================
    # NOTIFICATIONS
    # =========================

    @staticmethod
    def voir_notifications(profil_id):

        return ProfilRepositoryService.get_notifications(profil_id)

    # =========================
    # PROFIL
    # =========================

    @staticmethod
    def voir_profil(profil_id):

        return ProfilRepositoryService.get_profil(profil_id)


    @staticmethod
    def modifier_profil(profil_id, nom, email, telephone, adresse, disponibilite):

        ProfilRepositoryService.update_profil(
            profil_id,
            nom,
            email,
            telephone,
            adresse,
            disponibilite
        )

    # =========================
    # ABONNEMENT
    # =========================

    @staticmethod
    def payer_abonnement(profil_id, type_abonnement, montant):

        return AbonnementService.payer_abonnement(profil_id, type_abonnement, montant)


    @staticmethod
    def voir_abonnement(profil_id):

        return ProfilRepositoryService.get_abonnement(profil_id)

    # =========================
    # DASHBOARD
    # =========================

    @staticmethod
    def dashboard(profil_id):

        return {
            "prestations_attente":
                ProfilRepositoryService.count_prestations_attente(profil_id),

            "prestations_terminees":
                ProfilRepositoryService.count_prestations_terminees(profil_id),

            "note_moyenne":
                ProfilRepositoryService.moyenne_note(profil_id),

            "abonnement":
                ProfilRepositoryService.get_abonnement(profil_id)
        }