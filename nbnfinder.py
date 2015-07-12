__author__ = 'kevin'
import logging
from optparse import OptionParser
import ConfigParser

import nbn.search as n
import domain.search as d



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
    parser.add_option("", "--noUpdateAddresses",
                      dest="updateAddresses", default=True, action='store_false',
                      help="Don't Update addresses")
    (opts, args) = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    cache_file = 'cache.cfg'

    config = ConfigParser.RawConfigParser()
    config.read(cache_file)

    if opts.customurl is not "" and opts.customname is not "":
        if not config.has_section(opts.customurl):
            config.add_section(opts.customname)
            with open(cache_file, "w") as file:
                config.write(file)

    # Check and plan work
    sections = config.sections() if opts.customsect is "" else [opts.customsect]
    for sect in sections:
        logging.info("Processing section:" + sect)
        prev_addrs = [a for (a, t) in config.items(sect) if a is not "url"]

        if opts.updateAddresses:
            url = config.get(sect, "url")
            addrs = [str(add).lower() for add in d.search_new(url)]
            new_addrs = [a for a in addrs if a not in prev_addrs]

            logging.info("New addresses: " + "\n".join(new_addrs))

            for newa in new_addrs:
                config.set(sect, newa, "")

    with open(cache_file, "w") as file:
        config.write(file)

    config.read(cache_file)
    # Do work
    sections = config.sections() if opts.customsect is "" else [opts.customsect]
    for sect in sections:
        addrs = [(a, t) for (a, t) in config.items(sect) if a is not "url"]
        for (add, prev_t) in addrs:
            if prev_t is "":
                type = n.search_addr(add)
                config.set(sect, add, type)
                line = "\t".join([add, type])
                logging.info(line)
                if type is not "no":
                    logging.warn(line)

    with open(cache_file, "w") as file:
        config.write(file)


#####################################################################################
# Call main
if __name__ == '__main__':
    main(__file__)
