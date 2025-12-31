import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from apps.analytics.models import Decoupage

decoupage_mapping = {
    'provinces': 'PROVINCES',
    'cod_provinc': 'CODPROVINC',
    'communes': 'COMMUNES',
    'ccod_commun': 'CCODCOMMUN',
    'zones': 'ZONES',
    'ccod_zones': 'CCODZONES',
    'type_zone': 'TYPE',
    'colqtr': 'COLQTR',
    'ccodcolqtr': 'CCODCOLQTR',
    'geom': 'POLYGON',
}

# METS LE NOM EXACT DE TON NOUVEAU FICHIER ICI
shp_path = os.path.abspath(os.path.join('data', 'decoupage_administratif_burundi_complet.shp'))

def run(verbose=True):
    print(f"--- Démarrage de l'importation complète ({shp_path}) ---")
    
    # ÉTAPE CRUCIALE : Vider la table pour enlever les 35 anciens objets
    count_before = Decoupage.objects.count()
    print(f"Suppression de {count_before} anciennes entités...")
    Decoupage.objects.all().delete()
    
    lm = LayerMapping(
        Decoupage, shp_path, decoupage_mapping,
        transform=False
    )
    
    try:
        # On garde strict=False pour ne pas bloquer si une des 3000 lignes a un petit souci
        lm.save(strict=False, verbose=verbose)
        count_after = Decoupage.objects.count()
        print(f"\n✅ Importation terminée ! {count_after} entités enregistrées.")
    except Exception as e:
        print(f"\n❌ Erreur lors de l'import : {e}")