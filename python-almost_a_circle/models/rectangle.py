#!/usr/bin/python3
"""Modiule"""
from models.base import Base

class Rectangle(Base):
    """define rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of _my_attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """define width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of _my_attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """define height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the value of _my_attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """define x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Returns the value of _my_attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """define y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        else:
            self.__y = value
        
    def area(self):
        """Calcul de l'aire du rectangle"""
        return self.width * self.height
    
    def display(self):
        """display rectangle with # with x ,y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """prints a rectangle using '#'"""
        return f"[Rectangle] ({self.id}); {self.x}/{self.y} - {self.width}/{self.height}" 
    
    def update(self, *args, **kwargs):
        """Update attributes with provided arguments"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

