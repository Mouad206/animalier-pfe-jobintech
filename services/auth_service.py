import bcrypt

from repository.utilisateur_repository import UtilisateurRepository
from repository.client_repository import ClientRepository
from repository.veterinaire_repository import VeterinaireRepository
from repository.dresseur_repository import DresseurRepository
from repository.garde_repository import GardeRepository


class AuthService:

    current_user = None

    ROLES_AUTORISES = ["CLIENT", "VETERINAIRE", "DRESSEUR", "GARDE"]

    # ==========================
    # REGISTER
    # ==========================
    @staticmethod
    def register(nom, prenom, email, telephone, password, role):

            if role not in AuthService.ROLES_AUTORISES:
                print("❌ rôle invalide")
                return

            existing_user = UtilisateurRepository.find_by_email(email)

            if existing_user:
                print("❌ email déjà utilisé")
                return

            hashed_password = bcrypt.hashpw(
                password.encode(),
                bcrypt.gensalt()
            ).decode()

            user_id = UtilisateurRepository.create(
                nom,
                prenom,
                email,
                telephone,
                hashed_password,
                role
            )

            # créer client si rôle client
            if role == "CLIENT":
                ClientRepository.create(user_id)

            print("✅ Compte créé avec succès")

    # ==========================
    # LOGIN
    # ==========================
    @staticmethod
    def login(email, password):

        user = UtilisateurRepository.find_by_email(email)

        if not user:
            print("❌ email ou mot de passe incorrect")
            return None

        if bcrypt.checkpw(
            password.encode(),
            user["mot_de_passe"].encode()
        ):

            AuthService.current_user = user
            print("✅ connexion réussie")

            return user

        print("❌ email ou mot de passe incorrect")
        return None

    # ==========================
    # LOGOUT
    # ==========================
    @staticmethod
    def logout():

        AuthService.current_user = None
        print("👋 Déconnexion réussie")
        
        
    @staticmethod
    def update_password(email, new_password):

        user = UtilisateurRepository.find_by_email(email)

        if not user:
            print("❌ utilisateur non trouvé")
            return

        hashed_password = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()

        connection = UtilisateurRepository.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE utilisateurs
        SET mot_de_passe=%s
        WHERE email=%s
        """, (
            hashed_password,
            email
        ))

        connection.commit()

        cursor.close()
        connection.close()

        print("✅ mot de passe mis à jour avec succès")


    @staticmethod
    def get_current_user():
        return AuthService.current_user