# Loader

import numpy as np 

"""
'p' : 1, 'P' : 1
'r' : 2, 'R' : 2
'n' : 3, 'N' : 3
'b' : 4, 'B' : 4
'q' : 5, 'Q' : 5
'k' : 6, 'K' : 6
"""

def board_one_hot(board):
    """
    This method takes 8x8 size chess board, and expand it into 8x8x6 one-hot configuration.
    """
    board_one_hot = np.zeros((8,8,6))
    piece2num = {
            'p' : 0, 'P' : 0,
            'r' : 1, 'R' : 1,
            'n' : 2, 'N' : 2,
            'b' : 3, 'B' : 3,
            'q' : 4, 'Q' : 4,
            'k' : 5, 'K' : 5
            }
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.':
                height = piece2num[board[i][j]]
                isWhite = board[i][j] <= 'Z' # capital letter indicates white
                if isWhite: board[i][j] = 1
                else: board[i][j] = -1
                board_one_hot[i][j][height] = isWhite
    return board_one_hot

def load():
    """
    Try to interprete the textfiles, and generate datasets
    """
    x_data = []
    y_data = []

    # load black win
    for board in read_board("predictor/black_wins.txt"):
        x_data.append(board_one_hot(board))
        y_data.append([0,1])

    # load white win
    for board in read_board("predictor/white_wins.txt"):
        x_data.append(board_one_hot(board))
        y_data.append([1,0])

    print(len(x_data), "data loaded")
    return np.stack(x_data), np.stack(y_data)

def read_board(path):
    """
    This method iterate the chess board from .txt file
    First 8 movements will be skipped. (It is hard to tell who is likely to win at the beginning)
    """
    f = open(path, "r")
    row = 0
    movement = 0
    board = []
    for line in f:
        if line[0] == "=":
            # game ended
            row, movement = 0, 0
            board=[]
            continue
        if row < 8:
            board.append(line.strip().split())
            row += 1
        elif row == 8:
            if movement > 4:
                yield board
            movement += 1
            row = 0
            board = []
    raise StopIteration

if __name__ == "__main__":
    load()
