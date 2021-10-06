# Author: Emily Villalba
# Group 10

# Tracking of Modifications, Refactoring, and Corrections to code:
# DONE (Eugene Mondkar): Removed httplib2 import
# DONE (Eugene Mondkar): Added language parameter to append to csv filename
# DONE (Eugene Mondkar): Removed other unnecessary libraries
# DONE (Eugene Mondkar): Had to accomadate for links with commas (google maps links)
# DONE (Eugene Mondkar): Add Reports Directory

def write_csv(sites_and_outlinks, reports_directory, language):
    
    report_name = reports_directory + 'report_{}.csv'.format(language)

    # clear current report
    open(report_name, 'w').close()
    
    # opening a file in append mode
    report = open(report_name, 'a')

    for site, outlinks in sites_and_outlinks:
        site = site.replace(',','.')
        report.write("URL: {}, Number of Outlinks: {}".format(site, outlinks))
        report.write("\n")

    report.close()
