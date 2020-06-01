'''
overview of process:
    generate filled 2x2 board
    begin to remove numbers in some order (random for now),
        checking to see if another number can be placed there
    when no more numbers can be removed, this will probably be a puzzle

board representation:
    2-d array
''' 

QUADRANTS = [
        {(0, 0), (0, 1), (1, 0), (1, 1)},
        {(0, 2), (0, 3), (1, 2), (1, 3)},
        {(2, 0), (2, 1), (3, 0), (3, 1)},
        {(2, 2), (2, 3), (3, 2), (3, 3)},
        ]

# helper functions
def check_valid(coords, number, board):
    row, col = coords
    # check row for same numebr
    if number in board[row]:
        return False

    # check column for same number
    for r in range(len(board)):
        if number == board[row][col]:
            return False

    # check 2x2 area
    q_num = 0
    if row < 2 and col > 2:
        q_num = 1
    if row > 2 and col < 2:
        q_num = 2
    if row > 2 and col > 2:
        q_num = 3

    quadrant = QUADRANTS[q_num]

    for square in quadrant:
        r,c = square
        if number == board[r][c]:
            return False

    return True

# generate filled 2x2 boards
def generate_board():
    board = [[0 for i in range(4)] for i in range(4)]

    # place each number individually
    for number in range(4):
        for col in range(4): # place numbers column by column

    return board
