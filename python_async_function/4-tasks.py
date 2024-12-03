#!/usr/bin/env python3
"""
This file contains a function to create and return asyncio tasks for
wait_random.
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously runs task_wait_random n times with a specified max_delay.
    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.
    Returns:
        list: A list of random delays in ascending order without using sort().
    """
    gecikme = []
    for _ in range(n):
        notdelay = await wait_random(max_delay)
        gecikme.append(notdelay)
    return sorted(gecikme)
