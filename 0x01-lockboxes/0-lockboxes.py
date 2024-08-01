#!/usr/bin/python3
def canUnlockAll(boxes):
    # first create a set to keep track of which boxes have been open
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
