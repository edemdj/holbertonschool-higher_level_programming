import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_str(self):
        rect = Rectangle(3, 5, 1, 2, 10)
        self.assertEqual(str(rect), "[Rectangle] (10); 1/2 - 3/5")

    def test_update(self):
        rect = Rectangle(2, 3)
        rect.update(4, 5, 6, 7, 8)
        self.assertEqual(str(rect), "[Rectangle] (4); 7/8 - 5/6")

    def test_to_dictionary(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
