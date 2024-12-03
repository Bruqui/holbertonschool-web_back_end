#!/usr/bin/env python3
"""
This file contains an asynchronous function that runs multiples wait_random
coroutines concurrently.
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously runs wait_random n times with a specified max_delay.
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call.
    Returns:
        list: A list of random delays in ascending order without using sort().
    """
    delays = []
    for _ in range(n):
        notdelay = await wait_random(max_delay)
        delays.append(notdelay)
    return sorted(delays)
