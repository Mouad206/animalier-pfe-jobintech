from db import get_connection


def create_tables():

    connection = get_connection("aniservice_home")

    cursor = connection.cursor()

    # ==========================
    # Evaluation vétérinaire
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_prestation_veterinaire (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            client_id INT,
            date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (prestation_id)
            REFERENCES prestation_veterinaire(id)
            ON DELETE CASCADE,

            FOREIGN KEY (client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE
        )
    """)

    # ==========================
    # Evaluation garde
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_prestation_garde (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            client_id INT,
            date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (prestation_id)
            REFERENCES prestation_garde(id)
            ON DELETE CASCADE,

            FOREIGN KEY (client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE
        )
    """)

    # ==========================
    # Evaluation dressage
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_prestation_dresseur (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            client_id INT,
            date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (prestation_id)
            REFERENCES prestation_dresseur(id)
            ON DELETE CASCADE,

            FOREIGN KEY (client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("Tables evaluations créées avec succès.")


if __name__ == "__main__":
    create_tables()