#!/usr/bin/python3
"""Contains module that Validate UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    for item in data:
        for i in range(8):
            item //= 2
            if item == 0:
                break
        if item != 0:
            return False
    return True
