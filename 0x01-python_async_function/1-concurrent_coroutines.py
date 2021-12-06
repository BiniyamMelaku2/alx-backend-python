#!/usr/bin/env python3
""" asynchronous coroutine waits for a random delay between 0 and max_delay """
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' spawn n times wait for a random delay and returns List'''
    waitList = []
    for i in range(n):
        waitList += [await wait_random(max_delay)]
    return waitList
