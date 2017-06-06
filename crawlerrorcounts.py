import argparse
import sys
from googleapiclient import sample_tools

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,
                       	help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('error_category', type=str,
                    	help=('Acceptable values are: authPermissions,flashContent,manyToOneRedirect,'
                       'notFollowed,notFound,other,roboted,serverError,soft404'
                       'If not specified, returns results for all categories.'))
argparser.add_argument('platform_type', type=str,
                    	help=('Acceptable values are:mobile,smartphoneOnly,web'
                    	'If not specified, returns results for all platforms.'))  
def main(argv):
  	service, flags = sample_tools.init(
      argv, 'webmasters', 'v3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/webmasters.readonly')

	response = execute_request(service, flags.property_uri, flags.error_category, flags.platform_type)

	print_table(response, 'Crawl Error Counts')

def execute_request(service, property_uri, error_category, platform_type):
	print property_uri
	print error_category
	print platform_type

  	return service.urlcrawlerrorscounts().query(siteUrl=property_uri, category=error_category, latestCountsOnly=False, platform=platform_type).execute()

def print_table(response, title):
	
	print response
	
	if 'countPerTypes' not in response:
		print 'Empty response'	
	return

if __name__ == '__main__':
  	main(sys.argv)
