#!/usr/bin/env python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """
    Defines a class for caching infor in key value pairs
    Methods:
      get: gets a value for an item
      put: puts a value for an item
    """

    def __init__(self):
        """Initializes the class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Creates an entry in the dict"""
        if key is not None and item is not None:
            self.cache_data[item] = key

    def get(self, key):
        """Gets a cached item from the dictionary"""
        return self.cache_data.get(key)
        return None
