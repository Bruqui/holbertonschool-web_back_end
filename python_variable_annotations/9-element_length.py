#!/usr/bin/env python3
"""
This module provides a types-annotated function to return a list of tuples
with the element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuple where each tuple contains an element and its
    length.
    """
    return [(i, len(i)) for i in lst]
