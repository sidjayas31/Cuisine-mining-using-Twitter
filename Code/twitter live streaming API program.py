import tweepy
#import pprint
#import mechanize
#import os
#from BeautifulSoup import BeautifulSoup
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener,Stream,json
#from tweepy import Stream
import urllib
#import requests


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(StreamListener):
    imgcount=0
    functioncount=0

    def on_data(self, data):
        #self.imgcount=0
        self.functioncount=self.functioncount+1;
        #print data
        tweet = json.loads(data)
        tags=["#biryani", "#burger", "#taco", "#pizza", "#pasta", "#dosa", "#sushi"]
        khaana =''

        if u'entities' in tweet:
            tweettext=tweet[u'text']
            tweettext=tweettext.lower()
            #print "text"
            #print tweettext.encode("utf-8")
            for tag in tags:
                if tag in tweettext:
                    khaana=tag[1:]
                    print "!!!!for tag loop"
                    print "in tags ***********"
                    print khaana
                    break

            #khaana = tweet[u'entities'][u'hashtags'][0][u'text']
            #print khaana.encode("utf-8")
            if u'media' in tweet[u'entities']:
                if  u'media_url' in tweet[u'entities'][u'media'][0]:
                    print tweet[u'text'].encode("utf-8")
                    url = tweet[u'entities'][u'media'][0][u'media_url']
                    #print url.encode("utf-8")

                    #khaana = "khaana"
                    #if "#pizza" in tweet[u'text']:
                        #   print "HEYYYYYY....ITSS A pIZZA"
                        #  khaana = "pizza"
                    self.imgcount=self.imgcount+1
                    print khaana
                    print self.imgcount
                    #print self.functioncount
                    name=khaana+str(self.imgcount)+".jpg"
                    print name
                    print "*********************************"
                    urllib.urlretrieve(url, name)
        return True


    def on_error(self, status):
        print status


if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener1 = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener1)

    #This line filter Twitter Streams to capture data by the keywords: "#happy", "#sad", "#disgusted", "#fearful", "#angry", "#surprised", "#scared"
    print "before filter"
    stream.filter(track=["#biryani", "#burger", "#taco", "#pizza", "#pasta", "#dosa", "#sushi"])

# api.update_status(status=single_tweet)
print "updated"

