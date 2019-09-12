#!/usr/bin/env python3
"""This is a simple python3 calculator for demonstration purposes
some to-do's but we'll get to that"""

__author__ = "Sebastian Meier zu Biesen"
__copyright__ = "2000-2019 by MzB Solutions"
__email__ = "smzb@mitos-kalandiel.me"


class Calculator(object):

    @property
    def isDebug(self):
        return self._isDebug
    
    @isDebug.setter
    def isDebug(self, bDebug):
        self._isDebug = bDebug
    
    @isDebug.deleter
    def isDebug(self):
        del self._isDebug
    
    @property
    def isInteractive(self):
        return self._isInteractive

    @isInteractive.setter
    def isInteractive(self, bInteractive):
        self._isInteractive = bInteractive

    @isInteractive.deleter
    def isInteractive(self):
        del self._isInteractive

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, iOperation):
        self._Operation = iOperation

    @Operation.deleter
    def Operation(self):
        del self._Operation

    @property
    def Num1(self):
        return self._Num1

    @Num1.setter
    def Num1(self, iNum):
        if not isinstance(iNum, int):
            raise TypeError
        self._Num1 = iNum
    
    @Num1.deleter
    def Num1(self):
        del self._Num1
    
    @property
    def Num2(self):
        return self._Num2

    @Num2.setter
    def Num2(self, iNum):
        if not isinstance(iNum, int):
            raise TypeError
        self._Num2 = iNum

    @Num2.deleter
    def Num2(self):
        del self._Num2

    def __init__(self):
        self._isDebug = False
        self._isInteractive = False
        self._Operation = None
        self._Num1 = None
        self._Num2 = None

    def add(self):
        """This functions adds two numbers"""
        return self._Num1 + self._Num2

    def subtract(self):
        """This is a simple subtraction function"""
        return self._Num1 - self._Num2

    def multiply(self):
        """Again a simple multiplication"""
        return self._Num1 * self._Num2

    def divide(self):
        """division function
        todo: (smzb/js) make division by 0 impossible"""
        return self._Num1 / self._Num2

    def ask_op(self):
        """Lets ask what the user wants to do"""
        print("Please select operation -\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide\n")
        # Take input from the user
        result = input("Select operations from 1, 2, 3, 4 :")
        return result

    def ask_number():
        """Get a number from the user"""
        num = int(input("Enter an operand: "))
        return num

    def eval_operation(self):
        """Now evaluate what operation the user wants,
        and run the consecutive function"""
        if self._Operation == '1':
            print(self._Num1, "+", self._Num2, "=",
                  Calculator.add())

        elif self._Operation == '2':
            print(self._Num1, "-", self._Num2, "=",
                  Calculator.subtract())

        elif self._Operation == '3':
            print(self._Num1, "*", self._Num2, "=",
                  Calculator.multiply())

        elif self._Operation == '4':
            print(self._Num1, "/", self._Num2, "=",
                  Calculator.divide())
        elif self._Operation == '0':
            return
        else:
            print("Invalid operation")
