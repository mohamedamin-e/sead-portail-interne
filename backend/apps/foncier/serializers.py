from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class PhaseParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhaseParcelle
        fields = '__all__'

# Serializer GéoJSON pour afficher les polygones des parcelles sur React
class ParcelleGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Parcelle
        geo_field = 'geom'
        fields = '__all__'

class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelle
        fields = '__all__'

class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'

class TitreFoncierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitreFoncier
        fields = '__all__'

class ConflitFoncierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConflitFoncier
        fields = '__all__'

class ParcelleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelleLog
        fields = '__all__'