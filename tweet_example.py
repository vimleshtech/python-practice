import tweepy
from tweepy import OAuthHandler 
import re # regular expression
from textblob import TextBlob #text/tweet parse


ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"


auth = OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)

print(api,' login success ')

def getSentiment(tweet):
     
        analysis = TextBlob(tweet)
        #print(analysis)
        #print(analysis.sentiment.polarity)
        
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'    
        

def cleanData(tweet):
     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())     

def getTweets(p,coun):
     tweets = api.search(q=p,count=coun)
     pc = 0
     nc = 0
     netc = 0
     for t in tweets:
        tweetlist=  cleanData(t.text)
        #print(tweetlist)
        data = getSentiment(tweetlist)
        tweetdata = []
        tweetdata.append(data)

        
        for  t in tweetdata:
             if t == 'positive':
                    pc =pc+1
             elif t == 'negative':
                  nc = nc+1
             else:
                  netc = netc+1
     print('leader name :',p)
     print ('positive count ',pc)
     print ('negative count ',nc)
     print ('neutral count ',netc)
             
person = ["Narenda Modi","Soni Gandhi","Rahul Gandhi"]     
for p in person:
     getTweets(p,10)
     






     

     







            
