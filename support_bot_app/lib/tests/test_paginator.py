import unittest
from support_bot_app.lib.paginator.custom_paginator import CustomPaginator

class TestPaginator(unittest.TestCase):
    def setUp(self):
        pages_count = 11
        pagination_pages_range = 2
        self.custom_paginator = CustomPaginator(pages_count, pagination_pages_range)

    def test_pagination_list(self):
        page_num1 = 1
        page_num2 = 5
        page_num3 = 10
        correct_pagination_list1 = [1, 2, 3, 4, 5]
        correct_pagination_list2 = [3, 4, 5, 6, 7]
        correct_pagination_list3 = [7, 8, 9, 10, 11]
        test_pagination_list1 = self.custom_paginator.pagination_list(page_num1)
        test_pagination_list2 = self.custom_paginator.pagination_list(page_num2)
        test_pagination_list3 = self.custom_paginator.pagination_list(page_num3)
        self.assertEqual(correct_pagination_list1, test_pagination_list1)
        self.assertEqual(correct_pagination_list2, test_pagination_list2)
        self.assertEqual(correct_pagination_list3, test_pagination_list3)