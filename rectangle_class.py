class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._current_index = 0  # This helps us track where we are during iteration

    # This makes the object iterable
    def __iter__(self):
        self._current_index = 0  # Reset the iteration each time
        return self

    # This is used to get the next value during iteration
    def __next__(self):
        if self._current_index == 0:
            self._current_index += 1
            return {'length': self.length}
        elif self._current_index == 1:
            self._current_index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # This tells Python that iteration is complete

# Example usage
rectangle = Rectangle(10, 5) # or you can use input() method for asking user each time the value of length and width.


# Iterating over the rectangle instance
for value in rectangle:
    print(value)
