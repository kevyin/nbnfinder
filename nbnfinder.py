__author__ = 'kevin'
import os
import logging
from optparse import OptionParser
import nbn.search as n
import domain.search as d
import ConfigParser


#####################################################################################
## MAIN
def main(run_file):
	usage = """
            %prog [OPTIONS] """
	parser = OptionParser(usage=usage)
	parser.add_option("-u", "--url",
					  dest="customurl", default="",
					  help="Custom url to check")
	parser.add_option("-n", "--name",
					  dest="customname", default="",
					  help="Custom name of url to check. MUST BE SPECIFIED")
	parser.add_option("-s", "--customsection",
					  dest="customsect", default="",
					  help="Custom section to check")
	(opts, args) = parser.parse_args()


	logging.basicConfig(level=logging.INFO)
	darlo_search = "http://www.domain.com.au/search/buy/state/nsw/area/eastern-suburbs/sydney-city/region/sydney-region/suburb/darlinghurst/east-sydney/strawberry-hills/surry-hills/?ssubs=1&bedrooms=1&to=750000&searchterm=2010&features=broadband+internet+access|2&sort=date-asc"
	cache_file = 'cache.cfg'

	config = ConfigParser.RawConfigParser()
	config.read(cache_file)

	if opts.customurl is not "" and opts.customname is not "":
		if not config.has_section(opts.customurl):
			config.add_section(opts.customname)
			with open(cache_file, "w") as file:
				config.write(file)

	sections = config.sections() if opts.customsect is "" else [opts.customsect]

	for sect in sections:
		logging.info("Processing section:" + sect)
		url = config.get(sect, "url")
		addrs = d.search_new(url)
		for add in addrs:
			if not config.has_option(sect, add):
				type = n.search_addr(add)
				config.set(sect, add, type)
				line = "\t".join([add, type])
				logging.info(line)
				if type is not "no":
					logging.warn(line)


	# config.add_section("darlo")
	# config.set("darlo", "url", darlo_search)
	with open(cache_file, "w") as file:
		config.write(file)


	# addrs = d.search_new(darlo)
	# for add in addrs:
	# 	(yn, type) = n.search_addr(add)
	# 	print add, yn, type
	# search_addr("48-50 Burton Street, Darlinghurst, New South Wales, Australia")
	# n.search_addr("69/1-7 Pelican Street, Surry Hills NSW 2010")


#####################################################################################
# Call main
if __name__ == '__main__':
	main(__file__)
