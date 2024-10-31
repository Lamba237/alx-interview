#!/usr/bin/python3
""" UTF-8 Validation function"""


def validUTF8(data):
    """This function checks if a list is a
    valid UTF-8 encoding

    Args:
        data: receives a list of codes to be checked

    Return: True if UTF-8 else False
    """

    i = 0

    while i < len(data):
        if data[i] < 0x80:
            i += 1
            continue

        num_bytes = 0
        if data[i] & 0xF0 == 0xF0:
            num_bytes = 4
        elif data[i] & 0xE0 == 0xE0:
            num_bytes = 3
        elif data[i] & 0xC0 == 0xC0:
            num_bytes = 2
        else:
            return False

        for j in range(1, num_bytes):
            if i + j >= len(data) or (data[i+1] & 0xC0) != 0x80:
                return False
            i += num_bytes
    return True
