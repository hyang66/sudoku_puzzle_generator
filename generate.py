import random 

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
    number = str(number)
    row, col = coords

    # check row and col
    for i in range(4):
        if i != col:
            if board[row][i] == number:
                return False
        if i != row:
            if board[i][col] == number:
                return False

    # check 2x2 area
    q_num = 0
    if row < 2 and col >= 2:
        q_num = 1
    if row >= 2 and col < 2:
        q_num = 2
    if row >= 2 and col >= 2:
        q_num = 3

    quadrant = QUADRANTS[q_num]

    for square in quadrant:
        r,c = square
        if number == board[r][c]:
            return False

    return True

# generate filled 2x2 boards
def generate_board():

    # probably not optimal:
    # - generate 1 row at a time, and keep track of what is allowed
    redo = True # try to generate again
    while redo:
        board = [[0 for i in range(4)] for i in range(4)]
        redo = False
    
        for row_num in range(len(board)):
            for col_num in range(len(board)):
                if row_num == 0: # for the first row, doesnt matter what we do
                    board[row_num] = ["1", "2", "3", "4"]
                    random.shuffle(board[row_num])
                else: 
                    order = ["1", "2", "3", "4"]
                    random.shuffle(order) # shuffle the order we try the numbers in
                    for num in order:
                        coords = (row_num, col_num)
                        if check_valid(coords, num, board):
                            board[row_num][col_num] = num
                            break
                    # we chose a bad order of numbers
                    if board[row_num][col_num] == 0:
                        redo = True

    return board

# remove numbers
def remove_nums(board):
    more_to_remove = True
    while more_to_remove: # keep trying to remove things until nothing can be
        next_to_remove = [i for i in range(16)]
        random.shuffle(next_to_remove)
        # randomly try removing things in specific orders
        for next_ in next_to_remove:
            row = next_ // 4
            col = next_ % 4
            coords = (row, col)
            curr_num = board[row][col]
            removable = True
            more_to_remove = False
            # check to see if it can be replace with another number
            # if it can, then no unique solution = bad
            for number in range(1,5):
                if number != curr_num and check_valid(coords, number, board):
                    removable = False
            if removable:
                board[row][col] = "_"
                more_to_remove = True
    return board

def disp_board(board):
    for row_num in range(len(board)):
        row = ""
        if row_num == 2:
            print("________")
        for col_num in range(len(board)):
            if col_num == 2:
                row += "|"
            row += board[row_num][col_num] + " "
        print(row) 

b = generate_board()
disp_board(b)
print("after removing cells:")
disp_board(remove_nums(b))


#           TEST CASES
# print(check_valid((1,2), 2,
                  # [[1,2,3,4],
                   # [3,4,0,0],
                   # [0,0,0,0],
                   # [0,0,0,0]]))

# print(check_valid( (1,3), 3,
# [['2', '1', '4', '3'],
# ['2', '4', '1', '3'],
# ['1', '2', '3', '4'],
# ['4', '3', '2', '1']]
# ))
