#!/usr/bin/python3
""" Module """
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by JSON string"""
    object = json.loads(my_str)
    return object
