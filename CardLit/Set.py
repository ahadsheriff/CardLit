"""
Author: Matthew Toro
Date: 3/5/16
Desc: Class file for Set
"""

from Box import Box


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


def main():
    test = Set("Test")
    print(test.toString())

if __name__ == "__main__":
    main()
