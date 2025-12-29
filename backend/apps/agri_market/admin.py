from django.contrib import admin
from .models import ActeurExte, Marche, Produit, Prix, Historique, Offre, Demande

admin.site.register(ActeurExte)
admin.site.register(Marche)
admin.site.register(Produit)
admin.site.register(Prix)
admin.site.register(Historique)
admin.site.register(Offre)
admin.site.register(Demande)