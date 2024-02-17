#!/usr/bin/python3
""" Module """
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
