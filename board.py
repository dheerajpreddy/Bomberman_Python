"""Definition of class board."""


class Board(object):
    """Defining board."""

    def __init__(self, length, width):
        """Initializing the board."""
        self.length = length
        self.width = width
        self.matrix = []
        self.score = 0

        # Initializing matrix with blank spaces
        for x in range(0, length):
            self.matrix.append([])
            for y in range(0, width):
                self.matrix[x].append(' ')

    def returnMatrixBoard(self):
        """Return the board as a matrix."""
        return self.matrix

    def returnStringBoard(self):
        """Return the matrix in string format."""
        stringBoard = ""
        for x in range(0, self.length):
            for y in range(0, self.width):
                stringBoard += self.matrix[x][y]
            stringBoard += '\n'
        stringBoard += "SCORE: " + str(self.score) + "\n"
        stringBoard += "Press 'q' to exit\n"
        return stringBoard

    def editBoard(self, newMatrix):
        """Edit the matrix."""
        self.matrix = newMatrix
