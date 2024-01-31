import dotenv
import os
import tweepy

# LOAD ALL DOTENV CONFIGS
dotenv.load_dotenv(dotenv.find_dotenv())

# VARIABLES THAT WILL RECEIVE THE VALUES
_API_KEY = os.getenv('_API_KEY')
_API_KEY_SECRET = os.getenv('_API_KEY_SECRET')
_BEARER_TOKEN = os.getenv('_BEARER_TOKEN')
_ACESS_TOKEN = os.getenv('_ACESS_TOKEN')
_ACESS_TOKEN_SECRET = os.getenv('_ACESS_TOKEN_SECRET')

# SET CLIENT TWEEPY
client = tweepy.Client(_BEARER_TOKEN, _API_KEY, _API_KEY_SECRET, _ACESS_TOKEN, _ACESS_TOKEN_SECRET)

# OAUTH AND API
auth = tweepy.OAuth1UserHandler(_API_KEY, _API_KEY_SECRET, _ACESS_TOKEN, _ACESS_TOKEN_SECRET)
api = tweepy.API(auth)

#CHECK IF THE CREDENTIALS ARE CORRECT
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

client.create_tweet(text="Hello World i'm bot with python")

client.delete_tweet("ID Tweet Here")

