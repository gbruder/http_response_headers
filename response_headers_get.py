#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
"""
response_headers_get

python script to get reponse headers from 2 URLS and display / compare.

"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# TODO
#
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------

import sys
import requests
from optparse import OptionParser


# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------
def main():

    # get the command line options and extra(options) from the command line.
    (options, extras) = process_command_line_args()

    url1 = options.url1
    url2 = options.url2

    header_verify = options.header_verify

    print_response_headers(url1, header_verify)
    print_response_headers(url2, header_verify)

# ---------------------------------------------------------------------------------------------
#  Print request headers for a URL
#
# expects:
#    URL
#    header_verify
# returns:
#
# ---------------------------------------------------------------------------------------------
def print_response_headers(this_url, header_verify):

    print "\n---------------------------------------------------------------------------------"
    print   "URL:    " + this_url

    key = ""
    value = ""

    try:
        r = requests.get(this_url,verify = header_verify)
        headers = r.headers
        print "Response Header:"
        for key,value in headers.items():
            print("\t%s: %s " % (key, value))
    except Exception as e:
        print e.message, e.args
    print "---------------------------------------------------------------------------------\n"

    return()

# ---------------------------------------------------------------------------------------------
# Process command line options
#
# returns:
#    options - processed options
#    extras - command line options not processed
# ---------------------------------------------------------------------------------------------
def process_command_line_args():
    """
    Please run "run_render  --help" for the usage message.
    """
    usage = "usage: %prog  --url1 <URL> --url2 <URL> --verify || --noverify [-v] [-q]"
    parser = OptionParser(usage)

    parser.add_option("--url1",
                      dest="url1",
                      help="first URL to get response headers for")

    parser.add_option("--url2",
                      dest="url2",
                      help="second URL to get response headers for")

    parser.add_option("--verify",
                      action="store_true",
                      dest="header_verify",
                      help="verify the SSL certificate")

    parser.add_option("--noverify",
                      action="store_false",
                      dest="header_verify",
                      help="ignore verifying the SSL certificate")

    parser.add_option("-v", "--verbose",
                      action="store_true",
                      dest="verbose")

    parser.add_option("-q", "--quiet",
                      action="store_false",
                      dest="verbose")

    (options, args) = parser.parse_args()

    if options.url1:
       pass
    else:
        print ("url1 is not set")
        print usage
        sys.exit()

    if options.url2:
       pass
    else:
        print ("url2 is not set")
        print usage
        sys.exit()

    if options.header_verify == None:
        print ("set --verify or --noverify flag")
        print usage
        sys.exit()
    else:
        pass

    if len(args):
        parser.error("incorrect number of arguments")

    for arg in args:
        print("Illeagle option %s" % arg)
        sys.exit()

    return (options, args)


# ---------------------------------------------------------------------------------------------
# Execute the main routine and exit with the specified return value.
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    exit_status = main()
    sys.exit(exit_status)
