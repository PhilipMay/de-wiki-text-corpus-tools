INPUT_FILE = 'text_corpus.txt'

OUTPUT_FILE = 'vocab.txt'

vocab_dict = {}

token_count = 0

if __name__ == '__main__':
    with open(INPUT_FILE, "r") as input_file: 
        with open(OUTPUT_FILE, "w") as output_file:         
            for line in input_file:
                tokens = line.split()
                #print(tokens, "-", len(tokens))
                token_count += len(tokens)
                for token in tokens:
                    value = vocab_dict.get(token, 0)
                    vocab_dict[token] = value + 1
        
            #print(vocab_dict)
            data = [(value, key) for key, value in vocab_dict.items()]
            data.sort(reverse=True)
            #print(data)
            output_file.write("<S>\n</S>\n<UNK>")
            for d in data:
                _, key = d
                output_file.write("\n")
                output_file.write(key)

    print("Number of tokens:", token_count)

    # TODO: <S>, </S> and <UNK> on top of file

    #data = [(100, "Hallo"), (10, "du"), (20, "ich")]
    #data.sort()
    #print(data)