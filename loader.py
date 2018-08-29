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

def board_expand(board):
    board_exp = np.zeros((8,8,6))
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
                isWhite = board[i][j] <= 'Z'
                if isWhite: board[i][j] = 1
                else: board[i][j] = -1
                board_exp[i][j][height] = isWhite
    return board_exp

def load():
    x_data = []
    y_data = []

    # load black win
    for board in read_board("predictor/black_wins.txt"):
        x_data.append(board_expand(board))
        y_data.append([0,1])

    # load white win
    for board in read_board("predictor/white_wins.txt"):
        x_data.append(board_expand(board))
        y_data.append([1,0])

    print(len(x_data), "data loaded")
    return x_data, y_data

def read_board(path):
    f = open(path, "r")
    i = 0;
    board = []
    for line in f:
        if line[0] == "=":
            # game ended
            i = 0
            board=[]
            continue
        if i < 8:
            board.append(line.strip().split())
            i += 1
        elif i == 8:
            yield board
            i = 0
            board = []
    raise StopIteration

if __name__ == "__main__":
    load()
