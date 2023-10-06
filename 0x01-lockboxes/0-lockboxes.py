#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    Args::
        boxes(list): list of integer lists
    """
    if (len(boxes) == 0):
        return False

    for key in range(1, len(boxes) - 1):
        checked_boxes = False
        for idx in range(len(boxes)):
            checked_boxes = key in boxes[idx] and key != idx
            if checked_boxes:
                break
        if checked_boxes is False:
            return False
    return True
