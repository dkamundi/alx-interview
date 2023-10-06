#!/usr/bin/env python3

def canUnlockAll(boxes):
    # Initialize a list to keep track of the status of each box (0 for closed, 1 for opened)
    box_status = [0] * len(boxes)

    # Mark the first box as opened
    box_status[0] = 1

    # Create a stack for DFS and start with the first box
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box is closed, mark it as opened and add it to the stack
            if 0 <= key < len(boxes) and box_status[key] == 0:
                box_status[key] = 1
                stack.append(key)

    # Check if all boxes are opened (i.e., all elements in box_status are 1)
    return all(box_status)
