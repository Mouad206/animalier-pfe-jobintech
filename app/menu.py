# app/menu.py

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Dashboard")
        print("2. Ajouter utilisateur")
        print("3. Modifier utilisateur")
        print("4. Supprimer utilisateur")
        print("0. Déconnexion")

        choix = input("Choix: ")

        if choix == "1":
            print("Dashboard...")
        elif choix == "2":
            print("Ajouter utilisateur...")
        elif choix == "3":
            print("Modifier utilisateur...")
        elif choix == "4":
            print("Supprimer utilisateur...")
        elif choix == "0":
            break
        else:
            print("Choix invalide")


def client_menu():
    print("\n=== MENU CLIENT ===")


def veterinaire_menu():
    print("\n=== MENU VETERINAIRE ===")


def garde_menu():
    print("\n=== MENU GARDE ===")