#!/usr/bin/env python3
"""
This modules provides a types-annotated function to return a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of v as a float.
    """
    return (k, float(v ** 2))
