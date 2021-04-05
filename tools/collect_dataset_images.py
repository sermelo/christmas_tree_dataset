#!/usr/bin/env python3

import binascii
import os

import csv
import ntpath

import board
import neopixel

from camera import Camera

SIZE = 50
PIN = board.D18
PIXELS_ORDER = neopixel.RGB
OFF = (0, 0, 0)
GREEN = (0, 255, 0)
OUTPUT_DIR = 'data'
IMG_DIR = f'{OUTPUT_DIR}/images'



def capture_frames(camera, pixels, path_template, pos):
    frame_captured = False
    off_file_name = f'{path_template}_{pos}_off.png'
    on_file_name = f'{path_template}_{pos}_on.png'
    while not frame_captured:
        camera.frame_to_file(off_file_name)
        exposure_time_off = camera.get_exposure_speed()
        pixels[pos] = GREEN
        camera.frame_to_file(on_file_name)
        exposure_time_on = camera.get_exposure_speed()
        pixels[pos] = OFF
        frame_captured = exposure_time_on == exposure_time_off
    return ntpath.basename(off_file_name), ntpath.basename(on_file_name)


def create_dataset_series(pixels):
    camera = Camera()
    execution_id = binascii.b2a_hex(os.urandom(3)).decode()
    path_template = f'{IMG_DIR}/light_{execution_id}'

    data = []
    for i in range(SIZE):
        off_file, on_file = capture_frames(camera, pixels, path_template, i)
        data.append([off_file, on_file])
    data_to_file(execution_id, data)


def data_to_file(execution_id, data):
    data_file = f'{OUTPUT_DIR}/data_{execution_id}.csv'
    with open(data_file, 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(data)

if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

pixels = neopixel.NeoPixel(pin=PIN, n=SIZE, pixel_order=PIXELS_ORDER)
pixels.fill(OFF)
create_dataset_series(pixels)
