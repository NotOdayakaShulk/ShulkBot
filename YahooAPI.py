# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request

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
			return res

if __name__ == "__main__" :
	yahoo = YahooAPI("")
	yahoo.KeyPhrase("うんこ")
