# Module where everyone's components get imported

from genericpath import exists
import shutil
import os

#####################################
# Import everyone's components here #
#####################################

from crawler import http_crawler # Eugene's Component
from writer import write_csv # Emily' Component
from detectlanguage import detect_and_create # Rachel's component

#######################
# Add glue code below #
#######################

languages = ["English", "German", "Spanish"]

seed_01_english = "https://www.mtsac.edu/"
seed_02_german = "https://www.lmu.de/de/studium/studienangebot/index.html"
seed_03_spanish = "https://www.usal.es/"

seeds = [seed_01_english, seed_02_german, seed_03_spanish]

for language, seed in zip(languages, seeds):
    
    parent_path = ".\\Repository_{}\\".format(language)

    html_file_path = parent_path + 'html_files\\'

    text_file_path = parent_path + 'text_files\\'

    # Delete pre-exisitng directory paths
    if os.path.exists(parent_path):
        shutil.rmtree(parent_path)

    crawl_limit = 10

    sites_and_outlinks = http_crawler(seed, crawl_limit, html_file_path)

    write_csv(sites_and_outlinks, language)

    # detect_and_create(text_file_path, repository_path, 40)

