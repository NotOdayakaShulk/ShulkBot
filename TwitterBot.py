# -*- coding: utf-8 -*-
import tweepy
from datetime import datetime, timedelta, timezone
import pytz
import random

class TwitterBot:
	
	
	def __init__(self, api):
		self.api = api
	
	def GetTimeline(self):
		self.tweets = list()
		for status in tweepy.Cursor(self.api.home_timeline).items(100):
			self.tweets.append(status)
		return self.tweets
		
	def ExcludeTweets(self):
		JST = timezone(timedelta(hours=+9),"JST")
		now = datetime.now(JST)
		oldest = now- timedelta(hours = 1)
		
		# RTの除外
		self.tweets = [status for status in self.tweets if status.text[0:3] not in "RT `@"]
		
		# 1時間以上前のツイートを除外
		self.tweets = [status for status in self.tweets if \
		pytz.utc.localize(status.created_at).astimezone(JST) >= oldest ]
		
		# 鍵垢ツイートの除外
		self.tweets = [status for status in self.tweets if status.user.protected == False]
		
		# 自分のツイートの除外
		self.tweets = [status for status in self.tweets if status.user.screen_name is not self.api.me().screen_name]
		
		# メンションしてるツイートを除外
		self.tweets = [status for status in self.tweets if status.text not in "@"]
		
		# 画像のないツイートを除外
		self.tweets = [status for status in self.tweets if 'media' in status.entities]
		
		# 1枚目の画像のアスペクト比が16:9でないツイートを除外
		self.tweets = [status for status in self.tweets \
		if 9 / 16 == status.entities["media"][0]["sizes"]["large"]["h"] / status.entities["media"][0]["sizes"]["large"]["w"]]
		
		return self.tweets
		
	def PickTweet(self):
		return self.tweets.pop(random.randint(0,len(self.tweets)-1))


if __name__ == "__main__" :
	auth = tweepy.OAuthHandler(" -- Your Consumer Key -- ", " -- Your Consumer Secret -- ")
	auth.set_access_token(" -- Your Access Token -- ", " -- Your Access Token Secret-- ")
	api = tweepy.API(auth)
	
	ShulkBot = TwitterBot(api)
	
	for status in ShulkBot.GetTimeline():
		print(status.entities)
