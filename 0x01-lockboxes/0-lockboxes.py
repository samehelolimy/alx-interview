#!/usr/bin/python3
""" lockboxes solution """


def canUnlockAll(boxes):
"""determines if all the boxes can be opened """
	if (type(boxes)) is not list:
	return False
	elif (len(boxes)) == 0:
	return False

	for key in range(1, len(boxes) - 1):
	check_boxes = False
	for x in range(len(boxes)):
	check_boxes = key in boxes[x] and key != idx
	if check_boxes:
		break
	if check_boxes is False:
	return check_boxes
	return True
