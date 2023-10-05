#!/usr/bin/env python3
"""Task 8's module.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Creates a multiplier function. """
    def multiplier_func(n: float) -> float:
        """ Creates a multiplier function. """
        return n * multiplier
    return multiplier_func
