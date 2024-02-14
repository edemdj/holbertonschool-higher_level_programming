#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """if object is an instance of a class that inherited directly"""
    if (type(obj) is not a_class):
        return issubclass(type(obj), a_class)
    return False
