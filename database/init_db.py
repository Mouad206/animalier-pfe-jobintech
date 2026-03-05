from db import get_connection
from mysql.connector import Error

connection = get_connection(None)

if connection:
    try:
        cursor = connection.cursor()

        # ======================================
        # DATABASE
        # ======================================
        # cursor.execute("DROP DATABASE IF EXISTS aniservice_home")
        cursor.execute("""
        CREATE DATABASE IF NOT EXISTS aniservice_home
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
        """)
        cursor.execute("USE aniservice_home")

        # =========================
        # UTILISATEURS
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            prenom VARCHAR(100),
            email VARCHAR(150) UNIQUE,
            telephone VARCHAR(50),
            mot_de_passe VARCHAR(255),
            statutRole ENUM('CLIENT','ADMIN','PROFIL')
        )
        """)

        # =========================
        # CLIENTS
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            utilisateur_id INT PRIMARY KEY,
            adresse VARCHAR(255),
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
        )
        """)

        # =========================
        # PROFILS (VETERINAIRE / DRESSEUR / GARDE)
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS profils(
            utilisateur_id INT PRIMARY KEY,
            statutRole ENUM('VETERINAIRE','DRESSEUR','GARDE'),
            raison_sociale VARCHAR(150),
            certification BOOLEAN,
            annee_experience INT,
            adresse VARCHAR(255),
            disponibilite BOOLEAN,
            statut_abonnement ENUM('ACTIF','INACTIF'),
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
        )
        """)

        # =========================
        # ANIMAUX
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS animaux(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100),
            espece VARCHAR(100),
            race VARCHAR(100),
            age INT,
            client_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id)
        )
        """)

        # =========================
        # CATALOGUE VETERINAIRE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalogue_veterinaire(
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_service VARCHAR(100),
            tarif DECIMAL(10,2),
            description TEXT,
            veterinaire_id INT,
            FOREIGN KEY(veterinaire_id) REFERENCES profils(utilisateur_id)
        )
        """)

        # =========================
        # CATALOGUE DRESSAGE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalogue_dressage(
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_service VARCHAR(100),
            tarif DECIMAL(10,2),
            description TEXT,
            dresseur_id INT,
            FOREIGN KEY(dresseur_id) REFERENCES profils(utilisateur_id)
        )
        """)

        # =========================
        # CATALOGUE GARDE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalogue_garde(
            id INT AUTO_INCREMENT PRIMARY KEY,
            type_service VARCHAR(100),
            tarif DECIMAL(10,2),
            description TEXT,
            garde_id INT,
            FOREIGN KEY(garde_id) REFERENCES profils(utilisateur_id)
        )
        """)

        # =========================
        # PRESTATION VETERINAIRE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestation_veterinaire(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_debut DATETIME,
            date_fin DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE'),
            client_id INT,
            veterinaire_id INT,
            animal_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id),
            FOREIGN KEY(veterinaire_id) REFERENCES profils(utilisateur_id),
            FOREIGN KEY(animal_id) REFERENCES animaux(id)
        )
        """)

        # =========================
        # PRESTATION DRESSAGE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestation_dressage(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_debut DATETIME,
            date_fin DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE'),
            client_id INT,
            dresseur_id INT,
            animal_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id),
            FOREIGN KEY(dresseur_id) REFERENCES profils(utilisateur_id),
            FOREIGN KEY(animal_id) REFERENCES animaux(id)
        )
        """)

        # =========================
        # PRESTATION GARDE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestation_garde(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_debut DATETIME,
            date_fin DATETIME,
            statut ENUM('EN_ATTENTE','CONFIRMEE','TERMINEE'),
            client_id INT,
            garde_id INT,
            animal_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id),
            FOREIGN KEY(garde_id) REFERENCES profils(utilisateur_id),
            FOREIGN KEY(animal_id) REFERENCES animaux(id)
        )
        """)

        # =========================
        # EVALUATION VETERINAIRE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_veterinaire(
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT,
            commentaire TEXT,
            date DATETIME,
            prestation_id INT,
            FOREIGN KEY(prestation_id) REFERENCES prestation_veterinaire(id)
        )
        """)

        # =========================
        # EVALUATION DRESSAGE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_dressage(
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT,
            commentaire TEXT,
            date DATETIME,
            prestation_id INT,
            FOREIGN KEY(prestation_id) REFERENCES prestation_dressage(id)
        )
        """)

        # =========================
        # EVALUATION GARDE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_garde(
            id INT AUTO_INCREMENT PRIMARY KEY,
            note INT,
            commentaire TEXT,
            date DATETIME,
            prestation_id INT,
            FOREIGN KEY(prestation_id) REFERENCES prestation_garde(id)
        )
        """)

        # =========================
        # HISTORIQUE
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATETIME,
            action TEXT,
            utilisateur_id INT,
            prestation_id INT,
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
        )
        """)

        # =========================
        # DEMANDE RAPPEL
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS demande_rappel(
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT,
            statut ENUM('EN_ATTENTE','ACCEPTEE','REFUSEE'),
            client_id INT,
            profil_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id),
            FOREIGN KEY(profil_id) REFERENCES profils(utilisateur_id)
        )
        """)

        # =========================
        # RECLAMATIONS
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reclamations(
            id INT AUTO_INCREMENT PRIMARY KEY,
            motif VARCHAR(150),
            description TEXT,
            statut ENUM('EN_ATTENTE','TRAITEE','REJETEE'),
            client_id INT,
            profil_id INT,
            FOREIGN KEY(client_id) REFERENCES clients(utilisateur_id),
            FOREIGN KEY(profil_id) REFERENCES profils(utilisateur_id)
        )
        """)

        # =========================
        # NOTIFICATIONS
        # =========================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications(
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT,
            statut ENUM('NON_LUE','LUE'),
            utilisateur_id INT,
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id)
        )
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
