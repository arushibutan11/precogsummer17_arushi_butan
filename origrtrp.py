from odo import odo
import pandas as pd
from pymongo import MongoClient
import json
import matplotlib.pyplot as plt

clienta=MongoClient()
db=clienta.sampledb
str1=db.tweets.find()

def checkRT(jsonContents):
	Flag = True if "retweeted_status" in jsonContents else False
	return Flag

Retweet=0
Rep=0

for s in str1:
	if checkRT(s)==True:
		Retweet+=1
	if s['in_reply_to_user_id_str']!=None:
		Rep+=1


Orignal = db.tweets.count() - Retweet - Rep


labels = 'Remaining Tweets','Replies', 'Retweets'
sizes = [Orignal,Rep, Retweet]
colors = ['gold','lightcoral','lightskyblue']
explode = (0.1,0, 0)  # explode 1st slice


plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend(labels, loc="best")
plt.gcf().subplots_adjust(left=0.2)
plt.axis('equal')


plt.savefig("static/origrtrp.png")
		
