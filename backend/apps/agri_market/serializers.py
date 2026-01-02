from rest_framework import serializers
from .models import *

class ActeurExteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActeurExte
        fields = '__all__'

class MarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marche
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class PrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prix
        fields = '__all__'

class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historique
        fields = '__all__'

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = '__all__'