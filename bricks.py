"""Definition for bricks."""

from controllers import check4clash, overlayMatrix, check4clash2
from random import randint


class Bricks(object):
    """Defining Bricks."""

    def __init__(self, length, width):
        """Initializing bricks."""
        self.length = length
        self.width = width
        self.matrix = [['%', '%', '%', '%'], ['%', '%', '%', '%']]
        self.x = None
        self.y = None
        self.destroyed = False

    def returnMatrix(self):
        """Return the bricks matrix."""
        return self.matrix

    def setNewPosition(self, board_object, x, y):
        """Set position of person for the first time."""
        if check4clash(board_object, self, x, y) == 0:
            print(x, y)
            overlayMatrix(board_object, self, x, y)
            self.setPosition(x, y)
            return 0
        else:
            return 1

    def setPosition(self, x, y):
        """Set position of person once it's established."""
        self.x = x
        self.y = y

    def random(self, brd):
        """Randomly placing bricks."""
        placed = 0
        while placed == 0:
            x = 2 * randint(1, 15)
            y = 4 * randint(1, 15)
            if check4clash2(brd, x, y) == 0:
                overlayMatrix(brd, self, x, y)
                placed = 1
                self.x = x
                self.y = y

    def destroy(self, brd):
        """Destroying the brick."""
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        overlayMatrix(brd, self, self.x, self.y)
        if self.destroyed is False:
            brd.score += 20
            self.destroyed = True
