from django.contrib.gis.db import models as gis_models
from django.conf import settings

class PhaseParcelle(gis_models.Model):
    nom = gis_models.CharField(max_length=50)
    ordre = gis_models.IntegerField()

class Parcelle(gis_models.Model):
    code = gis_models.CharField(max_length=50, unique=True)
    # Champ SIG pour les parcelles individuelles
    geom = gis_models.PolygonField(srid=4326) 
    surface_culture_ha = gis_models.FloatField(default=0.0) # Pour A7
    est_securisee = gis_models.BooleanField(default=False) # Pour A15
    
    # Attributs MCD
    usg_parcelle = gis_models.CharField(max_length=100)
    secu_droit = gis_models.CharField(max_length=100)
    expl_comm = gis_models.BooleanField(default=False) # <--- RÉPARÉ
    int_comm = gis_models.BooleanField(default=False) 
    voisin_nord = gis_models.CharField(max_length=255)
    voisin_sud = gis_models.CharField(max_length=255)
    voisin_est = gis_models.CharField(max_length=255)
    voisin_ouest = gis_models.CharField(max_length=255)
    
    menage = gis_models.ForeignKey('analytics.Menage', on_delete=gis_models.CASCADE)
    phase_actuelle = gis_models.ForeignKey(PhaseParcelle, on_delete=gis_models.PROTECT, null=True)
    decoupage = gis_models.ForeignKey('analytics.Decoupage', on_delete=gis_models.SET_NULL, null=True, blank=True)

class Culture(gis_models.Model):
    parcelle = gis_models.ForeignKey(Parcelle, on_delete=gis_models.CASCADE)
    code = gis_models.CharField(max_length=50)
    surface_culture_ha = gis_models.FloatField()
    quantite_produite_kg = gis_models.FloatField()
    quantite_stockee_kg = gis_models.FloatField()
    quantite_vendue_kg = gis_models.FloatField()
    quantite_autoconsommee_kg = gis_models.FloatField()
    prix_unitaire_fbukg = gis_models.FloatField()
    pourcentage_transforme = gis_models.FloatField()
    type_transformation = gis_models.CharField(max_length=100)
    specialisation_dominante = gis_models.CharField(max_length=100)

class TitreFoncier(gis_models.Model):
    parcelle = gis_models.OneToOneField(Parcelle, on_delete=gis_models.CASCADE)
    doc_droit = gis_models.BooleanField()
    document = gis_models.CharField(max_length=255)
    num_demande = gis_models.CharField(max_length=100)
    date_de_demande = gis_models.DateField()

class ConflitFoncier(gis_models.Model):
    parcelle = gis_models.ForeignKey(Parcelle, on_delete=gis_models.CASCADE)
    conflit_foncier = gis_models.BooleanField()
    type = gis_models.CharField(max_length=100)
    conflit_avec = gis_models.CharField(max_length=255)
    raison_conflit = gis_models.TextField()
    ans_conflit = gis_models.IntegerField()

class ParcelleLog(gis_models.Model):
    parcelle = gis_models.ForeignKey(Parcelle, on_delete=gis_models.CASCADE)
    utilisateur = gis_models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=gis_models.SET_NULL, null=True)
    date_action = gis_models.DateTimeField(auto_now_add=True)
    details = gis_models.TextField()