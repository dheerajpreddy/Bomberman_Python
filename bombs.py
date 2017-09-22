"""Definition for bombs."""
from controllers import overlayMatrix
import time


class Bomb(object):
    """Defining Bomb."""

    def __init__(self, length, width):
        """Initializing bomb."""
        self.length = length
        self.width = width
        self.matrix = [['3', '3', '3', '3'], ['3', '3', '3', '3']]
        self.timeStamp = None
        self.x = None
        self.y = None
        self.count = 0

    def returnMatrix(self):
        """Return the matrix."""
        return self.matrix

    def editBomb(self, char):
        """Edit the matrix."""
        for i in range(0, self.length):
            for j in range(0, self.width):
                self.matrix[i][j] = char

    def placeBomb(self, board_object, bombman):
        """Place the bomb in the coordinates of the bomberman."""
        if self.count == 0:
            self.timeStamp = time.time()
            self.x = bombman.x
            self.y = bombman.y
            # print(bombman.x)
            overlayMatrix(board_object, self, bombman.x, bombman.y)
            # print(3)
            self.count = 1

    def update(self, brd, enemies, bricks, bombman):
        """Update the bomb based on timestamp."""
        if self.timeStamp is not None:
            timer = time.time() - self.timeStamp
            if timer <= 1 and timer > 0:
                self.editBomb('3')
                overlayMatrix(brd, self, self.x, self.y)
            elif timer <= 2 and timer > 1:
                self.editBomb('2')
                overlayMatrix(brd, self, self.x, self.y)
            elif timer <= 3 and timer > 2:
                self.editBomb('1')
                overlayMatrix(brd, self, self.x, self.y)
            else:
                self.editBomb(' ')
                overlayMatrix(brd, self, self.x, self.y)
                self.timeStamp = None
                self.count = 0
                self.explode(brd, enemies, bricks, bombman)

    def explode(self, brd, enemies, bricks, bombman):
            """Explode the bomb."""
            x = self.x
            y = self.y
            # Checking 2x4 cell above bomb
            for i in range(x - 2, x):
                for j in range(y, y + 4):
                    for k in range(0, 10):
                        if i >= bricks[k].x and i < bricks[k].x + 2 and\
                           j >= bricks[k].y and j < bricks[k].y + 4:
                            bricks[k].destroy(brd)
                        if i >= enemies[k].x and i < enemies[k].x + 2 and\
                           j >= enemies[k].y and j < enemies[k].y + 4:
                            enemies[k].destroy(brd)
                        if i >= bombman.x and i < bombman.x + 2 and\
                           j >= bombman.y and j < bombman.y + 4:
                            bombman.destroy(brd)

            # Checking 2x4 cell left of bomb
            for i in range(x, x + 2):
                for j in range(y - 4, y):
                    for k in range(0, 10):
                        if i >= bricks[k].x and i < bricks[k].x + 2 and\
                           j >= bricks[k].y and j < bricks[k].y + 4:
                            bricks[k].destroy(brd)
                        if i >= enemies[k].x and i < enemies[k].x + 2 and\
                           j >= enemies[k].y and j < enemies[k].y + 4:
                            enemies[k].destroy(brd)
                        if i >= bombman.x and i < bombman.x + 2 and\
                           j >= bombman.y and j < bombman.y + 4:
                            bombman.destroy(brd)

            # Checking 2x4 cell right of bomb
            for i in range(x, x + 2):
                for j in range(y + 4, y + 8):
                    for k in range(0, 10):
                        if i >= bricks[k].x and i < bricks[k].x + 2 and\
                           j >= bricks[k].y and j < bricks[k].y + 4:
                            bricks[k].destroy(brd)
                        if i >= enemies[k].x and i < enemies[k].x + 2 and\
                           j >= enemies[k].y and j < enemies[k].y + 4:
                            enemies[k].destroy(brd)
                        if i >= bombman.x and i < bombman.x + 2 and\
                           j >= bombman.y and j < bombman.y + 4:
                            bombman.destroy(brd)

            # Checking 2x4 cell below bomb
            for i in range(x + 2, x + 4):
                for j in range(y, y + 4):
                    for k in range(0, 10):
                        if i >= bricks[k].x and i < bricks[k].x + 2 and\
                           j >= bricks[k].y and j < bricks[k].y + 4:
                            bricks[k].destroy(brd)
                        if i >= enemies[k].x and i < enemies[k].x + 2 and\
                           j >= enemies[k].y and j < enemies[k].y + 4:
                            enemies[k].destroy(brd)
                        if i >= bombman.x and i < bombman.x + 2 and\
                           j >= bombman.y and j < bombman.y + 4:
                            bombman.destroy(brd)
