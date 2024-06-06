#!/usr/bin/env python3
''' function make_multiplier that returns a function
that multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by a specified multiplier.
    """
    def multiply_by(value: float) -> float:
        ''' A function that takes a float and returns it multiplied
        by the multiplier '''
        return value * multiplier

    return multiply_by
