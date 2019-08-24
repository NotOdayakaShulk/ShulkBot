# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import json
import sys

class YahooAPI:
	baseURL      = "https://jlp.yahooapis.jp/"
	keyphraseURL = "KeyphraseService/V1/extract"
	
	def __init__( self, appId ):
		self.appId = appId
	
	def KeyPhrase ( self, text, outFmt="json" ):
		param = {
			"appid"   : self.appId,
			"sentence": text,
			"output"  : outFmt
		}
		
		data = urllib.parse.urlencode( param )
		data = data.encode()
		
		url = urllib.parse.urljoin(YahooAPI.baseURL, YahooAPI.keyphraseURL)
		
		req = urllib.request.Request( url, data )
		with urllib.request.urlopen(req) as res:
			data = res.read()
			return json.loads(data.decode("utf-8"))
	
	def GetMostImportantWord(self, dic):
		
		try:
			for word, score in dic.items():
				if score == 100:
					return word
		except AttributeError:
			return ""

if __name__ == "__main__" :
	yahoo = YahooAPI(sys.argv[1])
	result = yahoo.KeyPhrase("")
	print(yahoo.GetMostImportantWord(result))
