#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    canUnlockAll: function that determines if all boxes can be opened
    Args:
      boxes: Is a list of lists
      Return: a boolean value
    """

    n = len(boxes)

    opened_boxes = set()
    Stack = [0]

    while Stack:
        box = Stack.pop()
        if box not in opened_boxes:
            opened_boxes.add(box)
            for key in boxes[box]:
                if key < n and key not in opened_boxes:
                    Stack.append(key)

    return len(opened_boxes) == n
