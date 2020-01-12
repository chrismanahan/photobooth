from image_helper import ImageHelper, ImagePosition
from printer import Printer
from camera_overlay import CameraOverlay
from gpiozero import Button
from ui import UI
from time import strftime, gmtime

class PhotoboothController:
	
	def __init__(self, camera, output_path, app):
		self.output_path = output_path
		self.last_file_path = None
		self.app = app
		self.camera = camera
		self.camera_overlay = CameraOverlay(self.camera)
		self.printer = Printer()
		self.green_btn = Button(23)
		self.red_btn = Button(25)
		self.green_btn.when_pressed = self.pressed_capture_button
		self.red_btn.when_pressed = self.pressed_reject_print_button
		self.ui = UI(self.camera_overlay, camera.picam.resolution)
		self.image_helper = ImageHelper(camera.picam.resolution)
		
		self.camera.show_preview(True)
		self.ui.show_main_screen()
		
		self.waiting_for_confirm = False
		self.busy = False
		
	def _reset_state(self):
		self.waiting_for_confirm = False
		self.busy = False
	
	def pressed_capture_button(self):
		print("\ncapture")
		output_path = None
		if self.waiting_for_confirm:
			self.printer.printFile(self.last_file_path)
			## todo show print screen
			self.ui.clear_screen()
			self.ui.show_main_screen()
			self._reset_state()
		elif not self.busy:
			self.busy = True
			# show countdown
			self.ui.clear_screen()
			self.ui.show_countdown()
			# flash lights
			# self._flash()
			# take photo
			self.last_file_path = self._capture()
			# confirm with user
			self._confirm_print(self.last_file_path)
			self.waiting_for_confirm = True

	def pressed_reject_print_button(self):
		if self.waiting_for_confirm:
			print("\nreject")
			self.last_file_path = None
			self.ui.clear_screen()
			self.ui.show_main_screen()
			self._reset_state()
		
	def _confirm_print(self, path):
		preview_image = self.image_helper.load_image(path)
		self.camera_overlay.add_overlay(preview_image)
		self.ui.show_confirm_screen()
		
	def _flash(self):
		pass
		#img = self.image_helper.create_flash_image()
		#self.camera_overlay.add_overlay(img)
		#time.sleep(0.2)
		#self.camera_overlay.remove_top_overlay()
		
	def _capture(self):
		output_path = self._new_output_path()
		print("saving photo to " + output_path)
		self.camera.capture(output_path)
		return output_path
		
	def _new_output_path(self):
		output_path = self.output_path + "image-%d-%mT%H:%M.png"
		return strftime(output_path, gmtime())
