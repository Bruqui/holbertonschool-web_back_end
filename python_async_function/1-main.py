#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))  # Test with 5 tasks and max_delay=5
print(asyncio.run(wait_n(10, 7)))  # Test with 10 tasks and max_delay=7
print(asyncio.run(wait_n(10, 0)))  # Test with 10 tasks and max_delay=0 (should return 0's)
