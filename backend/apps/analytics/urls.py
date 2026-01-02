from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DecoupageViewSet, MenageViewSet, ConsommationViewSet, 
    ElevageViewSet, IndicateurViewSet, ValeurViewSet,
    CompagneAgricoleViewSet, SaisonViewSet, InfrastructureViewSet,
    FicheProvincialeViewSet, FicheFiliereViewSet, AnomalieViewSet
)

router = DefaultRouter()
router.register(r'decoupage', DecoupageViewSet)
router.register(r'menages', MenageViewSet)
router.register(r'consommation', ConsommationViewSet)
router.register(r'elevage', ElevageViewSet)
router.register(r'indicateurs', IndicateurViewSet)
router.register(r'valeurs', ValeurViewSet)
router.register(r'campagnes', CompagneAgricoleViewSet)
router.register(r'saisons', SaisonViewSet)
router.register(r'infrastructures', InfrastructureViewSet)
router.register(r'fiches-provinciales', FicheProvincialeViewSet)
router.register(r'fiches-filieres', FicheFiliereViewSet)
router.register(r'anomalies', AnomalieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]