import tweepy
import random

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

# タイトルのパーツ数を決める
target_array = []
title_parts_number = random.randint(2, 4)
if title_parts_number == 2:
    target_array = TWO_PARTS
elif title_parts_number == 3:
    target_array = THREE_PARTS
elif title_parts_number == 4:
    target_array = FOUR_PARTS

# タイトルを組み合わせる
combi_title = ''
for i in range(title_parts_number):
    title = random.choice(target_array)
    separeted_title = title.split('-')
    combi_title += separeted_title[i]

# タイトルが実在するか確認する
title_exists = False
for i in target_array:
    if(not title_exists):
        title_exists = combi_title == i.replace('-', '')

# ツイート本文作成
TWEET_TEXT = "👦🏻「ママ！{}買って」".format(combi_title)
if(title_exists):
    TWEET_TEXT += "\n👩🏻「あら、次のクリスマスにならいいわよ〜」"
else:
    TWEET_TEXT += "\n👩🏻「そんなものないわよっ！！」"

# ツイート
api.update_status(TWEET_TEXT)
print(TWEET_TEXT)
