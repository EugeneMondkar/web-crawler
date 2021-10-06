# Author: Eugene Mondkar
# Group 10
#
# Module where everyone's components get imported
#
# DONE: Set up data structures to automate crawling process
# DONE: Write for loop to iterate over languages
#   DONE: Define File paths for each language
#   DONE: Test crawl for 50 sites per language
# DONE: Complete 500-site-crawls for each language
# DONE: Count number of files in each directory to provide arg for detectlanguage library
# DONE: Added documentation 
# DONE: Generate Text files for each respective language
# DONE: Add analysis functions from Neha's and Kylan's code
# DONE: produce reports on time measurements for function execution 

from genericpath import exists
import shutil
import os
from timeit import default_timer as timer
from pathlib import Path

#####################################
# Import everyone's components here #
#####################################

from crawler import http_crawler # Eugene's Component
from writer import write_csv # Emily's Component
from detect_language import detect_and_create # Rachel's component

from zipfs_law import zipfs_law # Kylan's component
from heaps_law import heaps_law # Neha's component

#######################
# Add glue code below #
#######################

languages = ["English", "German", "Spanish"]

seed_01_english = "https://www.mtsac.edu/"
seed_02_german = "https://www.lmu.de/de/studium/studienangebot/index.html"
seed_03_spanish = "https://www.usal.es/"

seeds = [seed_01_english, seed_02_german, seed_03_spanish]

# Report for crawl times
crawl_report = 'crawl_report.txt'
open(crawl_report, 'w').close()
crawl_report = open(crawl_report, 'a')


for language, seed in zip(languages, seeds):

    ##################################
    ######## File Path Set Up ########
    ##################################
    
    parent_path = ".\\Repository_{}\\".format(language)

    report_path = ".\\Reports_{}\\".format(language)
    Path(report_path).mkdir(parents=True, exist_ok=True)

    html_file_path = parent_path + 'html_files\\'

    text_file_path = parent_path + 'text_files\\'

    # Delete pre-exisitng directory paths
    if os.path.exists(parent_path):
        shutil.rmtree(parent_path)

    ##################################
    ########### Web Crawl ############
    ##################################

    crawl_limit = 500

    start_crawl_timer = timer()
    sites_and_outlinks = http_crawler(seed, crawl_limit, html_file_path)
    stop_crawl_timer = timer()

    crawl_report.write('Function time performance for {} crawl:'.format(language))
    crawl_report.write('\n')
    crawl_report.write("Elapsed time for {} crawl is {} seconds".format(language, stop_crawl_timer - start_crawl_timer))
    crawl_report.write('\n')

    ##################################
    ####### Report Generation ########
    ##################################

    start_report_timer = timer()
    write_csv(sites_and_outlinks, report_path, language)
    stop_report_timer = timer()

    crawl_report.write("Elapsed time for {} outlink report generation is {} seconds".format(language, stop_report_timer - start_report_timer))
    crawl_report.write('\n')

    ##################################
    ###### Text File Generation ######
    ##################################

    start_text_generation_timer = timer()
    # Count the number of files in a directory
    # Note: the number of files may not always equal the crawl limit
    root, directory, files = next(os.walk(html_file_path))
    number_of_files = len(files)

    # Create text file for the language
    detect_and_create(text_file_path, html_file_path, number_of_files)
    stop_text_generation_timer = timer()

    crawl_report.write("Elapsed time for {} text file generation is {} seconds".format(language, stop_report_timer - start_report_timer))
    crawl_report.write('\n\n')
    
    ##################################
    ##### Zipf's Law Analysis ########
    ##################################

    specific_language_text_file_path = text_file_path + language.lower() + ".txt"

    # Create analysis report file
    analysis_report_name = report_path + '{}_crawl_analysis_report.txt'.format(language)

    zipfs_law(specific_language_text_file_path, analysis_report_name, turn_off_plots=True)

    ##################################
    ##### Heap's Law Analysis ########
    ##################################

    heaps_law(specific_language_text_file_path, analysis_report_name, turn_off_plots=True)

crawl_report.close()


