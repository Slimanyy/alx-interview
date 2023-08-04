#!/usr/bin/python3
'''A function for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    viewed_boxes = set([0])
    unviewed_boxes = set(boxes[0]).difference(set([0]))
    while len(unviewed_boxes) > 0:
        boxIdx = unviewed_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in viewed_boxes:
            unviewed_boxes = unviewed_boxes.union(boxes[boxIdx])
            viewed_boxes.add(boxIdx)
    return n == len(viewed_boxes)
