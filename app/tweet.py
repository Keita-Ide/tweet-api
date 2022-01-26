# import sys
# sys.path.append('/usr/local/lib/python3.7/site-packages')
# import pprint
# pprint.pprint(sys.path)

import tweepy

from config import CONFIG

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = CONFIG["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

TWEET_TEXT = "Hello World!"
api.update_status(TWEET_TEXT)
print("「{}」というツイートをした".format(TWEET_TEXT))