#!/usr/bin/env python3
"""These are simply unit tests to demonstrate the facility
This is by no means meant to be comprehensive"""
import unittest

__author__= "Sebastian Meier zu Biesen"
__copyright__= "2000-2019 by MzB Solutions"
__email__= "smzb@mitos-kalandiel.me"

class Test_Calc(unittest.TestCase):

    def test_add_returns_correct_result(self):
        calc = Calculator()
