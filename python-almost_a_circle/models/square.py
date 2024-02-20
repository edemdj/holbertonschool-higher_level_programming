#!/usr/bin/python3
"""Module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Define a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """Getter for the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
