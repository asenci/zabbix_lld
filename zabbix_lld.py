#!/bin/env python2.6
import csv
import json
import logging
import sys

def getFS():
    fslist = []

    with open('/etc/mtab','r') as source:

        fieldnames=['{#FSDEV}',
                    '{#FSNAME}',
                    '{#FSTYPE}',
                    '{#FSOPTS}',
                    '{#FSDUMP}',
                    '{#FSCK}']
        parser = csv.DictReader(source,
                                delimiter=' ',
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_NONE)

        for line in parser:
            logging.info('FS: Fount filesystem "{0}", mounted on "{1}"'.format(line['{#FSDEV}'], line['{#FSNAME}']))
            fslist.append(line)

    dict = {'data': fslist}
    logging.debug(json.dumps(dict, indent=2))
    print json.dumps(dict)

def parseOptions():
    import optparse
    global options

    usage = 'Usage: %prog [options] <discovery type>'
    optparser = optparse.OptionParser(usage)

    optparser.add_option('-q', '--quiet', dest='quiet', default=False,
                      action='store_true',
                      help='print errors only')

    optparser.add_option('-v', '--verbose', dest='verbose', default=False,
                      action='store_true',
                      help='print info')

    optparser.add_option('-d', '--debug', dest='debug', default=False,
                      action='store_true',
                      help='print debug')

    (options, args) = optparser.parse_args()

    if len(args) == 1:
        options.action = args[0]
    else:
        optparser.print_help(sys.stderr)
        sys.exit(1)

    logformat = '%(message)s'
    if options.debug:
        logging.basicConfig(level=logging.DEBUG, format=logformat)
    elif options.verbose:
        logging.basicConfig(level=logging.INFO, format=logformat)
    elif options.quiet:
        logging.basicConfig(level=logging.ERROR, format=logformat)
    else:
        logging.basicConfig(level=logging.WARNING, format=logformat)

def main():
    parseOptions()

    if options.action == 'fs':
        getFS()
    else:
        logging.error('Not supported: {0}'.format(options.action))
        sys.exit(1)

    logging.shutdown()

if __name__ == '__main__':
    main()
