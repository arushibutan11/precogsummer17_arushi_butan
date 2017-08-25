import pymongo, json
from collections import Counter
from pymongo import MongoClient
import matplotlib.pyplot as plt

client=MongoClient()
db=client.sampledb
str1=db.tweets.find()

def checkJson(jsonContents):
	Flag = True if "retweeted_status" in jsonContents else False
	return Flag

data1 =[]
for s in str1:
	if checkJson(s)==True: 
		data1.append(s['retweeted_status']['favorite_count'])



datacount = Counter(data1)
y= datacount.values()
x= datacount.keys()

plt.axis([0, 10000, 0, 1000])
plt.hist(data1, range=[0,7000], bins=100)
plt.title("Favorite Count of Retweeted Tweets")
plt.ylabel("Number of Tweets")
plt.xlabel("Favorite")
plt.savefig("static/favcountRT.png")





