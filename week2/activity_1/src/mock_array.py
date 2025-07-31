class Array:
    __instance_count = 0  # private class attribute

    def __init__(self, max_size):
        self._array = [None] * max_size  # private instance attribute
        self._index = -1
        self._max_size = max_size
        Array.__instance_count += 1

    def append(self, item):
        if self._index + 1 >= self._max_size:
            self.__resize()
        self._index += 1
        self._array[self._index] = item

    def insert(self, item, pos):
        if not (0 <= pos <= self._index):
            raise IndexError("Index out of bounds")
        self._array[pos] = item

    def get(self, pos):
        if not (0 <= pos <= self._index):
            raise IndexError("Index out of bounds")
        return self._array[pos]

    @classmethod
    def get_instance_count(cls):
        return cls.__instance_count

    def __resize(self):  # private method
        temp_array = [None] * (self._max_size * 2)
        temp_array[:self._max_size] = self._array
        self._array = temp_array
        self._max_size *= 2

    @property
    def index(self):
        return self._index