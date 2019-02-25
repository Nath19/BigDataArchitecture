import tweepy

consumer_key='sYSWXHvt8o0d6O0DKFD1cjC1k'
consumer_secret='U4pWPbsGNPTTJoZdj8ZIBUbPzrvMVZwEOpB20glz71jrmN5PJw'
access_token='1010168482267267072-xClz1E70fqSSeMhhx5lKXQLonQsz2e'
access_token_secret='Hk5yMiXIldFJFgh2bUHyKuASobQkb9FDZNRXSHLG88o0w'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


for tweet in public_tweets:
    print( tweet.text)






# Get the User object for twitter...
user = api.get_user('twitter')

print (user.screen_name)