import os
from bs4 import BeautifulSoup, SoupStrainer

def write_csv(sites_and_outlinks):
    # clear current report
    open('report.csv', 'w').close()
    # opening a file in append mode
    report = open("report.csv", "a")
    for site, outlinks in sites_and_outlinks:
        report.write("URL: {}, Number of Outlinks: {}".format(site, outlinks))
        report.write("\n")
    report.close()
