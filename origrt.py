import pymongo, json
from pymongo import MongoClient
import matplotlib.pyplot as plt

client=MongoClient()
db=client.sampledb
str1=db.tweets.find()

def checkJson(jsonContents):
	Flag = True if "retweeted_status" in jsonContents else False
	return Flag

Retweet=0
for s in str1:
	if checkJson(s)==True:
		Retweet+=1

Orignal = db.tweets.count() - Retweet


labels = 'Orginal Tweets', 'Retweets'
sizes = [Orignal,Retweet]
colors = ['gold','lightskyblue']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend(labels, loc="best")

 
plt.axis('equal')
plt.savefig("static/origrt.png")
		
