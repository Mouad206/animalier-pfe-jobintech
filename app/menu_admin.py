from services.admin_service import AdminService
from utils.console_table import afficher_tableau


def menu_admin():

    while True:

        print("\n===== MENU ADMIN =====")
        print("1 Voir utilisateurs")
        print("2 Créer utilisateur")
        print("3 Modifier utilisateur")
        print("4 Supprimer utilisateur")
        print("5 Changer rôle utilisateur")

        print("\n6 Voir profils")
        print("7 Supprimer profil")

        print("\n8 Voir prestations")
        print("9 Supprimer prestation")

        print("\n10 Voir notifications")
        print("11 Supprimer notification")

        print("\n12 Voir historique")
        print("13 Vider historique")

        print("\n14 Voir logs")
        print("15 Vider logs")

        print("\n16 Dashboard")

        print("\n0 Déconnexion")

        choix = input("Choix : ")

        # =========================
        # UTILISATEURS
        # =========================

        if choix == "1":

            users = AdminService.voir_utilisateurs()

            print("\n===== UTILISATEURS =====")

            if not users:
                print("Aucun utilisateur")
                continue

            afficher_tableau(users)

        elif choix == "2":

            print("\nCréer utilisateur")

            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")
            password = input("Mot de passe : ")
            # role = input("Role (ADMIN / CLIENT / VETERINAIRE / DRESSEUR / GARDE) : ")
            print("Rôle : 1 ADMIN, 2 CLIENT, 3 VETERINAIRE, 4 DRESSEUR, 5 GARDE")
            role = {
                "1": "ADMIN",
                "2": "CLIENT",
                "3": "VETERINAIRE",
                "4": "DRESSEUR",
                "5": "GARDE"
            }
            role_input = input("Choix rôle : ")
            role = role.get(role_input)

            AdminService.creer_utilisateur(
                nom, prenom, email, telephone, password, role
            )

        elif choix == "3":

            users = AdminService.voir_utilisateurs()

            afficher_tableau(users)

            choix_user = int(input("Choisir utilisateur : "))

            if choix_user < 1 or choix_user > len(users):
                print("Choix invalide")
                continue

            user = users[choix_user-1]

            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")

            AdminService.modifier_utilisateur(
                user["id"], nom, prenom, email, telephone
            )

        elif choix == "4":

            users = AdminService.voir_utilisateurs()

            afficher_tableau(users)

            choix_user = int(input("Choisir utilisateur : "))

            if choix_user < 1 or choix_user > len(users):
                print("Choix invalide")
                continue

            user = users[choix_user-1]

            AdminService.supprimer_utilisateur(user["id"])

        elif choix == "5":

            users = AdminService.voir_utilisateurs()

            afficher_tableau(users)

            choix_user = int(input("Choisir utilisateur : "))

            if choix_user < 1 or choix_user > len(users):
                print("Choix invalide")
                continue

            user = users[choix_user-1]

            role = input("Nouveau rôle : ")

            AdminService.changer_role(user["id"], role)

        # =========================
        # PROFILS
        # =========================

        elif choix == "6":

            profils = AdminService.voir_profils()

            print("\n===== PROFILS =====")

            afficher_tableau(profils)

        elif choix == "7":

            profils = AdminService.voir_profils()

            afficher_tableau(profils)

            choix_p = int(input("Choisir profil : "))

            if choix_p < 1 or choix_p > len(profils):
                print("Choix invalide")
                continue

            profil = profils[choix_p-1]

            AdminService.supprimer_profil(profil["utilisateur_id"])

        # =========================
        # PRESTATIONS
        # =========================

        elif choix == "8":

            prestations = AdminService.voir_prestations()

            print("\n===== PRESTATIONS =====")

            afficher_tableau(prestations)

        elif choix == "9":

            prestations = AdminService.voir_prestations()

            afficher_tableau(prestations)

            choix_p = int(input("Choisir prestation : "))

            if choix_p < 1 or choix_p > len(prestations):
                print("Choix invalide")
                continue

            prestation = prestations[choix_p-1]

            AdminService.supprimer_prestation(prestation["id"])

        # =========================
        # NOTIFICATIONS
        # =========================

        elif choix == "10":

            notifications = AdminService.voir_notifications()

            afficher_tableau(notifications)

        elif choix == "11":

            notifications = AdminService.voir_notifications()

            afficher_tableau(notifications)

            choix_n = int(input("Choisir notification : "))

            if choix_n < 1 or choix_n > len(notifications):
                print("Choix invalide")
                continue

            notification = notifications[choix_n-1]

            AdminService.supprimer_notification(notification["id"])

        # =========================
        # HISTORIQUE
        # =========================

        elif choix == "12":

            historique = AdminService.voir_historique()

            afficher_tableau(historique)

        elif choix == "13":

            confirm = input("Confirmer suppression historique (oui/non) : ")

            if confirm == "oui":
                AdminService.vider_historique()

        # =========================
        # LOGS
        # =========================

        elif choix == "14":

            logs = AdminService.voir_logs()

            afficher_tableau(logs)

        elif choix == "15":

            confirm = input("Confirmer suppression logs (oui/non) : ")

            if confirm == "oui":
                AdminService.vider_logs()

        # =========================
        # DASHBOARD
        # =========================

        elif choix == "16":

            stats = AdminService.dashboard()

            print("\n===== DASHBOARD =====")

            data = [
                {"Statistique": k, "Valeur": v}
                for k, v in stats.items()
            ]

            afficher_tableau(data)

        elif choix == "0":
            print("Déconnexion admin")
            break

        else:
            print("Choix invalide")