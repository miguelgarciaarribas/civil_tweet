import json
import tweepy
import sys

def load_auth_tokens(config_file_name):
    with open(config_file_name) as config_file:
        json_configuration = json.loads(config_file.read())
    return json_configuration


auth = load_auth_tokens("config.json")
consumer_key = auth["consumer_key"]
consumer_secret = auth["consumer_secret"]
access_token = auth["access_token"]
access_token_secret = auth["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
page = 0
while page < 20:
 civil_tweets = api.user_timeline("Guerra_Civil_", count=200, page=page, tweet_mode="extended")
 i = 0
 for tweet in civil_tweets:
     i +=1
     tweets.append(tweet)          
 print i
 print page
 page += 1


f = open("all_tweets.json", "w")
f.write(json.dumps(map(lambda tweet : tweet._json, tweets)))
f.close()
