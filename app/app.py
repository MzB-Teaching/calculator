#!/usr/bin/env python3
"""This is the app wrapper for the calculator
here we process command line parameters"""
import argparse
from mods.calculator import Calculator

__author__ = "Sebastian Meier zu Biesen"
__copyright__ = "2000-2019 by MzB Solutions"
__email__ = "smzb@mitos-kalandiel.me"


class App(object):

    doDebug = True

    def __init__(self):
        print("Test2")

    def main():
        """A stupid hack to prevent a line to long issue when creating
        the parser further down the line """
        desc = "A simple interactive/non-interactive calculator"
        """Build the parser and describe it to the outside world"""
        my_parser = argparse.ArgumentParser(prog="Calculator",
                                            description=desc)
        """Add an argument
         In this case, we a flag, wether the app runs interactively or not"""
        my_parser.add_argument('-d',
                               '--debug',
                               dest='Debug',
                               action='store_true',
                               default=False,
                               help='When debugging is enabled, the app will \
                                   output extra information during execution')
        my_parser.add_argument('-i',
                               '--interactive',
                               dest='Interactive',
                               action='store_true',
                               default=False,
                               help='When interactive the app will ask your for \
                                     input, when non-interactive, the app \
                                     expects all input to be supplied via \
                                     cmdline')
        my_parser.add_argument('-o',
                               '--operation',
                               dest='Operation',
                               type=int,
                               help='Operation can be on of the following : \
                                    1 = add \
                                    2 = subtract \
                                    3 = multiply \
                                    4 = divide')
        my_parser.add_argument('-n1',
                               '--Number1',
                               dest='Num1',
                               type=int,
                               help='The first (integer) number in our \
                                     calculation')
        my_parser.add_argument('-n2',
                               '--Number2',
                               dest='Num2',
                               type=int,
                               help='The second (integer) number in our \
                                     calculation')
        """Execute the parser"""
        argParser = my_parser.parse_args()
        calc = Calculator()
        calc.isInteractive = argParser.Interactive
        calc.isDebug = argParser.Debug
        if calc.isInteractive:
            calc.Operation = calc.ask_op()
            calc.Num1 = calc.ask_number()
            calc.Num2 = calc.ask_number()
        else:
            calc.Operation = argParser.Operation
            calc.Num1 = argParser.Num1
            calc.Num2 = argParser.Num2
        calc.eval_operation()
        if calc.isDebug:
            print("Debugging : ", calc.isDebug)
            print("Interactive : ", calc.isInteractive)
            print("Operation : ", calc.Operation)
            print("Number 1 : ", calc.Num1)
            print("Number 2 : ", calc.Num2)
        pass
    
    if __name__ == '__main__':
        main()
