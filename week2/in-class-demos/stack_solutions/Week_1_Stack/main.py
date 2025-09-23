# INSTRUCTIONS
# In main.py...
#
# 1. prompt the user to enter a sentence.
# 2. import & use the Stack class to do the following.
# 3. create a second class which uses the stack to reverse the order of words
# in the sentence.
# 4. prints the reversed sentence.
# 5. continue to prompt the user until they enter "stop"
#
# Can you try to solve it and if you can reflect on how you approached
# the process of solving it.
import unittest

# APPROACH
# 1. Mentally parse and rephrase
#   So I already have a Stack class. I need to import it into main,
#   and in main, write a script that prompts the user then prints their
#   input sentence in reverse by word, and repeat until stopped. I need
#   to achieve this with functions from another class I write and import,
#   rather than simply hammering it out in main.py.
#
# 2. Glance over stack class to get an idea of what's on offer.
#
# 3. Hash out the algorithm for the main loop. This should clarify
# requirements of the new class. No pseudocode or UML, just Hulk smash.
#
# 4. Write the new class and get things wrong repeatedly. Stay mindful
# of production values.
#
# 5. Create unit tests and don't be lazy!
#
# 6. Donate to charity.
###############################################################################



# Import the 1st class here
from Week_1_Stack import stack

# Create the second class here
class SentenceWrangler:
    """Static functions to manipulate sentences."""

    '''
    No default constructor. I want this to serve as a static class, which
    Python doesn't explicitly offer. The more robust approach is to raise an
    exception on attempts to instantiate, however I'm not full bottle on
    'raise' so I'll leave it for now.
    '''

    @staticmethod
    def reverse_words(sentence: str) -> str:
        """Return a sentence with its words reversed, using a stack approach.
        :rtype: str
        :param sentence Sentence to reverse
        :return Sentence with reversed words
        """
        word_list = sentence.split()
        word_stack = stack.Stack(len(word_list))

        # Push words onto the stack, then pop and append each to a new sentence
        for word in word_list:
            word_stack.push(word)

        out_sentence = ""

        while not word_stack.is_empty():
            out_sentence += word_stack.pop()
            if not word_stack.is_empty():
                out_sentence += " "

        return out_sentence


if __name__ == "__main__":

    # Prompt the user for input to reverse until they tire of it
    while True:
        user_input = input("Gimme: ")
        if user_input == "stop":
            break

        print(SentenceWrangler.reverse_words(user_input))

    # Exit with a happy signoff
    print (SentenceWrangler.reverse_words(":) Have a nice day."))

    pass