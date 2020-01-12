from PIL import Image, ImageDraw, ImageFont
from enum import Enum

## breaks up the ui into a grid of six boxes that overlap
## either us the two center positions, or the four on the left and right.
## using center and left for example will result in overlap.
class ImagePosition(Enum):
	UPPERLEFT = 1
	UPPERCENTER = 2
	UPPERRIGHT = 3
	LOWERLEFT = 4
	LOWERCENTER = 5
	LOWERRIGHT = 6


class ImageHelper:
	
	def __init__(self, resolution):
		self.resolution = resolution
		
	def load_image(self, path):
		return Image.open(path)
		
	
	def create_text_image(self, text, font_size):
		img = Image.new('RGBA', self.resolution, (0, 0, 0, 0))
		
		font = ImageFont.truetype('/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf', font_size)
		
		drawing = ImageDraw.Draw(img)
		parentWidth, parentHeight = self.resolution[0], self.resolution[1]
		w, h = drawing.textsize(text, font=font)
		
		x = (self.resolution[0] - font_size) / 2
		y = (self.resolution[1] - font_size) / 2 
		drawing.text(((parentWidth-w)/2, (parentHeight-h)/2), text, font=font, fill=(255,255,255))
		return img
	
	## pw = parent width
	## ph = parent height
	def create_button_text_image(self, text, font_size, pw, ph, position, padding = 10):
		img = Image.new('RGBA', self.resolution, (0, 0, 0, 0))
		
		font = ImageFont.truetype('/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf', font_size)
		
		drawing = ImageDraw.Draw(img)
		coords = self.textPositionForBoundingBox(position, pw, ph, padding)
		drawing.text(coords, text, font=font, fill=(255,255,255, 128))
		return img

	def create_circle_image(self, dia, color, position, outline_color = "black", padding = 10):
		image = Image.new('RGBA', self.resolution)
		drawing = ImageDraw.Draw(image)
		bounding_box = self.createBoundingBox(position, dia, dia, padding)
		
		drawing.ellipse(bounding_box, fill = color, outline = outline_color)
		return image

	def combine_images(self, img1, img2):
		i1 = img1.convert('RGBA')
		i2 = img2.convert('RGBA')
		return Image.alpha_composite(i1, i2)
	
	def save_image(self, img, filename):
		img.save(img, filename)

	# note padding for our use case will only be applied 
	# along y = resolution.h / 2
	def createBoundingBox(self, position, w, h, padding):
		x = 0
		y = 0
		(xC, yC) = (self.resolution[0] / 2, self.resolution[1] / 2)
		if position == ImagePosition.UPPERLEFT:
			x = (xC / 2) - (w / 2)
			y = yC - h - padding
		if position == ImagePosition.UPPERCENTER: 
			x = xC - (w / 2)
			y = yC - h - padding
		if position == ImagePosition.UPPERRIGHT:
			x = ((xC / 2) + xC) - (w / 2)
			y = yC - h - padding
		if position == ImagePosition.LOWERLEFT:
			x = (xC / 2) - (w / 2)
			y = yC + padding
		if position == ImagePosition.LOWERCENTER:
			x = xC - (w / 2)
			y = yC + padding
		if position == ImagePosition.LOWERRIGHT:
			x = ((xC / 2) + xC) - (w / 2)
			y = yC + padding
			
		if x < 0:
			x = 0
		if y < 0:
			y = 0
			
		return [(x, y), (x+w, y+h)]
		
	def textPositionForBoundingBox(self, position, w, h, padding):
		box = self.createBoundingBox(position, w, h, padding)
		x = box[0][0]
		y = box[1][1]
		return (x, y)
		
		
