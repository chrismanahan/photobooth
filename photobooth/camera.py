from picamera import PiCamera
import time
from time import strftime, gmtime
from overlay_functions import *

class Camera:
    
    def __init__(self, resolution):
        self.camera = PiCamera()
        self.camera.hflip = True
        self.camera.resolution = resolution
        self.resolution = resolution
    
    def show_preview(self, show):
        if show:
            self.camera.start_preview()
        else:
            self.camera.stop_preview()           
    
    def capture(self, output_root):
        output = self._build_output(output_root)
        print("saving photo to " + output)
        self._start_countdown()
        self._flash()
        self.camera.capture(output)
               
    def show_overlay(self, path=None, img=None):
        if path is None and img is None:
            print("remove overlays")
            remove_overlays(self.camera)
        else:
            if path is not None:
                img = load_image(path)
            print("adding overlay")
            add_overlay(self.camera, img)
               
    def _build_output(self, path):
        output_path = path + "image-%d-%mT%H:%M.png"
        return strftime(output_path, gmtime())
        
    def _start_countdown(self):
        for i in range(3, 0, -1):
            img = image_from_text(str(i), self.camera.resolution, 128)
            preview_overlay(self.camera, img)
            time.sleep(1)
            remove_overlays(self.camera)
            time.sleep(0.05)
            
    def _flash(self):
        img = flash_image(self.camera.resolution)
        preview_overlay(self.camera, img)
        time.sleep(0.2)
        remove_overlays(self.camera)
        