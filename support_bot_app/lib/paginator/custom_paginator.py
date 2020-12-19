class CustomPaginator():
    def __init__(self, pages_count, pagination_pages_range):
        self.pages_count = pages_count
        self.pagination_pages_range = pagination_pages_range  #count of pages right and left to the current page
        self.pagination_pages_totally = pagination_pages_range * 2 + 1  #count of pages in pagination bar totally

    def pagination_list(self, page_num):
        pagination_list = []
        if self.pages_count <= self.pagination_pages_totally:
            for n in range(1, self.pages_count + 1):
                pagination_list.append(n)
        elif (page_num - self.pagination_pages_range > 0 and
              page_num + self.pagination_pages_range <= self.pages_count):
            for n in range(-self.pagination_pages_range, self.pagination_pages_range + 1):
                pagination_list.append(page_num + n)
        else:
            if page_num - self.pagination_pages_range <= 0:
                for n in range(1, self.pagination_pages_totally + 1):
                    pagination_list.append(n)
            else:
                for n in reversed(range(0, self.pagination_pages_totally)):
                    pagination_list.append(self.pages_count - n)
        return pagination_list
