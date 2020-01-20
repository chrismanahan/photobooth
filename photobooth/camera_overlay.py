from PIL import Image, ImageDraw, ImageFont
	
PREVIEW_INDEX = 2
	
class CameraOverlay:
	
	def __init__(self, camera):
		self.camera = camera
		
	def remove_overlays(self):
		for i in reversed(range(0, len(self.camera.picam.overlays))):
			self.remove_overlay(i)
			
	def remove_overlay(self, index):
		print("remove overlay index " + str(index))
		overlay = self.camera.picam.overlays[index]
		self.camera.picam.remove_overlay(overlay)
		
	def remove_top_overlay(self):
		index = len(self.camera.picam.overlays) - 1
		if index >= 0:
			self.remove_overlay(index)
			
	def add_overlay(self, overlay_img, alpha=0):
		layer_index = PREVIEW_INDEX + len(self.camera.picam.overlays) + 1
		print("adding overlay at index " + str(layer_index))
		pad = Image.new('RGBA', self._pad())
		pad.paste(overlay_img, (0,0))
		
		self.camera.picam.add_overlay(pad.tobytes(), alpha=alpha, layer=layer_index)
		
		return layer_index
		
	def add_overlays(self, overlay_imgs, alpha=0):
		for img in overlay_imgs:
			self.add_overlay(img, alpha)
	
	def _pad(self, width=32, height=16):
		resolution = self.camera.picam.resolution
		# Pads the specified resolution
		# up to the nearest multiple of *width* and *height*; this is
		# needed because overlays require padding to the camera's
		# block size (32x16)
		return (
			((resolution[0] + (width - 1)) // width) * width,
			((resolution[1] + (height - 1)) // height) * height,
		)
