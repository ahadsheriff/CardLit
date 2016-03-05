"""
Author: Matthew Toro
Date: 3/5/16
Desc: Class file for Card
"""


class Card():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.correct = False

    def setCorrect(self, input):
        if (isinstance(input, bool)):
            self.correct = input
        else:
            raise Exception("Input must be either True or False")

    def toString(self):
        return "Question: " + self.question + ", Answer: " + self.answer + ", Correct: " + str(self.correct)
