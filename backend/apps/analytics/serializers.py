from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class DecoupageGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Decoupage
        geo_field = 'geom'
        fields = '__all__'

class DecoupageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decoupage
        fields = ('id', 'provinces', 'communes', 'colqtr', 'ccodcolqtr')

class IndicateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicateur
        fields = '__all__'

class ValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valeur
        fields = '__all__'

class MenageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menage
        fields = '__all__'

class CompagneAgricoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompagneAgricole
        fields = '__all__'

class SaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saison
        fields = '__all__'

class ConsommationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommation
        fields = '__all__'

class ElevageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevage
        fields = '__all__'

class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'

class FicheProvincialeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheProvinciale
        fields = '__all__'

class FicheFiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheFiliere
        fields = '__all__'

class AnomalieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomalie
        fields = '__all__'