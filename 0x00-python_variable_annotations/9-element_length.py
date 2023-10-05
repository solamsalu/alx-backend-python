#!/usr/bin/env python3
""" Task 9's answer
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """ Computes the length of a list of sequences. """
    return [(i, len(i)) for i in lst]
