# -*-coding:Latin-1 -*
import tweepy
import time
import csv

import datetime


# import tokens to access twetter api
from auth.auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def get_followers(user_name):
    """
    get a list of all followers of a twitter account
    :param user_name: twitter username without '@' symbol
    :return: list of usernames without '@' symbol
    """
    api = tweepy.API(auth)
    followers = []
    for page in tweepy.Cursor(api.followers, screen_name=user_name, wait_on_rate_limit=True,count=200).pages():
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    return followers

    
def save_followers_to_csv(user_name, data):
    """
    saves json data to csv
    :param data: data recieved from twitter
    :return: None
    """
    HEADERS = ["name", "screen_name", "followers_count", "friends_count"]
    with open(user_name + "_followers.csv", 'w',encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        # csv_writer.writerow(HEADERS)
        for profile_data in data:
            profile = []
            for header in HEADERS:
                profile.append(profile_data._json[header])
            csv_writer.writerow(profile)


current_time = datetime.datetime.now()
# print (current_time.hour," , ", current_time.minute) 
# if(current_time.hour == 10 and current_time.minute == 30):

api = tweepy.API(auth)
user = api.get_user('manusquall')

#liste des unfollowers
unfollowersDict = {}





# print(user.screen_name)
# print("le nombre de personne qui vous suivent : ", user.followers_count)
# print("le nombre de personne que vous suivez : ", user.friends_count)
# for friend in user.friends():
#    print(friend.screen_name)
   
# print("-----------------------------------------------------")

# for friend in user.followers():
#    print(friend.screen_name)



user_name="manusquall"
followers = get_followers("manusquall")


try:
    f = open(user_name + "_followers.csv", 'r',encoding="utf-8")
    csv_f = csv.reader(f)






    for row in csv_f:

        if(row!=[]):
        # print(follower.screen_name)
            present = 0
            
            for follower in followers:
                if(present!=1):
                    # print (row[1])
                    if(row[1]== follower.screen_name):
                        # print (follower.screen_name)
                        present=1
                        break

                        
            if(follower.screen_name=="squallbot1"):
                print(present)
            if(present==0):
                print(row[1], " n'est plus présent")
                userFollower = api.get_user(follower.screen_name)
                unfollowersDict[row[0]] = ("@"+row[1])



    # HEADERS = ["name", "screen_name", "followers_count", "friends_count"]
    # for profile_data in followers:
    #     profile = []
    #     for header in HEADERS:
    #         profile.append(profile_data._json[header])
    #     print(profile)





    # save_followers_to_csv("manusquall", followers)


    # print(unfollowersDict)



    #direct messages:
    recipient_id= user.id_str

    if(bool(unfollowersDict)):
        text = "La liste des unfollowers depuis le dernier check: \n\n"


        for key in unfollowersDict:
            text += key + " : " + unfollowersDict[key]
            text += "\n"
    else:
        text = "La liste des unfollowers depuis le dernier check est vide"

    print(text)


    direct_message = api.send_direct_message(recipient_id, text)
    print(direct_message.message_create['message_data']['text'])


#if the csv file doesn't exist
except FileNotFoundError:
    print('Fichier csv non présent. Création d\'une nouvelle sauvegarde des followers')
    save_followers_to_csv("manusquall", followers)