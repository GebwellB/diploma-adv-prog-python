class Stack:
    def __init__(self, max_size=10):
        self.__max_size = max_size

        self.__top = 0

        self.__data = [None] * max_size

    def push(self, o):
        """Push object onto the stack.

        If the stack if full, raise an exception.

        :param o Object to push onto the stack
        :raise IndexError if the stack is full
        """
        if self.is_full():
            raise IndexError("Stack full!")

        self.__data[self.__top] = o
        self.__top += 1

    def pop(self):
        """Pop the top-most object from the stack.

        If the stack is empty, raise an exception.

        :raise IndexError if the stack if empty
        """
        if self.is_empty():
            raise IndexError("Stack empty!")

        self.__top -= 1
        return self.__data[self.__top]

    def peek(self):
        """Look at the top-most object on the stack.

        If the stack is empty, raise an exception.

        :raise IndexError if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack empty!")

        return self.__data[self.__top - 1]

    def is_empty(self):
        """Determine whether the stack is empty.

        :return True if the stack is empty, False otherwise
        """
        return self.__top == 0

    def is_full(self):
        """Determine whether the stack is full.

        :return True if the stack is full, False otherwise.
        """
        return self.__top == self.__max_size
