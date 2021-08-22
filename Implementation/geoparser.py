import geopandas as gpd
from __future__ import print_function
import numpy as np
import math
from scipy.integrate import simps
from numpy import trapz
import pandas as pd
import geopandas
import csv
from string import Template
from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template
from guess_language import guess_language
from shapely.geometry import Point
from pyproj import CRS


temp_df = pd.DataFrame()
append_json=[]
tweet_id=[]
loc_tweet=[]
data_2= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\manual_annotation_URI.csv", index_col=False)
#data_2=data_2.head(5)
for index, row in data_2.iterrows():
    loc=row['Tweet']
    print(loc)
    identifier=row['id']
    print(identifier)
     # initial consts
    try:
        BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}&types={types}'
        TEXT = str(loc)
        CONFIDENCE = '0.5'
        SUPPORT = '10'
        TYPES = 'DBpedia%3ALocation'
        REQUEST = BASE_URL.format(
            text=urllib.parse.quote_plus(TEXT), 
            confidence=CONFIDENCE, 
            support=SUPPORT,
            types=TYPES
        )
        HEADERS = {'Accept': 'application/json'}
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        all_urls = []
        r = requests.get(url=REQUEST, headers=HEADERS)
        response = r.json()
        append_json.append(response)                                                                                                                                                                                                                                                        
        resources = response['Resources']
        ab=pd.json_normalize(resources)
        abc=ab[['@URI']]
        #print(abc)
        df_t = abc.T
        #print(df_t)
        new_df=pd.DataFrame(df_t)
        temp_df=temp_df.append(new_df)
        tweet_id.append(identifier)
        loc_tweet.append(loc)

    except:
        print("Error occurred ")
# with open(r'C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\URI_Annotated_data.json', 'w') as json_file:
#         json.dump(all_urls, json_file)
temp_df["tweet"]=loc_tweet
temp_df["id"]=tweet_id
#temp_df.to_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\New folder\uri.csv")
cols = temp_df.columns.tolist()
cols=cols[-1:]+cols[:-1]
cols=cols[-1:]+cols[:-1]
temp_df=temp_df[cols]
print(cols)
print(temp_df)
temp_df.to_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\dbpedia_spotlight.csv",index=False)


crs_4326 = CRS.from_epsg(4326)
crs_4326
gdf.crs = {"init":"epsg:4326"}
gdf=gdf.to_crs(epsg=4326)


dbpedia_location= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\dbpedia_spotlight.csv")





# The y values.  A numpy array is used here,
# but a python list could also be used.
y = np.array(p)

# Compute the area using the composite trapezoidal rule.
area = trapz(y, dx=1)
print("area =", area)
n=math.log(20039)
print(n)
c=np.log(20039)
print(c)
x=[]
p=[]
for i in dis:
    if i != 0:
        z=np.log(i)
        p.append(z)

dbpedia_location= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\dbpedia_spotlight.csv")
df_rearrange = pd.DataFrame([]) #Storing coordinates in DataFrame
for index, row in dbpedia_location.iterrows():
    data={"id": [row[1]],"tweet": [row[0]],"0": [row[2]],"1": [row[3]],"2": [row[4]],"3": [row[5]],"4": [row[6]]}
    df=pd.DataFrame(data)
    f=df.loc[:, '0':'4']
    df_t = f.T
    a=row[0]
    b=row[1]
    for index, row in df_t.iterrows():
        df_rearrange = df_rearrange.append(pd.DataFrame({"id":b,"tweet": a,"Location_URI":row}))

df_rearrange=df_rearrange.dropna()
print(df_rearrange)
      
df_1 = pd.DataFrame([]) #Storing coordinates in DataFrame
error_data={}
for index, row in df_rearrange.iterrows():
    v=row[2]
    print(v) 
    try:
        sparql = SPARQLWrapper('http://dbpedia.org/sparql') 
        query = Template("""
                    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                    select ?capital where { <$m><http://dbpedia.org/ontology/capital> ?capital }
                    """)
        sparql.setQuery(query.substitute(m=v))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:

            Capital=result["capital"]["value"]
            df_1 = df_1.append(pd.DataFrame({"id":row[0],"tweet": row[1],"Location": row[2], "Capital_URI": [Capital]}))
    except:
        print("error")
        error_data.update({'{}'.format(row[0]):[row[1],row[2]]})
        #error_data.update({'{}'.format(row[0]):[v,row[1]]})
df_error_data = pd.DataFrame([([k] + v) for k, v in error_data.items()], columns=['id','Tweet','Location']) 


df_coordinate = pd.DataFrame([]) #Storing coordinates in DataFrame
error_data={}
for index, row in df_1.iterrows():
    v=row[3]
    print(v) 
    try:
        sparql = SPARQLWrapper('http://dbpedia.org/sparql') 
        query = Template("""
                    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                    select * { <$m> geo:lat ?lat ; geo:long ?long }
                """)
            
        sparql.setQuery(query.substitute(m=v))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
                        #print(result)

                #Displaying lat and long from SPARQL

                        #print(result["lat"]["value"],result["long"]["value"], result["s"]["value"])
            lat=float(result["lat"]["value"])

            long=float(result["long"]["value"])

            df_coordinate = df_coordinate.append(pd.DataFrame({"id":row[0],"tweet": row[1],"Location":row[3],"Lat": [lat],"Long":[long]}))
    except:
        print("error") 
        #error_data.update({'{}'.format(row[0]):[row[1],row[2]]})
        #error_data.update({'{}'.format(row[0]):[v,row[1]]})
#df_error_data = pd.DataFrame([([k] + v) for k, v in error_data.items()], columns=['id','Tweet','Location']) 


a=dbpedia_gdf[['id','geometry']]
for index, row in dbpedia_gdf.iterrows():
    dist = geopy.distance.geodesic((row[3],row[4]))
    print(dist.km)


frames = [a, b]

merge=pd.concat(frames, axis=1)	


gdf= geopandas.GeoDataFrame(a ,geometry=geopandas.points_from_xy(a.Lat, a.Long))


projection= geopandas.GeoDataFrame(a ,geometry=geopandas.points_from_xy(a.Lat, a.Long))
projection.columns = ['id', 'twee_t',"Locatio_n","La_t",'Lon_g']



import geopandas as gpd
from shapely.geometry import Point
dis = []
error_dis=[]
for (index, row) in merge.iterrows():
#     if row["twee_t"]==row["tweet"]:  
      v=[row["Long"], row["Lon_g"]],[row["Lat"], row["La_t"]]
      geom=[Point(xy) for xy in zip([row["Long"], row["Lon_g"]],[row["Lat"], row["La_t"]])]
      gdf=gpd.GeoDataFrame(geometry=geom,crs={'init':'epsg:4326'})
        #gdf.to_crs(epsg=4326,inplace=True)
      l=gdf.distance(gdf.shift())
      geodesic_dis=l
      #print(geodesic_dis[1])
      error_dis.append(geodesic_dis[1])
    
      if geodesic_dis[1] <= 20389:
  
          dis.append(geodesic_dis[1])
		  
location=[]
for index, row in manual_annotation.iterrows():
    #print(row[1])
    a=row[1]
    places = GeoText(a)
    cities = places.countries
    location.append(cities)
    print(cities)
    if len(cities) == 0:
        m=a.title()
        places = GeoText(m)
        cities = places.cities
        location.append(cities)
        print(cities)
        print (m)		 


geo_loc= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\geotext_loc.csv")
df_rearrange = pd.DataFrame([]) #Storing coordinates in DataFrame
for index, row in dbpedia_location.iterrows():
    data={"id": [row[1]],"tweet": [row[0]],"0": [row[2]],"1": [row[3]],"2": [row[4]],"3": [row[5]],"4": [row[6]]}
    df=pd.DataFrame(data)
    f=df.loc[:, '0':'4']
    df_t = f.T
    a=row[0]
    b=row[1]
    for index, row in df_t.iterrows():
        df_rearrange = df_rearrange.append(pd.DataFrame({"id":b,"tweet": a,"Location_URI":row}))

df_rearrange=df_rearrange.dropna()
print(df_rearrange)



df_1 = pd.DataFrame([]) #Storing coordinates in DataFrame
error_data={}
for index, row in df_rearrange.iterrows():
    v=row[2]
    print(v) 
    try:
        sparql = SPARQLWrapper('http://dbpedia.org/sparql') 
        query = Template("""
                    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                    select ?capital where { <$m><http://dbpedia.org/ontology/capital> ?capital }
                    """)
        sparql.setQuery(query.substitute(m=v))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:

            Capital=result["capital"]["value"]
            df_1 = df_1.append(pd.DataFrame({"id":row[0],"tweet": row[1],"Location": row[2], "Capital_URI": [Capital]}))
    except:
        print("error")
        error_data.update({'{}'.format(row[0]):[row[1],row[2]]})
        #error_data.update({'{}'.format(row[0]):[v,row[1]]})
df_error_data = pd.DataFrame([([k] + v) for k, v in error_data.items()], columns=['id','Tweet','Location']) 
    
