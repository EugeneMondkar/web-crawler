# Module where everyone's components get imported

#####################################
# Import everyone's components here #
#####################################

from crawler import http_crawler # Eugene's Component
from writer import write_csv # Emily' Component
from detectlanguage import detect_and_create # Rachel's component

detect_and_create('.\\textfiles\\', '.\\repository\\', 40)
#######################
# Add glue code below #
#######################


