import os
import shutil

INPUT_DIR = 'data/AA'

TARGET_FILE = 'output.txt'

first_file_written = False

if __name__ == '__main__':
    with open(TARGET_FILE, 'a') as output_file:
        for root_dir, _, files in os.walk(INPUT_DIR):
            for f in files:
                next_file = os.path.join(root_dir, f)
                print(next_file)
                #first_file_written = False
                with open(next_file, "r") as input_file:
                    if first_file_written:
                        output_file.write("\n")
                    else:
                        first_file_written = True

                    shutil.copyfileobj(input_file, output_file)
