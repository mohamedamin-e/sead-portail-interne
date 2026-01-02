from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActeurExteViewSet, MarcheViewSet, ProduitViewSet,
    PrixViewSet, HistoriqueViewSet, OffreViewSet, DemandeViewSet
)

router = DefaultRouter()
router.register(r'acteurs', ActeurExteViewSet)
router.register(r'marches', MarcheViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'prix', PrixViewSet)
router.register(r'historique-prix', HistoriqueViewSet)
router.register(r'offres', OffreViewSet)
router.register(r'demandes', DemandeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]