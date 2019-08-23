# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter


class VisionImg:
	imgHeight = 720
	imgWidth  = 1280
	
	tagHeight = 80
	tagWidth  = 932
	
	tagPos_x  = 70
	tagPos_y  = VisionImg.imgWidth - VisionImg.tagWidth
	
	def __init__( self, fontPath ):
		self.fontPath = fontPath
	
	# 文字列がタグの中に入りきるように切り詰める
	def TruncateText ( self, text ):
		
	
	
	def BorderText ( self, text ):
		
		
		


if __name__ == "__main__":
	
	
