
from twython import Twython, TwythonError
import time

APP_KEY = 'KHfa0WMJRhyOaRq2QuHtyKVyv'
APP_SECRET = 'rbN9arAeNZ4lVmVPB1YP24BZkd90GmLfibg348WFVmaunFBeHy'
OAUTH_TOKEN = '2777899702-E2vAdFYevgW4fGGBRDWLRyQNZszDHqMJrYkdcVF'
OAUTH_TOKEN_SECRET = '3l8xjmuXWqdH5w22Vi9OBNJzs0nmsPnXvo4JlyEKqZaBE'


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


try:
    # twitter.show_user(screen_name='galsendev221')
    # print (twitter.search(q='#galsendev'))
    # results = twitter.cursor(twitter.search, q='#galse')
    # for result in results:
    #     print(result)
    twitter.update_status(status='test')


except TwythonError as e:
    print(e)