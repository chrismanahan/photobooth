from image_helper import ImageHelper, ImagePosition
from camera_overlay import CameraOverlay
from PIL import Image
import time

class UIConst:
	BUTTON_DIA = 250
	FONT_SIZE = 128

class UI:
	def __init__(self, camera_overlay, resolution):
		self.camera_overlay = camera_overlay
		self.resolution = resolution
		self.image_helper = ImageHelper(resolution)
		self.main_screen_img = None
		self.confirm_screen_img = None
		
	def show_main_screen(self):
		if self.main_screen_img == None:			
			self.main_screen_img = Image.new('RGBA', self.resolution, (0, 0, 0, 0))
			self.image_helper.create_circle_image(self.main_screen_img, UIConst.BUTTON_DIA, "green", ImagePosition.LOWERCENTER)
			text = self.image_helper.create_button_text_image(self.main_screen_img, "Go!", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERCENTER)
		self.camera_overlay.add_overlay(self.main_screen_img)
		
	def show_confirm_screen(self):
		if self.confirm_screen_img == None:
			self.confirm_screen_img = Image.new('RGBA', self.resolution, (0, 0, 0, 0))
			red_button = self.image_helper.create_circle_image(self.confirm_screen_img, UIConst.BUTTON_DIA, "red", ImagePosition.LOWERLEFT)
			green_button = self.image_helper.create_circle_image(self.confirm_screen_img, UIConst.BUTTON_DIA, "green", ImagePosition.LOWERRIGHT)
			
			no_text = self.image_helper.create_button_text_image(self.confirm_screen_img, "Retake", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERLEFT)
			yes_text = self.image_helper.create_button_text_image(self.confirm_screen_img, "Print!", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERRIGHT)
		self.camera_overlay.add_overlay(self.confirm_screen_img)
		
	def clear_screen(self):
		self.camera_overlay.remove_overlays()

	def show_countdown(self):
		for i in range(3, 0, -1):
			img = Image.new('RGBA', self.resolution, (0, 0, 0, 0))
			self.image_helper.create_text_image(img, str(i), UIConst.FONT_SIZE, ImagePosition.UPPERCENTER)
			self.camera_overlay.add_overlay(img)
			time.sleep(1)
			self.camera_overlay.remove_top_overlay()
			time.sleep(0.05)
