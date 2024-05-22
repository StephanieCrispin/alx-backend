#!/usr/bin/env python3
""" Baseconfig module"""

from base_config import BaseCaching


class LIFOCache(BaseCaching):
    """The LIFOCache defines a LIFO system"""

    def __init__(self):
        """Initializes the parent class
        Methods:
        get
        put
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)

            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("Discard: {}".format(self.order(len(self.order) - 1)))
                del self.cache_data[self.order(len(self.order)-1)]
                del self.order[len(self.order) - 1]

            if key in self.order:
                del self.order[self.order.index(key)]

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value of a given key"""
        if key is not None and key is self.cache_data.key():
            return self.cache_data[key]
        return None
