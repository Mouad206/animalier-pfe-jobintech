from services.service_client import ClientService
from services.auth_service import AuthService


def menu_client():

    user = AuthService.get_current_user()

    while True:

        print("\n===== MENU CLIENT =====")
        print("1 Voir prestations")
        print("2 Ajouter prestation")
        print("3 Voir animaux")
        print("4 Ajouter animal")
        print("5 Supprimer animal")
        print("6 Modifier animal")
        print("7 Mon profil")
        print("8 Modifier profil")
        print("9 Modifier mot de passe")
        print("0 Déconnexion")

        choix = input("Choix : ")

        if choix == "1":

            prestations = ClientService.voir_prestations(user["id"])

            for p in prestations:
                print(p)

        elif choix == "2":

            type_service = input("Type service : ")
            description = input("Description : ")
            date = input("Date début : ")
            profil_id = input("ID profil : ")

            ClientService.creer_prestation(
                type_service,
                description,
                date,
                user["id"],
                profil_id
            )

        elif choix == "3":

            animaux = ClientService.voir_animaux(user["id"])

            for a in animaux:
                print(a)
                
        elif choix == "4":
            nom = input("Nom de l'animal : ")
            espece = input("Espèce : ")
            race = input("Race : ")
            age = input("Âge : ")

            ClientService.ajouter_animal(nom, espece, race, age, user["id"])
            
            
        elif choix == "5":
            animal_id = input("ID de l'animal à supprimer : ")
            ClientService.supprimer_animal(animal_id)
        elif choix == "6":
            animal_id = input("ID de l'animal à modifier : ")
            nom = input("Nouveau nom de l'animal : ")
            espece = input("Nouvelle espèce : ")
            race = input("Nouvelle race : ")
            age = input("Nouvel âge : ")
            ClientService.modifier_animal(animal_id, nom, espece, race, age)
            
            
        elif choix == "7":

            profil = ClientService.voir_profil(user["id"])

            print(profil)
            
        elif choix == "8":

            nom = input("Nouveau nom : ")
            email = input("Nouveau email : ")
            telephone = input("Nouveau téléphone : ")
            adresse = input("Nouvelle adresse : ")

            ClientService.modifier_profil(
                user["id"],
                nom,
                email,
                telephone,
                adresse
            )
            
        elif choix == "9":
            nouveau_mdp = input("Nouveau mot de passe : ")

            success = AuthService.update_password(
                user["email"],
                nouveau_mdp
            )

            if success:
                print("Mot de passe modifié avec succès.")
            else:
                print("Erreur lors de la modification du mot de passe.")

        elif choix == "0":
            break