from db import get_connection
from mysql.connector import Error

connection = get_connection(None)

if connection:
    try:
        cursor = connection.cursor()

        # ======================================
        # DATABASE
        # ======================================
        cursor.execute("""
        CREATE DATABASE IF NOT EXISTS aniservice_home
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
        """)
        cursor.execute("USE aniservice_home")

        # ======================================
        # UTILISATEURS (classe parent)
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            prenom VARCHAR(100),
            email VARCHAR(150) UNIQUE,
            telephone VARCHAR(50),
            mot_de_passe VARCHAR(255),

            role ENUM('ADMIN','CLIENT','VETERINAIRE','DRESSEUR','GARDE')
        ) ENGINE=InnoDB
        """)

        # ======================================
        # CLIENTS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            utilisateur_id INT PRIMARY KEY,
            adresse VARCHAR(255),

            FOREIGN KEY(utilisateur_id)
            REFERENCES utilisateurs(id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # PROFILS (hérite de utilisateur)
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS profils(

            utilisateur_id INT PRIMARY KEY,

            raison_sociale VARCHAR(150),
            certification BOOLEAN,
            annee_experience INT,

            adresse VARCHAR(255),
            ville VARCHAR(100),

            disponibilite BOOLEAN DEFAULT TRUE,

            FOREIGN KEY(utilisateur_id)
            REFERENCES utilisateurs(id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # TABLES METIERS (héritage profil)
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS veterinaires(

            utilisateur_id INT PRIMARY KEY,

            FOREIGN KEY(utilisateur_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dresseurs(

            utilisateur_id INT PRIMARY KEY,

            FOREIGN KEY(utilisateur_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gardes(

            utilisateur_id INT PRIMARY KEY,

            FOREIGN KEY(utilisateur_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # ANIMAUX
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS animaux(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            espece VARCHAR(100),
            race VARCHAR(100),
            age INT,

            client_id INT,

            FOREIGN KEY(client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # CATALOGUE SERVICES
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalogue_services (

            id INT AUTO_INCREMENT PRIMARY KEY,

            profil_id INT,

            type_service ENUM('VETERINAIRE','DRESSEUR','GARDE'),

            service_nom VARCHAR(150),
            description TEXT,
            tarif DECIMAL(10,2),

            FOREIGN KEY (profil_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # PRESTATIONS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestations (

            id INT AUTO_INCREMENT PRIMARY KEY,

            type_prestation ENUM('VETERINAIRE','DRESSEUR','GARDE'),

            client_id INT,
            profil_id INT,

            description TEXT,

            date_debut DATETIME,
            date_fin DATETIME,

            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE'),

            FOREIGN KEY(client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE,

            FOREIGN KEY(profil_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # EVALUATIONS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations(
            id INT AUTO_INCREMENT PRIMARY KEY,

            prestation_id INT,
            client_id INT,

            note INT CHECK (note BETWEEN 1 AND 5),
            commentaire TEXT,

            date_evaluation DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(prestation_id)
            REFERENCES prestations(id)
            ON DELETE CASCADE,

            FOREIGN KEY(client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # HISTORIQUE
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique_action(
            id INT AUTO_INCREMENT PRIMARY KEY,

            utilisateur_id INT,
            prestation_id INT NULL,

            action VARCHAR(255),

            date_action DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(utilisateur_id)
            REFERENCES utilisateurs(id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # RECLAMATIONS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reclamations(

            id INT AUTO_INCREMENT PRIMARY KEY,

            motif VARCHAR(150),
            description TEXT,

            statut ENUM('EN_ATTENTE','TRAITEE','REJETEE'),

            client_id INT,
            profil_id INT,

            FOREIGN KEY(client_id)
            REFERENCES clients(utilisateur_id)
            ON DELETE CASCADE,

            FOREIGN KEY(profil_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # NOTIFICATIONS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications(

            id INT AUTO_INCREMENT PRIMARY KEY,

            message TEXT,

            statut ENUM('NON_LUE','LUE') DEFAULT 'NON_LUE',

            utilisateur_id INT,

            date_notification DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(utilisateur_id)
            REFERENCES utilisateurs(id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # ABONNEMENTS
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS abonnements(

            id INT AUTO_INCREMENT PRIMARY KEY,

            profil_id INT,

            type_abonnement ENUM('BASIC','PREMIUM'),

            montant DECIMAL(10,2),

            date_debut DATETIME DEFAULT CURRENT_TIMESTAMP,
            date_fin DATETIME,

            statut ENUM('ACTIF','EXPIRE'),

            FOREIGN KEY(profil_id)
            REFERENCES profils(utilisateur_id)
            ON DELETE CASCADE
        ) ENGINE=InnoDB
        """)

        # ======================================
        # LOGS SYSTEME
        # ======================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs_systeme (

            id INT AUTO_INCREMENT PRIMARY KEY,

            niveau ENUM('INFO','WARNING','ERROR'),

            message TEXT,

            date_log DATETIME DEFAULT CURRENT_TIMESTAMP

        ) ENGINE=InnoDB
        """)
        
        cursor.execute("""
                       ALTER TABLE prestations
                        ADD animal_id INT NULL,
                        ADD CONSTRAINT fk_animal
                        FOREIGN KEY (animal_id)
                        REFERENCES animaux(id)
                        ON DELETE SET NULL;
        """)

        connection.commit()

        print("Base de données AniService_Home créée avec succès.")

    except Error as e:
        print("Erreur :", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()