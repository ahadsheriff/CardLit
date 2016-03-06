"""
    Author: Anthony Palumbo and Matthew Toro
    Date: 3-5-16
    Description: Read a test text file to test algorithm for CardLit.
"""

from Set import *
from Box import *
from Card import *


def clearBox(set, boxIndex):
    """
    Goes through a box and puts each card in the appropriate box based on correct boolean
    :param set: the set object
    :param boxIndex: the index of the box being cleared
    :return: nothing
    """
    removeList = []

    if boxIndex == 0:
        for card in set.boxes[0].cards:
            if card.correct:
                set.boxes[1].add(card)
                removeList.append(card)
        for card in removeList:
            set.boxes[0].cards.remove(card)
        removeList.clear()

    elif boxIndex == 1:
        for card in set.boxes[1].cards:
            if card.correct:
                set.boxes[2].add(card)
                removeList.append(card)
            else:
                set.boxes[0].add(card)
                removeList.append(card)
        for card in removeList:
            set.boxes[1].cards.remove(card)
        removeList.clear()

    elif boxIndex == 2:
        for card in set.boxes[2].cards:
            if not card.correct:
                set.boxes[0].add(card)
                removeList.append(card)
        for card in removeList:
            set.boxes[2].cards.remove(card)
        removeList.clear()


def readBox(set, boxIndex):
    """
    Goes through a box and changes the correct boolean based on user input.
    :param set: the set object
    :param boxIndex: the index of the box being read
    :return: the set after being read and cleared
    """
    for card in set.boxes[boxIndex].cards:
        print(card.toString())
        input1 = input("Correct or Incorrect(y or n): ")
        if input1 == "y":
            card.correct = True
        elif input1 == "n":
            card.correct = False

    clearBox(set, boxIndex)

    set.boxes[0].shuffle()
    set.boxes[1].shuffle()
    set.boxes[2].shuffle()


def createSet(set, cards):
    """
    Creates a set by adding cards to the first box in the set.
    :param set: the set object
    :param cards: the array of cards read in from quizlet
    :return: the set
    """
    for card in cards:
        set.boxes[0].add(card)

    return set


def readFile(filename):
    """
    Reads a file and creates a card array for testing the algorithm. Not intended for use later on.
    :param filename: the filename of the text file with questions and answers
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


def main():
    """
    Reads a test file to create a card array, makes a set, then prints the set.
    :return: nothing
    """
    cardArray = readFile("testingAlgorithm.txt")
    set1 = Set("TestSet")
    set1 = createSet(set1, cardArray)
    # readBox(set1, 0)
    print(set1.toString())
    # readBox(set1, 1)
    # print(set1.toString())

if __name__ == "__main__":
    main()
