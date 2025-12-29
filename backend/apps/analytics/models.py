from django.contrib.gis.db import models # Indispensable pour le shapefile

class Decoupage(models.Model):
    # Attributs du MCD
    provinces = models.CharField(max_length=100)
    cod_provinc = models.CharField(max_length=10)
    communes = models.CharField(max_length=100)
    ccod_commun = models.CharField(max_length=10)
    zones = models.CharField(max_length=100)
    ccod_zones = models.CharField(max_length=10)
    type_zone = models.CharField(max_length=50) # 'TYPE' dans le MCD
    colqtr = models.CharField(max_length=100)
    ccodcolqtr = models.CharField(max_length=20, unique=True)
    
    # Champ pour importer ton Shapefile (Multipolygon)
    geom = models.MultiPolygonField(srid=4326) 

    def __str__(self): return f"{self.colqtr} ({self.communes})"

class CompagneAgricole(models.Model):
    annee = models.IntegerField()
    mois = models.CharField(max_length=20)
    jours = models.IntegerField(null=True)
    date = models.DateField()
    def __str__(self): return str(self.annee)

class Saison(models.Model):
    campagne = models.ForeignKey(CompagneAgricole, on_delete=models.CASCADE)
    nom = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B')))

class Menage(models.Model):
    id_mcd = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    nom_chef_menage = models.CharField(max_length=255)
    prenom_c_m = models.CharField(max_length=255)
    sexe_c_m = models.CharField(max_length=1)
    statut_particulier = models.CharField(max_length=100, blank=True)
    niveau_educa_chef = models.CharField(max_length=100)
    statut_matrimonial = models.CharField(max_length=100)
    taille_menage = models.IntegerField()
    appartient_cooperative = models.BooleanField(default=False)
    nom_cooperative = models.CharField(max_length=255, blank=True)
    date_enquete = models.DateField()
    nom_enqueteur = models.CharField(max_length=255)
    source_saisie = models.CharField(max_length=100)
    
    # Lien vers la table plate Decoupage
    decoupage = models.ForeignKey(Decoupage, on_delete=models.PROTECT)

class Consommation(models.Model):
    menage = models.OneToOneField(Menage, on_delete=models.CASCADE)
    sdam_score = models.IntegerField()
    sca_score = models.FloatField()
    nb_repas_saison_normale = models.IntegerField()
    nb_repas_saison_soudure = models.IntegerField()
    difficultes_alimentaires_12m = models.BooleanField()
    frequence_difficultes = models.CharField(max_length=100)
    mois_plus_difficiles = models.CharField(max_length=255)
    chocs_5_derniers_ans = models.BooleanField()
    type_chocs = models.CharField(max_length=255)
    acces_eau_potable = models.BooleanField()
    acces_soins_base = models.BooleanField()
    distance_structure_sanitaire_km = models.FloatField()

class Elevage(models.Model):
    menage = models.ForeignKey(Menage, on_delete=models.CASCADE)
    espece = models.CharField(max_length=100)
    nb_animaux = models.FloatField()
    revenu_2020 = models.FloatField()
    revenu_2025 = models.FloatField()
    raison_absence_betail = models.TextField(blank=True)

class Indicateur(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=100)
    unite = models.CharField(max_length=50)
    frequence = models.CharField(max_length=100)
    formule_calcul = models.TextField()
    source_donnees = models.CharField(max_length=255)

class Valeur(models.Model):
    indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)
    decoupage = models.ForeignKey(Decoupage, on_delete=models.CASCADE)
    periode = models.CharField(max_length=100)
    valeur_calculee = models.FloatField()
    valeur_cible = models.FloatField()
    date = models.DateField()
    methode_calcul = models.TextField()

class FicheProvinciale(models.Model):
    annee = models.IntegerField()
    mode_saisie = models.CharField(max_length=100)
    statut = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(blank=True)

class FicheFiliere(models.Model):
    annee = models.IntegerField()
    statut = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

class Anomalie(models.Model):
    table_source = models.CharField(max_length=100)
    id_source = models.IntegerField()
    champ_concerne = models.CharField(max_length=100)
    type_anomalie = models.CharField(max_length=255)
    statut = models.CharField(max_length=50)
class Infrastructure(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    decoupage = models.ForeignKey(Decoupage, on_delete=models.CASCADE)