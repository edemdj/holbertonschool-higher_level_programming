#!usr/bin/python3
""" class Square that defines a square by: (based on 1-square.py)"""
class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """The __init__ method gets called after memory for the object is allocated"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
