#!/usr/bin/env python3
"""  Task 1's module """
from asyncio import sleep
from random import uniform
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions  """
    a = [i async for i in async_generator()]
    return a
