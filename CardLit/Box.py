"""
Author: Matthew Toro and Anthony Palumbo
Date: 3/5/16
Desc: Class file for box
"""


from Card import Card
import random


class Box:
    """
    The box class.
    """
    def __init__(self, proficiency_level):
        """
        Constructor for the box object.
        :param proficiency_level: 0, 1, or 2 for the index of the box
        :return: nothing
        """
        self.proficiency_level = proficiency_level
        self.cards = []

    def add(self, card):
        """
        Adds a card to the box.
        :param card: the card being added
        :return: nothing
        """
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise Exception("Invalid input: Card must be type 'Card'.")

    def takeOut(self, index):
        """
        Removes a card from the box at a given index.
        :param index: the index of the card being removed
        :return: the card being removed
        """
        card = self.cards[index]
        self.cards.remove(card)
        return card

    def shuffle(self):
        """
        Shuffles the box.
        :return: nothing
        """
        for i in range(len(self.cards)):
            From = random.randint(0, len(self.cards) - 1)
            To = random.randint(0, len(self.cards) - 1)
            Card1 = self.cards[From]
            self.cards[From] = self.cards[To]
            self.cards[To] = Card1

    def toString(self):
        """
        Creates a string representation of the box.
        :return: a string
        """
        string = "Proficiency Level: " + str(self.proficiency_level) + ", Cards: \n["

        for i in range(len(self.cards)):
            card = self.cards[i]
            string += " " + "(" + str(card.question) + "," + str(card.answer) + ")\n"

        string += " ]"
        return string


def main():
    """
    Used for testing the implementation of the box class.
    :return: nothing
    """
    box1 = Box(1)
    print(box1.toString())
    for i in range(1, 11):
        card = Card("q" + str(i), "a" + str(i))
        box1.add(card)
    print(box1.toString())
    box1.shuffle()
    print(box1.toString())
    card1 = box1.takeOut(4)
    print(box1.toString())
    print(card1.toString())

if __name__ == "__main__":
    main()
