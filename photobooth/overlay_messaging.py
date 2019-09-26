from camera import Camera
from overlay_functions import *
import time

def show_text(text, camera, size):
    img = image_from_text(text, camera.resolution, size)
    camera.show_overlay(img=img)