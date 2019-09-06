#!/usr/bin/env python3
"""This here module allows us to easily parse command line parameters
Again let's use an establised standard for this sort of thing"""
import sys, re, optparse

class CmdParser(object):
    first_re = re.compile(r'^\d{3}$')

    parser = optparse.OptionParser()
    parser.set_defaults(debug=False,interactive=False)
    parser.add_option('--debug', action='store_true', dest='debug')
    parser.add_option('--interactive', action='store_true', dest='interactive')
    (options, args) = parser.parse_args()

    if len(args) == 1:
        if first_re.match(args[0]):
            print "Primary argument is : ", args[0]
        else:
            raise ValueError("First argument should be ...")
    elif len(args) > 1:
        raise ValueError("Too many command line arguments")

    if options.debug:
        print 'debug flag'

    if options.xls:
        print 'interactive flag'
