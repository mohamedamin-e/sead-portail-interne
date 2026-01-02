from django.contrib.gis.db import models
from django.conf import settings

# --- 1. RÉFÉRENTIEL GÉOGRAPHIQUE (Shapefile) ---
class Decoupage(models.Model):
    provinces = models.CharField(max_length=100, null=True, blank=True)
    cod_provinc = models.CharField(max_length=10, null=True, blank=True)
    communes = models.CharField(max_length=100, null=True, blank=True)
    ccod_commun = models.CharField(max_length=10, null=True, blank=True)
    zones = models.CharField(max_length=100, null=True, blank=True)
    ccod_zones = models.CharField(max_length=10, null=True, blank=True)
    type_zone = models.CharField(max_length=50, null=True, blank=True) 
    colqtr = models.CharField(max_length=100, null=True, blank=True)
    ccodcolqtr = models.CharField(max_length=20, null=True, blank=True)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.colqtr if self.colqtr else "Zone sans nom"

# --- 2. TEMPORALITÉ (Demande Superviseur) ---
class CompagneAgricole(models.Model):
    annee = models.IntegerField()
    mois = models.CharField(max_length=20)
    jours = models.IntegerField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"Campagne {self.annee}"

class Saison(models.Model):
    campagne = models.ForeignKey(CompagneAgricole, on_delete=models.CASCADE, related_name='saisons')
    nom = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B')))

    def __str__(self):
        return f"{self.campagne} - Saison {self.nom}"

# --- 3. COLLECTE : MÉNAGE & EXPLOITANT ---
class Menage(models.Model):
    id_mcd = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True) # A12
    nom_chef_menage = models.CharField(max_length=255)
    prenom_c_m = models.CharField(max_length=255, default='')
    sexe_c_m = models.CharField(max_length=1, choices=(('H', 'H'), ('F', 'F'))) # A2
    age_c_m = models.IntegerField(default=0) # A3
    statut_particulier = models.CharField(max_length=100, blank=True)
    niveau_educa_chef = models.CharField(max_length=100) # A4
    statut_matrimonial = models.CharField(max_length=100)
    taille_menage = models.IntegerField() # A1
    appartient_cooperative = models.BooleanField(default=False) # A5
    nom_cooperative = models.CharField(max_length=255, blank=True)
    date_enquete = models.DateField(auto_now_add=True)
    nom_enqueteur = models.CharField(max_length=255, blank=True)
    source_saisie = models.CharField(max_length=100, default='QField')
    
    # Relations
    decoupage = models.ForeignKey(Decoupage, on_delete=models.PROTECT)
    campagne = models.ForeignKey(CompagneAgricole, on_delete=models.PROTECT, null=True)
    
    # Scores nutritionnels pour les indicateurs (A44, A45)
    sdam_score = models.FloatField(default=0, null=True, blank=True)
    sca_score = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.nom_chef_menage}"

class Consommation(models.Model):
    menage = models.OneToOneField(Menage, on_delete=models.CASCADE)
    nb_repas_saison_normale = models.IntegerField() # A46
    nb_repas_saison_soudure = models.IntegerField()
    difficultes_alimentaires_12m = models.BooleanField() # A47
    frequence_difficultes = models.CharField(max_length=100)
    mois_plus_difficiles = models.CharField(max_length=255)
    chocs_5_derniers_ans = models.BooleanField()
    type_chocs = models.CharField(max_length=255)
    acces_eau_potable = models.BooleanField() # A48
    acces_soins_base = models.BooleanField()
    distance_structure_sanitaire_km = models.FloatField()

class Elevage(models.Model):
    menage = models.ForeignKey(Menage, on_delete=models.CASCADE)
    espece = models.CharField(max_length=100) # A9
    nb_animaux = models.FloatField()
    revenu_2020 = models.FloatField(default=0)
    revenu_2025 = models.FloatField(default=0)
    raison_absence_betail = models.TextField(blank=True)

# --- 4. SYSTÈME D'INDICATEURS (Le Cerveau) ---
class Indicateur(models.Model):
    code = models.CharField(max_length=10, unique=True) # A1 à A56
    libelle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=100) # Suivi, Performance, Impact
    unite = models.CharField(max_length=50)
    frequence = models.CharField(max_length=100)
    formule_calcul = models.TextField()
    source_donnees = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.code} - {self.libelle}"

class Valeur(models.Model):
    indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)
    decoupage = models.ForeignKey(Decoupage, on_delete=models.CASCADE)
    saison = models.ForeignKey(Saison, on_delete=models.CASCADE, null=True)
    valeur_calculee = models.FloatField()
    valeur_cible = models.FloatField(default=0)
    date = models.DateField()
    methode_calcul = models.TextField(blank=True)

# --- 5. INFRASTRUCTURE & QUALITÉ ---
class Infrastructure(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    decoupage = models.ForeignKey(Decoupage, on_delete=models.CASCADE)

class FluxSynchronisation(models.Model):
    date_heure = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    type_fiche = models.CharField(max_length=5, choices=(('F1','F1'),('F2','F2'),('F3','F3'),('F4','F4'),('F5','F5')))
    nb_enregistrements = models.IntegerField()
    status = models.CharField(max_length=20, default='en_attente')
    details = models.JSONField(null=True, blank=True)

class Anomalie(models.Model):
    TYPES = (('valeur_aberrante', 'Valeur aberrante'),('doublon', 'Doublon'),('incoherence', 'Incohérence logique'),('manquant', 'Champ manquant'))
    SEVERITE = (('critique', 'Critique'), ('importante', 'Importante'), ('mineure', 'Mineure'))
    STATUS = (('non_traite', 'Non traité'), ('en_cours', 'En cours'), ('resolu', 'Résolu'))

    type = models.CharField(max_length=50, choices=TYPES, default='valeur_aberrante')
    severite = models.CharField(max_length=20, choices=SEVERITE, default='mineure')
    description = models.TextField(default='')
    table_source = models.CharField(max_length=100, default='inconnue') 
    id_source = models.CharField(max_length=50, default='0')
    champ_concerne = models.CharField(max_length=50, default='aucun')
    valeur_actuelle = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='non_traite')
    assigne_a = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, blank=True)
    detecte_le = models.DateTimeField(auto_now_add=True, null=True)
    commentaire = models.TextField(blank=True)

# --- 6. RAPPORTS ---
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