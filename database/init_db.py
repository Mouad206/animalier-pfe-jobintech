from db import get_connection
from mysql.connector import Error

connection = get_connection(None)

if connection:
    try:
        cursor = connection.cursor()

        # ======================================
        # DATABASE
        # ======================================
        cursor.execute("DROP DATABASE IF EXISTS aniservice_home")
        cursor.execute("""
        CREATE DATABASE aniservice_home
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
        """)
        cursor.execute("USE aniservice_home")

        # ======================================
        # UTILISATEURS (Classe abstraite)
        # ======================================
        cursor.execute("""
        CREATE TABLE utilisateurs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            prenom VARCHAR(100),
            email VARCHAR(150) UNIQUE NOT NULL,
            telephone VARCHAR(50) UNIQUE NOT NULL,
            mot_de_passe VARCHAR(255) NOT NULL,
            role ENUM('CLIENT','ADMIN','VETERINAIRE','DRESSEUR','GARDE') NOT NULL,
            date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # CLIENTS
        # ======================================
        cursor.execute("""
        CREATE TABLE clients (
            utilisateur_id INT NOT NULL,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_clients_utilisateur
                FOREIGN KEY (utilisateur_id)
                REFERENCES utilisateurs(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # ADMINISTRATEURS
        # ======================================
        cursor.execute("""
        CREATE TABLE administrateurs (
            utilisateur_id INT NOT NULL,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_admin_utilisateur
                FOREIGN KEY (utilisateur_id)
                REFERENCES utilisateurs(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # PROFILS (Classe abstraite fournisseur)
        # ======================================
        cursor.execute("""
        CREATE TABLE profils (
            utilisateur_id INT NOT NULL,
            raison_sociale VARCHAR(150),
            certification VARCHAR(150),
            annee_experience INT,
            adresse VARCHAR(255),
            ville VARCHAR(100),
            disponibilite BOOLEAN DEFAULT TRUE,
            statut_abonnement ENUM('ACTIF','INACTIF') DEFAULT 'INACTIF',
            type_abonnement ENUM('BASIC','PRIME') NOT NULL DEFAULT 'BASIC',
            prix_abonnement DECIMAL(10,2) NOT NULL DEFAULT 0.00,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_profils_utilisateur
                FOREIGN KEY (utilisateur_id)
                REFERENCES utilisateurs(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # VETERINAIRES
        # ======================================
        cursor.execute("""
        CREATE TABLE veterinaires (
            utilisateur_id INT NOT NULL,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_vet_profil
                FOREIGN KEY (utilisateur_id)
                REFERENCES profils(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # DRESSEURS
        # ======================================
        cursor.execute("""
        CREATE TABLE dresseurs (
            utilisateur_id INT NOT NULL,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_dresseur_profil
                FOREIGN KEY (utilisateur_id)
                REFERENCES profils(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # GARDES
        # ======================================
        cursor.execute("""
        CREATE TABLE gardes (
            utilisateur_id INT NOT NULL,
            PRIMARY KEY (utilisateur_id),
            CONSTRAINT fk_garde_profil
                FOREIGN KEY (utilisateur_id)
                REFERENCES profils(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # ANIMAUX
        # ======================================
        cursor.execute("""
        CREATE TABLE animaux (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            espece VARCHAR(100),
            race VARCHAR(100),
            age INT,
            client_id INT,
            CONSTRAINT fk_animal_client
                FOREIGN KEY (client_id)
                REFERENCES clients(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # CATALOGUES
        # ======================================
        cursor.execute("""
        CREATE TABLE catalogue_veterinaire (
            id INT AUTO_INCREMENT PRIMARY KEY,
            veterinaire_id INT,
            service VARCHAR(150),
            description TEXT,
            prix DECIMAL(10,2),
            CONSTRAINT fk_catalogue_vet
                FOREIGN KEY (veterinaire_id)
                REFERENCES veterinaires(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE catalogue_dresseur (
            id INT AUTO_INCREMENT PRIMARY KEY,
            dresseur_id INT,
            service VARCHAR(150),
            description TEXT,
            prix DECIMAL(10,2),
            CONSTRAINT fk_catalogue_dresseur
                FOREIGN KEY (dresseur_id)
                REFERENCES dresseurs(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE catalogue_garde (
            id INT AUTO_INCREMENT PRIMARY KEY,
            garde_id INT,
            service VARCHAR(150),
            description TEXT,
            prix DECIMAL(10,2),
            CONSTRAINT fk_catalogue_garde
                FOREIGN KEY (garde_id)
                REFERENCES gardes(utilisateur_id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # PRESTATIONS
        # ======================================
        cursor.execute("""
        CREATE TABLE prestation_veterinaire (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_service VARCHAR(100),
            date_debut DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE') DEFAULT 'EN_ATTENTE',
            client_id INT,
            veterinaire_id INT,
            CONSTRAINT fk_presta_vet_client
                FOREIGN KEY (client_id)
                REFERENCES clients(utilisateur_id),
            CONSTRAINT fk_presta_vet_vet
                FOREIGN KEY (veterinaire_id)
                REFERENCES veterinaires(utilisateur_id)
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE prestation_dresseur (
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_service VARCHAR(100),
            date_debut DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE') DEFAULT 'EN_ATTENTE',
            client_id INT,
            dresseur_id INT,
            CONSTRAINT fk_presta_dress_client
                FOREIGN KEY (client_id)
                REFERENCES clients(utilisateur_id),
            CONSTRAINT fk_presta_dress_dress
                FOREIGN KEY (dresseur_id)
                REFERENCES dresseurs(utilisateur_id)
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE prestation_garde (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_debut DATETIME,
            date_fin DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE') DEFAULT 'EN_ATTENTE',
            client_id INT,
            garde_id INT,
            CONSTRAINT fk_presta_garde_client
                FOREIGN KEY (client_id)
                REFERENCES clients(utilisateur_id),
            CONSTRAINT fk_presta_garde_garde
                FOREIGN KEY (garde_id)
                REFERENCES gardes(utilisateur_id)
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # EVALUATIONS
        # ======================================
        cursor.execute("""
        CREATE TABLE evaluation_prestation_veterinaire (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            CONSTRAINT fk_eval_vet
                FOREIGN KEY (prestation_id)
                REFERENCES prestation_veterinaire(id)
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE evaluation_prestation_dresseur (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            CONSTRAINT fk_eval_dress
                FOREIGN KEY (prestation_id)
                REFERENCES prestation_dresseur(id)
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE evaluation_prestation_garde (
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,
            prestation_id INT UNIQUE,
            CONSTRAINT fk_eval_garde
                FOREIGN KEY (prestation_id)
                REFERENCES prestation_garde(id)
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # HISTORIQUE
        # ======================================
        cursor.execute("""
        CREATE TABLE historique_action (
            id INT AUTO_INCREMENT PRIMARY KEY,
            utilisateur_id INT,
            action VARCHAR(255),
            date_action DATETIME DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_historique_user
                FOREIGN KEY (utilisateur_id)
                REFERENCES utilisateurs(id)
        ) ENGINE=InnoDB;
        """)

        # ======================================
        # LOGS SYSTEME
        # ======================================
        cursor.execute("""
        CREATE TABLE logs_systeme (
            id INT AUTO_INCREMENT PRIMARY KEY,
            niveau ENUM('INFO','WARNING','ERROR'),
            message TEXT,
            date_log DATETIME DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB;
        """)

        connection.commit()
        print("La création de la base de données pour l'application AniService_Home a été créée avec succès.")

    except Error as e:
        print("Erreur :", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
