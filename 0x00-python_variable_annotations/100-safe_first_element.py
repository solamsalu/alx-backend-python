#!/usr/bin/env python3
""" Task 100's answer """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Type-annotated function safe_first_element that takes a iterable argument.
    """
    if lst:
        return lst[0]
    else:
      return None