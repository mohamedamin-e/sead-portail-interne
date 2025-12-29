from django.db import models

class ActeurExte(models.Model):
    type = models.CharField(max_length=100)
    nom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    statut = models.CharField(max_length=50)

class Marche(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    jours_marche = models.CharField(max_length=100)
    # Lien vers Decoupage unique
    decoupage = models.ForeignKey('analytics.Decoupage', on_delete=models.CASCADE)

class Produit(models.Model):
    code = models.CharField(max_length=50)
    libelle = models.CharField(max_length=200)
    categorie = models.CharField(max_length=100)
    unite_mesure = models.CharField(max_length=50)
    specification_qualite = models.TextField()

class Prix(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    marche = models.ForeignKey(Marche, on_delete=models.CASCADE)
    date_releve = models.DateField()
    prix_vente_moyen = models.FloatField()
    prix_min = models.FloatField()
    prix_max = models.FloatField()
    unite_prix = models.CharField(max_length=50)

class Historique(models.Model):
    prix_ref = models.ForeignKey(Prix, on_delete=models.CASCADE)
    valeur_prix = models.FloatField() # 'liste_prix' dans le MCD
    date_historique = models.DateField(auto_now_add=True)
    
class Offre(models.Model):
    acteur = models.ForeignKey(ActeurExte, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_disponible = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut_offre = models.CharField(max_length=50)

class Demande(models.Model):
    acteur = models.ForeignKey(ActeurExte, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_recherchee = models.FloatField()
    prix_souhaite = models.FloatField()
    statut_demande = models.CharField(max_length=50)