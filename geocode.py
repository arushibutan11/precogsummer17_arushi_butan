from odo import odo
import pandas as pd
from pymongo import MongoClient
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import urllib, urllib2, json

def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]['geometry']['location']
        except:
                return None

coordinates = []
f = open('loc.txt', 'a')
clienta=MongoClient()
db=clienta.sampledb
str1=db.tweets.find()

n=0;
for s in str1:
	n+=1
	print n
	if s['coordinates']==None and s['user']['location']!=None:
		loc=s['user']['location']		
		try: 
			long=decode_address_to_coordinates(loc)
			coordinates.append(long)
		except:
			pass
			


		
		
		
