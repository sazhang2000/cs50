"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if sum([x.count(EMPTY) for x in board]) % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0], action[1]] == player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    RowX = [r.count(X) for r in board]
    RowO = [r.count(O) for r in board]
    ColX = [sum([1 for j in range(3) if board[i][j] == X]) for i in range(3)]
    ColO = [sum([1 for j in range(3) if board[i][j] == O]) for i in range(3)]
    DiagX = sum([1 for i in range(3) if board[i][i] == X])
    DiagO = sum([1 for i in range(3) if board[i][i] == O])
    Empty = sum([1 for i in range(3) for j in range(3) if board[i][j] == EMPTY])
    return True if 3 in RowX or 3 in RowO or 3 in ColX or 3 in ColO or DiagO == 3 or DiagX == 3 or Empty == 0 else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
