import collections
import matplotlib.pyplot as pythonplot

def remove_punctuation(text):
    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
    tr = str.maketrans("", "", chars_to_remove)
    return text.translate(tr)


def top_word_frequencies(text, top):
    words = text.split()
    word_frequencies = collections.Counter(words)
    top_word_frequencies = word_frequencies.most_common(top)
    return top_word_frequencies


def generate_zipf_table(text, top):
    text = remove_punctuation(text)
    text = text.lower()
    top_words = top_word_frequencies(text, top)
    zipf_table = create_zipf_table(top_words)
    return zipf_table


def create_zipf_table(frequencies):
    f = open("greatgatsby.txt", "r")
    text = f.read()
    words = text.split()
    length = len(words)
    f.close()
    zipf_table = []
    for index, item in enumerate(frequencies, start=1):
        prob_occurence = (item[1] / length) * 100
        zipf_table.append({
            "word": item[0],
            "word_count": item[1],
            "prob_occurence": prob_occurence
        })
    return zipf_table


def print_zipf_table(zipf_table):
    width = 80
    print("-" * width)
    print("|Rank|    Word    |Word Count |  Probability of Occurence|")
    print("-" * width)
    format_string = "|{:4}|{:12}|{:12.0f}|{:.4f}"
    for index, item in enumerate(zipf_table, start=1):
        print(
            format_string.format(index, item["word"], item["word_count"],
                                 item["prob_occurence"]))
    print("-" * width)
    x=[]
    y=[]
    for index, item in enumerate(zipf_table, start=1):
        x.append(index)
        y.append(item["word_count"])
        pythonplot.plot(x, y)
        pythonplot.xlabel('rank')
        pythonplot.ylabel('frequency')
    pythonplot.show()    