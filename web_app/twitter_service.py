from dotenv import load_dotenv
from os import getenv
from tweepy import API, OAuthHandler

load_dotenv()

TWITTER_API_KEY = getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = getenv('TWITTER_ACCESS_TOKEN_SECRET')

def twitter_api():
    auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = API(auth)
    return api

if __name__ == "__main__":
    api = twitter_api()