from somajo import Tokenizer, SentenceSplitter
import os

INPUT_TEXT_DIR = "data"

OUTPUT_FILE = "output.txt"

def is_doc_start_line(line):
    return line.startswith('<doc')

def is_doc_end_line(line):
    return line.startswith('</doc')

def remove_discussion_suffix(sentence):
    last_location = -1

    for loc, token in enumerate(sentence):
        if token == "--" or token == "--[" or token == "---":
            last_location = loc

    if last_location > -1:
        sentence = sentence[:last_location]

    return sentence

def process_text_line(line):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(line)

    sentence_splitter = SentenceSplitter()
    sentences = sentence_splitter.split(tokens)

    result = []

    for s in sentences:
        s = remove_discussion_suffix(s)


        if len(s) >= 4:
            sentence_string = " ".join(s)

            # check if this line still contains a dirty comment:
            if "( CEST )" not in sentence_string and "( CET )" not in sentence_string:
                result.append(sentence_string)

    return result

with open(OUTPUT_FILE, 'a') as output_file:

    # to avoid new line at end of file
    first_line_written = False

    # r_=root, d_=directories, f_=files
    for r_, d_, f_ in os.walk(INPUT_TEXT_DIR):
        for file_ in f_:
            next_input_file = os.path.join(r_, file_)
            print("Reading file:", next_input_file)

            with open(next_input_file, "r") as input_file:

                skip_next_line = False
                
                for line in input_file:

                    # drop line with start tag
                    if is_doc_start_line(line):
                        skip_next_line = True
                        continue

                    # drop line with end tag
                    if is_doc_end_line(line):
                        continue

                    # skip first line to skip headline
                    if skip_next_line == True:
                        skip_next_line = False
                        continue

                    # skip empty lines
                    if len(line) <= 1:
                        continue
                    
                    sentences = process_text_line(line)
                    
                    # ignore blank lines and make sure that stuff like "\n" is also ignored:
                    if len(sentences) > 2:
                        for sentence in sentences:
                            if first_line_written == True:
                                output_file.write("\n")
                            else:
                                first_line_written = True

                            output_file.write(sentence)
