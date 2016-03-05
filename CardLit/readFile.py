"""
    Author: Anthony Palumbo
    Date: 3-5-16
    Description: Read a test text file to test algorithm for CardLit.
"""

import Set.py as set


def readFile(filename):
    lineParts = []
    f = open(filename)
    for line in f:
        line = line.strip()
        lineParts += line.split(",")
        """Add card objects based on input"""
    f.close()


def main():
    readFile("testingAlgorithm.txt")

if __name__ == "__main__":
    main()
