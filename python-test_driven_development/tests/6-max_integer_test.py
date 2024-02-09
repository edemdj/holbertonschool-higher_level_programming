#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertIsNone(max_integer([]))

        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

        self.assertEqual(max_integer([-5, 10, -3, 8, -1]), 10)

        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.1]), 4.1)

        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4])

if __name__ == '__main__':
    unittest.main()
