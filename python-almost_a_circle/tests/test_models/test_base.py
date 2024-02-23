#!/usr/bin/python3
"""Module"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):

    def test_to_json_string_empty(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_from_json_string_empty(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        data = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = Base.from_json_string(data)
        self.assertEqual(result, [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

    def test_create_rectangle(self):
        data = {"id": 1, "width": 5, "height": 10}
        instance = Rectangle.create(**data)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 5)
        self.assertEqual(instance.height, 10)

    def test_create_square(self):
        data = {"id": 1, "size": 7}
        instance = Square.create(**data)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.size, 7)

if __name__ == '__main__':
    unittest.main()
