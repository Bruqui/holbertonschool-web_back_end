#!/usr/bin/env python3
"""
This module provides a type-annotated function to create a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
