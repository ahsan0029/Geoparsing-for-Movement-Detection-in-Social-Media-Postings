import pandas as pd
import geopandas
import csv
from string import Template
from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template
from guess_language import guess_language
from shapely.geometry import Point


tweet_data= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\tweet_data_3275.csv", index_col=0)
print(tweet_data)

tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manual_annotation_URI.csv", index_col=0)
print(tweet_location.head(10))



df = pd.DataFrame([]) #Storing coordinates in DataFrame
list_coordinate=[] 
error_uri={}
dict_uri_not_country = {}
#reading tweet with manual location annotataion
tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manual_annotation_URI.csv")
d=tweet_location.head(5)
for index, row in d.iterrows():
    a=list(row[2].split(","))   
    #print(a, index)
    text_id=index
    tweet_lang=str(row[1].split(",")) 
    lang = guess_language(tweet_lang)
    #print(lang)
    if lang == "en":
        sparql_db = "http://dbpedia.org/sparql"
    else:
        sparql_db = "http://{}.dbpedia.org/sparql".format(lang) #Harmonization between different DBpedia databases 
    length=len(a)
    #print(length)
    for i in a:                          #iterating depends on number of URIs in rows
        #print(i)
        #location=row['Location']
        location=i
        try:
            sparql = SPARQLWrapper(sparql_db) #It will go to different language database pages according to there language  
            query = Template("""
                PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                SELECT DISTINCT ?subject ?sa ?lat ?long ?capital WHERE {{
                 ?subject dbo:capital ?capital.
                 ?subject rdf:type dbo:Location.
                 ?subject geo:lat ?lat.
                 ?subject geo:long ?long
                 FILTER ((?sa = $uri || ?subject = $uri)).
                }} 
            """)
            c=location #row['Location']
            b='"'+c+'"'               
            #print(b)
            sparql.setQuery(query.substitute(uri=b))
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
            #print(type(results["results"]["bindings"]))
            if len(results["results"]["bindings"]) == 0:
                dict_uri_not_country.update({'{}'.format(text_id):[c,row[1]]})

                #df_not_country = df_not_country.append(pd.DataFrame({"id":text_id,"Location":c}))
                # print(df_not_country)



            for result in results["results"]["bindings"]:
            #Displaying lat and long from SPARQL

                    #print(result["lat"]["value"],result["long"]["value"], result["s"]["value"])
                lat=float(result["lat"]["value"])

                long=float(result["long"]["value"])

                capital=result["capital"]["value"]

                df = df.append(pd.DataFrame({"id":text_id,"tweet":row[1],"Location":c, "Lat": [lat],"Long":[long],"Capital":[capital]}))
                list_coordinate+=result["lat"]["value"],result["long"]["value"],result["capital"]["value"]
        except:
            #print("Error occurred ")
            #put list of uri for error
            error_uri.update({'{}'.format(text_id):[c,row[1]]})


df_err = pd.DataFrame([([k] + v) for k, v in error_uri.items()], columns=['id','Location','Tweet'])
#print(list_coordinate)
print(df_err)

print("---------------------------------------------------------------------------")

print(df)

newdf = df.drop_duplicates( 
  subset = ['id','Capital'],                     #drop duplicate value based on Lat Long
  keep = 'last').reset_index(drop = True)    

print(newdf) 
capital_con=newdf[["Capital"]]
df_1 = pd.DataFrame([]) #Storing coordinates in DataFrame
list_coordinate_1=[]
error_data={}
print(dict_uri_not_country) 
df_2 = pd.DataFrame([([k] + v) for k, v in dict_uri_not_country.items()], columns=['id','Location','Tweet'])

for index, row in newdf.iterrows():
    n=list(row[5].split(","))
    v=row[5]
    #print(v) 
    tweet_lang_1=str(row[1].split(",")) 
    lang_1 = guess_language(tweet_lang_1)
    #print(lang_1)
    if lang_1 == "en":
        sparql_db = "http://dbpedia.org/sparql"
    else:
        sparql_db = "http://{}.dbpedia.org/sparql".format(lang_1)  
    try:


        sparql = SPARQLWrapper(sparql_db) #It will go to different language database pages according to there language  
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

            df_1 = df_1.append(pd.DataFrame({"id":row[0],"tweet": row[1],"Location":v,"Lat": [lat],"Long":[long]}))
            list_coordinate_1+=result["lat"]["value"],result["long"]["value"]
    except:
        #print("error") 
        error_data.update({'{}'.format(row[0]):[v,row[1]]})
df_error_data = pd.DataFrame([([k] + v) for k, v in error_data.items()], columns=['id','Location','Tweet'])        
print(df_error_data) 
print("---------------------------------------------------------------------")
df_1 = df_1.drop_duplicates( 
  subset = ['id','Location'],                     #drop duplicate value based on Lat Long
  keep = 'last').reset_index(drop = True)
print(df_1)  


df_3 = pd.DataFrame([]) #Storing coordinates in DataFrame
error_data_1={}
print(df_2)
for index, row in df_2.iterrows():
    #n=list(row[2].split(","))
    v=row[1]
    #print(v) 
    tweet_lang_2=str(row[2].split(",")) 
    lang_2 = guess_language(tweet_lang_2)
    #print(lang_2)
    if lang_2 == "en":
        sparql_db = "http://dbpedia.org/sparql"
    else:
        sparql_db = "http://{}.dbpedia.org/sparql".format(lang_2)  
    try:


        sparql = SPARQLWrapper(sparql_db) #It will go to different language database pages according to there language  
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

            df_3 = df_3.append(pd.DataFrame({"id":row[0],"tweet": row[2],"Location":row[1],"Lat": [lat],"Long":[long]}))
    except:
        print("error") 

        error_data_1.update({'{}'.format(row[0]):[row[1],row[2]]})
df_3 = df_3.drop_duplicates( 
  subset = ['id','Location'],                     #drop duplicate value based on Lat Long
  keep = 'last').reset_index(drop = True)    

df_error_data_1 = pd.DataFrame([([k] + v) for k, v in error_data_1.items()], columns=['id','Location','Tweet'])        
print(df_error_data_1)
print("----------------------------------------------------------------------------------")
print(df_3)  


dataset_arrange=df_1.append(df_3)
dataset_arrange['id'] = dataset_arrange['id'].astype(int) 
dataset_arrange.sort_values(by='id', ascending=True, inplace=True) 
print(dataset_arrange)

dataset_arrange.to_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\Location_Coordinates.csv", index=False)




