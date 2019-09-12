#!/usr/bin/env python3
"""This is a simple python3 calculator for demonstration purposes
some to - do 's but we' ll get to that """
import argparse
from calculator import Calculator

__author__ = "Sebastian Meier zu Biesen"
__copyright__ = "2000-2019 by MzB Solutions"
__email__ = "smzb@mitos-kalandiel.me"


class App(object):

    def __init__(self):
        self.calc = Calculator()

    def main(self):
        """A stupid hack to prevent a line to long issue when creating
        the parser further down the line """
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
                               default=True,
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
        self.calc.isInteractive = argParser.Interactive
        if self.calc.isInteractive():
            self.calc.Operation = self.calc.ask_op()
            self.calc._Num1 = self.calc.ask_number()
            self.calc._Num2 = self.calc.ask_number()
        else:
            self.calc.Operation = argParser.Operation
            self.calc.Num1 = argParser.Num1
            self.calc.Num2 = argParser.Num2
        self.calc.eval_operation()
    pass
