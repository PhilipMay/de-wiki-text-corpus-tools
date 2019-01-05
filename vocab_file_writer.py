"""Create vocabolary file from text corpus.
"""
INPUT_FILE = 'train.txt'

OUTPUT_FILE = 'vocab-train.txt'

# Vocab max token size (number of words)
TOKEN_TO_PICK = 800000

vocab_dict = {}

token_count = 0

if __name__ == '__main__':
    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            for line in input_file:
                tokens = line.split()
                token_count += len(tokens)
                for token in tokens:
                    value = vocab_dict.get(token, 0)
                    vocab_dict[token] = value + 1

            data = [(value, key) for key, value in vocab_dict.items()]
            data.sort(reverse=True)

            ori_data_len = len(data)
            print("Found so many token:", ori_data_len)

            print("Selecting so many of the top token:", TOKEN_TO_PICK)

            data = data[:TOKEN_TO_PICK]

            print("New number of token:", len(data))
            print("Removed so many token:", ori_data_len - len(data))

            output_file.write("<S>\n</S>\n<UNK>")
            for d in data:
                value, key = d
                output_file.write("\n")
                output_file.write(key)
    print("Token count of input file:", token_count)
