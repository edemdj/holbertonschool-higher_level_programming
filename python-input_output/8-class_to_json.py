#!/usr/bin/python3
"""Module"""


def class_to_json(obj):
    """create class"""
    json_dict = {}
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
    return json_dict
