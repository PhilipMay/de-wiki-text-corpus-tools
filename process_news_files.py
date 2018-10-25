from somajo import Tokenizer, SentenceSplitter
import os
from multiprocessing import Pool, cpu_count

INPUT_DIR = "data/AA"

OUTPUT_DIR = "output"

def get_data_file_names(root_dir):
    result = []
    for _, _, files_ in os.walk(root_dir):
        for f in files_:
            result.append(f)
    return result

def process_text_line(line):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(line)

    sentence_splitter = SentenceSplitter()
    sentences = sentence_splitter.split(tokens)

    result = []

    for s in sentences:

        if len(s) >= 4:
            sentence_string = " ".join(s)
            result.append(sentence_string)

    return result

def process_directory(input_file, output_file):
    with open(output_file, 'a') as output_file:

        # to avoid new line at end of file
        first_line_written = False

        #print("Reading file:", input_file)

        with open(input_file, "r") as input_file:
            
            for line in input_file:

                # skip empty lines
                if len(line) <= 3:
                    continue
                
                #print("line:", line)

                sentences = process_text_line(line)

                #print("sentences", sentences)


                for sentence in sentences:

                    #print(sentence)

                    if len(sentence) > 2:

                        if first_line_written == True:
                            output_file.write("\n")
                        else:
                            first_line_written = True

                        output_file.write(sentence)

def pd(map_item):
    """Wrap call to process_directory to be called by map function"""
    input_file, output_file = map_item
    print("Creating:", output_file)
    process_directory(input_file, output_file)
    #print("Debug - :", input_file, "-", output_file)

if __name__ == '__main__':
    data_files = get_data_file_names(INPUT_DIR)
    #print(data_files)
    #data_dirs = get_data_dirs(INPUT_DIR)

    call_list = []
    for df in data_files:
        call_item = [os.path.join(INPUT_DIR, df), os.path.join(OUTPUT_DIR, df + "-tokenized.txt")]
        call_list.append(call_item)

    pool_size = cpu_count() * 2
    print("pool_size:", pool_size)

    with Pool(pool_size) as p:
        p.map(pd, call_list)

    print("Done!")
