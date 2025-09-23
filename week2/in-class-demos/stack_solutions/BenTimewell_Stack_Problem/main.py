from stack import Stack

class SentenceReverser:
    def reverse(self, sentence_to_reverse):
        stack = Stack()
        words = sentence_to_reverse.split()

        # Verify the sentence won't overflow the stack, if it does, only reverse the first 10 words.
        for word in words:
            try:
                stack.push(word)
            except IndexError:
                print("Stack is full! Only the first 10 words were reversed.")
                break

        reversed_words = []
        while not stack.is_empty():
            reversed_words.append(stack.pop())

        return ' '.join(reversed_words)

if __name__ == "__main__":
    reverser = SentenceReverser()

    while True:
        sentence_to_reverse = input("Enter a sentence to reverse (or type 'stop' to quit): ")
        if sentence_to_reverse.lower() == "stop":
            print("Stop detected, ending program.")
            break

        reversed_sentence = reverser.reverse(sentence_to_reverse)
        print("Reversed:", reversed_sentence)