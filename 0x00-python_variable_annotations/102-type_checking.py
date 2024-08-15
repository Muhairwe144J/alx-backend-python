#!/usr/bin/env python3
'''Modules of task-102.
'''

def zoom_array(lst, factor=2):
    # type: (tuple, int) -> list
    zoomed_in = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)  # Use a tuple as expected

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
