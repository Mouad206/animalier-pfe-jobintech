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
        print("5 Modifier statut prestation")
        print("6 Voir catalogue")
        print("7 Créer service catalogue")
        print("8 Modifier service catalogue")
        print("9 Supprimer service catalogue")
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
            
        elif choix == "5":
            prestation_id = input("ID de la prestation : ")
            print("Statuts possibles :")
            print("1. EN_COURS")
            print("2. TERMINEE")
            print("3. ANNULEE")
            statut_choice = input("Choix : ")
            statuts = {
                "1": "EN_COURS",
                "2": "TERMINEE",
                "3": "ANNULEE"
            }
            statut = statuts.get(statut_choice)

            if not statut:
                print("❌ Statut invalide")
                continue

            ProfilService.modifier_statut_prestation(prestation_id, statut)
            
        elif choix == "6":
            
            profil_id = user["id"]

            catalogue = ProfilService.consulter_catalogue_profil(profil_id)

            for c in catalogue:
                print(c)
        
        elif choix == "7":

            nom = input("Nom du service : ")
            description = input("Description du service : ")
            type_service = input("Type de service (VETERINAIRE, DRESSEUR, GARDE) : ")

            ProfilService.creer_service_catalogue(nom, description, type_service)
        

        elif choix == "8":
            service_id = input("ID du service à modifier : ")
            nom = input("Nouveau nom du service : ")
            description = input("Nouvelle description du service : ")
            type_service = input("Nouveau type de service (VETERINAIRE, DRESSEUR, GARDE) : ")

            ProfilService.modifier_service_catalogue(service_id, nom, description, type_service)

        elif choix == "0":
            break