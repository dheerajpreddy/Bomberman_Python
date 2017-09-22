"""Definition of enemey."""

from person import Person
from random import randint
from controllers import overlayMatrix, check4clash2


class Enemy(Person):
    """Docstring for Enemy."""

    def __init__(self, length, width, person_type):
        """Initializing Enemy."""
        Person.__init__(self, length, width, person_type)
        self.matrix = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
        self.destroyed = False

    def move(self, board_object, direction):
        """Moving the enemy in a given direction."""
        if self.destroyed is True:
            return
        if direction == 1:
            while self.moveUp(board_object) != 1:
                direction = 1
                return
        elif direction == 2:
            while self.moveLeft(board_object) != 1:
                direction = 2
                return
        elif direction == 3:
            while self.moveDown(board_object) != 1:
                direction = 3
                return
        else:
            while self.moveRight(board_object) != 1:
                direction = 4
                return

    def randomMove(self, board_object):
        """Choosing a random direction for the enemy."""
        random_direction = randint(1, 4)
        self.move(board_object, random_direction)

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
        """Destroying the enemy."""
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        overlayMatrix(brd, self, self.x, self.y)
        if self.destroyed is False:
            brd.score += 100
            self.destroyed = True
