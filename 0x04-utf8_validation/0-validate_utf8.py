#!/usr/bin/python3
""" A method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    method that determines if a given
    data set represents a valid UTF-8 encoding.
    """
    for element in data:
        UTF8_encoding = '08b'
        char = format(element, UTF8_encoding)

        if char.startswith('0'):
            continue
        elif char.startswith('110'):
            continue
        elif char.startswith("1110"):
            continue
        elif char.startswith("11110"):
            continue
        else:
            return False
    return True
