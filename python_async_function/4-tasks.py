#!/usr/bin/env python3
"""
This file contains a function to create and return asyncio tasks for wait_random.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Asynchronously runs task_wait_random n times with a specified max_delay.
    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.
    Returns:
        list: A list of random delays in ascending order without using sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
