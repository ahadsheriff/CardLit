"""
Author: Matthew Toro
Date: 3/5/16
Desc: Class file for box
"""


from Card import Card
import random


class Box():
    def __init__(self, proficiency_level):
        self.proficiency_level = proficiency_level
        self.cards = []

    def add(self, card):
        if (isinstance(card, Card)):
            self.cards.append(card)
        else:
            raise Exception("Invalid input: Card must be type 'Card'.")

    def takeOut(self, index):
        card = self.cards[index]
        self.cards.remove(card)
        return card

    def shuffle(self):
        for i in range(len(self.cards)):
            From = random.randint(0, len(self.cards) - 1)
            To = random.randint(0, len(self.cards) - 1)
            Card1 = self.cards[From]
            self.cards[From] = self.cards[To]
            self.cards[To] = Card1

    def toString(self):

        string = "Proficiency Level: " + str(self.proficiency_level) + ", Cards: \n["

        for i in range(len(self.cards)):
            card = self.cards[i]
            string += " " + "(" + str(card.question) + "," + str(card.answer) + ")"

        string += " ]"
        return string


def main():
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
