import unittest
from models.square import Square
import io
from contextlib import redirect_stdout

class TestSquareMethods(unittest.TestCase):

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        square = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            square.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_str(self):
        square = Square(3, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 3")

    def test_update(self):
        square = Square(2)
        square.update(4, 5, 6, 7)
        self.assertEqual(str(square), "[Square] (4) 6/7 - 5")

    def test_to_dictionary(self):
        square = Square(4, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
