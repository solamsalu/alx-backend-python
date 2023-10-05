#!/usr/bin/env python3
""" Task 102's answer """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Type-annotated function zoom_array. """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
