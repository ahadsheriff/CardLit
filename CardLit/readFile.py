"""
    Author: Anthony Palumbo
    Date: 3-5-16
    Description: Read a test text file to test algorithm for CardLit.
"""

from Set import *
from Box import *
from Card import *


def clearBox(set, boxIndex):
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
    for card in set.boxes[boxIndex].cards:
        print(card.toString())
        input1 = input("Correct or Incorrect(y or n): ")
        if input1 == "y":
            card.correct = True
        elif input1 == "n":
            card.correct = False
    clearBox(set, boxIndex)


def createSet(set, cards):
    for card in cards:
        set.boxes[0].add(card)
    return set


def readFile(filename):
    cards = []
    f = open(filename)
    for line in f:
        lineParts = line.split(",")
        for part in lineParts:
            part.strip("\n\r")
        card = Card(lineParts[0], lineParts[1])
        cards.append(card)
        lineParts.clear()
    f.close()
    return cards


def main():
    cardArray = readFile("testingAlgorithm.txt")
    set1 = Set("TestSet")
    set1 = createSet(set1, cardArray)
    readBox(set1, 0)
    print(set1.toString())
    readBox(set1, 1)
    print(set1.toString())

if __name__ == "__main__":
    main()
