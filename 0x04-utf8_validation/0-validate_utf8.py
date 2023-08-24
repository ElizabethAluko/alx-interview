#!/usr/bin/python3
"""Contains module that Validate UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    byte_remain = 0

    for byte in data:
        if byte_remain == 0:
            # Check for single-byte character
            if byte >> 7 == 0:
                byte_remain = 0
            # Check for two-byte character
            elif byte >> 5 == 0b110:
                byte_remain = 1
            # Check for single-byte character
            elif byte >> 4 == 0b1110:
                byte_remain = 2
            # Check for single-byte character
            elif byte >> 3 == 0b11110:
                byte_remain = 3
            #invalid byte pattern
            else:
                return False
        else:
            # Check for continuation byte
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            byte_remain -= 1
    #Put byte_remain = 0 to ensure all characters are properly formed
    return byte_remain == 0
