import binascii
import os

import board
import neopixel

from camera import Camera

SIZE = 50
PIN = board.D18
PIXELS_ORDER = neopixel.RGB
OFF = (0, 0, 0)
GREEN = (0, 255, 0)
IMG_DIR = 'images'

camera = Camera()
pixels = neopixel.NeoPixel(pin=PIN, n=SIZE, pixel_order=PIXELS_ORDER)
pixels.fill(OFF)

if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

execution_id = binascii.b2a_hex(os.urandom(3)).decode()
path_template = f'{IMG_DIR}/light_{execution_id}'

for i in range(SIZE):
    camera.frame_to_file(f'{path_template}_{i}_off.png')
    pixels[i] = GREEN
    on_frame = camera.get_frame()
    camera.frame_to_file(f'{path_template}_{i}_on.png')
    pixels[i] = OFF
