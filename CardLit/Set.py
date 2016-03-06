"""
Author: Matthew Toro and Anthony Palumbo
Date: 3/5/16
Desc: Class file for Set
"""

from Box import Box
from Card import Card


class Set:
    """
    The set class.
    """
    def __init__(self, name):
        """
        Constructor for the set class.
        :param name: the name of the set
        :return: nothing
        """
        self.name = name
        self.boxes = [Box(1), Box(2), Box(3)]

    def getBox(self, index):
        """
        Returns the box at a given index.
        :param index: the index of the box being returned
        :return: the box at the given index
        """
        return self.boxes[index]

    def getName(self):
        """
        Returns the name of the set.
        :return: the name as a string
        """
        return self.name

    def toString(self):
        """
        Creates a string representation of the set.
        :return: a string
        """
        return "Name: " + self.name + "\n" + "Box1: " + self.boxes[0].toString() + "\n" + "Box2: " + \
               self.boxes[1].toString() + "\n" + "Box3: " + self.boxes[2].toString()

    def readFile(self, filename):
        """
        Reads a text file for testing purposes and creates an array of cards.
        :param filename: the name of the testing file
        :return: an array of card objects
        """
        cards = []
        f = open(filename)

        for line in f:
            lineParts = line.strip()
            lineParts = lineParts.split(",")
            card = Card(lineParts[0], lineParts[1])
            cards.append(card)
            lineParts.clear()

        f.close()
        return cards

    def clearBox(self, boxIndex):
        """
        Goes through a box and moves the cards to the appropriate box based on whether the user got them correct or not.
        :param boxIndex: the index of the box to be cleared
        :return: nothing
        """
        removeList = []

        # Moves the correct cards from box 1 to box 3.
        if boxIndex == 0:
            for card in self.boxes[0].cards:
                if card.correct:
                    self.boxes[1].add(card)
                    removeList.append(card)
            for card in removeList:
                self.boxes[0].cards.remove(card)
            removeList.clear()

        # Moves the correct cards from box 2 to box 3 and the incorrect cards from box 2 to box 1.
        elif boxIndex == 1:
            for card in self.boxes[1].cards:
                if card.correct:
                    self.boxes[2].add(card)
                    removeList.append(card)
                else:
                    self.boxes[0].add(card)
                    removeList.append(card)
            for card in removeList:
                self.boxes[1].cards.remove(card)
            removeList.clear()

        # Moves the incorrect cards back to box 1 from box 3.
        elif boxIndex == 2:
            for card in self.boxes[2].cards:
                if not card.correct:
                    self.boxes[0].add(card)
                    removeList.append(card)
            for card in removeList:
                self.boxes[2].cards.remove(card)
            removeList.clear()

    def readBox(self, boxIndex):
        """
        Goes through a box of cards and changes the boolean correct to true or false based on input.
        :param boxIndex: the index of the box to be checked
        :return: nothing
        """
        for card in self.boxes[boxIndex].cards:
            print(card.toString())
            input1 = input("Correct or Incorrect(y or n): ")
            if input1 == "y":
                card.correct = True
            elif input1 == "n":
                card.correct = False

        self.clearBox(boxIndex)
        self.boxes[0].shuffle()
        self.boxes[1].shuffle()
        self.boxes[2].shuffle()

    def createSet(self, cards):
        """
        Creates a set by adding the cards in a set to the first box in a set.
        :param cards: the array of cards to be added
        :return: nothing
        """
        for card in cards:
            self.boxes[0].add(card)

    def startSession(self):
        """
        Starts a study session using an algorithm that makes studying more efficient.
        :return: nothing
        """
        while (len(self.boxes[0].cards)) > 0 or (len(self.boxes[1].cards)) > 0:
            while (len(self.boxes[0].cards)) > 0 or (len(self.boxes[1].cards)) > 0:
                # print("\nBOX #1: " + str(len(self.boxes[0].cards)))
                # print("------------------")
                self.readBox(0)
                # print("\nBOX #2: " + str(len(self.boxes[1].cards)))
                # print("------------------")
                self.readBox(1)
            # print("\nBOX #3: " + str(len(self.boxes[2].cards)))
            # print("------------------")
            self.readBox(2)


def main():
    """
    Main program used for testing the set class.
    :return: nothing
    """
    test = Set("Test")
    cards = test.readFile("testingAlgorithm.txt")
    test.createSet(cards)
    test.startSession()


if __name__ == "__main__":
    main()
