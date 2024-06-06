#!/usr/bin/env python3
''' string and int/float to tuple '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k
    and the second element
    is the square of the int/float v, annotated as a float.
    """
    return (k, v ** 2)
