import pandas as pd
import numpy as np
list_str=[]
labels=pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\New folder\movement_label.csv", index_col=0)

data=pd.read_csv(r"C:\Users\insan\OneDrive\thesis_development\Geoparsing_Thesis_Msc\Implementation\data\tweet_data_3275.csv", index_col=0)       
df = pd.DataFrame(data)
for index, row in labels.iterrows():
    #search_string='"'+row['Labels']+'"'
    list_str.append(row['Labels'])
   
print(list_str)
df_list1 = []  
for search_string in list_str:
    # print(search_string)
    df_list1.append(df.apply(lambda x: x.str.contains(search_string))
                    .any(axis=1)
                     .astype(int)
                     .rename(search_string))

#concatenate the list of series into a DataFrame with the original df
df = pd.concat([df] + df_list1, axis=1)
#print(df)
df1 = df.query('ENTERED == 1 or walking == 1 or walk == 1 or Walk == 1 or nach == 1 or ferry == 1 or headed ==1 or buses == 1 or onward == 1 or towards == 1 or crossed == 1 or marching == 1 or arrive == 1 or travel == 1 or station == 1 or foot == 1 or wheelchair == 1 or Walked == 1 or heading == 1 or entered == 1 or borders == 1 or march == 1 or nach == 1 or enter == 1 or Reach == 1 or arrived == 1 or go == 1')

df2=df1[['Tweet']]
df2.to_csv(r"C:\Users\insan\OneDrive\Desktop\DATA_TEST\New folder\movement800.csv")
print(df2)
