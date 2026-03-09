from repository.profil_repository import ProfilRepository
from services.historique_service import HistoriqueService
from infra.logger_config import LoggerConfig
from repository.veterinaire_repository import VeterinaireRepository
from repository.dresseur_repository import DresseurRepository
from repository.garde_repository import GardeRepository


class InscriptionService:

    logger = LoggerConfig.getInstance()

    # =========================
    # VERIFIER SI PROFIL EXISTE
    # =========================
    @staticmethod
    def profil_existe(utilisateur_id):

        profil = ProfilRepository.find_by_id(utilisateur_id)

        return profil is not None


    # =========================
    # INSCRIPTION PROFIL
    # =========================
    @staticmethod
    def inscrire_profil(profil):

        try:

            # créer profil
            ProfilRepository.create(profil)

            # créer table métier selon rôle
            if profil.role == "VETERINAIRE":
                VeterinaireRepository.create(profil.id)

            elif profil.role == "DRESSEUR":
                DresseurRepository.create(profil.id)

            elif profil.role == "GARDE":
                GardeRepository.create(profil.id)

            HistoriqueService.enregistrer_action(
                profil.id,
                "Inscription profil professionnel"
            )

            InscriptionService.logger.log(
                "INFO",
                profil.id,
                "Profil professionnel créé"
            )

            print("✅ Profil professionnel créé avec succès")

        except Exception as e:

            print("❌ Erreur SQL :", e)   # IMPORTANT pour debug

            InscriptionService.logger.log(
                "ERROR",
                profil.id,
                f"Erreur inscription profil : {e}"
            )

            print("❌ Erreur lors de l'inscription du profil")