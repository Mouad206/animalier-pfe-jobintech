from services.auth_service import AuthService
from services.inscription_service import InscriptionService
from factories.profil_factory_provider import ProfilFactoryProvider


def menu_inscription_profil():

    user = AuthService.get_current_user()

    # Vérifier si le profil existe déjà
    if InscriptionService.profil_existe(user["id"]):
        print("⚠️ Votre profil est déjà complété.")
        return

    print("\n===== COMPLÉTER VOTRE PROFIL PROFESSIONNEL =====")

    raison_sociale = input("Raison sociale : ")

    cert = input("Certification (oui/non) : ")
    certification = True if cert.lower() == "oui" else False

    experience = int(input("Années d'expérience : "))

    adresse = input("Adresse : ")

    ville = input("Ville : ")

    disponibilite = True

    # 🔵 utilisation de la factory
    factory = ProfilFactoryProvider.get_factory(user["role"])

    profil = factory.creer_profil(
        user,
        raison_sociale,
        certification,
        experience,
        adresse,
        ville,
        disponibilite
    )

    InscriptionService.inscrire_profil(profil)

    print("✅ Profil créé avec succès")