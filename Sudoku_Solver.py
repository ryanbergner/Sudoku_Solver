import pandas as pd
import numpy as np
import pprint


# Help from Tech with Tim, https://cs.lmu.edu/~ray/notes/backtracking/ 


def solve_board(board):

    get = locate_spaces(board)
    if not get:
        return True
    else:
        i, j = get
        

    for x in range(1,10):
        if is_valid(board, (i,j), x):
            board[i][j] = x

            if solve_board(board):
                return True

            board[i][j] = 0 

    return False


def is_valid(board, pos , num):

    # Row Chech
    for i in range(0, len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Column check
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    BoxRow =  pos[1]//3
    BoxColumn = pos[0]//3

    # Box Check
    for i in range(BoxColumn*3, BoxColumn*3 + 3):      
        for j in range(BoxRow*3, BoxRow*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True 


def locate_spaces(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end = " ")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end = " ")


#example

board1 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

pp = pprint.PrettyPrinter(width = 41, compact = True)

print("UNSOLVED")
print_board(board1)
solve_board(board1)
print('___________________')
print("SOLVED:")
print_board(board1)
