import tweepy
import time
# from time import sleep



# import tokens to access twetter api
from auth.auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
	bearer_token
)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token)


# Replace with your own search query
query = '#galsendev OR #GALSENDEV OR #GalsenDev'

# tweets = client.search_recent_tweets(query=query, max_results=100)

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    print(tweet.id)
    api.retweet(tweet.id)
    time.sleep(500)