# Author: Eugene Mondkar
# Group 10
# 
# This module holds the functions and classes required for web crawling

import urllib.request as urlreq
from bs4 import BeautifulSoup

seed = "https://www.mtsac.edu/"

frontier = []

html_reader = urlreq.urlopen(seed)

# Test to see if the URL request is working
# print(html_reader.read())

# Creating BeautifulSoup object
bs_obj = BeautifulSoup(html_reader)

print(bs_obj.h1)
