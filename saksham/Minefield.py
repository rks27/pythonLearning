

import random
tries = 0
board=[[]for i in range (10)]
def nummine(row, col):
    count = 0
    if row != 0 and row != len(board)-1 and col != 0 and col != len(board)-1:
        if board[row+1][col] == 1:
            count = count + 1
        if board[row-1][col] == 1:
            count = count + 1
        if board[row][col+1] == 1:
            count = count + 1
        if board[row][col-1] == 1:
            count = count + 1
        if row != 0 and row != len(board)-1 and col != 0 and col != len(board)-1:
            count = count + 1
        if row+1 < len(board)-1 and board[row+1][col] == 1:
            count = count+1
        if row - 1 < len(board)-1 and board[row - 1][col] == 1:
            count = count+1
        if col+1 < len(board)-1 and board[row][col+1] == 1:
            count = count + 1
        if count - 1 < len(board)-1 and board[row][col - 1] == 1:
            count = count+1
    return count
for i in range (10):
    for j in range(10):
        board[i].append(round(random.random()))

eachrow = ""
space = " "
for i in range(len(board)):
    eachrow = ""
    for j in range (len(board)):
        if board[i] [j] == 1:
            eachrow=eachrow+"*"+space
        else:
            eachrow=eachrow + str(nummine(i, j)) + space
for i in range (100):
    row=int(input("Write a row guess:"))
    col=int(input("Write a collum guess:"))
    if board[row][col] == 1:
        print("You hit a mine!")
        board[row-1][col-1] = ("B")
        tries = tries + 1
        print
    else:
        print("Try again!:")
        print(board[row][col])
        tries = tries+1
    if tries ==  70:
        print("Over")
        break
    if 1 not in board[i]:
        print("You win")
    


            
    
