class VerboseList(list):
    def append(self, item):
        """Override append method to print a message after appending an item."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Override extend method to print a message after extending the list."""
        length_before = len(self)
        super().extend(iterable)
        length_after = len(self)
        added_items = length_after - length_before
        print(f"Extended the list with {added_items} items.")

    def remove(self, item):
        """Override remove method to print a message before removing an item."""
        if item in self:
            print(f"Removed {item} from the list.")
            super().remove(item)
        else:
            print(f"Item {item} not found in the list.")

    def pop(self, index=-1):
        """Override pop method to print a message before popping an item."""
        if -len(self) <= index < len(self):
            item = self[index]
            print(f"Popped {item} from the list.")
            return super().pop(index)
        else:
            raise IndexError("pop index out of range")
