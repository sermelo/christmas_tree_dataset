#!/usr/bin/env python3

import argparse
import csv
from os import makedirs, path
from request_window import RequestWindow
from shutil import copyfile

class DataProcessor():
    def __init__(self, input_csv, output_csv):
        self.in_csv = input_csv
        self.in_imgs_dir = path.join(
            path.dirname(path.abspath(self.in_csv)),
            'images')
        self.out_csv = output_csv
        self.out_imgs_dir = path.join(
            path.dirname(path.abspath(self.out_csv)),
            'images')

    def process(self):
        self.check_output()
        data = self.get_processed_csv()
        self.store_data(data)

    def check_output(self):
        # Test output file is accesible
        open(self.out_csv, 'a').close()
        # Create output images dir if needed
        if not path.exists(self.out_imgs_dir):
            makedirs(self.out_imgs_dir)

    def get_processed_csv(self):
        generated_data = []
        window = RequestWindow()
        with open(self.in_csv, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                position = window.request_position(f'{self.in_imgs_dir}/{row[1]}')
                if position is not None:
                    generated_data.append([row[0], row[1], position[0], position[1]])
        return generated_data

    def store_data(self, data):
        with open(self.out_csv, 'a', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerows(data)

        for item in data:
            copyfile(f'{self.in_imgs_dir}/{item[0]}', f'{self.out_imgs_dir}/{item[0]}')
            copyfile(f'{self.in_imgs_dir}/{item[1]}', f'{self.out_imgs_dir}/{item[1]}')


def get_params():
    parser = argparse.ArgumentParser(description='Manually process images.')
    parser.add_argument('-i', '--input', required=True, help='CSV input file')
    parser.add_argument('-o', '--output', required=True, help='Output directory')
    return parser.parse_args()

args = get_params()
processor = DataProcessor(args.input, args.output)
processor.process()
