# Import the 1st class here
from stack import Stack

# Create the second class here


class Reverse:
    def __init__(self):
        pass

    def reverse(self, sentence: str, stack: Stack) -> str:
        word_list = sentence.split(" ")
        reverse_word_list = []
        reverse_sentence = ""

        self._push_words_to_stack(self, word_list, stack)

        reverse_word_list = self._pop_words_from_stack(self, word_list, stack)

        for i in reverse_word_list:
            reverse_sentence += f"{i} "

        return reverse_sentence

    def _push_words_to_stack(self, word_list: list, stack: Stack):
        for i in word_list:
            if stack.is_full():
                break
            stack.push(i)

    def _pop_words_from_stack(self, word_list: list, stack: Stack):
        temp_list = []
        for i in word_list:
            if (stack.is_empty()):
                break
            temp_list.append(stack.pop())
        return temp_list


if __name__ == "__main__":
    mystack = Stack()
    while True:
        user_input = input("Enter a sentence ('stop' to quit): ")
        if user_input.lower() == "stop":
            break
        # Execute the reverse class here
        print(Reverse.reverse(Reverse, user_input, mystack))
    pass
