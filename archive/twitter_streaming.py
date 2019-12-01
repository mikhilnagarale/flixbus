#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3889522514-2vMTI2pqboPzTIqcvZ7HNe66V0d0wpT5lHwIGHH"
access_token_secret = "ZdcTeTqMKNr7AWzmbArEeQcvtxYFQ5VTcIzIca7p3JtML"
consumer_key = "vYdqq8ZAbiPawJnjk63WB8Lqi"
consumer_secret = "YypynQ7riulCJ7Zbf9PQOHLz5rSQiSJZWViHr3z1yeyMbE1log"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#FlixBus'])
