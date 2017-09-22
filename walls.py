"""Walls."""

from controllers import overlayMatrix


class Walls(object):
    """Defining Walls."""

    def __init__(self, wall_length, wall_width):
        """Initializing the board with walls."""
        self.length = wall_length
        self.width = wall_width
        self.matrix = []
        for i in range(0, self.length):
            self.matrix.append([])
            for j in range(0, self.width):
                self.matrix[i].append('X')

    def placeWalls(self, board_object):
        """Placing walls on the board."""
        game_board = board_object.returnMatrixBoard()
        length = board_object.length
        width = board_object.width
        # Placing boundary walls
        for x in range(0, 2):
            for y in range(0, width):
                game_board[x][y] = 'X'

        for x in range(length-2, length):
            for y in range(0, width):
                game_board[x][y] = 'X'

        for y in range(0, 4):
            for x in range(0, length):
                game_board[x][y] = 'X'

        for y in range(width-4, width):
            for x in range(0, length):
                game_board[x][y] = 'X'

        # Placing walls between the board
        x = 4
        y = 8
        while x < (length - 4):
            while y < (width - 8):
                overlayMatrix(board_object, self, x, y)
                y += 4 + self.width
            x += 2 + self.length
            y = 8

    def returnMatrix(self):
        """Return wall in matrix form."""
        return self.matrix
