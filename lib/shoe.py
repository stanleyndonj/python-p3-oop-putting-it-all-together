#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        if not isinstance(brand, str) or len(brand) < 1 or len(brand) > 25:
            print("Brand must be string between 1 and 25 characters.")
            return
        self.brand = brand
        self.size = size  # Call the setter
        self.condition = 'New'  # Default condition when initialized

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")  # Update the message here