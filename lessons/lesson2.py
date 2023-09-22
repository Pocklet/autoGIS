import pathlib
pathlib.Path()

path = pathlib.Path()
path = path.resolve()
print(path)

import fiona
print(fiona.supported_drivers)

# NOTEBOOK_PATH = pathlib.Path().resolve()
# DATA_DIRECTORY = NOTEBOOK_PATH / "data"


import geopandas
# municipalities = geopandas.read_file(
#     DATA_DIRECTORY / "finland_municipalities" / "finland_municipalities_2021.gpkg"
# )
# municipalities.head()


nuts_regions = geopandas.read_file("https://gisco-services.ec.europa.eu/distribution/v2/nuts/shp/NUTS_RG_60M_2021_3035.shp.zip")
print(nuts_regions.head())

# nuts_regions.to_file(DATA_DIRECTORY / "europe_nuts_regions.geojson")


# reading and writing from databases
import sqlalchemy
DB_CONNECTION_URL = "postgresql://myusername:mypassword@myhost:5432/mydatabase";
db_engine = sqlalchemy.create_engine(DB_CONNECTION_URL)

countries = geopandas.read_postgis(
    "SELECT name, geometry FROM countries",
    db_engine
)
countries.to_postgis(
    "new_table", 
    db_engine
)

# reading data from web feature service
population_grid = geopandas.read_file(
    "https://kartta.hsy.fi/geoserver/wfs"
    "?service=wfs"
    "&version=2.0.0"
    "&request=GetFeature"
    "&typeName=asuminen_ja_maankaytto:Vaestotietoruudukko_2020"
    "&srsName=EPSG:3879"
    "&bbox=25494767,6671328,25497720,6673701,EPSG:3879",
    crs="EPSG:3879"
)
population_grid.head()