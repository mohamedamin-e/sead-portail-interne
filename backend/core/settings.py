"""
Django settings for SEAD project.
"""

import os
import sys
from pathlib import Path

# 1. BASE_DIR doit être défini en premier
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Ajout du dossier 'apps' au chemin système pour simplifier les imports
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2lt_7%=aw_i426-+h8=$z6@v(7(*_ir8y!4-9_rtis^p9m@ih1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Support Cartographique Géographique
    'django.contrib.gis', 

    # Librairies Tierces
    'rest_framework',
    'rest_framework_gis', # Pour envoyer du GeoJSON (parcelles) à React
    'corsheaders',        # Pour autoriser React à parler à Django

    # Tes Applications locales
    'apps.authentication',
    'apps.foncier',
    'apps.analytics',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # DOIT ÊTRE EN PREMIER
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Autoriser React (port 5173 par défaut avec Vite)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

ROOT_URLCONF = 'core.urls' # Vérifie que tu as bien renommé ton dossier en 'core'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Configuration de la Base de Données PostGIS (Crucial pour les parcelles)
# Assure-toi d'avoir créé une base nommée 'sead_db' dans PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sead_db',
        'USER': 'postgres',
        'PASSWORD': 'admin', # Même mot de passe que dans docker-compose
        'HOST': 'db',        # <--- TRÈS IMPORTANT : mettre 'db' et non 'localhost'
        'PORT': '5432',
    }
}


# On définit le modèle utilisateur personnalisé pour gérer les rôles
# (On le créera juste après dans apps/authentication/models.py)
AUTH_USER_MODEL = 'authentication.User'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
LANGUAGE_CODE = 'fr-fr' # Mis en français
TIME_ZONE = 'Africa/Bujumbura' # Fuseau horaire du Burundi
USE_I18N = True
USE_TZ = True


# Fichiers Statiques
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Fichiers Media (Pour stocker les certificats fonciers scannés et photos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Configuration de Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Autorise localhost et l'IP de docker
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
