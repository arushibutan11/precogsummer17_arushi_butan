from pymongo import MongoClient
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

client=MongoClient()
db=client.sampledb
str1=db.tweets.find()

def checkJson(jsonContents):
	Flag = True if "retweeted_status" in jsonContents and "extended_tweet" in jsonContents['retweeted_status'] and "media" in jsonContents['retweeted_status']['extended_tweet']['entities'] else False
	return Flag

tweet=0
image=0
video=0
gif=0
for s in str1:
	if s['text']!=None:
		tweet+=1
	
	if checkJson(s)==True:
		 if s['retweeted_status']['extended_tweet']['entities']['media'][0]['type']=='photo':
			image+=1	
		 if s['retweeted_status']['extended_tweet']['entities']['media'][0]['type']=='video':
			video+=1
		 if s['retweeted_status']['extended_tweet']['entities']['media'][0]['type']=='animated_gif':
			gif+=1



objects = ('Tweet', 'Image', 'Video', 'GIF')
y_pos = np.arange(len(objects))
performance = [tweet,image,video,gif]
 
plt.bar(y_pos, performance, align='center',color='red', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Tweets')
plt.title('Type of Tweet')
 
plt.savefig("static/typeoftweetbar.png")



