from services.auth_service import AuthService
from app.menu import admin_menu, client_menu, veterinaire_menu, garde_menu


def main():
    while True:
        print("\n=== AUTHENTIFICATION ===")
        print("1. Créer un compte")
        print("2. Login")
        print("0. Sortir")

        choix = input("Choix: ")

        # ==========================
        # CREATION DE COMPTE
        # ==========================
        if choix == "1":
            print("\n--- Création de compte ---")
            nom = input("Nom: ")
            email = input("Email: ")
            password = input("Mot de passe: ")

            print("\nChoisir rôle:")
            print("1. Client")
            print("2. Vétérinaire")
            print("3. Garde")

            role_choice = input("Choix: ")

            role_map = {
                "1": "client",
                "2": "veterinaire",
                "3": "garde"
            }

            if role_choice not in role_map:
                print("Rôle invalide.")
                continue

            AuthService.register(nom, email, password, role_map[role_choice])
            print("Compte créé avec succès.")

        # ==========================
        # LOGIN
        # ==========================
        elif choix == "2":
            print("\n--- Login ---")
            email = input("Email: ")
            password = input("Mot de passe: ")

            user = AuthService.login(email, password)

            if not user:
                print("Identifiants incorrects.")
                continue

            print(f"\nBienvenue {user.nom} ({user.role.value})")

            # Redirection selon rôle
            if user.role.value == "admin":
                admin_menu()
            elif user.role.value == "client":
                client_menu()
            elif user.role.value == "veterinaire":
                veterinaire_menu()
            elif user.role.value == "garde":
                garde_menu()

        # ==========================
        # SORTIR
        # ==========================
        elif choix == "0":
            print("Au revoir 👋")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
    
    