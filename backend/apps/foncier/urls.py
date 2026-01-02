from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ParcelleViewSet, TitreFoncierViewSet, ConflitFoncierViewSet,
    PhaseParcelleViewSet, CultureViewSet, ParcelleLogViewSet
)

router = DefaultRouter()
router.register(r'parcelles', ParcelleViewSet)
router.register(r'titres', TitreFoncierViewSet)
router.register(r'conflits', ConflitFoncierViewSet)
router.register(r'phases', PhaseParcelleViewSet)
router.register(r'cultures', CultureViewSet)
router.register(r'logs', ParcelleLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]