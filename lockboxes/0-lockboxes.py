#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    opened = {0}
    stack = [0]
    total_boxes = len(boxes)

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if 0 <= key < total_boxes and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == total_boxes
    