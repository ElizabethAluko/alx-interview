#!/usr/bin/python3
""" Module that text whether data is UTF-8 encoded"""


def validUTF8(data):
    """ Initialize a counter to keep track of the number of bytes
    in the current character
    """
    bytes_to_process = 0

    for num in data:
        # Convert the number to binary representation and get the last 8 bits
        binary_num = bin(num)[2:].zfill(8)[-8:]

        if bytes_to_process == 0:
            # Check the number of bytes needed for the current character
            if binary_num.startswith('0'):
                bytes_to_process = 0
            elif binary_num.startswith('110'):
                bytes_to_process = 1
            elif binary_num.startswith('1110'):
                bytes_to_process = 2
            elif binary_num.startswith('11110'):
                bytes_to_process = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte
            if not binary_num.startswith('10'):
                return False
            bytes_to_process -= 1

    # If all bytes are processed correctly, bytes_to_process should be 0
    return bytes_to_process == 0
