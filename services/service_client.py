import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="ton_user",
        password="ton_mdp",
        database="nom_de_ta_base"
    )


class ClientService:

    @staticmethod
    def consulter_catalogue_dressage():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prestation_dressage")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def consulter_catalogue_garde():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prestation_garde")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def consulter_catalogue_veterinaire():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prestation_veterinaire")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def demander_service(table_prestation, prestation_id, client_id):

        tables_autorisees = [
        "prestation_garde",
        "prestation_dressage",
        "prestation_veterinaire"
        ]

        if table_prestation not in tables_autorisees:
            raise ValueError("Type de prestation invalide")

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
    UPDATE {table_prestation}
    SET client_id = %s,
        statut = 'RESERVEE'
    WHERE id = %s
    """

    cursor.execute(sql, (client_id, prestation_id))
    conn.commit()
    cursor.close()
    conn.close()

   
    @staticmethod
    def confirmer_realisation(table_prestation, prestation_id):

        tables_autorisees = [
        "prestation_garde",
        "prestation_dressage",
        "prestation_veterinaire"
        ]

        if table_prestation not in tables_autorisees:
            raise ValueError("Type de prestation invalide")

    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
        UPDATE {table_prestation}
        SET statut = 'CONFIRMEE'
        WHERE id = %s
        """

    cursor.execute(sql, (prestation_id,))
    conn.commit()
    cursor.close()
    conn.close()