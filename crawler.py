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



import httplib2
from bs4 import BeautifulSoup, SoupStrainer

seed = "https://www.mtsac.edu/"

frontier = []

http_obj = httplib2.Http()

status, response = http_obj.request(seed)

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])


# Code using urllib modules

# import urllib.request as urlreq
# from urllib.error import HTTPError, URLError

# try:
#     html_reader = urlreq.urlopen(seed)
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print(e, "Server could not be found")
# else:
#     print("Something went wrong") 

# Test to see if the URL request is working
# print(html_reader.read())

# Creating BeautifulSoup object
# bs_obj = BeautifulSoup(html_reader)

# print(bs_obj)