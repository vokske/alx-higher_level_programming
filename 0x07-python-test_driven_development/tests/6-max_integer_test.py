#!/usr/bin/python3
"""Module contains unittests for the max_integer function."""


import unittest
import importlib
my_max_int = importlib.import_module("6-max_integer")
max_int = my_max_int.max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_int([2, 4, 6, 8]), 8)
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([-3, 0]), 0)
        self.assertEqual(max_int([-5, -2]), -2)
        self.assertEqual(max_int([2, 4, 6, 8]), 8)
        self.assertEqual(max_int([8, 3, 6]), 8)
        self.assertEqual(max_int([5, 6, 1]), 6)
        self.assertEqual(max_int([4]), 4)
