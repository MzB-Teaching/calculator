#!/usr/bin/env python3
"""These are simply unit tests to demonstrate the facility
This is by no means meant to be comprehensive
TODO: (smzb) we need to also test the failures of certain/all operations"""
import unittest
from app.calculator import Calculator

__author__ = "Sebastian Meier zu Biesen"
__copyright__ = "2000-2019 by MzB Solutions"
__email__ = "smzb@mitos-kalandiel.me"


class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_returns_correct_result(self):
        """Simple, make an instance of the app and test that 2+2=4"""
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
