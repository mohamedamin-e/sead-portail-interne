from django.contrib.gis import admin
from .models import PhaseParcelle, Parcelle, Culture, TitreFoncier, ConflitFoncier, ParcelleLog

@admin.register(Parcelle)
class ParcelleAdmin(admin.GISModelAdmin):
    list_display = ('code', 'menage', 'phase_actuelle')

admin.site.register(PhaseParcelle)
admin.site.register(Culture)
admin.site.register(TitreFoncier)
admin.site.register(ConflitFoncier)
admin.site.register(ParcelleLog)