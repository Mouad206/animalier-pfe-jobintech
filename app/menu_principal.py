from services.auth_service import AuthService
from services.inscription_service import InscriptionService

from app.menu_admin import menu_admin
from app.menu_client import menu_client
from app.menu_profil import menu_profil
from app.menu_inscription_profil import menu_inscription_profil
from getpass import getpass


def menu_principal():

    while True:

        print("\n===== APPLICATION SERVICE ANIMALIER =====")
        print("1. Se connecter")
        print("2. Créer un compte")
        print("0. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            login()

        elif choix == "2":
            register()

        elif choix == "0":
            print("Au revoir")
            break

        else:
            print("Choix invalide")


# =========================
# LOGIN
# =========================

def login():

    tentatives = 3

    while tentatives > 0:

        email = input("Email : ")
        password = getpass("Mot de passe : ")

        user = AuthService.login(email, password)

        if user:

            role = user["role"]

            print("Bienvenue", user["nom"], user["prenom"], "(", role, ")")

            if role == "ADMIN":
                menu_admin()

            elif role == "CLIENT":
                menu_client()

            elif role in ["VETERINAIRE", "DRESSEUR", "GARDE"]:

                # Vérifier si le profil professionnel existe
                if not InscriptionService.profil_existe(user["id"]):

                    print("\nVous devez compléter votre profil professionnel.")

                    menu_inscription_profil()

                # Accès au menu professionnel
                menu_profil()

            return

        else:
            tentatives -= 1
            print("Identifiants incorrects")

    print("Trop de tentatives échouées")


# =========================
# REGISTER
# =========================

def register():

    print("\n===== INSCRIPTION =====")

    nom = input("Nom : ")
    prenom = input("Prenom : ")
    email = input("Email : ")
    telephone = input("Téléphone : ")
    password = getpass("Mot de passe : ")

    print("\nChoisir un rôle :")
    print("1 CLIENT")
    print("2 VETERINAIRE")
    print("3 DRESSEUR")
    print("4 GARDE")

    choix = input("Choix : ")

    roles = {
        "1": "CLIENT",
        "2": "VETERINAIRE",
        "3": "DRESSEUR",
        "4": "GARDE"
    }

    role = roles.get(choix)

    if not role:
        print("Rôle invalide")
        return

    AuthService.register(
        nom,
        prenom,
        email,
        telephone,
        password,
        role
    )

    print("Compte créé avec succès")