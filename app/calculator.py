#!/usr/bin/env python3
"""This is a simple python3 calculator for demonstration purposes
some to-do's but we'll get to that"""
from app.cmd_parse import CmdParser

__author__= "Sebastian Meier zu Biesen"
__copyright__= "2000-2019 by MzB Solutions"
__email__= "smzb@mitos-kalandiel.me"

class Calculator(object):

    def add(self, num1, num2):
        """This functions adds two numbers"""
        return num1 + num2

    def subtract(self, num1, num2):
        """This is a simple subtraction function"""
        return num1 - num2

    def multiply(self, num1, num2):
        """Again a simple multiplication"""
        return num1 * num2

    def divide(self, num1, num2):
        """division function
        todo: (smzb/js) make division by 0 impossible"""
        return num1 / num2

    def ask_op():
        """Lets ask what the user wants to do"""
        print("Please select operation -\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide\n")

        # Take input from the user
        op = input("Select operations form 1, 2, 3, 4 :")
        return op

    def ask_number():
        """Get a number from the user"""
        num = int(input("Enter an operand: ")) 
        return num

    def init():
        """This should really only be run when "interactive"!"""
        gOperation=ask_op()
        gNum1=ask_number()
        gNum2=ask_number()
        return

    def eval_operation(self, operation):
        """..."""
        """Now evaluate what operation the user wants, and run the consecutive function"""
        if gOperation == '1':
            print(gNum1, "+", gNum2, "=",
                  add(gNum1, gNum2))

        elif gOperation == '2':
            print(gNum1, "-", gNum2, "=",
                  subtract(gNum1, gNum2))

        elif gOperation == '3':
            print(gNum1, "*", gNum2, "=",
                  multiply(gNum1, gNum2))

        elif gOperation == '4':
            print(gNum1, "/", gNum2, "=",
                  divide(gNum1, gNum2))
        elif gOperation == '0':
            return
        else:
            print("Invalid operation")


    """Really, this is all that is required to bootstrap python, nothing?!!!????!
    this is madness lol"""

    arguments = ['Interactve','Operation','Num1','Num2']
    live_args = CmdParser(arguments)

    """Debug flag"""
    DO_DEBUG=0

    """Lets start with some global vars (bad juju but it'll do just now)
    Did I mention I don't like pythons bootstrapping?"""
    gOperation=0
    gNum1=0
    gNum2=0

    if DO_DEBUG:
        print("Number 1: ", gNum1,
              "Number 2: ", gNum2,
              "operation :", gOperation)

    
