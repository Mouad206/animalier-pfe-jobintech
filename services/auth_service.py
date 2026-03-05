import bcrypt
from database.db import get_connection


class AuthService:

    current_user = None

    # rôles autorisés
    ROLES_AUTORISES = ["CLIENT", "VETERINAIRE", "DRESSEUR", "GARDE"]

    # ==========================
    # REGISTER
    # ==========================
    @staticmethod
    def register(nom, prenom, email, telephone, password, role):

        if role not in AuthService.ROLES_AUTORISES:
            print("❌ rôle invalide")
            return

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            # vérifier si email existe
            cursor.execute(
                "SELECT id FROM utilisateurs WHERE email=%s",
                (email,)
            )

            if cursor.fetchone():
                print("❌ email déjà utilisé")
                return

            # hash password
            hashed_password = bcrypt.hashpw(
                password.encode(),
                bcrypt.gensalt()
            )

            # insertion utilisateur
            cursor.execute("""
                INSERT INTO utilisateurs
                (nom, prenom, email, telephone, mot_de_passe, role)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (
                nom,
                prenom,
                email,
                telephone,
                hashed_password.decode(),
                role
            ))

            user_id = cursor.lastrowid

            # =====================
            # CLIENT
            # =====================
            if role == "CLIENT":

                cursor.execute(
                    "INSERT INTO clients (utilisateur_id) VALUES (%s)",
                    (user_id,)
                )

            # =====================
            # FOURNISSEURS
            # =====================
            elif role in ["VETERINAIRE", "DRESSEUR", "GARDE"]:

                # créer profil
                cursor.execute("""
                    INSERT INTO profils (utilisateur_id)
                    VALUES (%s)
                """, (user_id,))

                if role == "VETERINAIRE":

                    cursor.execute(
                        "INSERT INTO veterinaires (utilisateur_id) VALUES (%s)",
                        (user_id,)
                    )

                elif role == "DRESSEUR":

                    cursor.execute(
                        "INSERT INTO dresseurs (utilisateur_id) VALUES (%s)",
                        (user_id,)
                    )

                elif role == "GARDE":

                    cursor.execute(
                        "INSERT INTO gardes (utilisateur_id) VALUES (%s)",
                        (user_id,)
                    )

            connection.commit()

            print("✅ Compte créé avec succès")

        except Exception as e:

            connection.rollback()
            print("❌ erreur :", e)

        finally:

            if connection.is_connected():
                cursor.close()
                connection.close()

    # ==========================
    # LOGIN
    # ==========================
    @staticmethod
    def login(email, password):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM utilisateurs WHERE email=%s",
                (email,)
            )

            user = cursor.fetchone()

            if not user:
                print("❌ utilisateur introuvable")
                return None

            if bcrypt.checkpw(
                password.encode(),
                user["mot_de_passe"].encode()
            ):

                AuthService.current_user = user

                print("✅ connexion réussie")

                return user["role"]

            else:
                print("❌ mot de passe incorrect")
                return None

        finally:

            if connection.is_connected():
                cursor.close()
                connection.close()

    # ==========================
    # LOGOUT
    # ==========================
    @staticmethod
    def logout():

        AuthService.current_user = None
        print("👋 Déconnexion réussie")

    # ==========================
    # GET USER
    # ==========================
    @staticmethod
    def get_current_user():

        return AuthService.current_user