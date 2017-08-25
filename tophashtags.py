import pymongo, operator, json, re
from odo import odo
from collections import Counter
from pymongo import MongoClient
from nltk.tokenize import word_tokenize

client=MongoClient()
db=client.sampledb
str1=db.tweets.find()
emoticons_str = r"""
    (?:
        [:=;] 
        [oO\-]? 
        [D\)\]\(\]/\\OpP]
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', 
    r'(?:@[\w_]+)', 
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", 
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', 
    r"(?:[a-z][a-z'\-_]+[a-z])", 
    r'(?:[\w_]+)',
    r'(?:\S)' 
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

count= Counter()
stopwords = ['#trump', '#TRUMP', '#Trump' , '#Donaldtrump', '#Hillary', '#hillary','#clinton', '#Clinton', '#uselections', '#USelections', '#USELECTIONS', '#HillaryClinton', "#Hillary's"] #hashtags used for streaming
for s in str1:
	hashtag = [term for term in preprocess(s['text']) if term.startswith('#') and term not in stopwords]
	count.update(hashtag)

hashtaglist = []
listofht = []
listofht.append(( count.most_common(10))) #list of hashtags and count

for l in listofht[0]:
	hashtaglist.append(l[0]) 

print hashtaglist
#list of hashtags
	



	
	
	
