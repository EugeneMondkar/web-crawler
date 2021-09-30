# Author: Eugene Mondkar
# Group 10
# 
# This module holds the functions and classes required for web crawling
#
# DONE: Decide on HTTP request library: urllib or httplib2
# DONE: Retrieve all links and store in frontier
# DONE: Encapsulate Link Extraction
# DONE: Modify code to accomodate for multiple seeds
# DONE: Modify arguments for linkExtraction function to accomodate higher performance
# DONE: Iterate over the frontier and decide on crawl algo
# DONE: Encapsulate crawler into its own function
# DONE: Write out functionality to save html file on local machine
#   DONE: Check to see if directory exists
# DONE: Define function to process and save webpage into repository as a html document
# DONE: Decide on file format for webpage content in document store
# DONE: Handle HTTP error codes
# TODO: Add support for multiple threads (Motivation: to process multiple crawls across several seeds)


import httplib2
import os
from bs4 import BeautifulSoup, SoupStrainer


def linkExtraction(url, response, frontier):

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features='html.parser'):
        if link.has_attr('href') and len(link['href']) > 1:
            if link['href'][0] == '/':
                if url[-1] == '/':
                    extracted_url = url + link['href'][1:]
                elif url[-1] != '/':
                    extracted_url = url + link['href']

                if extracted_url not in frontier: # Avoiding duplicate links and redundancy
                    frontier.append(extracted_url)

            elif link['href'][:4] == 'http':
                extracted_url = link['href']

                if extracted_url not in frontier: 
                    frontier.append(extracted_url)           

def printFrontier(frontier):
    print('Stored Links:')
    for i, link in enumerate(frontier):
        print(i, link)

def saveHtmlFile(repository_path, response, status, pages_crawled):
           
    directory_exists = os.path.isdir(repository_path)

    # Get Web Document Encoding
    encoding = status['content-type'][status['content-type'].lower().find('utf'):].lower()
    
    if directory_exists:

        html_file_name = str(pages_crawled) + "_html_file.html"
        full_path_name = repository_path + html_file_name
        html_file = open(full_path_name, 'w')
        
        try:
            html_file.write(response.decode(encoding))
        except:
            pass

        html_file.close()

    else:

        os.mkdir(repository_path)
        html_file_name = str(pages_crawled) + "_html_file.html"
        full_path_name = repository_path + html_file_name
        html_file = open(full_path_name, 'w')
        
        try:
            html_file.write(response.decode(encoding))
        except:
            pass

        html_file.close()    

def http_crawler(seeds, crawl_limit, repository_path):
        
    frontier = seeds

    http_obj = httplib2.Http()

    pages_crawled = 0
    
    while len(frontier) > 0 and pages_crawled < crawl_limit:
        url = frontier.pop(0)

        try:
            status, response = http_obj.request(url)
        except:
            status = {'status':'400'}


        if status['status'] == '200':
            linkExtraction(url, response, frontier)
            pages_crawled += 1
            
            saveHtmlFile(repository_path, response, status, pages_crawled)

            # For Validating Results
            # print("Fronter after visit number: ", pages_crawled)
            # printFrontier(frontier)
    
    # For Validating Results
    # print("The number of links in frontier:", len(frontier))

    return pages_crawled

if __name__ == '__main__':

    seed_01 = "https://www.mtsac.edu/"

    seeds = [seed_01]
    
    crawl_limit = 300

    repository_path = '.\\repository\\'

    pages_crawled = http_crawler(seeds, crawl_limit, repository_path)

    print("The Number of Pages Crawled:", pages_crawled)
