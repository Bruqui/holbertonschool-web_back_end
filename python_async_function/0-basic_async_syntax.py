#!/usr/bin/env python3
"""
This file contains an asynchronous function that waits for a random delay and
returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time between 0 and max_delay
    seconds.
    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.
    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
