# Custom exception
class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        super().__init__(message)

class Node:
    def __init__(self, value, next_node=None):
        self._value = value          # The actual value stored in the node
        self._next = next_node       # Reference to the next node in the list

    def value(self):
        return self._value           # Returns the value stored in this node

    def next(self):
        return self._next            # Returns the next node

    def set_next(self, node):
        self._next = node            # Sets the next node reference


# Singly-linked list data structure
class LinkedList:
    def __init__(self, values=None):
        self._head = None            # Points to the first node in the list
        self._length = 0             # Tracks the number of elements in the list
        if values:
            # Push each value so the final list order matches input
            for value in reversed(list(values)):
                self.push(value)

    def __iter__(self):
        # Allows iteration through the list using for-loops or list()
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        # Returns the number of elements in the list
        return self._length

    def __getitem__(self, index):
        # Enables bracket access like linked_list[0]
        if not 0 <= index < self._length:
            raise IndexError("Index out of bounds.")
        current = self._head
        for _ in range(index):
            current = current.next()
        return current.value()

    def head(self):
        # Returns the head node; raises if list is empty
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value):
        # Adds a new node at the beginning of the list
        new_node = Node(value, self._head)
        self._head = new_node
        self._length += 1

    def pop(self):
        # Removes and returns the value at the head
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head.value()
        self._head = self._head.next()
        self._length -= 1
        return value

    def insert(self, index, value):
        # Inserts a value at a specific position
        if not 0 <= index <= self._length:
            raise IndexError("Index out of bounds.")
        if index == 0:
            self.push(value)
        else:
            current = self._head
            for _ in range(index - 1):
                current = current.next()
            new_node = Node(value, current.next())
            current.set_next(new_node)
            self._length += 1

    def delete(self, index):
        # Deletes the node at a specific index
        if not 0 <= index < self._length:
            raise IndexError("Index out of bounds.")
        if index == 0:
            self._head = self._head.next()
        else:
            current = self._head
            for _ in range(index - 1):
                current = current.next()
            current.set_next(current.next().next())
        self._length -= 1

    def reversed(self):
        # Returns a new LinkedList with the same elements in reverse order
        new_list = LinkedList()
        current = self._head
        while current:
            new_list.push(current.value())
            current = current.next()
        return new_list

if __name__ == "__main__":
    ll = LinkedList([1, 2, 3])
    ll.push(0)
    ll.insert(2, 99)
    print("List:", list(ll))              # [0, 1, 99, 2, 3]
    print("Item at index 3:", ll[3])      # 2
    ll.delete(2)
    print("After delete:", list(ll))      # [0, 1, 2, 3]
    print("Reversed:", list(ll.reversed()))  # [3, 2, 1, 0]