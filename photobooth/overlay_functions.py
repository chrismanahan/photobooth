# Adapted from some original code by bennuttall and waveform80
# -------------------------------------------------------------
 
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont


def load_image(file_path):
    return Image.open(file_path)

def _pad(resolution, width=32, height=16):
    # Pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because overlays require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )

def image_from_text(text, resolution, font_size):
    img = Image.new('RGBA', resolution, (0, 0, 0, 0))
    
    font = ImageFont.truetype('/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf', font_size)
    
    d = ImageDraw.Draw(img)
    d.text(((resolution[0]-font_size)/2, (resolution[1]-font_size)/2), text, font=font, fill=(255,255,255))
    return img

def flash_image(resolution):
    img = Image.new('RGB', resolution, (255, 255, 255))
    d = ImageDraw.Draw(img)
    return img

def remove_overlays(camera):
    
    # Remove all overlays from the camera preview
    for o in camera.overlays:
        camera.remove_overlay(o) 


def preview_overlay(camera=None, overlay_img=None):

    # Remove all overlays
    remove_overlays(camera)

    add_overlay(camera, overlay_img)
    
def add_overlay(camera=None, overlay_img=None):
    # Pad it to the right resolution
    pad = Image.new('RGBA', _pad(camera.resolution), (0, 0, 0, 0))
    pad.paste(overlay_img, (0, 0))

    # Add the overlay
    camera.add_overlay(pad.tobytes(), alpha=32, layer=3)

def output_overlay(output=None, overlay=None):

    # Take an overlay Image
    overlay_img = _get_overlay_image(overlay)

    # ...and a captured photo
    output_img = Image.open(output).convert('RGBA')

    # Combine the two and save the image as output
    new_output = Image.alpha_composite(output_img, overlay_img)
    new_output.save(output)
