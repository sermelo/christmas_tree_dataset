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

camera = Camera()
pixels = neopixel.NeoPixel(pin=PIN, n=SIZE, pixel_order=PIXELS_ORDER)
pixels.fill(OFF)

for i in range(SIZE):
    img_id = binascii.b2a_hex(os.urandom(3)).decode()
    camera.frame_to_file(f'light_{img_id}_off.png')
    pixels[i] = GREEN
    on_frame = camera.get_frame()
    camera.frame_to_file(f'light_on_{img_id}_on.png')
    pixels[i] = OFF
