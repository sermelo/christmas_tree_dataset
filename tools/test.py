#!/usr/bin/env python3

import argparse
import csv
import math
from os import path

def method(img1, img2):
    return (4, 5)


def test_image(off_image, on_image, x, y):
    pred_x, pred_y = method(off_image, on_image)
    print('-------------------')
    print(f'Image: {on_image}')
    print(f'Real:      {x}, {y}')
    print(f'Predicted: {pred_x}, {pred_y}')
    distance = math.sqrt((x - pred_x)**2 + (pred_y - y)**2)
    print(f'Distance: {distance}')


def test(in_csv):
    in_imgs_dir = path.join(
        path.dirname(path.abspath(in_csv)),
        'images')
    with open(in_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            test_image(row[0], row[1], int(row[2]), int(row[3]))

def get_params():
    parser = argparse.ArgumentParser(description='Manually process images.')
    parser.add_argument('-i', '--input', required=True, help='CSV input file')
    return parser.parse_args()

args = get_params()
test(args.input)
