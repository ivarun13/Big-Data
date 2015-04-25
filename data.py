from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey = "4lAbO1GoI2U0IqAy1SDHncbZd"
csecret = "9VKBmQCjzvfa9J44UeMrczuGehoiwSLSx6f5tXB4cJOfEZPoVI"
atoken= "2902111402-6njYp4DsIQZA8JkqKKIJbJ977Xb1qj9AXOrLPhz"
asecret= "vuGahDFX7T7PV2RJrLOcqWIjhVVaWqi5Un5oJeyV96EhI"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        output = open('output.json','a')
        output.write(data)
        output.write('\n')
        output.close()
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["iHrithik"])

