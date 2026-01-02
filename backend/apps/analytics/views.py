from rest_framework import viewsets
from django.db.models import Avg, Count
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from foncier.serializers import *


class DecoupageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Decoupage.objects.all()
    def get_serializer_class(self):
        if self.request.query_params.get('format') == 'geojson':
            return DecoupageGeoSerializer
        return DecoupageSerializer

class IndicateurViewSet(viewsets.ModelViewSet):
    queryset = Indicateur.objects.all()
    serializer_class = IndicateurSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ValeurViewSet(viewsets.ModelViewSet):
    queryset = Valeur.objects.all()
    serializer_class = ValeurSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['decoupage', 'indicateur__code', 'saison']

class MenageViewSet(viewsets.ModelViewSet):
    queryset = Menage.objects.all()
    serializer_class = MenageSerializer

class CompagneAgricoleViewSet(viewsets.ModelViewSet):
    queryset = CompagneAgricole.objects.all()
    serializer_class = CompagneAgricoleSerializer

class SaisonViewSet(viewsets.ModelViewSet):
    queryset = Saison.objects.all()
    serializer_class = SaisonSerializer

class ConsommationViewSet(viewsets.ModelViewSet):
    queryset = Consommation.objects.all()
    serializer_class = ConsommationSerializer

class ElevageViewSet(viewsets.ModelViewSet):
    queryset = Elevage.objects.all()
    serializer_class = ElevageSerializer

class InfrastructureViewSet(viewsets.ModelViewSet):
    queryset = Infrastructure.objects.all()
    serializer_class = InfrastructureSerializer

class FicheProvincialeViewSet(viewsets.ModelViewSet):
    queryset = FicheProvinciale.objects.all()
    serializer_class = FicheProvincialeSerializer

class FicheFiliereViewSet(viewsets.ModelViewSet):
    queryset = FicheFiliere.objects.all()
    serializer_class = FicheFiliereSerializer

class AnomalieViewSet(viewsets.ModelViewSet):
    queryset = Anomalie.objects.all()
    serializer_class = AnomalieSerializer




class KPIView(APIView):
    def get(self, request):
        # Exemple de calcul en temps réel pour A1 et A15
        avg_menage = Menage.objects.aggregate(val=Avg('taille_menage'))['val']
        total_parcelles = Parcelle.objects.count()
        secure_parcelles = Parcelle.objects.filter(est_securisee=True).count()
        
        kpis = [
            {
                "code": "A1",
                "label": "Taille moyenne du ménage",
                "value": round(avg_menage, 2) if avg_menage else 0,
                "unit": "personnes"
            },
            {
                "code": "A15",
                "label": "% parcelles sécurisées",
                "value": round((secure_parcelles / total_parcelles * 100), 2) if total_parcelles > 0 else 0,
                "unit": "%"
            }
        ]
        return Response({"kpis": kpis})