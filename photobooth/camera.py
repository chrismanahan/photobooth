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
               
    def show_overlay(self, path=None, img=None):
        if path is None and img is None:
            print("remove overlays")
            remove_overlays(self.picam)
        else:
            if path is not None:
                img = load_image(path)
            print("adding overlay")
            add_overlay(self.picam, img)
