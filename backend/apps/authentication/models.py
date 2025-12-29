from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    code = models.CharField(max_length=50, unique=True) # MCD : admin, enqueteur, etc.
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self): return self.libelle

class User(AbstractUser):
    ROLES_CHOICES = (
        ('super_admin', 'Super Administrateur'),
        ('admin_regional', 'Admin Régional (BPEAE)'),
        ('enqueteur', 'Enquêteur Terrain'),
        ('validateur', 'Validateur / Superviseur'),
        ('analyste', 'Analyste'),
    )
    role_systeme = models.CharField(max_length=20, choices=ROLES_CHOICES, default='enqueteur')
    role_mcd = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    organisme = models.CharField(max_length=100, blank=True)
    statut = models.CharField(max_length=50, default='Actif')

    def __str__(self): return f"{self.username} ({self.role_systeme})"
class JournalAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type_action = models.CharField(max_length=100) # typeAction
    table_cible = models.CharField(max_length=100) # table_cible
    id_enrege_cible = models.CharField(max_length=100) # id_enrege_cible
    details = models.TextField(blank=True)
    adresse_ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.type_action} - {self.date}"