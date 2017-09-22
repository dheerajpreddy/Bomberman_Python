"""Bomberman class definition."""

from person import Person
from controllers import overlayMatrix
import sys


class Bomberman(Person):
    """Definition for Bomberman."""

    def __init__(self, length, width, person_type):
        """Initializing Bomberman."""
        Person.__init__(self, length, width, person_type)
        self.matrix = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]

    def move(self, ch, board_object):
        """Function to read character input and move the Bomberman."""
        if ch == 'w':
            self.moveUp(board_object)
        elif ch == 'a':
            self.moveLeft(board_object)
        elif ch == 's':
            self.moveDown(board_object)
        elif ch == 'd':
            self.moveRight(board_object)

    def destroy(self, brd):
        """Destroying the enemy."""
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        overlayMatrix(brd, self, self.x, self.y)
        print("SORRY, YOU HAVE DIED.\nGAME OVER\n")
        sys.exit()
