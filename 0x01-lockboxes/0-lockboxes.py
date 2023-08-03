#!/usr/bin/python3
"""Lockboxes interview question"""


def canUnlockAll(boxes):
    """Try to open as many boxes as possible.
    the first box is opened
    """
    locked_boxes = [locked for locked in range(1, len(boxes))]
    box_keys = [key for key in boxes[0]]

    for key in box_keys:
        if key in locked_boxes:
            locked_boxes.remove(key)
            box_keys.extend(key for key in boxes[key])

    if not locked_boxes:
        return True
    else:
        return False
