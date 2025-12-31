import os
from django.contrib.gis.gdal import DataSource

shp_path = os.path.abspath(os.path.join('data', 'decoupage_burundi.shp'))
ds = DataSource(shp_path)
layer = ds[0]

print(f"Champs trouvés dans le Shapefile : {layer.fields}")