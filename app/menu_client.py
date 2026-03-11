from services.evaluation_service import EvaluationService
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
        print("14 Mes Evaluations")
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
            animaux = ClientService.voir_animaux(user["id"])

            print("\nChoisir un animal (optionnel)")

            if animaux:

                afficher_tableau(animaux)

                print("0 Aucun animal")

                choix = int(input("Choix : "))

                if choix == 0:
                    animal_id = None

                else:

                    animal_id = None

                    for a in animaux:
                        if a["id"] == choix:
                            animal_id = a["id"]
                            break

                    if animal_id is None:
                        print("❌ Animal invalide")
                        continue

            else:
                animal_id = None

            ClientService.creer_prestation(
                user["id"],
                service["profil_id"],
                service["id"],
                description,
                service["type_service"],
                animal_id
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
            prenom = input("Prénom : ")
            email = input("Email : ")
            telephone = input("Téléphone : ")
            adresse = input("Adresse : ")

            ClientService.modifier_profil(
                user["id"], nom, prenom, email, telephone, adresse
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
            print("Choisir type de service : ")
            type_service = {
                "1": "garde",
                "2": "dressage",
                "3": "veterinaire"
            }

            print("1. Garde")
            print("2. Dressage")
            print("3. Vétérinaire")

            choix_type = input("Choisir type de service : ")
            type_service = type_service.get(choix_type)

            if not type_service:
                print("Type de service invalide")
                continue

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
                    print("Toutes vos prestations terminées sont déjà évaluées.")
                    continue

                print("\n===== PRESTATIONS À ÉVALUER =====\n")

                for i, p in enumerate(prestations, 1):
                    print(i, "|", p["description"], "|", p["date_fin"], "|", p["nom"], p["prenom"])

                choix = int(input("\nChoisir prestation : "))

                if choix < 1 or choix > len(prestations):
                    print("Choix invalide")
                    continue

                prestation = prestations[choix-1]

                note = int(input("Note (1-5) : "))
                commentaire = input("Commentaire : ")

                ClientService.evaluer_prestation(prestation["id"], user["id"], note, commentaire)
                
        elif choix == "14":

            evaluations = EvaluationService.evaluation_client(user["id"])
 
            if not evaluations:
                print("Vous n'avez pas encore fait d'évaluation.")
                continue

            print("\n===== MES ÉVALUATIONS =====\n")

            for eval in evaluations:
                print(f"Prestation ID: {eval['prestation_id']} | Note: {eval['note']} | Commentaire: {eval['commentaire']}")

        elif choix == "0":
            break