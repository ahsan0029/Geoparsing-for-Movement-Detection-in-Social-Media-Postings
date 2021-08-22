python -m spacy download en
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_sm
pip install stanfordnlp
import stanfordnlp
nlp = stanfordnlp.Pipeline() 
import pandas as pd

pip install seaborn
from sklearn.metrics import accuracy_score
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
#tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manuaL_annotation_URI.csv")
for index, row in tweet_location.iterrows():
    a=row[1]
    doc = nlp(" RT @mims: 60,000 refugees are reportedly traveling to Hungary")
    for token in doc:
         print(row[0], str(token.text),  str(token.lemma_),  str(token.pos_),  str(token.dep_))

displacy.render(doc, style='dep', jupyter=True, options={'distance':120})




nlp = spacy.load('en_core_web_sm')
doc = nlp("Over 4,000 Walk From Serbia To Hungary")
for token in doc:
    
    print( str(token.lemma_),  str(token.pos_),  str(token.dep_))

displacy.render(doc, style='dep', jupyter=True, options={'distance':120})


for t in doc:
    #print (t.text,t.pos_, t.dep_)
    if t.pos_ in ["NOUN", "PROPN"] and t.dep_ in ["pobj"]:
        #print ("v",t)
        #print (t.head.text)
        if t.head.text in ["From","at"]:
            print ("Origin: ", t)
        if t.head.text in ["To"]:
            print ("Desination: ", t)
    if t.pos_ in ["NOUN"] and t.dep_ in ["dobj"]:
        print ("left child", list(t.lefts), t)
        left_child = list(t.lefts)[-1]
        if left_child.dep_ in ["compound"] and left_child.pos_ in ["PROPN", "NOUN"]:
            print ("ori", left_child.text)
 
 
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text) 
			

tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manual_annotation_URI.csv", index_col=0)
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

import pandas as pd
manual_annotation=pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\Location_Coordinates.csv")
geo_loc= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\geotext_loc.csv")




from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
x = df_3['Origin']
origin_num = label_encoder.fit_transform(x)
print(origin_num)
x = df_3['Destination']
dest_num = label_encoder.fit_transform(x)
print(len(origin_num))


#test dataset
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
x = df_5['Origin']
origin_num_test = label_encoder.fit_transform(x)
print(origin_num_test)
x = df_4['Destination']
dest_num = label_encoder.fit_transform(x)
print(len(origin_num_test))
print(accuracy_score(origin_num, origin_num_test))



tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manuaL_annotation_URI.csv")
for index, row in tweet_location.iterrows():
    a=row[1]
    doc = nlp(a)
    for t in doc:
        try:
            
    #print (t.text,t.pos_, t.dep_)
            if t.pos_ in ["NOUN", "PROPN"] and t.dep_ in ["pobj"]:
                #print ("v",t)
                #print (t.head.text)
                if t.head.text in ["From"]:
                    print ("Origin: ", t)
                if t.head.text in ["To"]:
                    print ("Desination: ", t)
            if t.pos_ in ["NOUN"] and t.dep_ in ["dobj"]:
                #print ("left child", list(t.lefts), t)
                left_child = list(t.lefts)[-1]
                if left_child.dep_ in ["compound"] and left_child.pos_ in ["PROPN", "NOUN"]:
                    print ("ori", left_child.text)
        except: 
            pass

list_data=[]
tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\Data_Set\manuaL_annotation_URI.csv")
for index, row in tweet_location.iterrows():
    a=row[1]
    doc = nlp(a)
    print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
    list_data.append(doc)
    			
				
				

			
			
 