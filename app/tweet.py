import tweepy
import random
import re

from config import CONFIG
from gametitle import TWO_PARTS, THREE_PARTS, FOUR_PARTS

# 認証
CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = CONFIG["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# 何パーツのタイトルにするかを決める
title_parts_number = random.randint(2, 4)
target_array = []
if title_parts_number == 2:
    target_array = TWO_PARTS
elif title_parts_number == 3:
    target_array = THREE_PARTS
elif title_parts_number == 4:
    target_array = FOUR_PARTS

TWEET_TEXT = ''
# 取得したタイトルを組み合わせる
for i in range(title_parts_number):
    title = random.choice(target_array)
    print(range(title_parts_number))
    texts = title.split('-')
    print(texts)
    TWEET_TEXT += texts[i]

# 存在するタイトルか確認する

# ツイート
api.update_status(TWEET_TEXT)
print("「{}」というツイートをした".format(TWEET_TEXT))
