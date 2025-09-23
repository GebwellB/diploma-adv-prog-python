from stack import Stack

class StackReverse:
    def __init__(self, sentence : str):
        self.sentence = sentence
        self.reversedSentence = ""
    
    def change_sentence(self, sentence):
        self.wordList = sentence.split()
        self.listAmount = len(self.wordList)

    def reverse_words(self, usedStack : Stack):

        for i in range (self.listAmount):
            usedStack.push(self.wordList[i])
            objPushed = i + 1
            
        for i in range (objPushed):
            self.reversedSentence += usedStack.peek() + " "
            usedStack.pop()
            print(self.reversedSentence)

        self.reversedSentence = ""

if __name__ == "__main__":
    # Execute the reverse class here
    newThing = StackReverse("")
    

    while (True):
        try:
            userSentenceInput = str(input("Put a sentence here : "))

            newThing.change_sentence(userSentenceInput)
            oldThing = Stack(newThing.listAmount)
            newThing.reverse_words(oldThing)

            userStopInput = str(input("Say 'stop' to stop (Case Sensitive) : "))

            if userStopInput == 'stop':
                break

        except TypeError:
            print("You did not put in a sentence i will now terminate")
            break