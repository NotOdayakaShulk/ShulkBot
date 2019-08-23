# -*- coding: utf-8 -*-
import tweepy



class ConsumerKey:
	def __init__(self, key, secret):
		self.key    = key
		self.secret = secret

class AccessToken:
	def __init__(self, token, secret):
		self.token  = token
		self.secret = secret

class APIKey:
	def __init__(self, consumerKey, accessToken ):
		self.consumer = consumerKey
		self.access   = accessToken

class myBotClass:
	def __init__ ( self, apiKey ):
		self.apiKey = apiKey
		
		self.auth = tweepy.OAuthHandler(self.apiKey., consumer_secret)
		
		auth.set_access_token(access_token, access_token_secret)
		
		api = tweepy.API(auth)

