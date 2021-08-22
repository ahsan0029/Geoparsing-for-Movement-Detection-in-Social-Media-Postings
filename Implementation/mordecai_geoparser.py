docker pull elasticsearch:5.5.2
curl https://andrewhalterman.com/files/geonames_index.tar.gz -o wget_log.txt
tar -xzf geonames_index.tar.gz
docker run -d -p 127.0.0.1:9200:9200 -v C:/Users/insan/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2

from mordecai import Geoparser
geo = Geoparser()
#test
a=geo.geoparse("input data")

tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\Location_Coordinates.csv")
tweet_location=tweet_location.head(10)
geo = Geoparser()
manual_annotation=pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\Location_Coordinates.csv")


loc=tweet_location.groups()
print(loc)
a=geo.geoparse(loc)
print(a)
error_data={}
for v in a:
    #print (v["word"],v["geo"]["lat"],v["geo"]["lon"])
    f=v["word"]
    j=v["geo"]["lat"]
    l=v["geo"]["lon"]
    
    error_data.update({'{}'.format(f):[j,l]})
        #error_data.update({'{}'.format(row[0]):[v,row[1]]})
df_error_data = pd.DataFrame([([k] + v) for k, v in error_data.items()], columns=['Location','Lat','Long']) 


for s in data_mordecai:
    for v in s:
        
        print(v)
        print (v["word"],v["geo"]["lat"],v["geo"]["lon"])
        f=v["word"]
        j=v["geo"]["lat"]
        l=v["geo"]["lon"]
        coordiantes_mordecai.update({'{}'.format(f):[j,l]})
    #error_data.update({'{}'.format(row[0]):[v,row[1]]})
df_coordiantes_mordecai = pd.DataFrame([([k] + v) for k, v in coordiantes_mordecai.items()], columns=['Location','Lat','Long'])
df_coordiantes_mordecai


frames = [data, df_coordiantes_mordecai]

merge=pd.concat(frames, axis=1)



import geopandas as gpd
from shapely.geometry import Point
dis = []
for (index, row) in merge.iterrows():
#     if row["twee_t"]==row["tweet"]:  
      v=[row["Long"], row["Lon_g"]],[row["Lat"], row["La_t"]]
      geom=[Point(xy) for xy in zip([row["Long"], row["Lon_g"]],[row["Lat"], row["La_t"]])]
      gdf=gpd.GeoDataFrame(geometry=geom,crs={'init':'epsg:4326'})
        #gdf.to_crs(epsg=4326,inplace=True)
      l=gdf.distance(gdf.shift())
      geodesic_dis=list(l)
      print(geodesic_dis[1])
