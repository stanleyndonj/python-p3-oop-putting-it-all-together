#!/usr/bin/env python3
class Book:
    def __init__(self, title, page_count):
        if not isinstance(title, str) or len(title) < 1 or len(title) > 25:
            print("Title must be string between 1 and 25 characters.")
            return
        self.title = title
        self.page_count = page_count  # Call the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")