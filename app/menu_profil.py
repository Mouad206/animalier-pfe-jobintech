from services.catalogue_service import CatalogueService
from services.service_profil import ProfilService
from services.auth_service import AuthService
from utils.console_table import afficher_tableau


def menu_profil():

    user = AuthService.get_current_user()

    while True:

        print("\n===== MENU PROFIL =====")
        print("1 Voir prestations")
        print("2 Voir notifications")
        print("3 Voir dashboard")
        print("4 Payer abonnement")
        print("5 Modifier statut prestation")
        print("6 Voir catalogue")
        print("7 Créer service catalogue")
        print("8 Modifier service catalogue")
        print("9 Supprimer service catalogue")
        print("0 Déconnexion")

        choix = input("Choix : ")

        # =====================
        # PRESTATIONS
        # =====================

        if choix == "1":

            prestations = ProfilService.voir_prestations(user["id"])

            if not prestations:
                print("Aucune prestation")
                continue

            print("\n===== MES PRESTATIONS =====")
            afficher_tableau(prestations)

        # =====================
        # NOTIFICATIONS
        # =====================

        elif choix == "2":

            notifications = ProfilService.voir_notifications(user["id"])

            if not notifications:
                print("Aucune notification")
                continue

            print("\n===== MES NOTIFICATIONS =====")
            afficher_tableau(notifications)

        # =====================
        # DASHBOARD
        # =====================

        elif choix == "3":

                stats = ProfilService.dashboard(user["id"])

                print("\n===== DASHBOARD =====")

                abonnement = stats["abonnement"]

                if abonnement:
                    dernier_abonnement = abonnement[-1]  # dernier abonnement
                    type_abonnement = dernier_abonnement["type_abonnement"]
                    statut_abonnement = dernier_abonnement["statut"]
                    date_fin = dernier_abonnement["date_fin"]
                else:
                    type_abonnement = "Aucun"
                    statut_abonnement = "INACTIF"
                    date_fin = "-"

                data = [
                    {"Statistique": "Prestations en attente", "Valeur": stats["prestations_attente"]},
                    {"Statistique": "Prestations terminées", "Valeur": stats["prestations_terminees"]},
                    {"Statistique": "Note moyenne", "Valeur": stats["note_moyenne"]},
                    {"Statistique": "Type abonnement", "Valeur": type_abonnement},
                    {"Statistique": "Statut abonnement", "Valeur": statut_abonnement},
                    {"Statistique": "Date fin abonnement", "Valeur": date_fin},
                ]

                afficher_tableau(data)

        # =====================
        # ABONNEMENT
        # =====================

        elif choix == "4":

            print("\nTypes d'abonnement :")
            print("1 Basic - 200/mois")
            print("2 Premium - 500/mois")

            type_abonnement = {
                "1": "BASIC",
                "2": "PREMIUM"
            }

            choix_abonnement = input("Choix : ")

            type_abonnement = type_abonnement.get(choix_abonnement)

            montant = float(input("Montant à payer : "))

            ProfilService.payer_abonnement(user["id"], type_abonnement, montant)

        # =====================
        # MODIFIER STATUT PRESTATION
        # =====================

        elif choix == "5":

            prestations = ProfilService.voir_prestations(user["id"])

            if not prestations:
                print("Aucune prestation")
                continue

            afficher_tableau(prestations)

            choix_p = int(input("Choisir prestation : "))

            if choix_p < 1 or choix_p > len(prestations):
                print("Choix invalide")
                continue

            prestation = prestations[choix_p-1]

            print("\nStatuts possibles :")
            print("1 EN_COURS")
            print("2 TERMINEE")
            print("3 ANNULEE")

            statut_choice = input("Choix : ")

            statuts = {
                "1": "EN_COURS",
                "2": "TERMINEE",
                "3": "ANNULEE"
            }

            statut = statuts.get(statut_choice)

            ProfilService.modifier_statut_prestation(prestation["id"], statut)

        # =====================
        # VOIR CATALOGUE
        # =====================

        elif choix == "6":

            catalogue = CatalogueService.consulter_catalogue_profil(user["id"])

            if not catalogue:
                print("Aucun service")
                continue

            print("\n===== MON CATALOGUE =====")

            afficher_tableau(catalogue)

        # =====================
        # CREER SERVICE
        # =====================

        elif choix == "7":

            print("\nTypes de service :")
            print("1 VETERINAIRE")
            print("2 DRESSEUR")
            print("3 GARDE")

            type_service = {
                "1": "VETERINAIRE",
                "2": "DRESSEUR",
                "3": "GARDE"
            }

            type_choice = input("Choix : ")

            type_service = type_service.get(type_choice)

            nom_service = input("Nom du service : ")
            description = input("Description : ")
            tarif = float(input("Tarif : "))

            CatalogueService.ajouter_service(
                user["id"],
                type_service,
                nom_service,
                description,
                tarif
            )

        # =====================
        # MODIFIER SERVICE
        # =====================

        elif choix == "8":

            catalogue = CatalogueService.consulter_catalogue_profil(user["id"])

            if not catalogue:
                print("Aucun service")
                continue

            afficher_tableau(catalogue)

            choix_s = int(input("Choisir service : "))

            if choix_s < 1 or choix_s > len(catalogue):
                print("Choix invalide")
                continue

            service = catalogue[choix_s-1]

            nom_service = input("Nouveau nom : ")
            description = input("Nouvelle description : ")

            print("\nType de service")
            print("1 VETERINAIRE")
            print("2 DRESSEUR")
            print("3 GARDE")

            choix_type = input("Choix : ")

            types = {
                "1": "VETERINAIRE",
                "2": "DRESSEUR",
                "3": "GARDE"
            }

            type_service = types.get(choix_type)

            tarif = float(input("Nouveau tarif : "))

            CatalogueService.modifier_service(
                service["id"],
                nom_service,
                description,
                type_service,
                tarif
            )

        # =====================
        # SUPPRIMER SERVICE
        # =====================

        elif choix == "9":

            catalogue = CatalogueService.consulter_catalogue_profil(user["id"])

            if not catalogue:
                print("Aucun service")
                continue

            afficher_tableau(catalogue)

            choix_s = int(input("Choisir service : "))

            if choix_s < 1 or choix_s > len(catalogue):
                print("Choix invalide")
                continue

            service = catalogue[choix_s-1]

            CatalogueService.supprimer_service(service["id"])

        elif choix == "0":
            break