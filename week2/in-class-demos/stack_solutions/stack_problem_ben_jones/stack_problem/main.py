# Import the 1st class here
from stack import Stack

# Create the second class here
class ReverseStack:
    def __init__(self, sentence):
        words = sentence.split()

        self.stack = Stack(len(words)) 

        for word in words:
            self.stack.push(word)

    def reverse_sentence(self):
        reversed_words = []

        while not self.stack.is_empty():
            reversed_words.append(self.stack.pop())

        return ' '.join(reversed_words)

if __name__ == "__main__":  
    # Execute the reverse class here

    while True:
        sentence = input("Enter a sentence or 'stop' to exit: ")
        if sentence.lower() == "stop":
            break
        reversed = ReverseStack(sentence)
        print("Reversed sentence: ", reversed.reverse_sentence())
    