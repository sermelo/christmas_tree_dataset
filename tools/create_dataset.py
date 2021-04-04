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

def create_dataset_series(pixels):
    camera = Camera()
    execution_id = binascii.b2a_hex(os.urandom(3)).decode()
    path_template = f'{IMG_DIR}/light_{execution_id}'

    for i in range(SIZE):
        frame_captured = False
        while not frame_captured:
            camera.frame_to_file(f'{path_template}_{i}_off.png')
            exposure_time_off = camera.get_exposure_speed()
            pixels[i] = GREEN
            on_frame = camera.get_frame()
            camera.frame_to_file(f'{path_template}_{i}_on.png')
            exposure_time_on = camera.get_exposure_speed()
            pixels[i] = OFF
            frame_captured = exposure_time_on == exposure_time_off

if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

pixels = neopixel.NeoPixel(pin=PIN, n=SIZE, pixel_order=PIXELS_ORDER)
pixels.fill(OFF)
create_dataset_series(pixels)
