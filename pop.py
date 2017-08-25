import pymongo, json
from collections import Counter
from pymongo import MongoClient
import matplotlib.pyplot as plt

client=MongoClient()
db=client.sampledb
str1=db.tweets.find()


user = list()
hillary = ["Hillary", "hillary", "Clinton", "#Imwithher"]
trump = ["trump", "Trump", "#MAGA", "Donald" ]
countt=0
counth=0
data1 =[]
for s in str1:
	      #to not get repeated tweets from same user/spam/bots
	if( s['user']['screen_name'] not in user ):
		words= s['text'].split()
		if "#Hillary"  in words:
			counth+=1
		if "#Trump" in words:
			countt+=1

	user.append(s['user']['screen_name'])
	
		

labels = 'Donald Trump', 'Hillary Clinton'
sizes = [countt, counth]
colors = ['blue','red']
explode = (0, 0.1)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=40)
plt.legend(labels, loc="best")

 
plt.axis('equal')
plt.savefig("static/pop.png")
