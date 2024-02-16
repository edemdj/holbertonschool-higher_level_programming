#!/usr/bin/python3
import json
""" Module """


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):"""
    json_string = json.dumps(my_obj)
    return json_string
