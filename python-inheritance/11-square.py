#!/usr/bin/python3
""" Module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""


    def __init__(self, size):
        """Instantiation"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
