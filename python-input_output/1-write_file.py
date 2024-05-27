#!/usr/bin/python3
""" Module """


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns number of characters"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
