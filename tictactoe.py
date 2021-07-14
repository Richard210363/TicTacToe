"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numberOfXsOnBoard = board[0].count(X) + board[1].count(X) + board[2].count(X)
    numberOfOsOnBoard = board[0].count(O) + board[1].count(O) + board[2].count(O)

    if numberOfXsOnBoard > numberOfOsOnBoard:
        return O

    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsAllowed = set()
    rowNumber = -1
    columnNumber = -1

    for row in board:
        rowNumber += 1
        columnNumber = -1
        for cell in row:
            columnNumber += 1
            if cell==None:
                actionsAllowed.add((rowNumber,columnNumber))
                

    return actionsAllowed


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nextPlayer = player(board)

    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]]=nextPlayer

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check for the 8 win conditions

    if board[0][0]==board[0][1]==board[0][2]:
        return board[0][0]
    if board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    if board[2][0]==board[2][1]==board[2][2]:
        return board[2][0]

    if board[0][0]==board[1][0]==board[2][0]:
        return board[0][0]
    if board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    if board[0][2]==board[1][2]==board[2][2]:
        return board[0][2]

    if board[0][0]==board[1][1]==board[2][2]:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    
    numberOfNonesOnBoard = board[0].count(None) + board[1].count(None) + board[2].count(None)
    if numberOfNonesOnBoard==0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    wonBy=winner(board)

    if wonBy==X:
        return 1
    if wonBy==O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)

    if current_player == X:
        currentMax = -math.inf
        for action in actions(board):
            foundMax = min_value(result(board, action))
            if foundMax > currentMax:
                currentMax = foundMax
                bestAction = action

    if current_player == O:
        currentMin = math.inf
        for action in actions(board):
            foundMin = max_value(result(board, action))
            if foundMin < currentMin:
                currentMin = foundMin
                bestAction = action

    return bestAction

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v





