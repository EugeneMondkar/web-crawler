# Module where everyone's components get imported

#####################################
# Import everyone's components here #
#####################################

from crawler import http_crawler # Eugene's Component
from writer import write_csv # Emily' Component
from detectlanguage import detect_and_create # Rachel's component

#######################
# Add glue code below #
#######################

# seed_01 = "https://www.mtsac.edu/"

# seeds = [seed_01]

# crawl_limit = 5

# html_file_path = '.\\repository\\html_files\\'

# text_file_path = '.\\repository\\text_files\\'

# sites_and_outlinks = http_crawler(seeds, crawl_limit, repository_path)


# detect_and_create(text_file_path, repository_path, 40)

