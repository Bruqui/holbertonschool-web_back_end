#!/usr/bin/env python3
"""
This modules provides a types-annoteted function to compute the sum of a list
containig integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float.
    """
    return sum(mxd_lst)
