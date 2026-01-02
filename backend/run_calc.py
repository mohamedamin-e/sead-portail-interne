import os
import django

# Configuration de l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from analytics.services.calculator import SEADCalculator
from analytics.models import Menage, Decoupage, CompagneAgricole
from foncier.models import Parcelle, PhaseParcelle

def run():
    print("--- 🏁 Nettoyage et Calcul ---")
    
    # On s'assure qu'il y a au moins une campagne pour les relations
    campagne = CompagneAgricole.objects.filter(annee=2026).first()
    if not campagne:
        campagne = CompagneAgricole.objects.create(annee=2026, mois='Janvier', date='2026-01-01')
    
    # On lance le calcul
    result = SEADCalculator.calculate_all()
    print(result)

if __name__ == "__main__":
    run()