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
title_parts_number = random.randint(2, 4)
target_array = []
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
TWEET_TEXT = ''
if(title_exists):
    TWEET_TEXT = "👦🏻「ママ！{}買って」\n👩🏻「あら、次のクリスマスにならいいわよ〜」".format(combi_title)
else:
    TWEET_TEXT = "👦🏻「ママ！{}買って」\n👩🏻「そんなものないわよっ！！」".format(combi_title)

# ツイート
api.update_status(TWEET_TEXT)
