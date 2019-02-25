import json 
import os 
from pymongo import MongoClient 
import pandas as pd 
path=os.getcwd()

os.rename('tweets.txt','tweets.json')
client=MongoClient('mongodb://twitterdb:UYR0ojAlVrKM08z1uES26JLp8NaK5LRGr5LTBErqjcgFC3JhSTb6anO3EsUiavPI2fpGmsJzwaHwTrC4Qm8ZTQ==@twitterdb.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')

db=client['Tasks']


collection=db['Items']


data = []
k=2
with open('tweets.json') as f:
	for line in f: 
		if(k%2==0):
			data.append(json.loads(line))
		else : 
			pass
		k=k+1


	
    #for line in f:
    
    	#data.append(json.loads(line))


#for i in range(len(data)):
	#collection.insert(data[i])
d=data[2]

#collection.insert(d)

sapin=data[5:15]

#print(sapin[2])

for chaque_tweet in sapin : 
	collection.insert(chaque_tweet)

