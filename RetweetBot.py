
from twython import Twython, TwythonError, TwythonStreamer
# import time
import json

# les tokens pour accéder à l'app twitter
APP_KEY = 'JIocjbl7odL5ICVf8lKpNvxl4'
APP_SECRET = 'OXTvQA9Am80cORrILvlw1zQpODkO9f9LqPyiClDwN2iBUKFGOr'
OAUTH_TOKEN = '1285781653160366080-mkQEgn51IYrrpu0uUBZ6bpf3jLud5u'
OAUTH_TOKEN_SECRET = 'Y6PWVxbar4Q69EonkhDq9XpeVVlvzuy9Sd4tXnzImzx98'


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# lastId.txt est le fichier qui contient le dernier Id de tweet où le un mot a été recherché
file_object  = open("lastId.txt", 'r') 
#print (file_object.read())  
# last "#galsendev" twett retweeted
LTweetId = file_object.read()
file_object.close()
# LTweetId = float(LTweetId)

print(LTweetId)

search_results = twitter.search(q="galsendev", since_id=LTweetId)

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
        
        # twitter.retweet(id = tweet["id_str"])
        # a= tweet["id_str"]

        
        print(tweet["id_str"])
        a= tweet["id_str"]

except TwythonError as e:
    print(e)


file_object  = open("lastId.txt", 'w') 
file_object.write(a)
file_object.close()