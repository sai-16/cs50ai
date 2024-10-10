"""
Tic Tac Toe Player
"""
import copy
import math

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
    c=0
    c1=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==X :
                c+=1
            elif board[i][j]==O:
                c1+=1
    if c>c1:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                s.add((i,j))
    return s




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not valid action")
    r,c=action
    b=copy.deepcopy(board)
    b[r][c]=player(board)
    return b

def isrow(board,player):
    for i in range(len(board)):
        if board[i][0]==player and board[i][1]==player and board[i][2]==player:
            return True
    return False
def iscol(board,player):
    c=0
    for i in range(len(board[0])):
        if board[0][i]==player and board[1][i]==player and board[2][i]==player:
            return True
    return False
def is1dia(board,player):
    c=0
    for i in range(len(board)):
        if board[i][i]==player:
            c+=1
    if c==3:
        return True
    else:
        return False
def is2dia(board,player):
    c=0
    n=len(board)
    for i in range(len(board)):
        if board[i][n-i-1]==player:
            c+=1
    if c==3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if iscol(board,X) or isrow(board,X) or is1dia(board,X) or is2dia(board,X):
        return X
    elif iscol(board,O) or isrow(board,O) or is1dia(board,O) or is2dia(board,O):
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    res=winner(board)
    if res==X or res==O:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def minValue(board):
    l=math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        l=min(l,maxValue(result(board,action)))
    return l
def maxValue(board):
    l=-math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        l=max(l,minValue(result(board,action)))
    return l
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board)==X:
        p=[]
        for i in actions(board):
            p.append([minValue(result(board,i)),i])


        return sorted(p,key=lambda x:x[0],reverse=True)[-1][1]

    elif player(board)==O:
        p=[]
        for i in actions(board):
            p.append([maxValue(result(board,i)),i])
        return sorted(p,key=lambda x:x[0])[0][1]




