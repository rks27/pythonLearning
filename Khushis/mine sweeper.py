import random
gameboard =[ [] for i in range(10)]

for i in range(10):
    for i in range(10):
        gameboard[i].append(round(random.random()))

for i in range(10):
    print(gameboard[i])

gameboard[0][1]

def getnumberofmines(row,col):
    count = 0

    if row != 0 and row != len(gameboard)-1 and col != 0 and col != len(gameboard) -1:
            if gameboard[row + 1] [col]:
                count = count + 1
            if gameboard[row- 1] [col+1]:
               count = count + 1
            if gameboard[row][col + 1]==1:
                count  =  count+1
            if gameboard[row ][col-1 ]:
                count = count + 1
            if gameboard[row+1][col+1]:
                count = count + 1
            if gameboard[row+1][col-1]:
                count = count + 1
            if gameboard[row-1][col-1]:
                count  = count + 1
            if gameboard[row-1][col-2]:
                count = count + 1
    return count
        
eachrow = ""
space = "   "
for i in range(len(gameboard)-1):
    eachrow = ""
    for j in range(len(gameboard)-1):
        if gameboard[i][j] == 1:
            eachrow = eachrow + "0" + space
        else:
            eachrow = eachrow + str(getnumberofmines(i,j))+ space
    print(eachrow)

