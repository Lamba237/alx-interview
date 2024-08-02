#!/usr/bin/python3
"""Lockbox solution"""


def canUnlockAll(boxes):
    """This functio checks if boxes can be opened
    Args:
       boxes: A list
    Return: boolean
    """
    
    n = len(boxes)

    opened = set()
    stack = [0] # default box to be processed

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
