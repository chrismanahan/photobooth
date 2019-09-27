from PIL import Image, ImageDraw, ImageFont

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

	def combine_images(self, img1, img2):
		i1 = img1.convert('RGBA')
		i2 = img2.convert('RGBA')
		return Image.alpha_composite(i1, i2)
	
	def save_image(self, img, filename):
		img.save(img, filename)
		
	def create_flash_image(self):
		img = Image.new('RGB', self.resolution, (255, 255, 255))
		d = ImageDraw.Draw(img)
		return img
