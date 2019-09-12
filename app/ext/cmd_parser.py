#!/usr/bin/env python3
"""This here module allows us to easily parse command line parameters
Again let's use an establised standard for this sort of thing"""
import argparse

__author__ = "Sebastian Meier zu Biesen"
__copyright__ = "2000-2019 by MzB Solutions"
__email__ = "smzb@mitos-kalandiel.me"


class CmdParser(object):
    def __init__(self, args):
        """lets deal with required arguments"""
        self.arguments = args

    """A stupid hack to prevent a line to long issue when creating
    the parser further down the line"""
    desc = "A simple interactive/non-interactive calculator"

    """Build the parser and describe it to the outside world"""
    my_parser = argparse.ArgumentParser(prog="Calculator",
                                        description=desc)

    """Add an argument
    In this case, we a flag, wether the app runs interactively or not"""
    my_parser.add_argument('-i',
                           '--interactive',
                           dest='Interactive',
                           action='store_true',
                           help='When interactive the app will ask your for \
                               input, when non-interactive, the app expects \
                                   all input to be supplied via cmdline')
    my_parser.add_argument('-o',
                           '--operation',
                           dest='Operation',
                           type=str,
                           help='Operation can be on of the following : add, \
                               sub, mul, div ')
    my_parser.add_argument('-n1',
                           '--Number1',
                           dest='Num1',
                           type=int,
                           help='The first (integer) number in our calculation')

    """Execute the parser"""
    argParse = my_parser.parse_args()

    arguments = dict()
    arguments["Interactive"] = argParse.Interactive
    arguments["Operation"] = argParse.Operation
    print(arguments)
