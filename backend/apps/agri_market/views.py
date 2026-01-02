from rest_framework import viewsets
from .models import *
from .serializers import *

class ActeurExteViewSet(viewsets.ModelViewSet):
    queryset = ActeurExte.objects.all()
    serializer_class = ActeurExteSerializer

class MarcheViewSet(viewsets.ModelViewSet):
    queryset = Marche.objects.all()
    serializer_class = MarcheSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class PrixViewSet(viewsets.ModelViewSet):
    queryset = Prix.objects.all()
    serializer_class = PrixSerializer

class HistoriqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Historique.objects.all()
    serializer_class = HistoriqueSerializer

class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

class DemandeViewSet(viewsets.ModelViewSet):
    queryset = Demande.objects.all()
    serializer_class = DemandeSerializer