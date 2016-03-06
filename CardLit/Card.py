"""
Author: Matthew Toro and Anthony Palumbo
Date: 3/5/16
Desc: Class file for Card
"""


class Card:
    """
    The card class, consists of a question and answer.
    """
    def __init__(self, question, answer):
        """
        Constructor for a card.
        :param question: the first side of the index card
        :param answer: the opposite side of the index card
        :return: nothing
        """
        self.question = question
        self.answer = answer
        self.correct = False

    def setCorrect(self, inpt):
        """
        Sets the correct boolean to True
        :param inpt: boolean, true if correct, false if incorrect
        :return: nothing
        """
        if isinstance(inpt, bool):
            self.correct = inpt
        else:
            raise Exception("Input must be either True or False")

    def toString(self):
        """
        Creates a string representation of the card.
        :return: a string
        """
        return "Question: " + self.question + ", Answer: " + self.answer + ", Correct: " + str(self.correct)
