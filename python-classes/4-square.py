#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """instantiation"""
        self.size = size

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """define special methods when modifying the attributes"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

