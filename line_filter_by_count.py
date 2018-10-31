INPUT_FILE = 'text_corpus.txt'

OUTPUT_FILE = 'text_corpus_filtered.txt'

TOP_WORS_TO_KEEP = 5

vocab_dict = {}

if __name__ == '__main__':
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file:
            tokens = line.split()
            for token in tokens:
                value = vocab_dict.get(token, 0)
                vocab_dict[token] = value + 1

        token_to_keep = [(value, key) for key, value in vocab_dict.items()]
        token_to_keep.sort(reverse=True)

        #print(data)

        token_to_keep = [x for _, x in token_to_keep[:TOP_WORS_TO_KEEP]]

        #print(data)

    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            first_line_written = False
            for line in input_file:
                tokens = line.split()
                token_missing = False
                for t in tokens:
                    if t not in token_to_keep:
                        token_missing = True
                        break
                if not token_missing:
                    line = line.replace('\n','')
                    if first_line_written:
                        output_file.write("\n")
                    else:
                        first_line_written = True
                    output_file.write(line)
                        

    # TODO: <S>, </S> and <UNK> on top of file

    #data = [(100, "Hallo"), (10, "du"), (20, "ich")]
    #data.sort()
    #print(data)
