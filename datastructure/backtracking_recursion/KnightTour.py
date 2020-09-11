'''
GFG:
https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/

Problem : A knight is placed on the first block of an empty board and, 
moving according to the rules of chess, must visit each square exactly once.

Input:
8

Output:
0 59 38 33 30 17 8 63 
37 34 31 60 9 62 29 16 
58 1 36 39 32 27 18 7 
35 48 41 26 61 10 15 28 
42 57 2 49 40 23 6 19 
47 50 45 54 25 20 11 14 
56 43 52 3 22 13 24 5 
51 46 55 44 53 4 21 12 

'''
# This solution is only to understand backtraking
# Other better solution available for this problem
# Python

def isSafe(x,y,n,board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def printSolution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end = ' ')
        print()    
            
def solveKT(n):
    board = [[-1 for x in range(n)] for y in range(n)]
    board[0][0] = 0
    pos = 1
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    if(not fillKT(board,n,0,0,move_x,move_y,pos)):
        print("Solution Does Not exist!")
    else:
        printSolution(board,n)

def fillKT(board,n,curr_x,curr_y,move_x,move_y,pos):
    if(pos == n**2):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x,new_y,n,board)):
            board[new_x][new_y] = pos
            if(fillKT(board,n,new_x,new_y,move_x,move_y,pos+1)):
                return True
            board[new_x][new_y] = -1
    return False
    
n = int(input())
solveKT(n)

