#!/usr/bin/python3
""" class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """class Square """
    def __init__(self, size=0):
        """instantiation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
