from repository.admin_repository import AdminRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig


class AdminService:

    logger = LoggerConfig.getInstance()

    # =========================
    # UTILISATEURS
    # =========================

    @staticmethod
    def voir_utilisateurs():
        return AdminRepository.get_all_users()


    @staticmethod
    def creer_utilisateur(nom, prenom, email, telephone, mot_de_passe, role):

        AdminRepository.create_user(
            nom,
            prenom,
            email,
            telephone,
            mot_de_passe,
            role
        )

        AdminService.logger.log(
            "INFO",
            None,
            f"Admin a créé l'utilisateur {email}"
        )


    @staticmethod
    def modifier_utilisateur(user_id, nom, prenom, email, telephone):

        AdminRepository.update_user(
            user_id,
            nom,
            prenom,
            email,
            telephone
        )

        HistoriqueService.enregistrer_action(
            user_id,
            "Modification utilisateur"
        )


    @staticmethod
    def supprimer_utilisateur(user_id):

        AdminRepository.delete_user(user_id)

        AdminService.logger.log(
            "WARNING",
            user_id,
            "Utilisateur supprimé par admin"
        )


    @staticmethod
    def changer_role(user_id, role):

        AdminRepository.change_role(user_id, role)

        HistoriqueService.enregistrer_action(
            user_id,
            f"Changement rôle vers {role}"
        )

    # =========================
    # PROFILS
    # =========================

    @staticmethod
    def voir_profils():
        return AdminRepository.get_all_profils()


    @staticmethod
    def supprimer_profil(profil_id):

        AdminRepository.delete_profil(profil_id)

        AdminService.logger.log(
            "WARNING",
            profil_id,
            "Profil supprimé par admin"
        )

    # =========================
    # PRESTATIONS
    # =========================

    @staticmethod
    def voir_prestations():
        return AdminRepository.get_all_prestations()


    @staticmethod
    def supprimer_prestation(prestation_id):

        AdminRepository.delete_prestation(prestation_id)

        AdminService.logger.log(
            "WARNING",
            None,
            f"Prestation {prestation_id} supprimée"
        )

    # =========================
    # NOTIFICATIONS
    # =========================

    @staticmethod
    def voir_notifications():
        return AdminRepository.get_all_notifications()


    @staticmethod
    def supprimer_notification(notification_id):

        AdminRepository.delete_notification(notification_id)

        AdminService.logger.log(
            "INFO",
            None,
            f"Notification {notification_id} supprimée"
        )

    # =========================
    # HISTORIQUE
    # =========================

    @staticmethod
    def voir_historique():
        return AdminRepository.get_historique()


    @staticmethod
    def vider_historique():

        AdminRepository.delete_historique()

        AdminService.logger.log(
            "WARNING",
            None,
            "Historique supprimé par admin"
        )

    # =========================
    # LOGS
    # =========================

    @staticmethod
    def voir_logs():
        return AdminRepository.get_logs()


    @staticmethod
    def vider_logs():

        AdminRepository.delete_logs()

        AdminService.logger.log(
            "WARNING",
            None,
            "Logs supprimés par admin"
        )

    # =========================
    # DASHBOARD
    # =========================

    @staticmethod
    def dashboard():

        stats = {
            "users": AdminRepository.count_users(),
            "clients": AdminRepository.count_clients(),
            "profils": AdminRepository.count_profils(),

            "profils_abonnes": AdminRepository.count_profils_abonnes(),
            "profils_non_abonnes": AdminRepository.count_profils_non_abonnes(),

            "prestations": AdminRepository.count_prestations(),
            "prestations_terminees": AdminRepository.count_prestations_terminees(),

            "notifications": AdminRepository.count_notifications(),
            "evaluations": AdminRepository.count_evaluations(),

            "animaux": AdminRepository.count_animaux(),

            "note_moyenne": AdminRepository.moyenne_evaluations(),
            "revenus": AdminRepository.revenus_generes()
        }

        return stats