#!/usr/bin/env python3
"""
Module for async_generator coroutine.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Asynchronously generate 10 random numbers between 0 and 10.
    Yields:
        A random float between 0and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
