#!/usr/bin/env python3
"""A file that contains a function that returns the first
 index and page size of data"""
from type import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function that returns the total data size and starting index 
    for a particular page in a set of data"""

    size = page_size * page_size
    return (size - page_size, size)
