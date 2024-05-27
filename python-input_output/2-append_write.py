#!/usr/bin/python3
""" Module """


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)"""
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
