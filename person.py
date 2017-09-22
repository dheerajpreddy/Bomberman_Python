"""Person definition."""
from controllers import overlayMatrix, check4clash


class Person(object):
    """Definition for Person."""

    def __init__(self, length, width, person_type):
        """Initializing person."""
        self.length = length
        self.width = width
        self.person_type = person_type
        self.matrix = []
        self.x = None
        self.y = None

    def setNewPosition(self, board_object, x, y):
        """Set position of person for the first time."""
        if check4clash(board_object, self, x, y) == 0:
            # print(x, y)
            overlayMatrix(board_object, self, x, y)
            self.setPosition(x, y)
            return 0
        else:
            return 1

    def setPosition(self, x, y):
        """Set position of person once it's established."""
        self.x = x
        self.y = y

    def returnMatrix(self):
        """Return person as a matrix."""
        return self.matrix

    def moveLeft(self, board_object):
        """Make person move left."""
        if check4clash(board_object, self, self.x, self.y-1) == 0:
            overlayMatrix(board_object, self, self.x, self.y-1)
            self.setPosition(self.x, self.y-1)
        else:
            return 1

    def moveRight(self, board_object):
        """Make person move right."""
        if check4clash(board_object, self, self.x, self.y+1) == 0:
            overlayMatrix(board_object, self, self.x, self.y+1)
            self.setPosition(self.x, self.y+1)
        else:
            return 1

    def moveUp(self, board_object):
        """Make person move up."""
        if check4clash(board_object, self, self.x-1, self.y) == 0:
            overlayMatrix(board_object, self, self.x-1, self.y)
            self.setPosition(self.x-1, self.y)
        else:
            return 1

    def moveDown(self, board_object):
        """Make person move down."""
        if check4clash(board_object, self, self.x+1, self.y) == 0:
            # erase upper part
            overlayMatrix(board_object, self, self.x+1, self.y)
            self.setPosition(self.x+1, self.y)
        else:
            # print("error")
            return 1

    def destroy(self, brd):
        """Destroying the enemy."""
        self.matrix = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        overlayMatrix(brd, self, self.x, self.y)
