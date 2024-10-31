#!/usr/bin/python3
""" UTF-8 Validation function"""


def validUTF8(data):
    """This function checks if a list is a valid UTF-8 encoding

    Args:
        data: receives a list of codes to be checked

    Return: True if UTF-8 else False
    """
    def is_valid_byte(byte):
        return byte & 0b11000000 == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0b10000000 == 0:
            # 1-byte character
            i += 1
            continue
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte character
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte character
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte character
            num_bytes = 4
        else:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if not is_valid_byte(data[i + j]):
                return False

        i += num_bytes

    return True
