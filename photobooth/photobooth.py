from gpiozero import Button
from guizero import App, Text, Picture
from camera import Camera
from photobooth_controller import PhotoboothController

PREVIEW_SECONDS = 5
FONT_SIZE = 128
OUTPUT_PATH = "/home/pi/photobooth/output/"    

green_btn = Button(23)
red_btn = Button(25)
camera = Camera(resolution=(1024, 768))
controller = PhotoboothController(camera, OUTPUT_PATH)

green_btn.when_pressed = controller.pressed_capture_button
red_btn.when_pressed = controller.pressed_reject_print_button

app = App("Chris and Samiha's Wedding Photobooth!", 50, 50)

app.display()
camera.show_preview(False)
