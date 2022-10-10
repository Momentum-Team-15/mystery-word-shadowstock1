import string
from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    # open the file
    with open(file, 'r') as file:
        file_text = file.read()
        words = file_text.split()
        table = str.maketrans("", "", string.punctuation)
        stripped_words = [w.translate(table) for w in words]
        # print(stripped_words)

        lower_words = []
        for word in stripped_words:
            lower_words.append(word.lower())

        # print(lower_words)

        new_list = [word for word in lower_words if word not in STOP_WORDS]

    word_dict = {}
    for word in new_list:
        if word not in word_dict:
            word_dict[word] = 1
        word_dict[word] += 1
    # print(word_dict)

    word_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    sort_list = dict(word_list)
    for (key, value) in sort_list.items():
        star_mark = ''
        i = 0
        while i < value:
            star_mark += '*'
            i += 1
        print(f'{key} |'.rjust(20), value, star_mark)


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
