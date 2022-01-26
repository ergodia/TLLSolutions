import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
# https://www.cbs.nl/en-gb/onze-diensten/open-data/statline-as-open-data/cartography

# Retrieve data with municipal boundaries from PDOK
geodata_url = 'https://geodata.nationaalgeoregister.nl/cbsgebiedsindelingen/wfs?request=GetFeature&service=WFS&version=2.0.0&typeName=cbs_gemeente_2017_gegeneraliseerd&outputFormat=json'
municipal_boundaries = gpd.read_file(geodata_url)

# Create a thematic map
p = municipal_boundaries.plot(figsize = (10,8))
p.axis('off')
p.set_title('Birth rate per 1,000 population, 2017')



# geo_df = gpd.read_file('../../data/Netherlands_shapefile/nl_1km.shp')
# fig, ax = plt.subplots()
# geo_df.plot(ax=ax,color='white', edgecolor='black')
# ax.set_aspect('equal')
plt.show()

