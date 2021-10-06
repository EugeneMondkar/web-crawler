# CSV Report Writer Module by Emily Villalba
# DONE (Eugene Mondkar): Removed httplib2 import
# DONE (Eugene Mondkar): Added language parameter to append to csv filename
# DONE (Eugene Mondkar): Removed other unnecessary libraries
# DONE (Eugene Mondkar): Had to accomadate for links with commas (google maps links)

def write_csv(sites_and_outlinks, language):
    
    report_name = 'report_{}.csv'.format(language)

    # clear current report
    open(report_name, 'w').close()
    
    # opening a file in append mode
    report = open(report_name, 'a')

    for site, outlinks in sites_and_outlinks:
        site = site.replace(',','.')
        report.write("URL: {}, Number of Outlinks: {}".format(site, outlinks))
        report.write("\n")

    report.close()
