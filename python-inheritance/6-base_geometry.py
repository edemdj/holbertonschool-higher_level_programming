#!/usr/bin/python3
""" Module """


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Calculate the area."""
        raise Exception("area() is not implemented")
