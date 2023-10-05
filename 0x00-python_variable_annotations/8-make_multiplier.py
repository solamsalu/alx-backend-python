#!/usr/bin/env python3
"""Task 8's module.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(number: float) -> float:
        """ Creates a multiplier function. """
        return number * multiplier
    return multiplier_func
