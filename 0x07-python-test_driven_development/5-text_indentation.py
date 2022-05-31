#!/usr/bin/python3
"""
4. Text indentation
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not type(text) == str:
        """
        raise a TypeError exception if text is not a string
        """
        raise TypeError("text must be a string")

    counter = 0
    for char in text:
        if counter == 0:
            if char == " ":
                continue
            else:
                counter = 1
        if counter == 1:
            if char == "." or char == "?" or char == ":":
                print(char)
                print()
                counter = 0
            else:
                print(char, end="")
