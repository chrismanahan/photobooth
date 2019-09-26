from gpiozero import Button
from guizero import App, Text, Picture
from camera import Camera
from overlay_messaging import * 

preview = False

take_photo_btn = Button(23)
other_btn = Button(25)

camera = Camera(resolution=(1024, 768))

PREVIEW_SECONDS = 5
FONT_SIZE = 128
OUTPUT_PATH = "/home/pi/photobooth/output/"    

def pressed_take_photo():
    output = camera.capture(OUTPUT_PATH)
    _preview_image(output)
    show_text("Print?\nGreen - Yes\nRed - No", camera, FONT_SIZE)
    time.sleep(10)
    camera.show_overlay(None)
    
def _preview_image(path):
    camera.show_overlay(path=path)

def pressed_other_btn():
    global preview
    preview = not preview
    camera.show_preview(preview)

take_photo_btn.when_pressed = pressed_take_photo
other_btn.when_pressed = pressed_other_btn
pressed_other_btn()

app = App("Chris and Samiha's Wedding Photobooth!", 50, 50)

app.display()