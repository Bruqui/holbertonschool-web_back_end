#!/usr/bin/env python3

"""This file contains a function to measure the time of executing the wait_n coroutine."""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total time it takes to execute wait_n(n, max_delay), and returns the average time per task.
    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.
    Returns:
        float: The average time per task (total time divided by n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
