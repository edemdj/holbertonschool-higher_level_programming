#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """test for max integer"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def not_an_int(self):
        """tests for not an int"""
        self.assertIsInstance(max_integer("Hello"), int)
if __name__ == '__main__':
    unittest.main()
