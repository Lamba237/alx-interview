#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    canUnlockAll: function that determines if all boxes can be opened
    Args:
      boxes: Is a list of lists
      Return: a boolean value
    """

    opened_boxes = set()
    keys = [0]

    while keys:
        key = keys.pop()
        if key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
