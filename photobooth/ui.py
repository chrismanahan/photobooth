from image_helper import ImageHelper, ImagePosition
from camera_overlay import CameraOverlay
import time

class UIConst:
	BUTTON_DIA = 250
	FONT_SIZE = 30

class UI:
	def __init__(self, camera_overlay, resolution):
		self.camera_overlay = camera_overlay
		self.image_helper = ImageHelper(resolution)
		
	def show_main_screen(self):
		self.clear_screen()
		img = self.image_helper.create_circle_image(UIConst.BUTTON_DIA, "green", ImagePosition.LOWERCENTER)
		text = self.image_helper.create_button_text_image("Go!", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERCENTER)
		self.camera_overlay.add_overlays([img, text])
		## todo: add text
		
	def show_confirm_screen(self):
		self.clear_screen()
		red_button = self.image_helper.create_circle_image(UIConst.BUTTON_DIA, "red", ImagePosition.LOWERLEFT)
		green_button = self.image_helper.create_circle_image(UIConst.BUTTON_DIA, "green", ImagePosition.LOWERRIGHT)
		
		no_text = self.image_helper.create_button_text_image("Retake", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERLEFT)
		yes_text = self.image_helper.create_button_text_image("Print!", UIConst.FONT_SIZE, UIConst.BUTTON_DIA, UIConst.BUTTON_DIA, ImagePosition.LOWERRIGHT)
		self.camera_overlay.add_overlays([red_button, green_button, no_text, yes_text])
		## todo: add text
		
	def clear_screen(self):
		self.camera_overlay.remove_overlays()

	def show_countdown(self):
		self.clear_screen()
		for i in range(3, 0, -1):
			label = self.image_helper.create_text_image(str(i), 128)
			self.camera_overlay.add_overlay(label)
			time.sleep(1)
			self.camera_overlay.remove_top_overlay()
			time.sleep(0.05)
