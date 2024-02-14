#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited (directly or indirectly)"""
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False