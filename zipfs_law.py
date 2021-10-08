# Author: Kylan Parayao
# Group 10
#
# Tracking of Modifications, Refactoring, and Corrections to code:
# TODO (Eugene Mondkar): Redo entire module from stracth to remove copied code
#
# Previous Version
# DONE (Eugene Mondkar): Encapsulate code into module file and respective functions
# DONE (Eugene Mondkar): Validate and Test Code --> Code validated on 10-06-2021 1:00 am
# DONE (Eugene Mondkar): Kylan hardcoded greatgatsby.txt file name into subfunctions causing errors, needed to search to fix
# DONE (Eugene Mondkar): Rearranged Function Order
# DONE (Eugene Mondkar): Generate Analysis Report
# TODO (Eugene Mondkar): Need to add titles to plots
# TODO (Eugene Mondkar): Programmatically Add Plots to PDF

# WARNING: Unbeknownst to me (Eugene Mondkar) code was plagiarized by original author from https://www.codedrome.com/zipfs-law-in-python/
# The proper citation is now included. 

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

def create_zipf_table(text_file_path, frequencies):
    f = open(text_file_path, "r")
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

def generate_zipf_table(text_file_path, text, top):
    text = remove_punctuation(text)
    text = text.lower()
    top_words = top_word_frequencies(text, top)
    zipf_table = create_zipf_table(text_file_path, top_words)
    return zipf_table

def print_zipf_table(zipf_table, analysis_report_name, turn_off_plots):

    analysis_report = open(analysis_report_name, 'a')
    
    width = 80
    analysis_report.write("-" * width)
    analysis_report.write("\n")
    analysis_report.write("|Rank|    Word    |Word Count |  Probability of Occurence|")
    analysis_report.write("\n")
    analysis_report.write("-" * width)
    analysis_report.write("\n")
    format_string = "|{:4}|{:12}|{:12.0f}|{:.4f}"

    for index, item in enumerate(zipf_table, start=1):
        analysis_report.write(
            format_string.format(index, item["word"], item["word_count"],
                                 item["prob_occurence"]))
        analysis_report.write("\n")
    
    analysis_report.write("-" * width)
    analysis_report.write("\n\n")
    analysis_report.close()

    x=[]
    y=[]
    for index, item in enumerate(zipf_table, start=1):
        x.append(index)
        y.append(item["word_count"])
        pythonplot.plot(x, y)
        pythonplot.xlabel('rank')
        pythonplot.ylabel('frequency')

    if not(turn_off_plots):
        pythonplot.show()
    

def zipfs_law(text_file_path, analysis_report_name, turn_off_plots=False):
    try:

        open(analysis_report_name, 'w').close()
        analysis_report = open(analysis_report_name, 'a')

        f = open(text_file_path, "r")
        text = f.read()
        words = text.split()
        length = len(words)
        analysis_report.write("ZIPF'S LAW ANALYSIS")
        analysis_report.write("\n")
        analysis_report.write("\n")
        analysis_report.write('-----------------')
        analysis_report.write("\n")
        analysis_report.write('|Zipfs Law                   |')
        analysis_report.write("\n")
        analysis_report.write('|Total number of words: ' + str(length) + '|')
        analysis_report.write("\n")
        analysis_report.write('-----------------\n')
        analysis_report.write("\n")
        f.close()
        analysis_report.close()

        zipf_table = generate_zipf_table(text_file_path, text, 100)

        print_zipf_table(zipf_table, analysis_report_name, turn_off_plots)
        

    except IOError as e:

        print(e)
