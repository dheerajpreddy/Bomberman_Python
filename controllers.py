"""Controllers."""


def overlayMatrix(board_object, item_object, x, y):
    """Overlay item on board with top left corner of item at (x,y) of board."""
    board_matrix = board_object.returnMatrixBoard()
    item_matrix = item_object.returnMatrix()
    k = 0
    l = 0
    # print(x, y)
    for i in range(x, x + item_object.length):
        for j in range(y, y + item_object.width):
            board_matrix[i][j] = item_matrix[k][l]
            l += 1
        k += 1
        l = 0
    board_object.editBoard(board_matrix)


def check4clash(board_object, item_object, x, y):
    """Check if the item_object clashes with a wall."""
    """Here, (x, y) represent potential new position."""
    board_matrix = board_object.returnMatrixBoard()
    prev_x = item_object.x
    prev_y = item_object.y

    # Erase object before checking
    if prev_x is not None:
        for i in range(prev_x, prev_x+item_object.length):
            for j in range(prev_y, prev_y+item_object.width):
                board_matrix[i][j] = ' '

    # Check for clash
    for i in range(x, x+item_object.length):
        for j in range(y, y+item_object.width):
            if board_matrix[i][j] != ' ':
                overlayMatrix(board_object, item_object, prev_x, prev_y)
                return 1
    return 0


def check4clash2(board_object, x, y):
    """Checking for clash."""
    board_matrix = board_object.returnMatrixBoard()

    # Check for clash
    for i in range(x, x+2):
        for j in range(y, y+4):
            if board_matrix[i][j] != ' ':
                return 1
    return 0
