# Author: Eugene Mondkar
# Group 10
# 
# This module holds the functions and classes required for web crawling
#
# TODO: Decide on HTTP request library: urllib or httplib2
# TODO: Retrieve all links and store in frontier
# TODO: Iterate over the frontier and decide on crawl algo
# TODO: Process webpages and extract information for document store
# TODO: Decide on file format for webpage content in document store

import urllib.request as urlreq
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup, SoupStrainer

seed = "https://www.mtsac.edu/"

frontier = []

try:
    html_reader = urlreq.urlopen(seed)
except HTTPError as e:
    print(e)
except URLError as e:
    print(e, "Server could not be found")
else:
    print("Something went wrong") 

# Test to see if the URL request is working
# print(html_reader.read())

# Creating BeautifulSoup object
bs_obj = BeautifulSoup(html_reader)

print(bs_obj)
