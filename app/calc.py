#!/usr/bin/env python3
"""This is a simple python3 calculator for demonstration purposes
some to-do's but we'll get to that"""

__author__= "Sebastian Meier zu Biesen"
__copyright__= "2000-2019 by MzB Solutions"
__email__= "smzb@mitos-kalandiel.me"

def add(num1, num2):
    """This functions adds two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """This is a simple subtraction function"""
    return num1 - num2

def multiply(num1, num2):
    """Again a simple multiplication"""
    return num1 * num2

def divide(num1, num2):
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

"""Some debugging"""
DO_DEBUG=1

"""Lets start by getting all necessary information"""
operation=ask_op()
num1=ask_number()
num2=ask_number()

if DO_DEBUG:
    print("Number 1: ", num1,
          "Number 2: ", num2,
          "operation :", operation)

"""Now evaluate what operation the user wants, and run the consecutive function"""
if operation == '1':
    print(num1, "+", num2, "=",
                    add(num1, num2))

elif operation == '2':
    print(num1, "-", num2, "=",
                    subtract(num1, num2))

elif operation == '3':
    print(num1, "*", num2, "=",
                    multiply(num1, num2))

elif operation == '4':
    print(num1, "/", num2, "=",
                    divide(num1, num2))
else:
    print("Invalid operation")
