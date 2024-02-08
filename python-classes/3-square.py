#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    def __init__(self, size=0):
        """instantiation"""
        self._square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return area"""
        self.area = self._square__size ** 2
        return self.area
