
from twython import Twython, TwythonError, TwythonStreamer

# import tokens to access twetter api
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# import time
import json

# set tokens 
APP_KEY = consumer_key
APP_SECRET = consumer_secret
OAUTH_TOKEN = access_token
OAUTH_TOKEN_SECRET = access_token_secret


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

while(1==1):
    # lastId.txt est le fichier qui contient le dernier Id de tweet où le un mot a été recherché
    file_object  = open("lastId.txt", 'r') 
    #print (file_object.read())  
    # last "#galsendev" twett retweeted
    LTweetId = file_object.read()
    file_object.close()
    # LTweetId = float(LTweetId)

    print(LTweetId)

    search_results = twitter.search(q="@manusquall", since_id=LTweetId)

    # print the result of the output
    # search_results["statuses"]
    # s1 = json.dumps(search_results["statuses"])
    # d2 = json.loads(s1)
    # print( d2)
    a=""
    try:
        # print(search_results)
        # for tweet in search_results["statuses"]:
        for tweet in search_results["statuses"]:
            
            
            twitter.retweet(id = tweet["id_str"])
            # a= tweet["id_str"]

            
            # print(tweet["id_str"])
            a= tweet["id_str"]

    except TwythonError as e:
        print(e)


    file_object  = open("lastId.txt", 'w') 
    file_object.write(a)
    file_object.close()