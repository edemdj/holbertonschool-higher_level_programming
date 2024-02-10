#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """ defines an empty class rectangle """
    def __init__(self, width=0, height=0):
        """ initializes height and width """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width with new value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height with new value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns de area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
