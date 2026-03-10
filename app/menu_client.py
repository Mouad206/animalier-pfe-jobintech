from services.service_client import ClientService
from services.auth_service import AuthService
from utils.console_table import afficher_tableau
from getpass import getpass


def menu_client():

    user = AuthService.get_current_user()

    while True:

        print("\n========= MENU CLIENT =========")
        print("1  Mes prestations")
        print("2  Ajouter prestation")
        print("3  Mes animaux")
        print("4  Ajouter animal")
        print("5  Modifier animal")
        print("6  Supprimer animal")
        print("7  Mon compte")
        print("8  Modifier mon compte")
        print("9  Modifier mot de passe")
        print("10 Catalogue complet")
        print("11 Catalogue par type")
        print("12 Catalogue d'un profil")
        print("13 Évaluer prestation terminée")
        print("0  Déconnexion")

        choix = input("\nChoix : ")

        # =====================
        # PRESTATIONS
        # =====================

        if choix == "1":

            prestations = ClientService.voir_prestations(user["id"])

            print("\n===== MES PRESTATIONS =====")
            afficher_tableau(prestations)

        elif choix == "2":

            catalogue = ClientService.consulter_catalogue()

            print("\n===== SERVICES DISPONIBLES =====")
            afficher_tableau(catalogue)

            choix_service = int(input("Choisir service : "))
            service = catalogue[choix_service-1]

            description = input("Description : ")

            ClientService.creer_prestation(
                user["id"],
                service["profil_id"],
                service["id"],
                description,
                service["type_service"]
            )

        # =====================
        # ANIMAUX
        # =====================

        elif choix == "3":

            animaux = ClientService.voir_animaux(user["id"])

            print("\n===== MES ANIMAUX =====")
            afficher_tableau(animaux)

        elif choix == "4":

            nom = input("Nom : ")
            espece = input("Espèce : ")
            race = input("Race : ")
            age = input("Âge : ")

            ClientService.ajouter_animal(
                nom, espece, race, age, user["id"]
            )

        elif choix == "5":

            animaux = ClientService.voir_animaux(user["id"])
            afficher_tableau(animaux)

            choix = int(input("Choisir animal : "))
            animal = animaux[choix-1]

            nom = input("Nouveau nom : ")
            espece = input("Espèce : ")
            race = input("Race : ")
            age = input("Âge : ")

            ClientService.modifier_animal(
                animal["id"], nom, espece, race, age
            )

        elif choix == "6":

            animaux = ClientService.voir_animaux(user["id"])
            afficher_tableau(animaux)

            choix = int(input("Choisir animal : "))
            animal = animaux[choix-1]

            ClientService.supprimer_animal(animal["id"])

        # =====================
        # PROFIL
        # =====================

        elif choix == "7":

            profil = ClientService.voir_profil(user["id"])

            print("\n===== MON PROFIL =====")
            afficher_tableau([profil])

        elif choix == "8":

            nom = input("Nom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")
            adresse = input("Adresse : ")

            ClientService.modifier_profil(
                user["id"], nom, email, telephone, adresse
            )

        elif choix == "9":

            nouveau_mdp = getpass("Nouveau mot de passe : ")

            success = AuthService.update_password(
                user["email"],
                nouveau_mdp
            )

            if success:
                print("✅ Mot de passe modifié")
            else:
                print("❌ Erreur modification")

        # =====================
        # CATALOGUE
        # =====================

        elif choix == "10":

            catalogue = ClientService.consulter_catalogue()

            print("\n===== CATALOGUE =====")
            afficher_tableau(catalogue)

        elif choix == "11":

            type_service = input("Type (VETERINAIRE/DRESSEUR/GARDE) : ")

            catalogue = ClientService.consulter_catalogue_par_type(type_service)

            afficher_tableau(catalogue)

        elif choix == "12":

            profils = ClientService.profils_disponibles()

            afficher_tableau(profils)

            choix = int(input("Choisir profil : "))
            profil = profils[choix-1]

            catalogue = ClientService.consulter_catalogue_profil(profil["utilisateur_id"])

            afficher_tableau(catalogue)

        # =====================
        # EVALUATION
        # =====================

        elif choix == "13":

            prestations = ClientService.prestations_a_evaluer(user["id"])

            if not prestations:
                print("Aucune prestation à évaluer")
                continue

            afficher_tableau(prestations)

            choix = int(input("Choisir prestation : "))
            prestation = prestations[choix-1]

            note = int(input("Note (1-5) : "))
            commentaire = input("Commentaire : ")

            ClientService.evaluer_prestation(
                prestation["id"],
                user["id"],
                note,
                commentaire
            )

        elif choix == "0":
            break