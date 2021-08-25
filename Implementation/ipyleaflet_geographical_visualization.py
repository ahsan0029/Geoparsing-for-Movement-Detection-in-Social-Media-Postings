import pandas as pd
a=pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\Geoparsing-for-Movement-Detection-in-Social-Media-Postings\Results\geoparsing_dataset\mordecai_Coordinates.csv")

b=pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\coordinates_dbpedia_spotlight.csv")


#dataset from dbpedia framework
from ipyleaflet import Map, Marker

dbpedia = b

# create map
dbpedia_map = Map(center=(1, -99), zoom=1)
for (index, row) in dbpedia.iterrows():
    marker = Marker(location=[row.loc['Lat'], row.loc['Long']], 
                    title=row.loc['Location'])
    dbpedia_map.add_layer(marker)

# display map    
dbpedia_map


#manual annotated dataset
from ipyleaflet import Map, Marker, AwesomeIcon

manual = b
manual_map = Map(center=(1, -99), zoom=1)
icon1 = AwesomeIcon(
    name='circle',
    marker_color="green",
    spin=False
)

for (index, row) in manual.iterrows():
    marker = Marker(location=[row.loc['Lat'], row.loc['Long']], 
                    title=row.loc['Location'],icon=icon1)
    manual_map.add_layer(marker)

# display map   
manual_map

import geocoder
import ipyleaflet
from ipyleaflet import Map, FullScreenControl

listlatlong=[]
for (index, row) in manual.iterrows():
    listlatlong.append([row.loc['Lat'], row.loc['Long']])
cities_heatmap = Map(center=(40, -99), zoom=4)
heatmap_layer = ipyleaflet.Heatmap(locations=listlatlong, radius=30, blur=20)
heatmap_full_screen_control = FullScreenControl()
cities_heatmap.add_layer(heatmap_layer)
cities_heatmap.add_control(heatmap_full_screen_control)

# display map
cities_heatmap



import ipyleaflet
from random import randint

from ipyleaflet import Map, Heatmap
listlatlong=[]
for (index, row) in a.iterrows():
    listlatlong.append([row.loc['Lat'], row.loc['Long'], 2])
cities_heatmap = Map(center=(0, 0), zoom=2)
heatmap_layer = ipyleaflet.Heatmap(locations=listlatlong, radius=15, blur=2, min_opacity = 0.3)
#heatmap_full_screen_control = FullScreenControl()
cities_heatmap.add_layer(heatmap_layer)
cities_heatmap