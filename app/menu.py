from services.auth_service import AuthService
from services.service_adminsitrateur import ServiceAdministrateur
from services.service_client import ServiceClient
from services.evaluation_veterinaire_service import EvaluationVeterinaire
from services.evaluation_dresseur_service import EvaluationDresseur
from services.evaluation_garde_service import EvaluationGarde



# ===============================
# MENU PRINCIPAL
# ===============================
def menu_principal():

    while True:

        print("\n===== AniService Home =====")
        print("1️⃣  Créer un compte")
        print("2️⃣  Se connecter")
        print("3️⃣  Quitter")

        choix = input("Choix : ")

        if choix == "1":
            register_menu()

        elif choix == "2":
            login_menu()

        elif choix == "3":
            print("Au revoir 👋")
            break

        else:
            print("Choix invalide")


# ===============================
# REGISTER
# ===============================
def register_menu():

    print("\n=== Création compte ===")

    nom = input("Nom : ")
    prenom = input("Prénom : ")
    email = input("Email : ")
    telephone = input("Téléphone : ")
    password = input("Mot de passe : ")

    print("Rôles disponibles : CLIENT / VETERINAIRE / DRESSEUR / GARDE")
    role = input("Rôle : ").upper()

    AuthService.register(
        nom,
        prenom,
        email,
        telephone,
        password,
        role
    )


# ===============================
# LOGIN
# ===============================
def login_menu():

    print("\n=== Connexion ===")

    email = input("Email : ")
    password = input("Mot de passe : ")

    role = AuthService.login(email, password)

    if role == "ADMIN":
        menu_admin()

    elif role == "CLIENT":
        menu_client()

    elif role == "VETERINAIRE":
        menu_veterinaire()

    elif role == "DRESSEUR":
        menu_dresseur()

    elif role == "GARDE":
        menu_garde()

    else:
        print("Connexion échouée")


# ===============================
# MENU ADMIN
# ===============================
def menu_admin():

    while True:

        print("\n===== MENU ADMIN =====")
        print("1️⃣ Dashboard")
        print("2️⃣ Voir clients")
        print("3️⃣ Déconnexion")

        choix = input("Choix : ")

        if choix == "1":

            dashboard = ServiceAdministrateur.voir_dashboard()

            print("\n📊 Dashboard")
            print("Clients :", dashboard["clients"])
            print("Vétérinaires :", dashboard["veterinaires"])
            print("Dresseurs :", dashboard["dresseurs"])
            print("Gardes :", dashboard["gardes"])
            print("Prestations :", dashboard["prestations"])

        elif choix == "2":

            clients = ServiceAdministrateur.voir_clients_inscrits()

            for c in clients:
                print(c)

        elif choix == "3":

            AuthService.logout()
            break


# ===============================
# MENU CLIENT
# ===============================
def menu_client():

    while True:

        print("\n===== MENU CLIENT =====")
        print("1️⃣ Voir mes prestations")
        print("2️⃣ Créer prestation")
        print("3️⃣ Évaluer prestation")
        print("4️⃣ Ajouter animal")
        print("5️⃣ Voir mes animaux")
        print("6️⃣ Modifier profil")
        print("7️⃣ Déconnexion")

        choix = input("Choix : ")

        # ===============================
        # Voir prestations
        # ===============================
        if choix == "1":

            prestations = ServiceClient.voir_prestations()

            print("\n--- Prestations vétérinaire ---")
            for p in prestations["veterinaire"]:
                print(p)

            print("\n--- Prestations dressage ---")
            for p in prestations["dressage"]:
                print(p)

            print("\n--- Prestations garde ---")
            for p in prestations["garde"]:
                print(p)

        # ===============================
        # Créer prestation
        # ===============================
        elif choix == "2":

            print("\nType prestation :")
            print("1 Veterinaire")
            print("2 Dressage")
            print("3 Garde")

            type_prestation = input("Choix : ")

            if type_prestation == "1":

                veterinaire_id = input("ID vétérinaire : ")
                type_service = input("Type service : ")
                date = input("Date début : ")

                ServiceClient.demander_veterinaire(
                    veterinaire_id,
                    type_service,
                    date
                )

            elif type_prestation == "2":

                dresseur_id = input("ID dresseur : ")
                type_service = input("Type dressage : ")
                date = input("Date début : ")

                ServiceClient.demander_dressage(
                    dresseur_id,
                    type_service,
                    date
                )

            elif type_prestation == "3":

                garde_id = input("ID garde : ")
                date_debut = input("Date début : ")
                date_fin = input("Date fin : ")

                ServiceClient.demander_garde(
                    garde_id,
                    date_debut,
                    date_fin
                )

        # ===============================
        # Evaluation
        # ===============================
        elif choix == "3":

            print("\nType prestation :")
            print("1 Veterinaire")
            print("2 Dressage")
            print("3 Garde")

            type_eval = input("Choix : ")

            prestation_id = int(input("ID prestation : "))
            note = int(input("Note (1-5) : "))
            commentaire = input("Commentaire : ")

            client_id = AuthService.current_user["id"]

            if type_eval == "1":

                evaluation = EvaluationVeterinaire(
                    note,
                    commentaire,
                    prestation_id,
                    client_id
                )

                evaluation.sauvegarder()

            elif type_eval == "2":

                evaluation = EvaluationDresseur(
                    note,
                    commentaire,
                    prestation_id,
                    client_id
                )

                evaluation.sauvegarder()

            elif type_eval == "3":

                evaluation = EvaluationGarde(
                    note,
                    commentaire,
                    prestation_id,
                    client_id
                )

                evaluation.sauvegarder()

            print("✅ Evaluation enregistrée")

        # ===============================
        # Ajouter animal
        # ===============================
        elif choix == "4":

            nom = input("Nom animal : ")
            espece = input("Espèce : ")
            race = input("Race : ")
            age = input("Age : ")

            ServiceClient.ajouter_animal(
                nom,
                espece,
                race,
                age
            )

        # ===============================
        # Voir animaux
        # ===============================
        elif choix == "5":

            animaux = ServiceClient.voir_animaux()

            print("\n--- Mes animaux ---")

            for a in animaux:
                print(a)

        # ===============================
        # Modifier profil
        # ===============================
        elif choix == "6":

            nom = input("Nom : ")
            prenom = input("Prénom : ")
            telephone = input("Téléphone : ")

            ServiceClient.modifier_profil(
                nom,
                prenom,
                telephone
            )

        # ===============================
        # Logout
        # ===============================
        elif choix == "7":

            AuthService.logout()
            break

        else:
            print("Choix invalide")


# ===============================
# MENU VETERINAIRE
# ===============================
def menu_veterinaire():

    while True:

        print("\n===== MENU VETERINAIRE =====")
        print("1️⃣ Voir mes prestations")
        print("2️⃣ Déconnexion")

        choix = input("Choix : ")

        if choix == "1":
            print("Liste prestations vétérinaire")

        elif choix == "2":
            AuthService.logout()
            break


# ===============================
# MENU DRESSEUR
# ===============================
def menu_dresseur():

    while True:

        print("\n===== MENU DRESSEUR =====")
        print("1️⃣ Voir mes prestations")
        print("2️⃣ Déconnexion")

        choix = input("Choix : ")

        if choix == "1":
            print("Liste prestations dressage")

        elif choix == "2":
            AuthService.logout()
            break


# ===============================
# MENU GARDE
# ===============================
def menu_garde():

    while True:

        print("\n===== MENU GARDE =====")
        print("1️⃣ Voir mes prestations")
        print("2️⃣ Déconnexion")

        choix = input("Choix : ")

        if choix == "1":
            print("Liste prestations garde")

        elif choix == "2":
            AuthService.logout()
            break