from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Les rôles du cahier des charges
    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Administrateur'),
        ('ADMIN_REGIONAL', 'Administrateur Régional'),
        ('UGP_MANAGER', 'Manager UGP'),
        ('EXPERT', 'Expert Ministère'),
        ('SUPERVISEUR', 'Superviseur Provincial'),
        ('AGENT', 'Agent de terrain'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='AGENT')
    user_type = models.CharField(max_length=10, choices=(('INTERNE', 'Interne'), ('EXTERNE', 'Externe')), default='INTERNE')