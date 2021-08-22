import pandas as pd

#raw json data 
tweet_data = pd.read_json(r"C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\Tweet_data\all_data.json")
print(tweet_data)


data_1 = pd.DataFrame([]) #Storing Tweet in DataFrame
for key, value in tweet_data.items():
    if key == "text" :
        #select the tweet data from json 
        data_1 = data_1.append(pd.DataFrame({'Tweet': value}))
        
#removing http URL from raw tweet         
data_1['Tweet'] = data_1['Tweet'].replace(r'http\S+', '', regex=True)

#Displaying top 5 row of the DataFrame
print(data_1)
# saving tweet data from raw tweet in csv 
data_1.to_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\tweet_data_3275.csv")
#manual annotation
tweet_location= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\Tweet_data\raw_tweet.csv",sep=";",index_col=0)
print(tweet_location)