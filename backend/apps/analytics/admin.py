from django.contrib.gis import admin
from .models import (
    Decoupage, Infrastructure, CompagneAgricole, Saison, 
    Menage, Consommation, Elevage, Indicateur, Valeur, 
    FicheProvinciale, FicheFiliere, Anomalie
)

@admin.register(Decoupage)
class DecoupageAdmin(admin.GISModelAdmin): # Affiche une carte dans l'admin
    list_display = ('colqtr', 'communes', 'provinces')
    search_fields = ('colqtr', 'communes')

admin.site.register(Infrastructure)
admin.site.register(CompagneAgricole)
admin.site.register(Saison)
admin.site.register(Menage)
admin.site.register(Consommation)
admin.site.register(Elevage)
admin.site.register(Indicateur)
admin.site.register(Valeur)
admin.site.register(FicheProvinciale)
admin.site.register(FicheFiliere)
admin.site.register(Anomalie)