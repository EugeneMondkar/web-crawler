# Author: Eugene Mondkar
# Group 10
# 
# This module holds the functions and classes required for web crawling
#
# DONE: Decide on HTTP request library: urllib or httplib2
# DONE: Retrieve all links and store in frontier
# TODO: Encapsulate Link Extraction
# TODO: Iterate over the frontier and decide on crawl algo
# TODO: Process webpages and extract information for document store
# TODO: Decide on file format for webpage content in document store
# TODO: Handle HTTP error codes



import httplib2
from bs4 import BeautifulSoup, SoupStrainer

if __name__ == '__main__':

    seed = "https://www.mtsac.edu"

    frontier = []

    http_obj = httplib2.Http()

    # encapsulate into function
    url = seed # function argument
    # additional function arguments: http object from httplib2.Http(), and frontier
    status, response = http_obj.request(url)

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features='html.parser'):
        if link.has_attr('href'):
            if link['href'][0] == '/':
                extracted_url = url + link['href']
            elif link['href'][:4] == 'http':
                extracted_url = link['href']
            
            frontier.append(extracted_url)

    print('Stored Links:')
    for i, link in enumerate(frontier):
        print(i, link)

    # end of function






## Code using urllib modules ##

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