#!/usr/bin/python3
"""Module"""
import json
import sys
import os.path

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

def add_item_to_list(args):
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args)
    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    args = sys.argv[1:]
    add_item_to_list(args)

