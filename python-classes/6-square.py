#!/usr/bin/python3
"""class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set position"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
