#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""
def text_indentation(text):
    """function that prints a text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for char in text:
        if i == 0:
            if char == " ":
                continue
            else:
                i = 1
        if i == 1:
            if char in [".", "?", ":"]:
                print((char))
                print()
                i = 0
            else:
                print((char), end=(""))
