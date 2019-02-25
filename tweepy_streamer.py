# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import subprocess
import asyncio
import time 
import sys
import os
from interruptingcow import timeout
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        print("A\n")
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        print("B\n")
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        print("C\n")
        stream = Stream(auth, listener)
        print("D\n")

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)
        print("E\n")


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["PSG"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    
    #twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    #time.sleep(10)
    #sys.exit(0)

    try:
        with timeout(20, exception=RuntimeError):
            twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
            pass
    except RuntimeError:
            print("didn't finish within 20 seconds")


    os.system('python import_json.py')

    