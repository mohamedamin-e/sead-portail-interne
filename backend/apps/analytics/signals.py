from django.db.models.signals import post_save
from django.dispatch import receiver
from analytics.models import Menage
from analytics.services.calculator import SEADCalculator

@receiver(post_save, sender=Menage)
def trigger_indicator_update(sender, instance, **kwargs):
    """Dès qu'un ménage est enregistré, on recalcule les indicateurs de sa zone"""
    print(f"Signal reçu : Recalcul pour la zone {instance.decoupage.colqtr}")
    SEADCalculator.calculate_all(province_name=instance.decoupage.provinces)