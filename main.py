# -*- coding: utf-8 -*-
from YahooAPI import YahooAPI
from ImageGeneration import VisionPic
from TwitterBot import TwitterBot

from PIL import Image
from io     import BytesIO

import tweepy
import re
import requests
import random
import tempfile


words = [\
"視えてきた...!",\
"来る...!",\
"視える...!",\
"来た...!"\
]

def shapeText(text):
	# URLとスクリーンネームの除去
	text = re.sub("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "", text)
	text = re.sub("@[\\w]{1,15}", "", text)
	return text

if __name__ == "__main__":
	consumerKey = "gYtqbIkCR0jNMgn8d4k9T5A4L"
	consumerSecret = "SgoZChCN4w5bnNUSGtT98GNjjSwzsWayrnioOikOeNoZBiBLK6"
	
	accessToken = "999299384285184000-YIlYfcLh4mFUZNUDDvWktmPcgGZNKUu"
	accessSecret = "WZcJaFoKPZ2MEDhylqn4E6CgLX5oD8e6Up7L23TZFfgyq"
	
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessSecret)
	api = tweepy.API(auth)
	
	ShulkBot = TwitterBot(api)
	
	yahoo = YahooAPI("dj00aiZpPXJmNUFMVWhTUUtNYyZzPWNvbnN1bWVyc2VjcmV0Jng9ZjQ-")
	
	ShulkBot.GetTimeline()
	ShulkBot.ExcludeTweets()
	
	while True:
		try:
			status = ShulkBot.PickTweet()
		except ValueError:
			exit()
		result = yahoo.KeyPhrase( shapeText( status.text ) )
		keyPhrase = yahoo.GetMostImportantWord( result )
		
		if keyPhrase is not None or "":
			break
	
	vision = VisionPic("/usr/share/fonts/truetype/ricty-diminished/RictyDiminished-Regular.ttf")
	
	imgResponse = requests.get( status.entities["media"][0]["media_url"] )
	image = Image.open( BytesIO( imgResponse.content ) )
	image.convert("RGBA")
	
	iconResponse = requests.get( status.user.profile_image_url )
	icon = Image.open( BytesIO( iconResponse.content ) )
	icon.convert("RGBA")
	
	vision.GenerateTagImage( icon,keyPhrase, random.randrange(1, 114514) )
	
	with tempfile.NamedTemporaryFile( prefix="Vision", suffix=".png", mode='w+') as fp:
		vision.GenerateVisionImage( image ).save( fp.name, format="png" )
		
		api.update_with_media( fp.name, status=random.choice(words) )


