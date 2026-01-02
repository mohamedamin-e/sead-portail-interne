import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from analytics.models import Menage, Decoupage, CompagneAgricole, Saison, Indicateur, Valeur
from foncier.models import Parcelle, PhaseParcelle
from authentication.models import User, LogActivite

def run_test():
    print("--- 🚀 Démarrage du Test Système ---")
    
    # 1. Créer une campagne et une saison
    campagne, _ = CompagneAgricole.objects.get_or_create(annee=2026, defaults={'mois': 'Janvier', 'date': '2026-01-01'})
    saison, _ = Saison.objects.get_or_create(campagne=campagne, nom='A')
    phase, _ = PhaseParcelle.objects.get_or_create(nom='enquete', defaults={'ordre': 1})
    
    # 2. Choisir une colline au hasard dans les 3071 importées
    zone = Decoupage.objects.order_by('?').first()
    print(f"📍 Zone de test : {zone.colqtr} (Commune: {zone.communes})")

    # 3. CRÉATION D'UN MÉNAGE (POST simulé)
    # Cela va déclencher le SIGNAL qui lance le CALCULATOR
    m, created = Menage.objects.get_or_create(
        code=f"TEST_MEN_{random.randint(100,999)}",
        defaults={
            'nom_chef_menage': 'Test User',
            'prenom_c_m': 'Mohamed',
            'sexe_c_m': 'H',
            'age_c_m': 30,
            'taille_menage': 8, # On met 8 personnes
            'decoupage': zone,
            'campagne': campagne,
            'sdam_score': 5.5
        }
    )
    print(f"🏠 Ménage créé : {m.code}")

    # 4. CRÉATION D'UNE PARCELLE liée (POST simulé)
    p = Parcelle.objects.create(
        code=f"PARC_{random.randint(100,999)}",
        menage=m,
        geom='POLYGON((30 -2, 31 -2, 31 -3, 30 -3, 30 -2))', # Carré fictif
        surface_culture_ha=2.5,
        phase_actuelle=phase,
        est_securisee=True
    )
    print(f"🗺️ Parcelle de 2.5ha créée pour le ménage.")

    # 5. VÉRIFICATION DES RÉSULTATS (GET simulé)
    print("\n--- 📊 Vérification du Moteur d'Analytics ---")
    valeurs = Valeur.objects.filter(decoupage=zone)
    for v in valeurs:
        print(f"✅ Indicateur {v.indicateur.code} ({v.indicateur.libelle}) = {v.valeur_calculee}")

    print("\n--- 📜 Vérification des Logs ---")
    logs = LogActivite.objects.all()[:2]
    for l in logs:
        print(f"📝 Log : {l.action} sur {l.ressource_type} à {l.timestamp}")

run_test()