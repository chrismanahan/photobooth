from picamera import PiCamera
import time
from photobooth_controller import PhotoboothController

class Camera:
    
    def __init__(self, resolution):
        self.picam = PiCamera()
        self.picam.hflip = True
        self.picam.resolution = resolution
    
    def show_preview(self, show):
        if show:
            self.picam.start_preview()
        else:
            self.picam.stop_preview()           
    
    def capture(self, output_path):
        self.picam.capture(output_path, format="jpeg")
