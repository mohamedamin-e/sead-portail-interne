from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)
# IMPORT DES VUES JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- DOCUMENTATION API ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # --- AUTHENTIFICATION JWT (C'est ce qui te manquait) ---
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # --- TES APIS ---
    path('api/auth/', include('authentication.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/foncier/', include('foncier.urls')),
    path('api/market/', include('agri_market.urls')),
]