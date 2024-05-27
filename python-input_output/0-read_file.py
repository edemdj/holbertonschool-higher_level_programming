#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """Reads and prints the content of a text file."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
