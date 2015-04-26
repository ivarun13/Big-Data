# http://pythonprogramming.net/use-twitter-api-v1-1-python-stream-tweets/

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

try:
    os.remove('twitter.txt')
except OSError:
    pass

ckey = "4lAbO1GoI2U0IqAy1SDHncbZd"
csecret = "9VKBmQCjzvfa9J44UeMrczuGehoiwSLSx6f5tXB4cJOfEZPoVI"
atoken= "2902111402-6njYp4DsIQZA8JkqKKIJbJ977Xb1qj9AXOrLPhz"
asecret= "vuGahDFX7T7PV2RJrLOcqWIjhVVaWqi5Un5oJeyV96EhI"

class listener (StreamListener):

    def on_data(self,data):
        try:

            time=data.split('"created_at":"')[1].split('","id')[0]
            tweet=data.split(',"text":"')[1].split('","source')[0]
            name=data.split(',"name":"')[1].split('","screen_name')[0]
            location=data.split(',"location":"')[1].split('","url')[0]
            time_zone=data.split(',"time_zone":"')[1].split('","geo_enabled')[0]
            lang=data.split(',"lang":"')[1].split('","contributors_enabled')[0]
            Data='Created at:: '+time+'\n'+'Tweet:: '+tweet+'\n'+'Name:: '+name+'\n'+'Location:: '+location+'\n'+'Time_Zone:: '+time_zone+'\n'+'Language:: '+lang+'\n'
            print (Data)
            output=open('twitter.txt','a')
            output.write(Data)
            output.write('\n')
            output.close()
            return True
        except BaseException, e:
            print 'error', str(e)

    def on_error(self,status):
        print status

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["google"])
