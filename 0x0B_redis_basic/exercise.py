#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis data store.
It allows for storing data under automatically generated unique UUID keys.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for managing data storage inside a Redis database instance.
    It handles initialization, database flushing, and data persistence.
    """

    def __init__(self) -> None:
        """
        Initializes the Redis client instance as a private variable
        and flushes the current database to ensure a clean state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random UUID string key, stores the provided data
        in Redis using that key, and returns the generated key string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
