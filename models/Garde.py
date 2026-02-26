
from models.utilisateur import Utilisateur
from repository.catalogue_garde_repository import catalogue_garde
from services.prestation_garde import prestation_garde
import services.profilAnimalier
from enum import Enum




class StatutAbonnement(enums.Enum):
    ACTIF = "ACTIF"
    INACTIF = "INACTIF"




    