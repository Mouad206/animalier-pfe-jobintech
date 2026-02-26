import mysql.connector
from db_config import DB_CONFIG

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('admin', 'client', 'veterinaire', 'garde') NOT NULL,
    telephone VARCHAR(20)
)
""")

print("Table utilisateurs créée ")

cursor.close()
connection.close()