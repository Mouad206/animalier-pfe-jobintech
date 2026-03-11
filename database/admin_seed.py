import bcrypt
from db import get_connection


def seed_admin():

    connection = get_connection("aniservice_home")

    try:
        cursor = connection.cursor()

        email_admin = "admin@aniservice.com"

        # vérifier si admin existe
        cursor.execute(
            "SELECT id FROM utilisateurs WHERE email=%s",
            (email_admin,)
        )

        if cursor.fetchone():
            print("⚠️ Admin existe déjà")
            return

        # hash password
        password = "admin123"
        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        # insertion utilisateur admin
        cursor.execute("""
            INSERT INTO utilisateurs
            (nom, prenom, email, telephone, mot_de_passe, role)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            "Admin",
            "System",
            email_admin,
            "0600000000",
            hashed_password.decode(),
            "ADMIN"
        ))
        


        connection.commit()

        print("✅ Admin créé avec succès")
        print("Email :", email_admin)
        print("Mot de passe : admin123")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    seed_admin()