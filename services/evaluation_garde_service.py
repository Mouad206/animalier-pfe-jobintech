from database.db import get_connection
from models.evaluation import Evaluation


class EvaluationGarde(Evaluation):

    def sauvegarder(self):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            # 1️⃣ vérifier prestation valide
            cursor.execute("""
                SELECT garde_id
                FROM prestation_garde
                WHERE id=%s AND client_id=%s AND statut='TERMINEE'
            """, (self.prestation_id, self.client_id))

            result = cursor.fetchone()

            if not result:
                print("❌ Evaluation impossible")
                return

            garde_id = result[0]

            # 2️⃣ insérer évaluation
            cursor.execute("""
                INSERT INTO evaluation_prestation_garde
                (note, commentaire, prestation_id, client_id)
                VALUES (%s, %s, %s, %s)
            """, (
                self.note,
                self.commentaire,
                self.prestation_id,
                self.client_id
            ))

            connection.commit()

            # 3️⃣ calcul moyenne
            cursor.execute("""
                SELECT AVG(e.note)
                FROM evaluation_prestation_garde e
                JOIN prestation_garde p
                    ON e.prestation_id = p.id
                WHERE p.garde_id=%s
            """, (garde_id,))

            moyenne = cursor.fetchone()[0]

            # 4️⃣ mise à jour profils
            cursor.execute("""
                UPDATE profils
                SET moyenne_note=%s
                WHERE utilisateur_id=%s
            """, (moyenne, garde_id))

            connection.commit()

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()