from services.admin_service import AdminService


def menu_admin():

    while True:

        print("\n===== MENU ADMIN =====")
        print("1. Voir utilisateurs")
        print("2. Créer utilisateur")
        print("3. Modifier utilisateur")
        print("4. Supprimer utilisateur")
        print("5. Changer rôle utilisateur")

        print("\n6. Voir profils")
        print("7. Supprimer profil")

        print("\n8. Voir prestations")
        print("9. Supprimer prestation")

        print("\n10. Voir notifications")
        print("11. Supprimer notification")

        print("\n12. Voir historique")
        print("13. Vider historique")

        print("\n14. Voir logs")
        print("15. Vider logs")

        print("\n16. Dashboard")
        
        print("\n17. Voir catalogue")
        print("\n18. Créer service catalogue")
        print("\n19. Modifier catalogue")
        print("\n20. Supprimer catalogue")

        print("\n0. Déconnexion")

        choix = input("Choix : ")

        # =========================
        # UTILISATEURS
        # =========================

        if choix == "1":

            users = AdminService.voir_utilisateurs()

            print("\n===== UTILISATEURS =====")
            for u in users:
                print(u)

        elif choix == "2":

            print("\nCréer utilisateur")

            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")
            password = input("Mot de passe : ")
            role = input("Role (ADMIN / CLIENT / VETERINAIRE / DRESSEUR / GARDE) : ")

            AdminService.creer_utilisateur(
                nom, prenom, email, telephone, password, role
            )

        elif choix == "3":

            user_id = input("ID utilisateur : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")

            AdminService.modifier_utilisateur(
                user_id, nom, prenom, email, telephone
            )

        elif choix == "4":

            user_id = input("ID utilisateur à supprimer : ")

            AdminService.supprimer_utilisateur(user_id)

        elif choix == "5":

            user_id = input("ID utilisateur : ")
            role = input("Nouveau rôle : ")

            AdminService.changer_role(user_id, role)

        # =========================
        # PROFILS
        # =========================

        elif choix == "6":

            profils = AdminService.voir_profils()

            print("\n===== PROFILS =====")
            for p in profils:
                print(p)

        elif choix == "7":

            profil_id = input("ID profil à supprimer : ")

            AdminService.supprimer_profil(profil_id)

        # =========================
        # PRESTATIONS
        # =========================

        elif choix == "8":

            prestations = AdminService.voir_prestations()

            print("\n===== PRESTATIONS =====")
            for p in prestations:
                print(p)

        elif choix == "9":

            prestation_id = input("ID prestation à supprimer : ")

            AdminService.supprimer_prestation(prestation_id)

        # =========================
        # NOTIFICATIONS
        # =========================

        elif choix == "10":

            notifications = AdminService.voir_notifications()

            print("\n===== NOTIFICATIONS =====")
            for n in notifications:
                print(n)

        elif choix == "11":

            notification_id = input("ID notification : ")

            AdminService.supprimer_notification(notification_id)

        # =========================
        # HISTORIQUE
        # =========================

        elif choix == "12":

            historique = AdminService.voir_historique()

            print("\n===== HISTORIQUE =====")
            for h in historique:
                print(h)

        elif choix == "13":

            confirm = input("Confirmer suppression historique (oui/non) : ")

            if confirm == "oui":
                AdminService.vider_historique()

        # =========================
        # LOGS
        # =========================

        elif choix == "14":

            logs = AdminService.voir_logs()

            print("\n===== LOGS =====")
            for l in logs:
                print(l)

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

            for k, v in stats.items():
                print(k, ":", v)

        elif choix == "0":
            print("Déconnexion admin")
            break

        else:
            print("Choix invalide")