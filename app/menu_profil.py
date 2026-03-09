from services.service_profil import ProfilService
from services.auth_service import AuthService


def menu_profil():

    user = AuthService.get_current_user()

    while True:

        print("\n===== MENU PROFIL =====")
        print("1 Voir prestations")
        print("2 Voir notifications")
        print("3 Voir dashboard")
        print("4 Payer abonnement")
        print("0 Déconnexion")

        choix = input("Choix : ")

        if choix == "1":

            prestations = ProfilService.voir_prestations(user["id"])

            for p in prestations:
                print(p)

        elif choix == "2":

            notifications = ProfilService.voir_notifications(user["id"])

            for n in notifications:
                print(n)

        elif choix == "3":

            stats = ProfilService.dashboard(user["id"])

            for k, v in stats.items():
                print(k, ":", v)

        elif choix == "4":
            print("Types d'abonnement :")
            print("Entrez le numéro du type d'abonnement que vous souhaitez payer :")
            print("1. Basic - 200/mois")
            print("2. Premium - 500/mois")
            type_abonnement = {
                "1": "BASIC",
                "2": "PREMIUM"
            }
            choix_abonnement = input("Choix : ")
            type_abonnement = type_abonnement.get(choix_abonnement)
            montant = float(input("Entrez le montant à payer : "))
            ProfilService.payer_abonnement(user["id"],type_abonnement, montant, )

        elif choix == "0":
            break