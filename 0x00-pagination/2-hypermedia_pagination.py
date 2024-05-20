#!/usr/bin/env python3
"""A file that contains a function that returns the first
 index and page size of data"""


import csv
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """

        data = self.dataset()

        assert page is int and page > 0
        assert page_size is int and page_size > 0
        try:
            indexes = index_range(page, page_size)
            return data[indexes[0]: indexes[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Takes 2 integer arguments and returns details from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        data = self.dataset()
        data_length = len(data)

        assert page is int and page > 0
        assert page_size is int and page_size > 0

        result = {
            "page_size": page_size if page_size <= len(data) else len(data),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= data_length else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": data_length
        }
        return result
