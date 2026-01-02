from django.db.models import Avg, Count, Sum
from analytics.models import Menage, Valeur, Indicateur, Decoupage, CompagneAgricole
from foncier.models import Parcelle
from django.utils import timezone

class SEADCalculator:
    @staticmethod
    def calculate_all(province_name=None):
        # On récupère toutes les zones qui ont au moins un ménage enregistré
        zones_ids = Menage.objects.values_list('decoupage_id', flat=True).distinct()
        zones = Decoupage.objects.filter(id__in=zones_ids)
        
        if province_name:
            zones = zones.filter(provinces=province_name)

        print(f"--- 🚀 Calcul pour {zones.count()} zones avec données ---")

        for zone in zones:
            # --- A1 : Taille ménage (On prend tous les ménages de la zone) ---
            res_a1 = Menage.objects.filter(decoupage=zone).aggregate(Avg('taille_menage'))['taille_menage__avg']
            SEADCalculator._save_valeur('A1', zone, res_a1)

            # --- A7 : Superficie ---
            res_a7 = Parcelle.objects.filter(menage__decoupage=zone).aggregate(Avg('surface_culture_ha'))['surface_culture_ha__avg']
            SEADCalculator._save_valeur('A7', zone, res_a7)

            # --- A15 : % sécurisées ---
            query_p = Parcelle.objects.filter(menage__decoupage=zone)
            total_p = query_p.count()
            secure_p = query_p.filter(est_securisee=True).count()
            res_a15 = (secure_p / total_p * 100) if total_p > 0 else 0
            SEADCalculator._save_valeur('A15', zone, res_a15)

            # --- A44 : Score Nutrition ---
            res_a44 = Menage.objects.filter(decoupage=zone).aggregate(Avg('sdam_score'))['sdam_score__avg']
            SEADCalculator._save_valeur('A44', zone, res_a44)

        return f"Calcul terminé pour {zones.count()} zones."

    @staticmethod
    def _save_valeur(code, zone, value):
        if value is None: value = 0
        try:
            indic = Indicateur.objects.get(code=code)
            Valeur.objects.update_or_create(
                indicateur=indic,
                decoupage=zone,
                defaults={'valeur_calculee': round(float(value), 2), 'date': timezone.now().date()}
            )
            print(f"✅ {code} pour {zone.colqtr} = {value}")
        except Exception as e:
            print(f"❌ Erreur {code}: {e}")