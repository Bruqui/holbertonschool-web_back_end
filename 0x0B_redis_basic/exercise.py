#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis data store.
It allows for storing data under automatically generated unique UUID keys
and retrieving it with optional type conversion.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class for managing data storage inside a Redis database instance.
    It handles initialization, database flushing, data persistence, and
    type-safe retrieval.
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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis for the given key. If a callable function
        'fn' is provided, it transforms the data before returning it.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from Redis as a string by decoding the bytes
        using UTF-8 encoding.
        """
        value = self.get(key, fn=lambda d: d.decode("utf-8"))
        return str(value) if value is not None else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from Redis and converts it to an integer.
        """
        value = self.get(key, fn=int)
        return int(value) if value is not None else None
