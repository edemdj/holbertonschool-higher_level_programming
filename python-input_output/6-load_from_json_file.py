#!/usr/bin/python3
""" Module """
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:"""
    with open(filename, 'w') as f:
        return json.loads(f)
