import json
import tweepy
from tweepy import OAuthHandler

# Authenticate
CONSUMER_KEY = "yW9QON4EzjzmswRvAN53oWAzP" #@param {type:"string"}
CONSUMER_SECRET_KEY = "fupiN9yTbHVjXAg4M8PdaIACRM4NMBJHxsOKXhG5TvIFS6Rqvq" #@param {type:"string"}
ACCESS_TOKEN_KEY = "1240304078-8j7Qhtl5zcXyrF4g6JbY7ueWCEHU0COTZ5TukHd" #@param {type:"string"}
ACCESS_TOKEN_SECRET_KEY = "BJT08jP4VpYbK62lhYHVHHAk4t82XjQD3vr8x90fPWrVP" #@param {type:"string"}

#Creates a JSON Files with the API credentials
with open('api_keys.json', 'w') as outfile:
    json.dump({
    "consumer_key":CONSUMER_KEY,
    "consumer_secret":CONSUMER_SECRET_KEY,
    "access_token":ACCESS_TOKEN_KEY,
    "access_token_secret": ACCESS_TOKEN_SECRET_KEY
     }, outfile)

#The lines below are just to test if the twitter credentials are correct
# Authenticate
#auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)

#api = tweepy.API(auth, wait_on_rate_limit=True)
