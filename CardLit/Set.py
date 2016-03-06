"""
Author: Matthew Toro
Date: 3/5/16
Desc: Class file for Set
"""

from Box import Box
from Card import Card


class Set():
    def __init__(self, name):
        self.name = name
        self.boxes = [Box(1), Box(2), Box(3)]

    def getBox(self, index):
        return self.boxes[index]

    def getName(self):
        return self.name

    def toString(self):
        return "Name: " + self.name + "\n" + "Box1: " + self.boxes[0].toString() + "\n" + "Box2: " + \
               self.boxes[1].toString() + "\n" + "Box3: " + self.boxes[2].toString()


    def readFile(self, filename):
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
        removeList = []

        if boxIndex == 0:
            for card in self.boxes[0].cards:
                if card.correct:
                    self.boxes[1].add(card)
                    removeList.append(card)
            for card in removeList:
                self.boxes[0].cards.remove(card)
            removeList.clear()

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

        elif boxIndex == 2:
            for card in self.boxes[2].cards:
                if not card.correct:
                    self.boxes[0].add(card)
                    removeList.append(card)
            for card in removeList:
                self.boxes[2].cards.remove(card)
            removeList.clear()


    def readBox(self, boxIndex):

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
        for card in cards:
            self.boxes[0].add(card)



    def startSession(self):

        while (len(self.boxes[0].cards)) > 0 or (len(self.boxes[1].cards)) > 0:
            while (len(self.boxes[0].cards)) > 0 or (len(self.boxes[1].cards)) > 0:
                #print("\nBOX #1: " + str(len(self.boxes[0].cards)))
                #print("------------------")
                self.readBox(0)
                #print("\nBOX #2: " + str(len(self.boxes[1].cards)))
                #print("------------------")
                self.readBox(1)
            #print("\nBOX #3: " + str(len(self.boxes[2].cards)))
            #print("------------------")
            self.readBox(2)



def main():
    test = Set("Test")
    Cards = test.readFile("testingAlgorithm.txt")
    test.createSet(Cards)
    test.startSession()



if __name__ == "__main__":
    main()
