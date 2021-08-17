# Geoparsing-for-Movement-Detection-in-Social-Media-Postings


# Abstract

In the last two decades, Natural Language Processing has evolved, which further help in developing Geoparsing frameworks and Dependency parsing. 
Geoparsing is a method of extracting and grounding of mentioned location name (toponyms) from the text.  
Let understand with an example: "The Latest: 11,000 migrants entered Austria, more coming". 
Austria place name will be extracted using geoparsing. 
However, we will create a pipeline that provides information about the migrant's location and movements.  
Therefore by using the geoparsing framework and dependency parsing.

 
In our thesis, we focus on detecting mentioned location and movement information from the tweet. 
We used the refugee dataset who came to Europe during the 2015 migrants crisis for a better life. 
We have created a pipeline that will take tweets as input and provide all the refugee information about its location and movement information (i.e., origin and destination) if it is present in the input tweet text.
To create our movement detection pipeline, we firstly used DBpedia Spotlight, Mordecai and GeoText, geoparsing frameworks to extract the mentioned location in tweets. Afterwards, we used distance-based evaluation metrics to analyze which geoparsing frameworks perform more accurate on social media text. 
Secondly, we used StanfordNLP and spaCy dependency parsing to detect the tweets grammatical information, which further helps detect the refugee's origin and destination location. 
Finally, we examine and demonstrate our geoparsing pipeline and discuss the results which we achieved from experiments.
