#!/usr/bin/python3
import json
""" Module """


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:"""
    with open(filename, 'w') as f:
        json.loads(f)
