# Author: Eugene Mondkar
# Group 10
# 
# This module holds the functions and classes required for web crawling
#
# Eugene's TODO List Only (your own code should have a separate TODO list):
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
# DONE: Have http_crawler return list of tuples, i.e. (link, number_of_outlinks)
# DONE: Include means to check if link is both in the frontier and visted_sites
# DONE: Added padding to number when generating html file name
# DONE: Fix Function isAlreadyIncludedOrVisited: sites_visited isn't being properly checked
# DONE: Fix File counter
# DONE: Disabled SSL Verification
# DONE: Add politness rules
# TODO: Add support for multiple threads (Motivation: to process multiple crawls across several seeds)

import httplib2
import time
import os
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer

def isAlreadyIncludedOrVisited(url, frontier, sites_visited):
    return ( url not in frontier ) and ( url not in sites_visited )

def linkExtraction(url, response, frontier, sites_visited):

    num_of_links_extracted = 0

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features='html.parser'):
        
        if link.has_attr('href') and len(link['href']) > 1:
            
            if link['href'][0] == '/':
                
                if url[-1] == '/':
                    extracted_url = url + link['href'][1:]
                elif url[-1] != '/':
                    extracted_url = url + link['href']

                if isAlreadyIncludedOrVisited(extracted_url, frontier, sites_visited): # Avoiding duplicate links and redundancy
                    frontier.append(extracted_url)
                    num_of_links_extracted += 1

            elif link['href'][:4] == 'http':
                
                extracted_url = link['href']

                if isAlreadyIncludedOrVisited(extracted_url, frontier, sites_visited): 
                    frontier.append(extracted_url)
                    num_of_links_extracted += 1

    return num_of_links_extracted

def printFrontier(frontier):
    print('Stored Links:')
    for i, link in enumerate(frontier):
        print(i, link)

def saveHtmlFile(repository_path, response, status, current_html_number):
           
    directory_exists = os.path.isdir(repository_path)

    # Get Web Document Encoding
    encoding = status['content-type'][status['content-type'].lower().find('utf'):].lower()

    if status['content-type'] == 'text/html':
        encoding = 'utf-8'
    
    if directory_exists:

        html_file_name = "{:04d}".format(current_html_number) + "_html_file.html"
        full_path_name = repository_path + html_file_name
        html_file = open(full_path_name, 'w')
        
        try:

            html_file.write(response.decode(encoding))
            
        except:

            return False

        html_file.close()

    else:

        Path(repository_path).mkdir(parents=True, exist_ok=True)

        html_file_name = "{:04d}".format(current_html_number) + "_html_file.html"
        full_path_name = repository_path + html_file_name
        html_file = open(full_path_name, 'w')
        
        try:

            html_file.write(response.decode(encoding))
            
        except:

            return False

        html_file.close()

    return True   

def http_crawler(seed, crawl_limit, repository_path):
        
    frontier = []
    frontier.append(seed)

    visited_sites = []
    number_of_outlinks_per_site = []

    http_obj = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

    pages_crawled = 0

    current_html_file_number = 0
    
    while len(frontier) > 0 and pages_crawled < crawl_limit:
        
        url = frontier.pop(0)

        try:
            status, response = http_obj.request(url)
        except:
            status = {'status':'400'}


        if status['status'] == '200':

            if saveHtmlFile(repository_path, response, status, current_html_file_number):

                current_html_file_number += 1

                num_of_links_extracted = linkExtraction(url, response, frontier, visited_sites)
                pages_crawled += 1

                # Parallel lists for to maintain peformance of checking urls against visited sites
                visited_sites.append(url)
                number_of_outlinks_per_site.append(num_of_links_extracted)

        # Politiness Rule: 350 millisecond pause
        time.sleep(0.500)

    return list(zip(visited_sites, number_of_outlinks_per_site))


if __name__ == '__main__':

    pass

    #################################################################################################
    # Code below For Testing Purposes Only.                                                         #
    #                                                                                               #
    # Not to be used as main code.                                                                  #  
    #                                                                                               #
    # Refer to the main module to add code.                                                         #
    #                                                                                               #
    # Documentation:                                                                                #
    #                                                                                               # 
    # import the crawler module into the main module                                                #
    #                                                                                               # 
    # The crawler.http_crawler function takes 3 arguments: lists of seeds, crawl limit, and         #
    # repository path.                                                                              # 
    #                                                                                               #
    # The function returns a list of tuples with hold the sites visited                             #
    # and saved as html documents in the repository along with the number of outlinks               #
    # extracted and added to the frontier for traversal                                             #  
    #                                                                                               #
    # 10/03/2021 - Eugene Mondkar                                                                   #
    #################################################################################################

    # seed_01 = "https://www.mtsac.edu/"

    # seed_01 = "https://www.uni-heidelberg.de/de/universitaet"
    
    # crawl_limit = 5

    # repository_path = '.\\repository\\'

    # sites_and_outlinks = http_crawler(seed_01, crawl_limit, repository_path)

    # for site, outlinks in sites_and_outlinks:
    #     print("Site: {}, Number of Outlinks: {}".format(site, outlinks))
     
