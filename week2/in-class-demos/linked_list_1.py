class Node:
    def __init__(self, int_val, float_val):
        self.int_val = int_val
        self.float_val = float_val
        self.next = None

    def __str__(self):
        return str(self.int_val) + ", " + str(self.float_val)


class LinkedList:
    def __init__(self):
        self.__first = None

    def is_empty(self):
        return self.__first is None

    def find(self, key):
        current = self.__first
        while current and current.int_val != key:
            current = current.next

        return current

    def insert_first(self, key, dd):
        new_node = Node(key, dd)
        new_node.next = self.__first
        self.__first = new_node

    def delete(self, key):
        current = self.__first
        previous = self.__first
        while current and current.int_val != key:
            previous = current
            current = current.next

        if current is not None:
            if current == self.__first:
                self.__first = self.__first.next
            else:
                previous.next = current.next

        return current

    def delete_first(self):
        temp_node = self.__first
        if self.__first is not None:
            self.__first = self.__first.next

        return temp_node

    def display(self):
        print("List first to last:")
        current = self.__first
        while current is not None:
            print(current)
            current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_first(1, 1.5)
    linked_list.insert_first(2, 3.5)
    linked_list.insert_first(3, 7.5)
    linked_list.insert_first(4, 9.5)

    linked_list.display()

    linked_list.delete_first()

    linked_list.display()

    found_node = linked_list.find(3)
    if found_node is not None:
        print("Found node:", found_node)
    else:
        print("Could not find node")

    deleted_node = linked_list.delete(3)
    if deleted_node is not None:
        print("Deleted node:", deleted_node)
        linked_list.display()
    else:
        print("Could not delete node")