from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]




def print_word_freq(file):
    text_file = open(file)
    data = text_file.read()
    data_list = data.split('\n')
    text_file.close()
    """print (data.lower())"""
    """Read in `file` and print out the frequency of words in that file."""
    print(data_list)
    
    import string

    clean_words = []
    for word in data_list:
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter,"")
        clean_words.append(word)

    print (clean_words)

    squeaky_words = []
    for word in clean_words:
        squeaky_words.append(word.lower())

    print (", ".join(squeaky_words))

"""So this gets the txt file into list of strings. It is all lower case and most
of the punctuation is taken out (still having trouble with some commas). Still need
to remove the stop words and count/print frequency"""


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
