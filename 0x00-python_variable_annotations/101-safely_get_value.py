#!/usr/bin/env python3
''' Duck typing - first element of a sequence '''
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None
                     ) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary,
    returning a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
