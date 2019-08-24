# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

class VisionPic:
	imgHeight = 720
	imgWidth  = 1280
	
	tagHeight = 80
	tagWidth  = 932
	
	tagPos    = ( imgWidth - tagWidth, 70 )
	
	fontSize = 40
	
	txtBoxWidth  = 320
	txtBoxTopLeft = ( 180, int((tagHeight - fontSize) / 2) )
	
	dmgBoxTopLeft = ( 764, int((tagHeight - fontSize) / 2) )
	
	def __init__( self, fontPath ):
		self.img = Image.new( "RGBA", (VisionPic.imgWidth, VisionPic.imgHeight) )
		self.tag = Image.open( "tag.png" )
		self.font = ImageFont.truetype(fontPath, VisionPic.fontSize)
	
	
	# 文字列がタグの中に入りきるように切り詰める
	def TruncateText ( self, text ):
		draw = ImageDraw.Draw( self.tag )
		
		if draw.textsize( text , self.font )[0] <= VisionPic.txtBoxWidth :
			return text
		
		while draw.textsize( text + "...", self.font )[0] > VisionPic.txtBoxWidth:
			text = text[0:len(text) - 1]
		
		return text + "..."
	
	# 縁取った文字を描画する
	def BorderText ( self, text, pos, img, font, bw, frontColor, bgColor ):
		draw = ImageDraw.Draw(img)
		
		draw.font = font
		
		pos = np.array( pos )
		
		draw.text(pos-(-bw, -bw), text, bgColor)
		draw.text(pos-(-bw, +bw), text, bgColor)
		draw.text(pos-(+bw, -bw), text, bgColor)
		draw.text(pos-(+bw, +bw), text, bgColor)
		draw.text(pos-(0, -bw), text, bgColor)
		draw.text(pos-(0, +bw), text, bgColor)
		draw.text(pos-(-bw, 0), text, bgColor)
		draw.text(pos-(+bw, 0), text, bgColor)
		draw.text(pos, text, frontColor)
		
		return draw
	
	# 未来視タグの画像生成
	def GenerateTagImage( self, enemyIcon, text, damage ):
		text = self.TruncateText(text)
		
		tag = self.tag.copy()
		draw = ImageDraw.Draw( tag )
		
		mask = Image.new("L", (64, 64), 0)
		drawMask = ImageDraw.Draw(mask)
		drawMask.ellipse( (0, 0, 64, 64), fill=255)
		
		maskBulr = mask.filter(ImageFilter.GaussianBlur(2))
		
		enemyIcon = enemyIcon.convert('L').resize((64, 64))
		tag.paste(enemyIcon, (54, 8), maskBulr)
		
		draw = self.BorderText( text, VisionPic.txtBoxTopLeft, tag,
									self.font,2, "white", "black")
		draw = self.BorderText( str(damage), VisionPic.dmgBoxTopLeft,
									tag, self.font, 2, "white", "black")
		
		self.tag = tag.resize(tag.size, Image.ANTIALIAS)
	
	# 画面全体にかかるエフェクトの生成
	def makeEffect(self):
		self.effect = Image.new("RGBA", (VisionPic.imgWidth, VisionPic.imgHeight),
								(126, 158, 183, 255))
	
	def GenerateVisionImage(self, img):
		
		self.makeEffect()
		img = img.convert("RGBA")
		img = img.resize( self.effect.size )
		
		ret = Image.blend(img, self.effect, 0.25)
		ret.paste(self.tag, VisionPic.tagPos, mask = self.tag)
		
		return ret
	

if __name__ == "__main__":
	vision = VisionPic("/usr/share/fonts/truetype/ricty-diminished/RictyDiminished-Regular.ttf")
	
	image = Image.open("test.jpg")
	image.convert("RGBA")
	icon = Image.open("icon.jpg")
	icon.convert("RGBA")
	vision.GenerateTagImage( icon,"うんうんうんち", 114514 )
	vision.GenerateVisionImage( image ).show()
