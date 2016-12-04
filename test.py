from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#consumer key, consumer secret, access token, access secret.
ckey="UVR0x8bGcnxFPRVz0JjLBynNl"
csecret="VhCIULiNgJks2Q26dezijcRLf2sHO8Qb0kfuN05IqTqJ5WW8QA"
atoken="2648898811-8QkSuPHERin9ogvU2CgtnmwsMnvZSefroJcmEzz"
asecret="V3OYH4cmPsTX8JPXrIrShVHbSrmCAwNEIZE6irixoQRdp"
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sid = SentimentIntensityAnalyzer()
        output = open("output.txt",'a')
        print(tweet)
        print(sid.polarity_scores(tweet))
        print(all_data)
        output.write(tweet + "\n")
        output.write(str(sid.polarity_scores(tweet)) + "\n")
        output.write(str(all_data) + "\n")
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener(), language = "en", locations="41.25,-72.03,42.08,-71.01")
twitterStream.filter(track=["ripta","RIPTA"])
