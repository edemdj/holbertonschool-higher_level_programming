#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the integer value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
