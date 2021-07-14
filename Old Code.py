"""
Tic Tac Toe Player
"""





"""



"""

import math
import copy

outputFile=open("logging.txt", "a")

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

    #return [[EMPTY, O, X],
    #        [X, O, EMPTY],
    #        [X, EMPTY, EMPTY]]


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


def resultX(board, action):
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


def minimax(currentGameBoard):
    """
    Returns the optimal action for the current player on the board.
    """
    #get current player  NB This is always the AI
    # get top level available actions
    # determine if min or max type player
    # run each one at a time through MinMax algorithm
    # pick min or max out of top level actions
    # tea

    topLevelActions = actions(currentGameBoard)    

    currentPlayer = player(currentGameBoard)

    print("==========================================")
    print("Next Turn")
    print("==========================================")

    outputFile.write("==========================================\n")
    outputFile.write("Next Turn\n")
    outputFile.write("==========================================\n")
    outputFile.flush()


    resultList =[]

    if currentPlayer==X:
        for action in actions(board):
            manipulableCopyOfBoard=result(board, action)
            finalUtility=max_value(manipulableCopyOfBoard)
            resultList.append((action,finalUtility))

        currentMax=resultList[0][1]
        currentBestResult=resultList[0][0]
        for result in resultList:
            if result[1]>currentMax:
                currentBestResult=result[0]
        return currentBestResult

       #return the action with the Highest utility

    if currentPlayer==O:
        for action in actions(currentGameBoard):

            print("----------------------------------")
            print("Checking Action: ")
            print(action)
            print("----------------------------------")


            outputFile.write("----------------------------------\n")
            outputFile.write("Checking Action:\n")
            outputFile.write(str(action))
            outputFile.write("\n")
            outputFile.write("----------------------------------\n")
            outputFile.flush()

            outputFile.write("----------------------------------\n")
            outputFile.write("Current Game Board Before:\n")
            outputFile.write(str(currentGameBoard))
            outputFile.write("\n")
            outputFile.write("----------------------------------\n")
            outputFile.flush()


            workingBored=resultX(currentGameBoard, action)

            outputFile.write("----------------------------------\n")
            outputFile.write("Current Game Board After:\n")
            outputFile.write(str(currentGameBoard))
            outputFile.write("\n")
            outputFile.write("----------------------------------\n")
            outputFile.flush()


            outputFile.write("----------------------------------\n")
            outputFile.write("cloneOfCurrentGameBoard:\n")
            outputFile.write(str(cloneOfCurrentGameBoard))
            outputFile.write("\n")
            outputFile.write("----------------------------------\n")
            outputFile.flush()


            outputFile.write("----------------------------------\n")
            outputFile.write("resultantBoard After:\n")
            outputFile.write(str(resultantCurrentGameBoardAfterTopLevelAction))
            outputFile.write("\n")
            outputFile.write("----------------------------------\n")
            outputFile.flush()

            finalv=max_value(workingBored)

            #finalUtility=utility(resultantBoard)
            resultList.append((action,finalUtility))

        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("Result List")
        print(resultList)
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


        outputFile.write("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
        outputFile.write("Result List:\n")
        outputFile.write(str(resultList))
        outputFile.write("\n")
        outputFile.write("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
        outputFile.flush()

        currentMin=resultList[0][1]
        currentBestResult=resultList[0][0]
        for result in resultList:
            if result[1]<currentMin:
                currentBestResult=result[0]
        return currentBestResult

def max_value(board):
    print("///////////////////////////////////")
    print("MAX: Input Bored")
    print(board)
    print("///////////////////////////////////")

    outputFile.write("///////////////////////////////////\n")
    outputFile.write("MAX: Input Bored:\n")
    outputFile.write(str(board))
    outputFile.write("\n")
    outputFile.write("///////////////////////////////////\n")
    outputFile.flush()

    if terminal(board):
        print("++++++++++++++++++++++++++++++++++")
        print("MAX: Utility")
        util=utility(board)
        print(util)
        print("++++++++++++++++++++++++++++++++++")

        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.write("MAX: Utility:\n")
        outputFile.write(str(util))
        outputFile.write("\n")
        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.flush()


        return utility(board)
    v=1000000
    for action in actions(board): #This bored is fixed as i tprovides the items in the loop
        print("MAX: Action:")
        print(action)

        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.write("MAX: Action::\n")
        outputFile.write(str(action))
        outputFile.write("\n")
        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.flush()



        maxManipulableCopyOfBoard = copy.deepcopy(board)
        v=max(v,min_value(resultX(maxManipulableCopyOfBoard, action)))  #This bored needs to change
        print("MAX: New V")
        print(v)

        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.write("MAX: New V: \n")
        outputFile.write(str(v))
        outputFile.write("\n")
        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.flush()


    return v

def min_value(board):
    
    if terminal(board):
        return utility(board)
    v=-1000000
    for action in actions(board):
        print("MIN: Action:")
        print(action)






        minManipulableCopyOfBoard = copy.deepcopy(board)
        v=min(v,max_value(resultX(minManipulableCopyOfBoard, action)))
        
        print("MIN: New V")
        print(v)

        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.write("MIN: New V: \n")
        outputFile.write(str(v))
        outputFile.write("\n")
        outputFile.write("++++++++++++++++++++++++++++++++++\n")
        outputFile.flush()
    return v

