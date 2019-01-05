"""Concat all files from a directory to one file.
"""
import os
import shutil

INPUT_DIR = 'train'

TARGET_FILE = 'train.txt'

if __name__ == '__main__':
    with open(TARGET_FILE, 'a') as output_file:
        for root_dir, _, files in os.walk(INPUT_DIR):
            for f in files:
                next_file = os.path.join(root_dir, f)
                print(next_file)
                with open(next_file, "r") as input_file:
                    shutil.copyfileobj(input_file, output_file)
