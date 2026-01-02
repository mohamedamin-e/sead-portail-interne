from urllib import response
from rest_framework import viewsets
from .models import *
from .serializers import *

class PhaseParcelleViewSet(viewsets.ModelViewSet):
    queryset = PhaseParcelle.objects.all()
    serializer_class = PhaseParcelleSerializer

class ParcelleViewSet(viewsets.ModelViewSet):
    queryset = Parcelle.objects.all()
    def get_serializer_class(self):
        # Utilise le format GéoJSON si demandé dans l'URL
        if self.request.query_params.get('format') == 'geojson':
            return ParcelleGeoSerializer
        return ParcelleSerializer

class CultureViewSet(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer

class TitreFoncierViewSet(viewsets.ModelViewSet):
    queryset = TitreFoncier.objects.all()
    serializer_class = TitreFoncierSerializer

class ConflitFoncierViewSet(viewsets.ModelViewSet):
    queryset = ConflitFoncier.objects.all()
    serializer_class = ConflitFoncierSerializer

class ParcelleLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ParcelleLog.objects.all()
    serializer_class = ParcelleLogSerializer



from authentication.models import LogActivite 
from analytics.models import Decoupage 
from .models import Parcelle, PhaseParcelle, Culture, TitreFoncier, ConflitFoncier, ParcelleLog
from .serializers import *
from rest_framework.decorators import action  # <-- CRUCIAL : Import manquant réglé ici

class ParcelleViewSet(viewsets.ModelViewSet):
    queryset = Parcelle.objects.all()

    def get_serializer_class(self):
        if self.request.query_params.get('format') == 'geojson':
            return ParcelleGeoSerializer
        return ParcelleSerializer

    # LOGIQUE STEP 3 : Géo-validation automatique lors de la création
    def perform_create(self, serializer):
        # 1. On récupère la géométrie envoyée par le frontend
        geom = serializer.validated_data.get('geom')
        
        # 2. On cherche automatiquement dans quel découpage se trouve la parcelle
        # geom__contains : On cherche la zone qui contient le centre de la parcelle
        zone = Decoupage.objects.filter(geom__contains=geom.centroid).first()
        
        # 3. On enregistre avec la zone trouvée (ou None si hors Burundi)
        instance = serializer.save(decoupage=zone)

        # 4. On crée un log automatique (Demande superviseur n°2)
        LogActivite.objects.create(
            action="creation",
            module="foncier",
            ressource_type="Parcelle",
            ressource_id=instance.id,
            user=self.request.user,
            details={"message": f"Parcelle {instance.code} créée et liée à la zone {zone.colqtr if zone else 'Inconnue'}"}
        )

    # LOGIQUE STEP 3 : Workflow de validation (Bouton Valider sur React)
    @action(detail=True, methods=['post'], url_path='valider')
    def valider_parcelle(self, request, pk=None):
        parcelle = self.get_object()
        # On passe à la phase "Validation" (ID 3 dans ton modèle Phase)
        parcelle.phase_actuelle_id = 3 
        parcelle.save()
        
        LogActivite.objects.create(
            action="validation",
            module="foncier",
            ressource_type="Parcelle",
            ressource_id=parcelle.id,
            user=request.user,
            details={"message": "Passage en phase de validation terminé"}
        )
        return response({"status": "Parcelle validée"})