#!/usr/bin/env python3
"""This here module allows us to easily parse command line parameters
Again let's use an establised standard for this sort of thing"""
import argparse

class CmdParser(object):
    def __init__(self, arguments):
        """lets deal with required arguments"""
        print(arguments)
        self.is_interactive=0
        
    """Build the parser and describe it to the outside world"""
    my_parser = argparse.ArgumentParser(prog='calculator',description='A simple interactive/non-interactive calculator')

    """Add an argument
    In this case, we a flag, wether the app runs interactively or not"""
    my_parser.add_argument('-i',
        '--interactive',
        metavar='Interactive',
        action='store_true',
        help='When interactive the app will ask your for input, when non-interactive, the app expects all input to be supplied via cmdline')
    my_parser.add_argument('-o',
                           '--operation',
                           type=str,
                           help='Operation can be on of the following : add, sub, mul, div')

    """Execute the parser"""
    args = my_parser.parse_args()

    is_interactive = args.Interactive

