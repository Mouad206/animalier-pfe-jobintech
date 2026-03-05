from database.db import get_connection
from models.evaluation import Evaluation
from services.log_service import LogService


class EvaluationVeterinaire(Evaluation):

    def sauvegarder(self):

        connection = get_connection("aniservice_home")

        try:
            cursor = connection.cursor()

            # 1️⃣ Vérifier prestation valide
            cursor.execute("""
                SELECT veterinaire_id
                FROM prestation_veterinaire
                WHERE id=%s AND client_id=%s AND statut='TERMINEE'
            """, (self.prestation_id, self.client_id))

            result = cursor.fetchone()

            if not result:
                print("❌ Evaluation impossible")
                return

            veterinaire_id = result[0]

            # 2️⃣ Insérer évaluation
            cursor.execute("""
                INSERT INTO evaluation_prestation_veterinaire
                (note, commentaire, prestation_id, client_id)
                VALUES (%s, %s, %s, %s)
            """, (
                self.note,
                self.commentaire,
                self.prestation_id,
                self.client_id
            ))

            connection.commit()

            # 3️⃣ Calcul moyenne
            cursor.execute("""
                SELECT AVG(e.note)
                FROM evaluation_prestation_veterinaire e
                JOIN prestation_veterinaire p
                    ON e.prestation_id = p.id
                WHERE p.veterinaire_id=%s
            """, (veterinaire_id,))

            moyenne = cursor.fetchone()[0]

            # 4️⃣ Mise à jour profils
            cursor.execute("""
                UPDATE profils
                SET moyenne_note=%s
                WHERE utilisateur_id=%s
            """, (moyenne, veterinaire_id))

            connection.commit()

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()