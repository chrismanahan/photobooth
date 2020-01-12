from guizero import App, Text, Picture, PushButton
from camera import Camera
from photobooth_controller import PhotoboothController

PREVIEW_SECONDS = 5
FONT_SIZE = 128
OUTPUT_PATH = "/home/pi/photobooth/output/"    

app = App("Chris and Samiha's Wedding Photobooth!", 20, 20)


camera = Camera(resolution=(1024, 768))
controller = PhotoboothController(camera, OUTPUT_PATH, app)

app.display()
camera.show_preview(False)
