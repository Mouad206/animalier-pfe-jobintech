from db import get_connection

def seed():
    print("seed demarre")
    conn = get_connection()
    cursor = conn.cursor()

    try:
        print("=== DEMARRAGE SEED ===")

        # ==============================
        # 1️⃣ Vérifier ou créer utilisateur
        # ==============================
        email = "ikbalita@mail.com"

        cursor.execute(
            "SELECT id FROM utilisateurs WHERE email = %s",
            (email,)
        )

        row = cursor.fetchone()

        if row is not None:
            user_id = row[0]
            print("Utilisateur déjà existant, ID :", user_id)
        else:
            print("Insertion utilisateur...")

            cursor.execute("""
                INSERT INTO utilisateurs 
                (nom, prenom, email, telephone, mot_de_passe, role)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, ("Saiss", "Ikbal", email, "0601012315", "1234", "CLIENT"))

            user_id = cursor.lastrowid
            print("Utilisateur inséré, ID :", user_id)

        # ==============================
        # 2️⃣ Vérifier ou créer client
        # ==============================
        cursor.execute(
            "SELECT utilisateur_id FROM clients WHERE utilisateur_id = %s",
            (user_id,)
        )

        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO clients (utilisateur_id) VALUES (%s)",
                (user_id,)
            )
            print("Client inséré")
        else:
            print("Client déjà existant")

        # ==============================
        # 3️⃣ Insérer deux chats (sans doublon)
        # ==============================
        animaux = [
            ("Tom", "CHAT", "Siamois", 4, user_id),
            ("Silver", "CHAT", "Persan", 1, user_id)
        ]

        for animal in animaux:
            cursor.execute("""
                SELECT id FROM animaux 
                WHERE nom = %s AND client_id = %s
            """, (animal[0], user_id))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO animaux (nom, espece, race, age, client_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, animal)
                print(f"Animal {animal[0]} inséré")
            else:
                print(f"Animal {animal[0]} déjà existant")

        # ==============================
        # 4️⃣ Commit
        # ==============================
        conn.commit()
        print("COMMIT effectué")
        print("=== SEED TERMINE AVEC SUCCES ===")

    except Exception:
        import traceback
        traceback.print_exc()
        conn.rollback()

    finally:
        conn.close()
        print("Connexion fermée")

if __name__ == "__main__":
        seed()