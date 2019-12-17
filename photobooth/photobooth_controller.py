from image_helper import ImageHelper
from printer import Printer
from image_helper import ImageHelper
from camera_overlay import CameraOverlay
from time import strftime, gmtime
import time

class PhotoboothController:
	
	def __init__(self, camera, output_path):
		self.output_path = output_path
		self.last_file_path = None
		self.camera = camera
		self.camera.show_preview(True)
		self.image_helper = ImageHelper(camera.picam.resolution)
		self.camera_overlay = CameraOverlay(self.camera)
		self.waiting_for_confirm = False
		self.printer = Printer()
	
	def pressed_capture_button(self):
		print("\ncapture")
		output_path = None
		if self.waiting_for_confirm:
			self.pressed_accept_print_button()
			self.waiting_for_confirm = False
		else:
			self._show_countdown()
			self._flash()
			self.last_file_path = self._capture()
			self._confirm_print(self.last_file_path)
			self.waiting_for_confirm = True

	def pressed_reject_print_button(self):
		print("\nreject")
		self.last_file_path = None
		self.camera_overlay.remove_overlays()
		self.waiting_for_confirm = False
		
	def pressed_accept_print_button(self):
		self.camera_overlay.remove_top_overlay()
		self._show_printing()
		self.printer.printFile(self.last_file_path)
		self.camera_overlay.remove_overlays()
		
	def _show_countdown(self):
		for i in range(3, 0, -1):
			label = self.image_helper.create_text_image(str(i), 128)
			self.camera_overlay.add_overlay(label)
			time.sleep(1)
			self.camera_overlay.remove_top_overlay()
			time.sleep(0.05)
		
	def _show_printing(self):
		print_message = self.image_helper.create_text_image("Printing...", 128)
		self.camera_overlay.add_overlay(print_message)
		
	def _confirm_print(self, path):
		preview_image = self.image_helper.load_image(path)
		confirm_message = self.image_helper.create_text_image("Red - Do Over\nGreen - Print!", 64)
		self.camera_overlay.add_overlays([preview_image, confirm_message])
		
	def _flash(self):
		img = self.image_helper.create_flash_image()
		self.camera_overlay.add_overlay(img)
		time.sleep(0.2)
		self.camera_overlay.remove_top_overlay()
		
	def _capture(self):
		output_path = self._new_output_path()
		print("saving photo to " + output_path)
		self.camera.capture(output_path)
		return output_path
		
	def _new_output_path(self):
		output_path = self.output_path + "image-%d-%mT%H:%M.png"
		return strftime(output_path, gmtime())
