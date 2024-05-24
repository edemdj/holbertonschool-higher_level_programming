#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.counter

    def __next__(self):
        """Return the next item from the iterator and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Return the iterator itself."""
        return self
