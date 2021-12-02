#!/usr/bin/env python3
"""Duck-typed annotations python"""
from typing import Union, Mapping, Any, TypeVar

Ty = TypeVar("Ty")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[Ty, None] = None
                     ) -> Union[Any, Ty]:
    '''correct duck-typed annotations'''
    if key in dct:
        return dct[key]
    else:
        return default
