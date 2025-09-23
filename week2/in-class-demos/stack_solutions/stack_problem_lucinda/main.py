# Import the 1st class here
from src.stack import Stack
# Create the second class here
class StringReverser:
    def __init__(self, string_to_reverse: str):
        self.string_to_reverse = string_to_reverse
        self.stack = Stack(20)
        for char in self.string_to_reverse:
            self.stack.push(char)
        pass

    def create_reversed_string(self):
        reversed_string = ""
        for char in self.string_to_reverse:
            letter = self.stack.pop()
            reversed_string += letter
        return reversed_string


if __name__ == "__main__":
    # Execute the reverse class here
    while True:
        user_input = input("write something: ")
        if user_input == "stop":
            break
        else:
            try:
                reverser = StringReverser(user_input)
            except:
                print("string must be less than 20 characters")
                continue
            print(reverser.create_reversed_string())
    pass